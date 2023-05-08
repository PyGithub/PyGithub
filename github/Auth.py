############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Aleksei Fedotov <aleksei@fedotov.email>                       #
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
import jwt
import time
import abc
import base64
import datetime
from datetime import timedelta

from github import Consts
from github.Requester import Requester, WithRequester


# For App authentication, time remaining before token expiration to request a new one
ACCESS_TOKEN_REFRESH_THRESHOLD_SECONDS = 20
TOKEN_REFRESH_THRESHOLD_TIMEDELTA = timedelta(seconds=ACCESS_TOKEN_REFRESH_THRESHOLD_SECONDS)


class Auth:
    """
    This class is the base class of all authentication methods for Requester.
    """
    @property
    @abc.abstractmethod
    def token_type(self):
        """
        The type of the auth token as used in the HTTP Authorization header, e.g. Bearer or Basic.
        :return: token type
        """
        pass

    @property
    @abc.abstractmethod
    def token(self):
        """
        The auth token as used in the HTTP Authorization header.
        :return: token
        """
        pass


class Login(Auth):
    """
    This class is used to authenticate Requester with login and password.
    """
    def __init__(self, login, password):
        self._login = login
        self.__password = password

    @property
    def login(self):
        return self._login

    @property
    def token_type(self):
        return "Basic"

    @property
    def token(self):
        return base64.b64encode(
            f"{self.login}:{self.__password}".encode()
        ).decode("utf-8").replace("\n", "")


class Token(Auth):
    """
    This class is used to authenticate Requester with a single constant token.
    """
    def __init__(self, token):
        self.__token = token

    @property
    def token_type(self):
        return "token"

    @property
    def token(self):
        return self.__token


class JWT(Auth):
    """
    This class is the base class to authenticate with a JSON Web Token (JWT).
    https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-json-web-token-jwt-for-a-github-app
    """
    @property
    def token_type(self):
        return "Bearer"


class AppAuth(JWT):
    """
    This class is used to authenticate Requester as a GitHub App.
    https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app
    """
    def __init__(
        self,
        app_id,
        private_key,
        jwt_expiry=Consts.DEFAULT_JWT_EXPIRY,
        jwt_issued_at=Consts.DEFAULT_JWT_ISSUED_AT,
        jwt_algorithm=Consts.DEFAULT_JWT_ALGORITHM,
    ):
        assert isinstance(app_id, (int, str)), app_id
        assert isinstance(private_key, str)

        self._app_id = app_id
        self._private_key = private_key
        self._jwt_expiry = jwt_expiry
        self._jwt_issued_at = jwt_issued_at
        self._jwt_algorithm = jwt_algorithm

    @property
    def app_id(self):
        return self._app_id

    @property
    def private_key(self):
        return self._private_key

    @property
    def token(self):
        return self.create_jwt()

    def get_installation_auth(self, installation_id, token_permissions):
        """
        Creates a github.Auth.AppInstallationAuth instance for an installation.
        :param installation_id:
        :param token_permissions:
        :return:
        """
        return AppInstallationAuth(self, installation_id, token_permissions)

    def create_jwt(self, expiration=None):
        """
        Create a signed JWT
        https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app

        :return string: jwt
        """
        if expiration is not None:
            assert isinstance(expiration, int), expiration
            assert (
                    Consts.MIN_JWT_EXPIRY <= expiration <= Consts.MAX_JWT_EXPIRY
            ), expiration

        now = int(time.time())
        payload = {
            "iat": now + self._jwt_issued_at,
            "exp": now + (expiration if expiration is not None else self._jwt_expiry),
            "iss": self._app_id,
        }
        encrypted = jwt.encode(payload, key=self.private_key, algorithm=self._jwt_algorithm)

        if isinstance(encrypted, bytes):
            encrypted = encrypted.decode("utf-8")

        return encrypted


class AppAuthToken(JWT):
    """
    This class is used to authenticate Requester as a GitHub App with a single constant JWT.
    https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app
    """
    def __init__(self, token):
        self.__token = token

    @property
    def token(self):
        return self.__token


class AppInstallationAuth(Auth, WithRequester["AppInstallationAuth"]):
    """
    This class is used to authenticate Requester as a GitHub App Installation.
    https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation
    """
    def __init__(self,
                 app_auth,
                 installation_id,
                 token_permissions=None):
        super().__init__()

        assert isinstance(app_auth, AppAuth), app_auth
        assert isinstance(installation_id, int), installation_id
        assert token_permissions is None or isinstance(
            token_permissions, dict
        ), token_permissions

        self.__app_auth = app_auth
        self._installation_id = installation_id
        self._token_permissions = token_permissions

        self.__installations = None
        self.__installation_authorization = None

    def withRequester(self, requester: Requester):
        from github.GithubIntegration import GithubIntegration

        requester = requester.withAuth(self.__app_auth)
        self.__installations = GithubIntegration(
            self.__app_auth.app_id,
            self.__app_auth.private_key,
            base_url=requester._Requester__base_url,
            jwt_expiry=self.__app_auth._jwt_expiry,
            jwt_issued_at=self.__app_auth._jwt_issued_at,
            jwt_algorithm=self.__app_auth._jwt_algorithm,
        )
        return self

    @property
    def app_id(self):
        return self.__app_auth.app_id

    @property
    def private_key(self):
        return self.__app_auth.private_key

    @property
    def installation_id(self):
        return self._installation_id

    @property
    def token_permissions(self):
        return self._token_permissions

    @property
    def token_type(self):
        return "token"

    @property
    def token(self):
        if self.__installation_authorization is None or self._is_expired:
            self.__installation_authorization = self._get_installation_authorization()
        return self.__installation_authorization.expires_at

    @property
    def _is_expired(self):
        assert self.__installation_authorization is not None
        token_expires_at = self.__installation_authorization.expires_at - TOKEN_REFRESH_THRESHOLD_TIMEDELTA
        return token_expires_at < datetime.datetime.utcnow()

    def _get_installation_authorization(self):
        assert self.__installations is not None, "Method withRequester(Requester) must be called first"
        return self.__installations.get_access_token(
            self._installation_id,
            permissions=self._token_permissions,
        )


class AppUserAuth(Auth):
    """
    This class is used to authenticate Requester as a GitHub App Installation on behalf of a user.
    https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-with-a-github-app-on-behalf-of-a-user
    """
    def __init__(self):
        raise NotImplementedError
