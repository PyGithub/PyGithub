############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Denis Blanchette <dblanchette@coveo.com>                      #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Hemslo Wang <hemslo.wang@gmail.com>                           #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Mark Amery <markamery@btinternet.com>                         #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 chantra <chantra@users.noreply.github.com>                    #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Min RK <benjaminrk@gmail.com>                                 #
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
import warnings
from typing import Any

import deprecated
import urllib3
from urllib3 import Retry

import github
from github import Consts
from github.Auth import AppAuth
from github.GithubApp import GithubApp
from github.GithubException import GithubException
from github.Installation import Installation
from github.InstallationAuthorization import InstallationAuthorization
from github.PaginatedList import PaginatedList
from github.Requester import Requester


class GithubIntegration:
    """
    Main class to obtain tokens for a GitHub integration.
    """

    # keep non-deprecated arguments in-sync with Requester
    # v3: remove integration_id, private_key, jwt_expiry, jwt_issued_at and jwt_algorithm
    # v3: move auth to the front of arguments
    # v3: move * before first argument so all arguments must be named,
    #     allows to reorder / add new arguments / remove deprecated arguments without breaking user code
    #     added here to force named parameters because new parameters have been added
    auth: AppAuth
    base_url: str
    __requester: Requester

    def __init__(
        self,
        integration_id: int | str | None = None,
        private_key: str | None = None,
        base_url: str = Consts.DEFAULT_BASE_URL,
        *,
        timeout: int = Consts.DEFAULT_TIMEOUT,
        user_agent: str = Consts.DEFAULT_USER_AGENT,
        per_page: int = Consts.DEFAULT_PER_PAGE,
        verify: bool | str = True,
        retry: int | Retry | None = None,
        pool_size: int | None = None,
        seconds_between_requests: float | None = Consts.DEFAULT_SECONDS_BETWEEN_REQUESTS,
        seconds_between_writes: float | None = Consts.DEFAULT_SECONDS_BETWEEN_WRITES,
        jwt_expiry: int = Consts.DEFAULT_JWT_EXPIRY,
        jwt_issued_at: int = Consts.DEFAULT_JWT_ISSUED_AT,
        jwt_algorithm: str = Consts.DEFAULT_JWT_ALGORITHM,
        auth: AppAuth | None = None,
    ) -> None:
        """
        :param integration_id: int deprecated, use auth=github.Auth.AppAuth(...) instead
        :param private_key: string deprecated, use auth=github.Auth.AppAuth(...) instead
        :param base_url: string
        :param timeout: integer
        :param user_agent: string
        :param per_page: int
        :param verify: boolean or string
        :param retry: int or urllib3.util.retry.Retry object
        :param pool_size: int
        :param seconds_between_requests: float
        :param seconds_between_writes: float
        :param jwt_expiry: int deprecated, use auth=github.Auth.AppAuth(...) instead
        :param jwt_issued_at: int deprecated, use auth=github.Auth.AppAuth(...) instead
        :param jwt_algorithm: string deprecated, use auth=github.Auth.AppAuth(...) instead
        :param auth: authentication method
        """
        if integration_id is not None:
            assert isinstance(integration_id, (int, str)), integration_id
        if private_key is not None:
            assert isinstance(private_key, str), "supplied private key should be a string"
        assert isinstance(base_url, str), base_url
        assert isinstance(timeout, int), timeout
        assert user_agent is None or isinstance(user_agent, str), user_agent
        assert isinstance(per_page, int), per_page
        assert isinstance(verify, (bool, str)), verify
        assert retry is None or isinstance(retry, int) or isinstance(retry, urllib3.util.Retry), retry
        assert pool_size is None or isinstance(pool_size, int), pool_size
        assert seconds_between_requests is None or seconds_between_requests >= 0
        assert seconds_between_writes is None or seconds_between_writes >= 0
        assert isinstance(jwt_expiry, int), jwt_expiry
        assert Consts.MIN_JWT_EXPIRY <= jwt_expiry <= Consts.MAX_JWT_EXPIRY, jwt_expiry
        assert isinstance(jwt_issued_at, int)

        self.base_url = base_url

        if (
            integration_id is not None
            or private_key is not None
            or jwt_expiry != Consts.DEFAULT_JWT_EXPIRY
            or jwt_issued_at != Consts.DEFAULT_JWT_ISSUED_AT
            or jwt_algorithm != Consts.DEFAULT_JWT_ALGORITHM
        ):
            warnings.warn(
                "Arguments integration_id, private_key, jwt_expiry, jwt_issued_at and jwt_algorithm are deprecated, "
                "please use auth=github.Auth.AppAuth(...) instead",
                category=DeprecationWarning,
            )
            auth = AppAuth(
                integration_id,  # type: ignore
                private_key,  # type: ignore
                jwt_expiry=jwt_expiry,
                jwt_issued_at=jwt_issued_at,
                jwt_algorithm=jwt_algorithm,
            )

        assert isinstance(
            auth, AppAuth
        ), f"GithubIntegration requires github.Auth.AppAuth authentication, not {type(auth)}"

        self.auth = auth

        self.__requester = Requester(
            auth=auth,
            base_url=self.base_url,
            timeout=timeout,
            user_agent=user_agent,
            per_page=per_page,
            verify=verify,
            retry=retry,
            pool_size=pool_size,
            seconds_between_requests=seconds_between_requests,
            seconds_between_writes=seconds_between_writes,
        )

    def close(self) -> None:
        """Close connections to the server. Alternatively, use the
        GithubIntegration object as a context manager:

        .. code-block:: python

          with github.GithubIntegration(...) as gi:
            # do something
        """
        self.__requester.close()

    def __enter__(self) -> GithubIntegration:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()

    def get_github_for_installation(
        self, installation_id: int, token_permissions: dict[str, str] | None = None
    ) -> github.Github:
        # The installation has to authenticate as an installation, not an app
        auth = self.auth.get_installation_auth(installation_id, token_permissions, self.__requester)
        return github.Github(**self.__requester.withAuth(auth).kwargs)

    @property
    def requester(self) -> Requester:
        """
        Return my Requester object.

        For example, to make requests to API endpoints not yet supported by PyGitHub.

        """
        return self.__requester

    def _get_headers(self) -> dict[str, str]:
        """
        Get headers for the requests.
        """
        return {
            "Accept": Consts.mediaTypeIntegrationPreview,
        }

    def _get_installed_app(self, url: str) -> Installation:
        """
        Get installation for the given URL.
        """
        headers, response = self.__requester.requestJsonAndCheck("GET", url, headers=self._get_headers())

        return Installation(
            requester=self.__requester,
            headers=headers,
            attributes=response,
            completed=True,
        )

    @deprecated.deprecated(
        "Use github.Github(auth=github.Auth.AppAuth), github.Auth.AppAuth.token or github.Auth.AppAuth.create_jwt(expiration) instead"
    )
    def create_jwt(self, expiration: int | None = None) -> str:
        """
        Create a signed JWT
        https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app
        """
        return self.auth.create_jwt(expiration)

    def get_access_token(
        self, installation_id: int, permissions: dict[str, str] | None = None
    ) -> InstallationAuthorization:
        """
        :calls: `POST /app/installations/{installation_id}/access_tokens <https://docs.github.com/en/rest/apps/apps#create-an-installation-access-token-for-an-app>`
        """
        if permissions is None:
            permissions = {}

        if not isinstance(permissions, dict):
            raise GithubException(status=400, data={"message": "Invalid permissions"}, headers=None)

        body = {"permissions": permissions}
        headers, response = self.__requester.requestJsonAndCheck(
            "POST",
            f"/app/installations/{installation_id}/access_tokens",
            headers=self._get_headers(),
            input=body,
        )

        return InstallationAuthorization(
            requester=self.__requester,
            headers=headers,
            attributes=response,
            completed=True,
        )

    @deprecated.deprecated("Use get_repo_installation")
    def get_installation(self, owner: str, repo: str) -> Installation:
        """
        Deprecated by get_repo_installation.

        :calls:`GET /repos/{owner}/{repo}/installation <https://docs.github.com/en/rest/reference/apps#get-a-repository-
        installation-for-the-authenticated-app>`
        :calls:`GET /repos/{owner}/{repo}/installation <https://docs.github.com/en/rest/reference/apps#get-a-repository-
        installation-for-the-authenticated-app>`

        """
        owner = urllib.parse.quote(owner)
        repo = urllib.parse.quote(repo)
        return self._get_installed_app(url=f"/repos/{owner}/{repo}/installation")

    def get_installations(self) -> PaginatedList[Installation]:
        """
        :calls: GET /app/installations <https://docs.github.com/en/rest/reference/apps#list-installations-for-the-authenticated-app>
        """
        return PaginatedList(
            contentClass=Installation,
            requester=self.__requester,
            firstUrl="/app/installations",
            firstParams=None,
            headers=self._get_headers(),
            list_item="installations",
        )

    def get_org_installation(self, org: str) -> Installation:
        """
        :calls: `GET /orgs/{org}/installation <https://docs.github.com/en/rest/apps/apps#get-an-organization-installation-for-the-authenticated-app>`
        """
        org = urllib.parse.quote(org)
        return self._get_installed_app(url=f"/orgs/{org}/installation")

    def get_repo_installation(self, owner: str, repo: str) -> Installation:
        """
        :calls: `GET /repos/{owner}/{repo}/installation <https://docs.github.com/en/rest/reference/apps#get-a-repository-installation-for-the-authenticated-app>`
        """
        owner = urllib.parse.quote(owner)
        repo = urllib.parse.quote(repo)
        return self._get_installed_app(url=f"/repos/{owner}/{repo}/installation")

    def get_user_installation(self, username: str) -> Installation:
        """
        :calls: `GET /users/{username}/installation <https://docs.github.com/en/rest/apps/apps#get-a-user-installation-for-the-authenticated-app>`
        """
        username = urllib.parse.quote(username)
        return self._get_installed_app(url=f"/users/{username}/installation")

    def get_app_installation(self, installation_id: int) -> Installation:
        """
        :calls: `GET /app/installations/{installation_id} <https://docs.github.com/en/rest/apps/apps#get-an-installation-for-the-authenticated-app>`
        """
        return self._get_installed_app(url=f"/app/installations/{installation_id}")

    def get_app(self) -> GithubApp:
        """
        :calls: `GET /app <https://docs.github.com/en/rest/reference/apps#get-the-authenticated-app>`_
        """

        headers, data = self.__requester.requestJsonAndCheck("GET", "/app", headers=self._get_headers())
        return GithubApp(requester=self.__requester, headers=headers, attributes=data, completed=True)
