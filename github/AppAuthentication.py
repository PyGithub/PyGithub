############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Denis Blanchette <denisblanchette@gmail.com>                  #
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

import datetime

from github import Consts
from github import GithubException
from github.InstallationAuthorization import InstallationAuthorization
from github.GithubIntegration import create_jwt

# For App authentication, time remaining before token expiration to request a new one
ACCESS_TOKEN_REFRESH_THRESHOLD_SECONDS = 20


class AppAuthentication:
    def __init__(
        self,
        app_id,
        private_key,
        installation_id,
        token_permissions=None,
        jwt_expiry=Consts.DEFAULT_JWT_EXPIRY,
        jwt_issued_at=Consts.DEFAULT_JWT_ISSUED_AT,
    ):
        """
        :param app_id: int
        :param private_key: string
        :param installation_id: int
        :param jwt_expiry: int. Expiry of the JWT used to get the information about this integration.
          The default expiration is in 5 minutes and is capped at 10 minutes according to GitHub documentation
          https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#generating-a-json-web-token-jwt
        :param jwt_issued_at: int. Number of seconds, relative to now, to set for the "iat" (issued at) parameter.
          The default value is -60 to protect against clock drift
        """
        assert isinstance(app_id, (int, str)), app_id
        assert isinstance(private_key, str)
        assert isinstance(installation_id, int), installation_id
        assert token_permissions is None or isinstance(
            token_permissions, dict
        ), token_permissions
        assert isinstance(jwt_expiry, int), jwt_expiry
        assert Consts.MIN_JWT_EXPIRY <= jwt_expiry <= Consts.MAX_JWT_EXPIRY, jwt_expiry
        assert isinstance(jwt_issued_at, int)

        self.app_id = app_id
        self.private_key = private_key
        self.installation_id = installation_id
        self.token_permissions = token_permissions
        self.jwt_expiry = jwt_expiry
        self.jwt_issued_at = jwt_issued_at

        self.auth = None
        self.auth_permissions = None

    def get_access_token(self, requester, permissions=None):
        """
        :calls: `POST /app/installations/{installation_id}/access_tokens <https://docs.github.com/en/rest/apps/apps#create-an-installation-access-token-for-an-app>`
        :param requester: Requester
        :param permissions: dict
        :return: :class:`github.InstallationAuthorization.InstallationAuthorization`
        """
        if permissions is None:
            permissions = {}

        if not isinstance(permissions, dict):
            raise GithubException(
                status=400, data={"message": "Invalid permissions"}, headers=None
            )

        if self.auth is None or permissions != self.auth_permissions or \
                self.auth.expires_at < datetime.datetime.utcnow() - datetime.timedelta(seconds=ACCESS_TOKEN_REFRESH_THRESHOLD_SECONDS):
            body = {"permissions": permissions}
            jwt = create_jwt(self.app_id, self.private_key, self.jwt_expiry, self.jwt_issued_at)
            headers, response = requester.with_jwt(jwt).requestJsonAndCheck(
                "POST",
                f"/app/installations/{self.installation_id}/access_tokens",
                input=body,
            )

            self.auth = InstallationAuthorization(
                requester=requester,
                headers=headers,
                attributes=response,
                completed=True,
            )
            self.auth_permissions = permissions.copy()

        return self.auth
