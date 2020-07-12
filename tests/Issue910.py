# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import os
import warnings
from ast import literal_eval
from contextlib import contextmanager
from functools import wraps
from io import BytesIO
from textwrap import dedent
from urllib.parse import urlparse

from requests import Response
from requests.adapters import HTTPAdapter
from requests.structures import CaseInsensitiveDict

import github

from . import Framework


class NetrcManager(object):
    def __init__(self, path="~/.netrc", host="api.github.com"):
        self.path = os.path.expanduser(path)
        self.backup_path = self.path + ".pygithub-test-backup"
        self.host = host

    @contextmanager
    def remove(self):
        if os.path.exists(self.path):
            os.rename(self.path, self.backup_path)
            try:
                yield
            finally:
                os.rename(self.backup_path, self.path)
        else:
            yield

    @contextmanager
    def override(self, login, password):
        with self.remove():
            content = dedent(
                """\
                machine {}
                login {}
                password {}
                """
            ).format(self.host, login, password)

            with open(self.path, "w") as f:
                f.write(content)
            try:
                yield
            finally:
                os.remove(self.path)


class Issue910(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.netrc = NetrcManager()
        # Ignore the warning since client_{id,secret} are deprecated
        warnings.filterwarnings("ignore", category=FutureWarning)

    def tearDown(self):
        super().tearDown()
        warnings.resetwarnings()

    # No auth
    def testNoAuthWithoutNetrc(self):
        g = github.Github()
        with self.netrc.remove():
            # This should fail with "401 Requires authentication"
            with self.assertRaises(github.GithubException):
                g.get_user().login

    def testNoAuthWithNetrc(self):
        g = github.Github()
        with self.netrc.override(self.login_netrc, self.password_netrc):
            # If no auth given but ~/.netrc file exists, that netrc will be used
            self.assertEqual(g.get_user().login, "tmshn")

    # Password authentication
    def testPasswordWithoutNetrc(self):
        g = github.Github(self.login, self.password)
        with self.netrc.remove():
            self.assertEqual(g.get_user().login, "tmshn-bot")

    def testPasswordWithNetrc(self):
        g = github.Github(self.login, self.password)
        with self.netrc.override(self.login_netrc, self.password_netrc):
            self.assertEqual(g.get_user().login, "tmshn-bot")

    # OAuth token auhtentication
    def testTokenWithoutNetrc(self):
        g = github.Github(self.oauth_token)
        with self.netrc.remove():
            self.assertEqual(g.get_user().login, "tmshn-bot")

    def testTokenWithNetrc(self):
        g = github.Github(self.oauth_token)
        with self.netrc.override(self.login_netrc, self.password_netrc):
            self.assertEqual(g.get_user().login, "tmshn-bot")

    # Client ID+Secret auhtentication
    def testClientIdClientSecretWithoutNetrc(self):
        # g = github.Github(client_id=self.client_id, client_secret=self.client_secret)
        g = github.Github(client_id="redacted_id", client_secret="redacted_secret")
        with self.netrc.remove():
            # This should fail with "401 Requires authentication"
            # because client_id/secret themselves are not tied to any user
            with self.assertRaises(github.GithubException):
                g.get_user().login

    def testClientIdClientSecretWithNetrc(self):
        # g = github.Github(client_id=self.client_id, client_secret=self.client_secret)
        g = github.Github(client_id="redacted_id", client_secret="redacted_secret")
        with self.netrc.override(self.login_netrc, self.password_netrc):
            # This should fail with "401 Requires authentication"
            # because client_id/secret themselves are not tied to any user
            with self.assertRaises(github.GithubException):
                g.get_user().login

    # JWT authentication
    def testJwtWithoutNetrc(self):
        g = github.Github(jwt=self.jwt)
        with self.netrc.remove():
            # This should fail with "401 Bad credentials"
            # because jwt should cannot be used to call apis directry (instead expected to obtain token)
            with self.assertRaises(github.GithubException):
                g.get_user().login

    def testJwtWithNetrc(self):
        g = github.Github(jwt=self.jwt)
        with self.netrc.override(self.login_netrc, self.password_netrc):
            # This should fail with "401 Bad credentials"
            # because jwt should cannot be used to call apis directry (instead expected to obtain token)
            with self.assertRaises(github.GithubException):
                g.get_user().login


class ReqResRecorder:
    def __init__(self, filename, record_mode):
        self.filename = filename
        self.record_mode = record_mode
        self.original_send = None

        self.pos = 0
        if self.record_mode:
            with open(self.filename, "w"):
                pass  # clear its content

    def patch_send(self):
        self.original_send = HTTPAdapter.send

        if self.record_mode:

            @wraps(self.original_send)
            def send(
                self_inner,
                request,
                stream=False,
                timeout=None,
                verify=True,
                cert=None,
                proxies=None,
            ):
                response = self.original_send(
                    self_inner, request, stream, timeout, verify, cert, proxies
                )
                self.record(request, response)
                return response

        else:

            @wraps(self.original_send)
            def send(
                self_inner,
                request,
                stream=False,
                timeout=None,
                verify=True,
                cert=None,
                proxies=None,
            ):
                return self.replay(request)

        HTTPAdapter.send = send

    def cleanup_send(self):
        HTTPAdapter.send = self.original_send
        self.original_send = None

    def format_request(self, request):
        url = urlparse(request.url)
        Framework.fixAuthorizationHeader(request.headers)
        return list(
            map(
                str,
                [
                    url.scheme,
                    request.method,
                    url.hostname,
                    url.port,
                    url.path,
                    request.headers,
                    str(request.body).replace("\n", "").replace("\r", ""),
                ],
            )
        )

    def format_response(self, response):
        return list(
            map(
                str,
                [response.status_code, list(response.headers.items()), response.text],
            )
        )

    def record(self, request, response):
        with open(self.filename, "a") as f:
            f.write(
                "\n".join(
                    self.format_request(request)
                    + self.format_response(response)
                    + ["\n"]  # Extra empty line to split each req/res pair
                )
            )

    def replay(self, request):
        with open(self.filename) as f:
            f.seek(self.pos)
            lines = [f.readline().rstrip("\n") for _ in range(11)]
            self.pos = f.tell()
        assert lines[:5] == self.format_request(request)[:5]  # schme~path
        assert literal_eval(lines[5]) == request.headers
        assert lines[6] == self.format_request(request)[6]  # body
        status, headers, body = lines[7:10]

        response = Response()
        response.status_code = int(status)
        response.headers = CaseInsensitiveDict(literal_eval(headers))
        response.raw = BytesIO(body.encode("utf-8"))
        response.url = request.url
        response.request = request
        return response


class Issue910Installation(Framework.TestCase):
    def setUp(self):
        super().setUp()

        filename = os.path.join(
            self.replayDataFolder,
            self.__class__.__name__ + "." + self._testMethodName + ".txt",
        )
        self.recorder = ReqResRecorder(filename, self.recordMode)
        self.recorder.patch_send()

        self.netrc = NetrcManager()
        self.integration = github.GithubIntegration(
            self.integration_id, self.integration_private_key
        )

        self.origin_installation_check_after_init_flag = (
            github.Installation.Installation.CHECK_AFTER_INIT_FLAG
        )
        github.Installation.Installation.setCheckAfterInitFlag(False)

        self.origin_installationauthorization_check_after_init_flag = (
            github.InstallationAuthorization.InstallationAuthorization.CHECK_AFTER_INIT_FLAG
        )
        github.InstallationAuthorization.InstallationAuthorization.setCheckAfterInitFlag(
            False
        )

    def tearDown(self):
        super().tearDown()

        self.recorder.cleanup_send()

        github.Installation.Installation.setCheckAfterInitFlag(
            self.origin_installation_check_after_init_flag
        )
        github.InstallationAuthorization.InstallationAuthorization.setCheckAfterInitFlag(
            self.origin_installationauthorization_check_after_init_flag
        )

    def testIntegrationWithoutNetrc(self):
        with self.netrc.remove():
            installation = self.integration.get_installation("tmshn", "PyGithub")
            token = self.integration.get_access_token(installation.id.value)
            self.assertIsNotNone(token)

    def testIntegrationWithNetrc(self):
        with self.netrc.override(self.login_netrc, self.password_netrc):
            installation = self.integration.get_installation("tmshn", "PyGithub")
            token = self.integration.get_access_token(installation.id.value)
            self.assertIsNotNone(token)
