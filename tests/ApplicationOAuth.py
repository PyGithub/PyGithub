############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
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

from datetime import datetime, timezone
from unittest import mock

import github
from github.ApplicationOAuth import ApplicationOAuth as aoa

from . import Framework


class ApplicationOAuth(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.CLIENT_ID = "client_id_removed"
        self.CLIENT_SECRET = "client_secret_removed"
        self.app = self.g.get_oauth_application(self.CLIENT_ID, self.CLIENT_SECRET)

    def testLoginURL(self):
        BASE_URL = "https://github.com/login/oauth/authorize"
        sample_uri = "https://myapp.com/some/path"
        sample_uri_encoded = "https%3A%2F%2Fmyapp.com%2Fsome%2Fpath"
        self.assertEqual(
            self.app.get_login_url(), f"{BASE_URL}?client_id={self.CLIENT_ID}"
        )
        self.assertTrue(
            f"redirect_uri={sample_uri_encoded}"
            in self.app.get_login_url(redirect_uri=sample_uri)
        )
        self.assertTrue(
            f"client_id={self.CLIENT_ID}"
            in self.app.get_login_url(redirect_uri=sample_uri)
        )
        self.assertTrue(
            "state=123abc" in self.app.get_login_url(state="123abc", login="user")
        )
        self.assertTrue(
            "login=user" in self.app.get_login_url(state="123abc", login="user")
        )
        self.assertTrue(
            f"client_id={self.CLIENT_ID}"
            in self.app.get_login_url(state="123abc", login="user")
        )

    def testGetAccessToken(self):
        access_token = self.app.get_access_token(
            "oauth_code_removed", state="state_removed"
        )
        # Test string representation
        self.assertEqual(
            str(access_token),
            'AccessToken(type="bearer", token="acces...", scope="", '
            "refresh_token_expires_in=None, refresh_token=None, expires_in=None)",
        )
        self.assertEqual(access_token.token, "access_token_removed")
        self.assertEqual(access_token.type, "bearer")
        self.assertEqual(access_token.scope, "")
        self.assertIsNone(access_token.expires_in)
        self.assertIsNone(access_token.expires_at)
        self.assertIsNone(access_token.refresh_token)
        self.assertIsNone(access_token.refresh_expires_in)
        self.assertIsNone(access_token.refresh_expires_at)

    def testGetAccessTokenWithExpiry(self):
        with mock.patch("github.AccessToken.datetime") as dt:
            dt.now = mock.Mock(
                return_value=datetime(2023, 6, 7, 12, 0, 0, 123, tzinfo=timezone.utc)
            )
            access_token = self.app.get_access_token(
                "oauth_code_removed", state="state_removed"
            )
        # Test string representation
        self.assertEqual(
            str(access_token),
            'AccessToken(type="bearer", token="acces...", scope="", '
            'refresh_token_expires_in=15811200, refresh_token="refre...", expires_in=28800)',
        )
        self.assertEqual(access_token.token, "access_token_removed")
        self.assertEqual(access_token.type, "bearer")
        self.assertEqual(access_token.scope, "")
        self.assertEqual(access_token.expires_in, 28800)
        self.assertEqual(
            access_token.expires_at,
            datetime(2023, 6, 7, 20, 0, 0, 123, tzinfo=timezone.utc),
        )
        self.assertEqual(access_token.refresh_token, "refresh_token_removed")
        self.assertEqual(access_token.refresh_expires_in, 15811200)
        self.assertEqual(
            access_token.refresh_expires_at,
            datetime(2023, 12, 7, 12, 0, 0, 123, tzinfo=timezone.utc),
        )

    def testRefreshAccessToken(self):
        access_token = self.app.get_access_token(
            "oauth_code_removed", state="state_removed"
        )

        with mock.patch("github.AccessToken.datetime") as dt:
            dt.now = mock.Mock(
                return_value=datetime(2023, 6, 7, 12, 0, 0, 123, tzinfo=timezone.utc)
            )
            refreshed = self.app.refresh_access_token(access_token.refresh_token)

        self.assertNotEqual(refreshed.token, access_token.token)
        self.assertNotEqual(refreshed.refresh_token, access_token.refresh_token)
        self.assertNotEqual(refreshed.created, access_token.created)
        # Test string representation
        self.assertEqual(
            str(refreshed),
            'AccessToken(type="bearer", token="anoth...", scope="", '
            'refresh_token_expires_in=15811200, refresh_token="anoth...", expires_in=28800)',
        )
        self.assertEqual(refreshed.token, "another_access_token_removed")
        self.assertEqual(refreshed.type, "bearer")
        self.assertEqual(refreshed.scope, "")
        self.assertEqual(
            refreshed.created,
            datetime(2023, 6, 7, 12, 0, 0, 123, tzinfo=timezone.utc),
        )
        self.assertEqual(refreshed.expires_in, 28800)
        self.assertEqual(
            refreshed.expires_at,
            datetime(2023, 6, 7, 20, 0, 0, 123, tzinfo=timezone.utc),
        )
        self.assertEqual(refreshed.refresh_token, "another_refresh_token_removed")
        self.assertEqual(refreshed.refresh_expires_in, 15811200)
        self.assertEqual(
            refreshed.refresh_expires_at,
            datetime(2023, 12, 7, 12, 0, 0, 123, tzinfo=timezone.utc),
        )

    def testGetAccessTokenBadCode(self):
        with self.assertRaises(github.BadCredentialsException) as exc:
            self.app.get_access_token("oauth_code_removed", state="state_removed")
        self.assertEqual(exc.exception.status, 200)
        self.assertIn("error", exc.exception.data)
        self.assertEqual(exc.exception.data["error"], "bad_verification_code")

    def testGetAccessTokenUnknownError(self):
        with self.assertRaises(github.GithubException) as exc:
            self.app.get_access_token("oauth_code_removed", state="state_removed")
        self.assertEqual(exc.exception.status, 200)
        self.assertIn("error", exc.exception.data)
        self.assertEqual(exc.exception.data["error"], "some_unknown_error")

    def testRefreshAccessTokenBadCode(self):
        with self.assertRaises(github.BadCredentialsException) as exc:
            self.app.refresh_access_token("oauth_code_removed")
        self.assertEqual(exc.exception.status, 200)
        self.assertIn("error", exc.exception.data)
        self.assertEqual(exc.exception.data["error"], "bad_verification_code")

    def testRefreshAccessTokenUnknownError(self):
        with self.assertRaises(github.GithubException) as exc:
            self.app.refresh_access_token("oauth_code_removed")
        self.assertEqual(exc.exception.status, 200)
        self.assertIn("error", exc.exception.data)
        self.assertEqual(exc.exception.data["error"], "some_unknown_error")

    def testCheckError(self):
        expected_header = {"header": True}
        expected_data = {"data": True}

        header, data = aoa._checkError(expected_header, None)
        self.assertEqual(header, expected_header)
        self.assertIsNone(data)

        header, data = aoa._checkError(expected_header, expected_data)
        self.assertEqual(header, expected_header)
        self.assertEqual(data, expected_data)

        with self.assertRaises(github.BadCredentialsException) as exc:
            aoa._checkError({}, {"error": "bad_verification_code"})
        self.assertEqual(exc.exception.status, 200)
        self.assertIn("error", exc.exception.data)
        self.assertEqual(exc.exception.data["error"], "bad_verification_code")

        with self.assertRaises(github.GithubException) as exc:
            aoa._checkError({}, {"error": "other"})
        self.assertEqual(exc.exception.status, 200)
        self.assertIn("error", exc.exception.data)
        self.assertEqual(exc.exception.data["error"], "other")
