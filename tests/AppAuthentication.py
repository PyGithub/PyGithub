############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

import sys

import jwt

import github

from . import Framework
from .GithubIntegration import APP_ID, PRIVATE_KEY, PUBLIC_KEY


class AppAuthentication(Framework.TestCase):
    def testCreateJWT(self):
        self.origin_time = sys.modules["time"].time
        sys.modules["time"].time = lambda: 1550055331.7435968
        token = github.AppAuthentication(
            app_id=APP_ID, private_key=PRIVATE_KEY
        ).create_jwt()
        payload = jwt.decode(
            token,
            key=PUBLIC_KEY,
            algorithms=["RS256"],
            options={"verify_exp": False},
        )
        self.assertDictEqual(
            payload, {"iat": 1550055271, "exp": 1550055631, "iss": APP_ID}
        )
        sys.modules["time"].time = self.origin_time

    def testCreateJWTWithExpiration(self):
        self.origin_time = sys.modules["time"].time
        sys.modules["time"].time = lambda: 1550055331.7435968
        token = github.AppAuthentication(
            app_id=APP_ID,
            private_key=PRIVATE_KEY,
            jwt_expiry=60,
            jwt_issued_at=-30,
        ).create_jwt()
        payload = jwt.decode(
            token,
            key=PUBLIC_KEY,
            algorithms=["RS256"],
            options={"verify_exp": False},
        )
        self.assertDictEqual(
            payload, {"iat": 1550055301, "exp": 1550055391, "iss": APP_ID}
        )
        sys.modules["time"].time = self.origin_time
