############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from __future__ import annotations

import urllib.parse
from typing import TYPE_CHECKING, Any

import github.AccessToken
import github.Auth
from github.Consts import DEFAULT_BASE_URL, DEFAULT_OAUTH_URL
from github.GithubException import BadCredentialsException, GithubException
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet
from github.Requester import Requester

if TYPE_CHECKING:
    from github.AccessToken import AccessToken
    from github.Auth import AppUserAuth


class ApplicationOAuth(NonCompletableGithubObject):
    """
    This class is used for identifying and authorizing users for Github Apps.

    The reference can be found at
    https://docs.github.com/en/developers/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps

    """

    def _initAttributes(self) -> None:
        self._client_id: Attribute[str] = NotSet
        self._client_secret: Attribute[str] = NotSet

    def __init__(
        self,
        requester: Requester,
        headers: dict[str, Any],
        attributes: Any,
        completed: bool,
    ) -> None:
        # this object requires a request without authentication
        requester = requester.withAuth(auth=None)
        super().__init__(requester, headers, attributes, completed)

    def __repr__(self) -> str:
        return self.get__repr__({"client_id": self._client_id.value})

    @property
    def client_id(self) -> str:
        return self._client_id.value

    @property
    def client_secret(self) -> str:
        return self._client_secret.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "client_id" in attributes:  # pragma no branch
            self._client_id = self._makeStringAttribute(attributes["client_id"])
        if "client_secret" in attributes:  # pragma no branch
            self._client_secret = self._makeStringAttribute(attributes["client_secret"])

    def get_oauth_url(self, path: str) -> str:
        if not path.startswith("/"):
            path = f"/{path}"

        if self._requester.base_url == DEFAULT_BASE_URL:
            base_url = DEFAULT_OAUTH_URL
        else:
            base_url = f"{self._requester.scheme}://{self._requester.hostname_and_port}/login/oauth"
        return f"{base_url}{path}"

    def get_login_url(
        self,
        redirect_uri: str | None = None,
        state: str | None = None,
        login: str | None = None,
    ) -> str:
        """
        Return the URL you need to redirect a user to in order to authorize your App.
        """
        parameters = {"client_id": self.client_id}
        if redirect_uri is not None:
            assert isinstance(redirect_uri, str), redirect_uri
            parameters["redirect_uri"] = redirect_uri
        if state is not None:
            assert isinstance(state, str), state
            parameters["state"] = state
        if login is not None:
            assert isinstance(login, str), login
            parameters["login"] = login

        query = urllib.parse.urlencode(parameters)

        return self.get_oauth_url(f"/authorize?{query}")

    def get_access_token(self, code: str, state: str | None = None) -> AccessToken:
        """
        :calls: `POST /login/oauth/access_token <https://docs.github.com/en/developers/apps/identifying-and-authorizing-users-for-github-apps>`_
        """
        assert isinstance(code, str), code
        post_parameters = {
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        if state is not None:
            post_parameters["state"] = state

        headers, data = self._checkError(
            *self._requester.requestJsonAndCheck(
                "POST",
                self.get_oauth_url("/access_token"),
                headers={"Accept": "application/json"},
                input=post_parameters,
            )
        )

        return github.AccessToken.AccessToken(
            requester=self._requester,
            headers=headers,
            attributes=data,
            completed=False,
        )

    def get_app_user_auth(self, token: AccessToken) -> AppUserAuth:
        return github.Auth.AppUserAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            token=token.token,
            token_type=token.type,
            expires_at=token.expires_at,
            refresh_token=token.refresh_token,
            refresh_expires_at=token.refresh_expires_at,
            requester=self._requester,
        )

    def refresh_access_token(self, refresh_token: str) -> AccessToken:
        """
        :calls: `POST /login/oauth/access_token <https://docs.github.com/en/developers/apps/identifying-and-authorizing-users-for-github-apps>`_
        :param refresh_token: string
        """
        assert isinstance(refresh_token, str)
        post_parameters = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }

        headers, data = self._checkError(
            *self._requester.requestJsonAndCheck(
                "POST",
                self.get_oauth_url("/access_token"),
                headers={"Accept": "application/json"},
                input=post_parameters,
            )
        )

        return github.AccessToken.AccessToken(
            requester=self._requester,
            headers=headers,
            attributes=data,
            completed=False,
        )

    @staticmethod
    def _checkError(headers: dict[str, Any], data: Any) -> tuple[dict[str, Any], Any]:
        if isinstance(data, dict) and "error" in data:
            if data["error"] == "bad_verification_code":
                raise BadCredentialsException(200, data, headers)
            raise GithubException(200, data, headers)

        return headers, data
