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

import time

import jwt

from github import Consts


class AppAuthentication:
    def __init__(
        self,
        app_id,
        private_key,
        jwt_expiry=Consts.DEFAULT_JWT_EXPIRY,
        jwt_issued_at=Consts.DEFAULT_JWT_ISSUED_AT,
    ):
        """
        :param app_id: int
        :param private_key: string
        :param jwt_expiry: int. Expiry of the JWT used to get the information about this integration.
          The default expiration is in 5 minutes and is capped at 10 minutes according to GitHub documentation
          https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#generating-a-json-web-token-jwt
        :param jwt_issued_at: int. Number of seconds, relative to now, to set for the "iat" (issued at) parameter.
          The default value is -60 to protect against clock drift
        """
        assert isinstance(app_id, (int, str)), app_id
        assert isinstance(private_key, str)
        assert isinstance(jwt_expiry, int), jwt_expiry
        assert Consts.MIN_JWT_EXPIRY <= jwt_expiry <= Consts.MAX_JWT_EXPIRY, jwt_expiry
        assert isinstance(jwt_issued_at, int)

        self.app_id = app_id
        self.private_key = private_key
        self.jwt_expiry = jwt_expiry
        self.jwt_issued_at = jwt_issued_at

        self.auth = None
        self.auth_permissions = None

    def create_jwt(self):
        """
        Create a signed JWT
        https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app

        :return string:
        """

        now = int(time.time())
        payload = {
            "iat": now + self.jwt_issued_at,
            "exp": now + self.jwt_expiry,
            "iss": self.app_id,
        }
        encrypted = jwt.encode(payload, key=self.private_key, algorithm="RS256")

        if isinstance(encrypted, bytes):
            encrypted = encrypted.decode("utf-8")

        return encrypted
