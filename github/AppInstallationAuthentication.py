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
from github.AppAuthentication import AppAuthentication
from github.InstallationAuthorization import InstallationAuthorization

# For App authentication, time remaining before token expiration to request a new one
ACCESS_TOKEN_REFRESH_THRESHOLD_SECONDS = 20
ACCESS_TOKEN_REFRESH_THRESHOLD_DELTA = datetime.timedelta(
    seconds=ACCESS_TOKEN_REFRESH_THRESHOLD_SECONDS
)


class AppInstallationAuthentication:
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
        self.app_auth = AppAuthentication(app_id, private_key)
        self.installation_id = installation_id
        self.token_permissions = {} if token_permissions is None else token_permissions
        self.jwt_expiry = jwt_expiry
        self.jwt_issued_at = jwt_issued_at

        self.auth = None
        self.auth_permissions = None

    def __get_access_token(self, requester):
        """
        :calls: `POST /app/installations/{installation_id}/access_tokens <https://docs.github.com/en/rest/apps/apps#create-an-installation-access-token-for-an-app>`
        :param requester: Requester. The requester has to have JWT authentication
        :return: :class:`github.InstallationAuthorization.InstallationAuthorization`
        """
        body = {"permissions": self.token_permissions}

        headers, response = requester.requestJsonAndCheck(
            "POST",
            f"/app/installations/{self.installation_id}/access_tokens",
            input=body,
        )

        return InstallationAuthorization(
            requester=requester,
            headers=headers,
            attributes=response,
            completed=True,
        )

    def _get_access_token_func(self, requester):
        """
        Returns a function that, when called, provides a working access token.
        :param requester: Requester. This requester is used to fetch new tokens.
                                     The authentication provided by this method.
        """
        # this requester can fetch access tokens as it provides a jwt (created each request)
        jwt_requester = requester.with_jwt(self.app_auth.create_jwt)

        # this stores the latest access token we have fetched, fetch now to fail early
        auth = [self.__get_access_token(jwt_requester)]

        # this function fetches a new token when expired, and returns the latest token
        def func():
            if (
                auth[0].expires_at
                < datetime.datetime.utcnow() - ACCESS_TOKEN_REFRESH_THRESHOLD_DELTA
            ):
                auth[0] = self.__get_access_token(jwt_requester)
            return auth[0]

        return func
