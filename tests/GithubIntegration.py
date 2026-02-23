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

# openssl genrsa -out jwt-key 4096
PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
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
hnehvrJjdBVnbCiK/JgecRkP9e7UzdI2qpMX/7UCggEAJjirIOs8FUWTZn0/zldy
oKtojeeN7VuzQ6zbxkf+z/HeymqpO8JVdHljs73L3i99uDOvoopF0MU5+1Ita7z0
Z25+Bmf4R+epkptCjKLsrEttuzOUCG6sLtmaiE20uDsvPfJnP/e0RAVnv1d6VAE/
Ata7w9f+RZtc+B1UzbvnoJnHnYjsKga2ukMP2s6JBRFKccz87qZHmDMXoqb5jQsG
+4M9Tgq3nEWEX1d5haE3BW+kUe3qO/P+05lQWTCC++h6PF1zTfpK3O9E94G1ETmD
ZkFJABimxVFtVQD320MpwieUe1+OSlJSdtN7bTTWzVZAeHiVZudNTSgME8fc5W+L
eQKCAQBqhlauG4WJm47nh21ZbErukpNKRR4dwYU3iPM6TMZtc5N1AV4T23uOhjQN
xQSLbpIorRZR33dOOBeroSj2oOFAx/UzgoaYUj5qqqcFfQh8QdIi98lb/25qXL49
WQlihvh8yDFc+t/HOZPn6orl0p1tcBao+uS9CCWfURv2l0KyS+JeGySQC0amxyEl
ZAQqOpkSzdk6j8MlHnebI3W9AcUkl0LY+OKU3u0iFENmLl/y/SnDWGEfJYAQuR74
VJxIu9b4GbDLqSIlg2Wk4qgxDwU1GI9Bzk1UPAy0/Qwl495oLpZ5gM71uJXRS4tZ
3i4Fanvj0vm8BvdFVxkxZoSNiMAX
-----END PRIVATE KEY-----
"""

# openssl rsa -in jwt-key -pubout
PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAwKhT/K0ouFrM4+f2dvJj
Q6kYRuGvCIpJ+4XXpAPYBDUYcc7XeqKVHtUeLO44uB1w6YKYH7/ItEDemGZmg6BU
KRUlnPJLPCfd2Hk1vizdqgnz6l3KZMgXifm7Dm9JJ1xWnOOn8w86lUvFmSRKY4gi
07B/H67JMSlok7AppnGT0yIfrGnl3SeUx58A9SrLH4gkn/AuT3U+6Qgn25ozXqxy
kQPvf3ZKIYxPQy9Vt9hJ6KiKHfUS1CRVKuEeRU0cR1k5nYYJ9os41JWywi7s2yOM
XqcZ3UY/1czYCAkTLTDffL+aBdnGg9J3On9kFjyRF0iLXX16Q54QLspaXocmU9Am
2wSwE7K/W0aWsq2eltYx65P70ibxAbPZ0qot3ABcOnzWR+9c7aOd/9rRgw6KPGtv
ViprbRNHQ4ZPWcw7LjS8u4xpsl2vm7smwxodKst+HeJgGYwaMm6d+7stFgC2CLJV
M8p2CxGUdj1+NdmuVFBk3AU653FFnGofa10DyrEaIvTEd28I5amCpG9mdwmAryyx
jOl2likiCzdMkGcQpPiMexU4hxd4FZ8TVdwwTsjttEvta+v4QrN+nsBGKHqstaFK
zBcbwf2c3X55/TnP6kDcdpqQSppqCxwG6UHtrxOZbpM0rIheyjgsOG0sJkzhJosR
PT71+DeL7V18EpRoxNU+v4sCAwEAAQ==
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
        github_integration = github.GithubIntegration(
            auth=auth, seconds_between_writes=None, seconds_between_requests=None
        )

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
