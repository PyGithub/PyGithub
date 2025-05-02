############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Jake Wilkins <jakewilkins@github.com>                         #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Tomas Tomecek <nereone@gmail.com>                             #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2019 秋葉 <ambiguous404@gmail.com>                                   #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Denis Blanchette <dblanchette@coveo.com>                      #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 chantra <chantra@users.noreply.github.com>                    #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Min RK <benjaminrk@gmail.com>                                 #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

import time  # NOQA

import requests  # NOQA
from urllib3.exceptions import InsecureRequestWarning

import github
from github import Consts
from github.Auth import AppInstallationAuth, Login

from . import Framework

APP_ID = 243473
PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC+5ePolLv6VcWLp2f17g6r6vHl+eoLuodOOfUl8JK+MVmvXbPa
xDy0SS0pQhwTOMtB0VdSt++elklDCadeokhEoGDQp411o+kiOhzLxfakp/kewf4U
HJnu4M/A2nHmxXVe2lzYnZvZHX5BM4SJo5PGdr0Ue2JtSXoAtYr6qE9maQIDAQAB
AoGAFhOJ7sy8jG+837Clcihso+8QuHLVYTPaD+7d7dxLbBlS8NfaQ9Nr3cGUqm/N
xV9NCjiGa7d/y4w/vrPwGh6UUsA+CvndwDgBd0S3WgIdWvAvHM8wKgNh/GBLLzhT
Bg9BouRUzcT1MjAnkGkWqqCAgN7WrCSUMLt57TNleNWfX90CQQDjvVKTT3pOiavD
3YcLxwkyeGd0VMvKiS4nV0XXJ97cGXs2GpOGXldstDTnF5AnB6PbukdFLHpsx4sW
Hft3LRWnAkEA1pY15ke08wX6DZVXy7zuQ2izTrWSGySn7B41pn55dlKpttjHeutA
3BEQKTFvMhBCphr8qST7Wf1SR9FgO0tFbwJAEhHji2yy96hUyKW7IWQZhrem/cP8
p4Va9CQolnnDZRNgg1p4eiDiLu3dhLiJ547joXuWTBbLX/Y1Qvv+B+a74QJBAMCW
O3WbMZlS6eK6//rIa4ZwN00SxDg8I8FUM45jwBsjgVGrKQz2ilV3sutlhIiH82kk
m1Iq8LMJGYl/LkDJA10CQBV1C+Xu3ukknr7C4A/4lDCa6Xb27cr1HanY7i89A+Ab
eatdM6f/XVqWp8uPT9RggUV9TjppJobYGT2WrWJMkYw=
-----END RSA PRIVATE KEY-----
"""
PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+5ePolLv6VcWLp2f17g6r6vHl
+eoLuodOOfUl8JK+MVmvXbPaxDy0SS0pQhwTOMtB0VdSt++elklDCadeokhEoGDQ
p411o+kiOhzLxfakp/kewf4UHJnu4M/A2nHmxXVe2lzYnZvZHX5BM4SJo5PGdr0U
e2JtSXoAtYr6qE9maQIDAQAB
-----END PUBLIC KEY-----
"""


