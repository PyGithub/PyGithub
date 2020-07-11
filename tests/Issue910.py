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
from contextlib import contextmanager
from textwrap import dedent

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

    # No auth
    def testNoAuthWithoutNetrc(self):
        g = github.Github()
        with self.netrc.remove():
            # This should fail with "401 Requires authentication"
            with self.assertRaises(github.GithubException):
                self.assertEqual(g.get_user().login, "tmshn")

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

    # TODO: JWT authentication
    # TODO: Client-id/secret authentication
