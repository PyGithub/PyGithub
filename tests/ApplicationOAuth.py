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
            str(access_token), 'AccessToken(type="bearer", token="acces...", scope="")'
        )
        self.assertEqual(access_token.token, "access_token_removed")
        self.assertEqual(access_token.scope, "")
        self.assertEqual(access_token.type, "bearer")