class GithubIntegration(Framework.BasicTestCase):
    def setUp(self):
        super().setUp()
        self.org_installation_id = 30614487
        self.repo_installation_id = 30614431
        self.user_installation_id = 30614431

    def testDeprecatedAppAuth(self):
        # Replay data copied from testGetInstallations to test authentication only
        with self.assertWarns(DeprecationWarning) as warning:
            github_integration = github.GithubIntegration(integration_id=APP_ID, private_key=PRIVATE_KEY)
        installations = github_integration.get_installations()
        self.assertEqual(len(list(installations)), 2)
        self.assertWarning(
            warning,
            "Arguments integration_id, private_key, jwt_expiry, jwt_issued_at and "
            "jwt_algorithm are deprecated, please use auth=github.Auth.AppAuth(...) "
            "instead",
        )

    def testRequiredAppAuth(self):
        # GithubIntegration requires AppAuth authentication.
        for auth in [self.oauth_token, self.jwt, Login("login", "password")]:
            with self.assertRaises(AssertionError) as r:
                github.GithubIntegration(auth=auth)
            self.assertEqual(
                str(r.exception),
                f"GithubIntegration requires github.Auth.AppAuth authentication, not {type(auth)}",
            )

    def testAppAuth(self):
        # Replay data copied from testDeprecatedAppAuth to test parity
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installations = github_integration.get_installations()
        self.assertEqual(len(list(installations)), 2)

    def testNoneAppAuth(self):
        with self.assertRaises(AssertionError):
            github.GithubIntegration(auth=None)

    def testGetInstallations(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installations = github_integration.get_installations()

        self.assertEqual(len(list(installations)), 2)
        self.assertEqual(installations[0].id, self.org_installation_id)
        self.assertEqual(installations[1].id, self.repo_installation_id)

    def testGetGithubForInstallation(self):
        # with verify=False, urllib3.connectionpool rightly may issue an InsecureRequestWarning
        # we ignore InsecureRequestWarning from urllib3.connectionpool
        with self.ignoreWarning(category=InsecureRequestWarning, module="urllib3.connectionpool"):
            kwargs = dict(
                auth=github.Auth.AppAuth(APP_ID, PRIVATE_KEY),
                # http protocol used to deviate from default base url, recording data might require https
                base_url="http://api.github.com",
                timeout=Consts.DEFAULT_TIMEOUT + 10,
                user_agent="PyGithub/Python-Test",
                per_page=Consts.DEFAULT_PER_PAGE + 10,
                verify=False,
                retry=3,
                pool_size=10,
                seconds_between_requests=100,
                seconds_between_writes=1000,
                # v3: this should not be the default value, so if this has been changed in v3,
                # change it here is well
                lazy=True,
            )

            # assert kwargs consists of ALL requester constructor arguments
            self.assertEqual(kwargs.keys(), github.Requester.Requester.__init__.__annotations__.keys())

            github_integration = github.GithubIntegration(**kwargs)
            g = github_integration.get_github_for_installation(36541767)

            self.assertIsInstance(g._Github__requester.auth, AppInstallationAuth)

            actual = g._Github__requester.kwargs
            kwargs.update(auth=str(AppInstallationAuth))
            actual.update(auth=str(type(actual["auth"])))
            self.assertDictEqual(kwargs, actual)

            repo = g.get_repo("PyGithub/PyGithub")
            self.assertEqual(repo.full_name, "PyGithub/PyGithub")

    def testGetAccessToken(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)

        # Get repo installation access token
        repo_installation_authorization = github_integration.get_access_token(self.repo_installation_id)
        self.assertEqual(
            repo_installation_authorization.token,
            "ghs_1llwuELtXN5HDOB99XhpcTXdJxbOuF0ZlSmj",
        )
        self.assertDictEqual(
            repo_installation_authorization.permissions,
            {"issues": "read", "metadata": "read"},
        )
        self.assertEqual(repo_installation_authorization.repository_selection, "selected")
        self.assertIsNone(repo_installation_authorization.repositories)
        self.assertIsNone(repo_installation_authorization.single_file)
        self.assertIsNone(repo_installation_authorization.has_multiple_single_files)
        self.assertIsNone(repo_installation_authorization.single_file_paths)

        # Get org installation access token
        org_installation_authorization = github_integration.get_access_token(self.org_installation_id)
        self.assertEqual(
            org_installation_authorization.token,
            "ghs_V0xygF8yACXSDz5FM65QWV1BT2vtxw0cbgPw",
        )
        org_permissions = {
            "administration": "write",
            "issues": "write",
            "metadata": "read",
            "organization_administration": "read",
        }
        self.assertDictEqual(org_installation_authorization.permissions, org_permissions)
        self.assertEqual(org_installation_authorization.repository_selection, "selected")
        self.assertIsNone(org_installation_authorization.repositories)
        self.assertIsNone(org_installation_authorization.single_file)
        self.assertIsNone(org_installation_authorization.has_multiple_single_files)
        self.assertIsNone(org_installation_authorization.single_file_paths)

        # Get user installation access token
        user_installation_authorization = github_integration.get_access_token(self.user_installation_id)
        self.assertEqual(
            user_installation_authorization.token,
            "ghs_1llwuELtXN5HDOB99XhpcTXdJxbOuF0ZlSmj",
        )
        self.assertDictEqual(
            user_installation_authorization.permissions,
            {"issues": "read", "metadata": "read"},
        )
        self.assertEqual(user_installation_authorization.repository_selection, "selected")
        self.assertIsNone(user_installation_authorization.repositories)
        self.assertIsNone(user_installation_authorization.single_file)
        self.assertIsNone(user_installation_authorization.has_multiple_single_files)
        self.assertIsNone(user_installation_authorization.single_file_paths)

    def testGetUserInstallation(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installation = github_integration.get_user_installation(username="ammarmallik")

        self.assertEqual(installation.id, self.user_installation_id)

    def testGetOrgInstallation(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installation = github_integration.get_org_installation(org="GithubApp-Test-Org")

        self.assertEqual(installation.id, self.org_installation_id)

    def testGetRepoInstallation(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installation = github_integration.get_repo_installation(owner="ammarmallik", repo="test-runner")

        self.assertEqual(installation.id, self.repo_installation_id)

    def testGetAppInstallation(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        installation = github_integration.get_app_installation(installation_id=self.org_installation_id)

        self.assertEqual(installation.id, self.org_installation_id)

    def testGetInstallationNotFound(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.UnknownObjectException) as raisedexp:
            github_integration.get_org_installation(org="GithubApp-Test-Org-404")

        self.assertEqual(raisedexp.exception.status, 404)

    def testGetInstallationWithExpiredJWT(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_org_installation(org="GithubApp-Test-Org")
        self.assertEqual(
            raisedexp.exception.message,
            "'Expiration time' claim ('exp') must be a numeric value representing the future time at which the assertion expires",
        )
        self.assertEqual(raisedexp.exception.status, 401)

    def testGetAccessTokenWithExpiredJWT(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_access_token(self.repo_installation_id)
        self.assertEqual(
            raisedexp.exception.message,
            "'Expiration time' claim ('exp') must be a numeric value representing the future time at which the assertion expires",
        )
        self.assertEqual(raisedexp.exception.status, 401)

    def testGetAccessTokenForNoInstallation(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.UnknownObjectException) as raisedexp:
            github_integration.get_access_token(40432121)

        self.assertEqual(raisedexp.exception.status, 404)

    def testGetAccessTokenWithInvalidPermissions(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_access_token(self.repo_installation_id, permissions={"test-permissions": "read"})
        self.assertEqual(raisedexp.exception.message, "The permissions requested are not granted to this installation.")
        self.assertEqual(raisedexp.exception.status, 422)

    def testGetAccessTokenWithInvalidData(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        with self.assertRaises(github.GithubException) as raisedexp:
            github_integration.get_access_token(self.repo_installation_id, permissions="invalid_data")
        self.assertIsNone(raisedexp.exception.message)
        self.assertEqual(raisedexp.exception.status, 400)

    def testGetApp(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)
        github_integration = github.GithubIntegration(auth=auth)
        app = github_integration.get_app()

        self.assertEqual(app.name, "PyGithubTest")
        self.assertEqual(app.url, "/apps/pygithubtest")

        assert github_integration.requester is github_integration.__requester
        assert app.requester is app._requester
