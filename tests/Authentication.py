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
import warnings
from unittest import mock

import jwt

import github

from . import Framework
from .GithubIntegration import APP_ID, PRIVATE_KEY, PUBLIC_KEY


class Authentication(Framework.BasicTestCase):
    def testNoAuthentication(self):
        g = github.Github()
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def assertWarning(self, warning, expected):
        self.assertWarnings(warning, expected)

    def assertWarnings(self, warning, *expecteds):
        self.assertEqual(len(warning.warnings), len(expecteds))
        for message, expected in zip(warning.warnings, expecteds):
            self.assertIsInstance(message, warnings.WarningMessage)
            self.assertIsInstance(message.message, DeprecationWarning)
            self.assertEqual(message.message.args, (expected,))

    def testBasicAuthentication(self):
        with self.assertWarns(DeprecationWarning) as warning:
            g = github.Github(self.login.login, self.login.password)
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")
        self.assertWarning(
            warning,
            "Arguments login_or_token and password are deprecated, please use auth=github.Auth.Login(...) instead",
        )

    def testOAuthAuthentication(self):
        with self.assertWarns(DeprecationWarning) as warning:
            g = github.Github(self.oauth_token.token)
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")
        self.assertWarning(
            warning,
            "Argument login_or_token is deprecated, please use auth=github.Auth.Token(...) instead",
        )

    def testJWTAuthentication(self):
        with self.assertWarns(DeprecationWarning) as warning:
            g = github.Github(jwt=self.jwt.token)
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")
        self.assertWarning(
            warning,
            "Argument jwt is deprecated, please use auth=github.Auth.AppAuth(...) or "
            "auth=github.Auth.AppAuthToken(...) instead",
        )

    def testAppAuthentication(self):
        with self.assertWarns(DeprecationWarning) as warning:
            app_auth = github.AppAuthentication(
                app_id=self.app_auth.app_id,
                private_key=self.app_auth.private_key,
                installation_id=29782936,
            )
            g = github.Github(app_auth=app_auth)
        self.assertEqual(g.get_user("ammarmallik").name, "Ammar Akbar")
        self.assertWarnings(
            warning,
            "Call to deprecated class AppAuthentication. (Use app.Auth.AppInstallationAuth instead)",
            "Argument app_auth is deprecated, please use auth=github.Auth.AppInstallationAuth(...) instead",
        )

    def testLoginAuthentication(self):
        # test data copied from testBasicAuthentication to test parity
        g = github.Github(auth=self.login)
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testTokenAuthentication(self):
        # test data copied from testOAuthAuthentication to test parity
        g = github.Github(auth=self.oauth_token)
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testAppAuthTokenAuthentication(self):
        # test data copied from testJWTAuthentication to test parity
        g = github.Github(auth=self.app_auth)
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testAppInstallationAuthAuthentication(self):
        # test data copied from testAppAuthentication to test parity
        installation_auth = github.Auth.AppInstallationAuth(self.app_auth, 29782936)
        g = github.Github(auth=installation_auth)
        self.assertEqual(g.get_user("ammarmallik").name, "Ammar Akbar")

    def testCreateJWT(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY)

        with mock.patch("github.Auth.time") as t:
            t.time = mock.Mock(return_value=1550055331.7435968)
            token = auth.create_jwt()

        payload = jwt.decode(
            token,
            key=PUBLIC_KEY,
            algorithms=["RS256"],
            options={"verify_exp": False},
        )
        self.assertDictEqual(
            payload, {"iat": 1550055271, "exp": 1550055631, "iss": APP_ID}
        )

    def testCreateJWTWithExpiration(self):
        auth = github.Auth.AppAuth(
            APP_ID, PRIVATE_KEY, jwt_expiry=120, jwt_issued_at=-30
        )

        with mock.patch("github.Auth.time") as t:
            t.time = mock.Mock(return_value=1550055331.7435968)
            token = auth.create_jwt(60)

        payload = jwt.decode(
            token,
            key=PUBLIC_KEY,
            algorithms=["RS256"],
            options={"verify_exp": False},
        )
        self.assertDictEqual(
            payload, {"iat": 1550055301, "exp": 1550055391, "iss": APP_ID}
        )

    def testUserAgent(self):
        g = github.Github(user_agent="PyGithubTester")
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testAuthorizationHeaderWithLogin(self):
        # See special case in Framework.fixAuthorizationHeader
        g = github.Github(auth=github.Auth.Login("fake_login", "fake_password"))
        with self.assertRaises(github.GithubException):
            g.get_user().name

    def testAuthorizationHeaderWithToken(self):
        # See special case in Framework.fixAuthorizationHeader
        g = github.Github(auth=github.Auth.Token("ZmFrZV9sb2dpbjpmYWtlX3Bhc3N3b3Jk"))
        with self.assertRaises(github.GithubException):
            g.get_user().name
