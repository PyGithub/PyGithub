############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Arda Kuyumcu <kuyumcuarda@gmail.com>                          #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Denis Blanchette <dblanchette@coveo.com>                      #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 chantra <chantra@users.noreply.github.com>                    #
# Copyright 2024 Bernhard M. Wiedemann <githubbmwprimary@lsmod.de>             #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jonathan Kliem <jonathan.kliem@gmail.com>                     #
# Copyright 2025 Christoph Reiter <reiter.christoph@gmail.com>                 #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Neel Malik <41765022+neel-m@users.noreply.github.com>         #
# Copyright 2025 Soubhik Kumar Mitra <59209034+x612skm@users.noreply.github.com>#
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
from datetime import datetime, timezone
from tempfile import NamedTemporaryFile
from unittest import mock
from unittest.mock import Mock

import jwt

import github
from github.Auth import Auth, Login

from . import Framework
from .GithubIntegration import APP_ID, PRIVATE_KEY, PUBLIC_KEY


class Authentication(Framework.BasicTestCase):
    def testNoAuthentication(self):
        g = github.Github()
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testBasicAuthentication(self):
        with self.assertWarns(DeprecationWarning) as warning:
            g = github.Github("login", "password")
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
                app_id=APP_ID,
                private_key=PRIVATE_KEY,
                installation_id=29782936,
            )
            g = github.Github(app_auth=app_auth)
        self.assertEqual(g.get_user("ammarmallik").name, "Ammar Akbar")
        self.assertWarnings(
            warning,
            "Use github.Auth.AppInstallationAuth instead",
            "Argument app_auth is deprecated, please use auth=github.Auth.AppInstallationAuth(...) instead",
        )

    def testLoginAuthentication(self):
        # test data copied from testBasicAuthentication to test parity
        g = github.Github(auth=Login("login", "password"))
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testTokenAuthentication(self):
        # test data copied from testOAuthAuthentication to test parity
        g = github.Github(auth=self.oauth_token)
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testAppAuthTokenAuthentication(self):
        # test data copied from testJWTAuthentication to test parity
        g = github.Github(auth=self.jwt)
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testAppAuthAuthentication(self):
        # test data copied from testAppAuthentication to test parity
        g = github.Github(auth=self.app_auth.get_installation_auth(29782936))
        self.assertEqual(g.get_user("ammarmallik").name, "Ammar Akbar")

    def assert_requester_args(self, g, expected_requester):
        expected_args = expected_requester.kwargs
        expected_args.pop("auth")

        auth_args = g._Github__requester.auth.requester.kwargs
        auth_args.pop("auth")

        self.assertEqual(expected_args, auth_args)

        auth_integration_args = (
            g._Github__requester.auth._AppInstallationAuth__integration._GithubIntegration__requester.kwargs
        )
        auth_integration_args.pop("auth")

        self.assertEqual(expected_args, auth_integration_args)

    def testAppAuthAuthenticationWithGithubRequesterArgs(self):
        # test that Requester arguments given to github.Github are passed to auth and auth.__integration
        g = github.Github(
            auth=self.app_auth.get_installation_auth(29782936),
            base_url="https://base.net/",
            timeout=60,
            user_agent="agent",
            per_page=100,
            verify="cert",
            retry=999,
            pool_size=10,
            seconds_between_requests=100,
            seconds_between_writes=1000,
        )

        self.assert_requester_args(g, g._Github__requester)

    def testAppAuthAuthenticationWithGithubIntegrationRequesterArgs(self):
        # test that Requester arguments given to github.GithubIntegration are passed to auth and auth.__integration
        gi = github.GithubIntegration(
            auth=self.app_auth,
            base_url="https://base.net/",
            timeout=60,
            user_agent="agent",
            per_page=100,
            verify="cert",
            retry=999,
            pool_size=10,
            seconds_between_requests=100,
            seconds_between_writes=1000,
        )

        self.assert_requester_args(gi.get_github_for_installation(29782936), gi._GithubIntegration__requester)

    def testAppInstallationAuthAuthentication(self):
        # test data copied from testAppAuthentication to test parity
        installation_auth = github.Auth.AppInstallationAuth(self.app_auth, 29782936)
        g = github.Github(auth=installation_auth)

        # token expires 2024-11-25 01:00:02
        token = installation_auth.token
        self.assertEqual(
            installation_auth._AppInstallationAuth__installation_authorization.expires_at,
            datetime(2024, 11, 25, 1, 0, 2, tzinfo=timezone.utc),
        )

        # test token expiry
        # control the current time used by _is_expired
        with mock.patch("github.Auth.datetime") as dt:
            # just before expiry
            dt.now = mock.Mock(return_value=datetime(2024, 11, 25, 0, 59, 3, tzinfo=timezone.utc))
            self.assertFalse(installation_auth._is_expired)

            # just after expiry
            dt.now = mock.Mock(return_value=datetime(2024, 11, 25, 1, 0, 3, tzinfo=timezone.utc))
            self.assertTrue(installation_auth._is_expired)

            # expect refreshing the token
            refreshed_token = installation_auth.token
            self.assertNotEqual(refreshed_token, token)
            self.assertFalse(installation_auth._is_expired)
            self.assertEqual(
                installation_auth._AppInstallationAuth__installation_authorization.expires_at,
                datetime(2025, 11, 25, 1, 0, 2, tzinfo=timezone.utc),
            )

            # use the token
            self.assertEqual(g.get_user("ammarmallik").name, "Ammar Akbar")
            self.assertEqual(g.get_repo("PyGithub/PyGithub").full_name, "PyGithub/PyGithub")

    def testAppInstallationAuthAuthenticationRequesterArgs(self):
        installation_auth = github.Auth.AppInstallationAuth(self.app_auth, 29782936)
        github.Github(
            auth=installation_auth,
        )

    def testAppUserAuthentication(self):
        client_id = "removed client id"
        client_secret = "removed client secret"
        refresh_token = "removed refresh token"

        g = github.Github()
        app = g.get_oauth_application(client_id, client_secret)
        with mock.patch("github.AccessToken.datetime") as dt:
            dt.now = mock.Mock(return_value=datetime(2023, 6, 7, 12, 0, 0, 123, tzinfo=timezone.utc))
            token = app.refresh_access_token(refresh_token)
        self.assertEqual(token.token, "fresh access token")
        self.assertEqual(token.type, "bearer")
        self.assertEqual(token.scope, "")
        self.assertEqual(token.expires_in, 28800)
        self.assertEqual(
            token.expires_at,
            datetime(2023, 6, 7, 20, 0, 0, 123, tzinfo=timezone.utc),
        )
        self.assertEqual(token.refresh_token, "fresh refresh token")
        self.assertEqual(token.refresh_expires_in, 15811200)
        self.assertEqual(
            token.refresh_expires_at,
            datetime(2023, 12, 7, 12, 0, 0, 123, tzinfo=timezone.utc),
        )

        auth = app.get_app_user_auth(token)
        with mock.patch("github.Auth.datetime") as dt:
            dt.now = mock.Mock(return_value=datetime(2023, 6, 7, 20, 0, 0, 123, tzinfo=timezone.utc))
            self.assertEqual(auth._is_expired, False)
            self.assertEqual(auth.token, "fresh access token")
        self.assertEqual(auth.token_type, "bearer")
        self.assertEqual(auth.refresh_token, "fresh refresh token")

        # expire auth token
        with mock.patch("github.Auth.datetime") as dt:
            dt.now = mock.Mock(return_value=datetime(2023, 6, 7, 20, 0, 1, 123, tzinfo=timezone.utc))
            self.assertEqual(auth._is_expired, True)
            self.assertEqual(auth.token, "another access token")
            self.assertEqual(auth._is_expired, False)
        self.assertEqual(auth.token_type, "bearer")
        self.assertEqual(auth.refresh_token, "another refresh token")

        g = github.Github(auth=auth)
        user = g.get_user()
        self.assertEqual(user.login, "EnricoMi")

    def testNetrcAuth(self):
        with NamedTemporaryFile("wt", delete=False) as tmp:
            # write temporary netrc file
            tmp.write("machine api.github.com\n")
            tmp.write("login github-user\n")
            tmp.write("password github-password\n")
            tmp.close()

            auth = github.Auth.NetrcAuth()
            with mock.patch.dict(os.environ, {"NETRC": tmp.name}):
                github.Github(auth=auth)

            self.assertEqual(auth.login, "github-user")
            self.assertEqual(auth.password, "github-password")
            self.assertEqual(auth.token, "Z2l0aHViLXVzZXI6Z2l0aHViLXBhc3N3b3Jk")
            self.assertEqual(auth.token_type, "Basic")

    def testNetrcAuthFails(self):
        # provide an empty netrc file to make sure this test does not find one
        with NamedTemporaryFile("wt", delete=False) as tmp:
            tmp.close()
            auth = github.Auth.NetrcAuth()
            with mock.patch.dict(os.environ, {"NETRC": tmp.name}):
                with self.assertRaises(RuntimeError) as exc:
                    github.Github(auth=auth)
                self.assertEqual(exc.exception.args, ("Could not get credentials from netrc for host api.github.com",))

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
            issuer=str(APP_ID),
        )
        self.assertDictEqual(payload, {"iat": 1550055271, "exp": 1550055631, "iss": str(APP_ID)})

    def testCreateJWTWithExpiration(self):
        auth = github.Auth.AppAuth(APP_ID, PRIVATE_KEY, jwt_expiry=120, jwt_issued_at=-30)

        with mock.patch("github.Auth.time") as t:
            t.time = mock.Mock(return_value=1550055331.7435968)
            token = auth.create_jwt(60)

        payload = jwt.decode(
            token,
            key=PUBLIC_KEY,
            algorithms=["RS256"],
            options={"verify_exp": False},
            issuer=str(APP_ID),
        )
        self.assertDictEqual(payload, {"iat": 1550055301, "exp": 1550055391, "iss": str(APP_ID)})

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

    def testAddingCustomHeaders(self):
        requester = github.Github(auth=CustomAuth())._Github__requester

        def requestRaw(cnx, verb, url, requestHeaders, encoded_input, stream=False, follow_302_redirect=False):
            self.modifiedHeaders = requestHeaders
            return Mock(), {}, Mock()

        requester._Requester__requestRaw = requestRaw
        requestHeaders = {"Custom key": "secret"}
        requester._Requester__requestEncode(None, "GET", "http://github.com", None, requestHeaders, None, Mock())

        self.assertEqual("Custom token", self.modifiedHeaders["Custom key"])


class CustomAuth(Auth):
    @property
    def token_type(self) -> str:
        return "custom auth"

    @property
    def token(self) -> str:
        return "Custom token"

    def authentication(self, headers):
        headers["Custom key"] = self.token

    def mask_authentication(self, headers):
        headers["Custom key"] = "Masked custom header"
