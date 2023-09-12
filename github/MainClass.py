############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Ed Jackson <ed.jackson@gmail.com>                             #
# Copyright 2013 Jonathan J Hunt <hunt@braincorporation.com>                   #
# Copyright 2013 Peter Golm <golm.peter@gmail.com>                             #
# Copyright 2013 Steve Brown <steve@evolvedlight.co.uk>                        #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 C. R. Oldham <cro@ncbt.org>                                   #
# Copyright 2014 Thialfihar <thi@thialfihar.org>                               #
# Copyright 2014 Tyler Treat <ttreat31@gmail.com>                              #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Daniel Pocock <daniel@pocock.pro>                             #
# Copyright 2015 Joseph Rawson <joseph.rawson.works@littledebian.org>          #
# Copyright 2015 Uriel Corfa <uriel@corfa.fr>                                  #
# Copyright 2015 edhollandAL <eholland@alertlogic.com>                         #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Colin Hoglund <colinhoglund@users.noreply.github.com>         #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2018 Agor Maxime <maxime.agor23@gmail.com>                         #
# Copyright 2018 Joshua Hoblitt <josh@hoblitt.com>                             #
# Copyright 2018 Maarten Fonville <mfonville@users.noreply.github.com>         #
# Copyright 2018 Mike Miller <github@mikeage.net>                              #
# Copyright 2018 Svend Sorensen <svend@svends.net>                             #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2018 itsbruce <it.is.bruce@gmail.com>                              #
# Copyright 2019 Tomas Tomecek <tomas@tomecek.net>                             #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
# Copyright 2023 Yugo Hino <henom06@gmail.com>                                 #
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

import pickle
import warnings
from datetime import datetime
from typing import TYPE_CHECKING, Any, BinaryIO, TypeVar

import urllib3
from urllib3.util import Retry

import github.ApplicationOAuth
import github.Auth
import github.AuthenticatedUser
import github.Enterprise
import github.Event
import github.Gist
import github.GithubApp
import github.GithubIntegration
import github.GithubRetry
import github.GitignoreTemplate
import github.License
import github.NamedUser
import github.Topic
from github import Consts
from github.GithubIntegration import GithubIntegration
from github.GithubObject import GithubObject, NotSet, Opt, is_defined
from github.GithubRetry import GithubRetry
from github.HookDelivery import HookDelivery, HookDeliverySummary
from github.HookDescription import HookDescription
from github.PaginatedList import PaginatedList
from github.RateLimit import RateLimit
from github.Requester import Requester

if TYPE_CHECKING:
    from github.AppAuthentication import AppAuthentication
    from github.ApplicationOAuth import ApplicationOAuth
    from github.AuthenticatedUser import AuthenticatedUser
    from github.Commit import Commit
    from github.ContentFile import ContentFile
    from github.Event import Event
    from github.Gist import Gist
    from github.GithubApp import GithubApp
    from github.GitignoreTemplate import GitignoreTemplate
    from github.Issue import Issue
    from github.License import License
    from github.NamedUser import NamedUser
    from github.Organization import Organization
    from github.Project import Project
    from github.ProjectColumn import ProjectColumn
    from github.Repository import Repository
    from github.Topic import Topic

TGithubObject = TypeVar("TGithubObject", bound=GithubObject)


class Github:
    """
    This is the main class you instantiate to access the Github API v3. Optional parameters allow different authentication methods.
    """

    __requester: Requester

    default_retry = GithubRetry()

    # keep non-deprecated arguments in-sync with Requester
    # v3: remove login_or_token, password, jwt and app_auth
    # v3: move auth to the front of arguments
    # v3: add * before first argument so all arguments must be named,
    #     allows to reorder / add new arguments / remove deprecated arguments without breaking user code
    def __init__(
        self,
        login_or_token: str | None = None,
        password: str | None = None,
        jwt: str | None = None,
        app_auth: AppAuthentication | None = None,
        base_url: str = Consts.DEFAULT_BASE_URL,
        timeout: int = Consts.DEFAULT_TIMEOUT,
        user_agent: str = Consts.DEFAULT_USER_AGENT,
        per_page: int = Consts.DEFAULT_PER_PAGE,
        verify: bool | str = True,
        retry: int | Retry | None = default_retry,
        pool_size: int | None = None,
        seconds_between_requests: float | None = Consts.DEFAULT_SECONDS_BETWEEN_REQUESTS,
        seconds_between_writes: float | None = Consts.DEFAULT_SECONDS_BETWEEN_WRITES,
        auth: github.Auth.Auth | None = None,
    ) -> None:
        """
        :param login_or_token: string deprecated, use auth=github.Auth.Login(...) or auth=github.Auth.Token(...) instead
        :param password: string deprecated, use auth=github.Auth.Login(...) instead
        :param jwt: string deprecated, use auth=github.Auth.AppAuth(...) or auth=github.Auth.AppAuthToken(...) instead
        :param app_auth: github.AppAuthentication deprecated, use auth=github.Auth.AppInstallationAuth(...) instead
        :param base_url: string
        :param timeout: integer
        :param user_agent: string
        :param per_page: int
        :param verify: boolean or string
        :param retry: int or urllib3.util.retry.Retry object,
                      defaults to github.Github.default_retry,
                      set to None to disable retries
        :param pool_size: int
        :param seconds_between_requests: float
        :param seconds_between_writes: float
        :param auth: authentication method
        """

        assert login_or_token is None or isinstance(login_or_token, str), login_or_token
        assert password is None or isinstance(password, str), password
        assert jwt is None or isinstance(jwt, str), jwt
        assert isinstance(base_url, str), base_url
        assert isinstance(timeout, int), timeout
        assert user_agent is None or isinstance(user_agent, str), user_agent
        assert isinstance(per_page, int), per_page
        assert isinstance(verify, (bool, str)), verify
        assert retry is None or isinstance(retry, int) or isinstance(retry, urllib3.util.Retry), retry
        assert pool_size is None or isinstance(pool_size, int), pool_size
        assert seconds_between_requests is None or seconds_between_requests >= 0
        assert seconds_between_writes is None or seconds_between_writes >= 0
        assert auth is None or isinstance(auth, github.Auth.Auth), auth

        if password is not None:
            warnings.warn(
                "Arguments login_or_token and password are deprecated, please use "
                "auth=github.Auth.Login(...) instead",
                category=DeprecationWarning,
            )
            auth = github.Auth.Login(login_or_token, password)  # type: ignore
        elif login_or_token is not None:
            warnings.warn(
                "Argument login_or_token is deprecated, please use " "auth=github.Auth.Token(...) instead",
                category=DeprecationWarning,
            )
            auth = github.Auth.Token(login_or_token)
        elif jwt is not None:
            warnings.warn(
                "Argument jwt is deprecated, please use "
                "auth=github.Auth.AppAuth(...) or "
                "auth=github.Auth.AppAuthToken(...) instead",
                category=DeprecationWarning,
            )
            auth = github.Auth.AppAuthToken(jwt)
        elif app_auth is not None:
            warnings.warn(
                "Argument app_auth is deprecated, please use " "auth=github.Auth.AppInstallationAuth(...) instead",
                category=DeprecationWarning,
            )
            auth = app_auth

        self.__requester = Requester(
            auth,
            base_url,
            timeout,
            user_agent,
            per_page,
            verify,
            retry,
            pool_size,
            seconds_between_requests,
            seconds_between_writes,
        )

    def close(self) -> None:
        """
        Close connections to the server. Alternatively, use the Github object as a context manager:

        .. code-block:: python

          with github.Github(...) as gh:
            # do something
        """
        self.__requester.close()

    def __enter__(self) -> Github:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()

    @property
    def FIX_REPO_GET_GIT_REF(self) -> bool:
        return self.__requester.FIX_REPO_GET_GIT_REF

    @FIX_REPO_GET_GIT_REF.setter
    def FIX_REPO_GET_GIT_REF(self, value: bool) -> None:
        self.__requester.FIX_REPO_GET_GIT_REF = value

    # v3: Remove this property? Why should it be necessary to read/modify it after construction
    @property
    def per_page(self) -> int:
        return self.__requester.per_page

    @per_page.setter
    def per_page(self, value: int) -> None:
        self.__requester.per_page = value

    # v3: Provide a unified way to access values of headers of last response
    # v3: (and add/keep ad hoc properties for specific useful headers like rate limiting, oauth scopes, etc.)
    # v3: Return an instance of a class: using a tuple did not allow to add a field "resettime"
    @property
    def rate_limiting(self) -> tuple[int, int]:
        """
        First value is requests remaining, second value is request limit.
        """
        remaining, limit = self.__requester.rate_limiting
        if limit < 0:
            self.get_rate_limit()
        return self.__requester.rate_limiting

    @property
    def rate_limiting_resettime(self) -> int:
        """
        Unix timestamp indicating when rate limiting will reset.
        """
        if self.__requester.rate_limiting_resettime == 0:
            self.get_rate_limit()
        return self.__requester.rate_limiting_resettime

    def get_rate_limit(self) -> RateLimit:
        """
        Rate limit status for different resources (core/search/graphql).

        :calls: `GET /rate_limit <https://docs.github.com/en/rest/reference/rate-limit>`_
        """
        headers, data = self.__requester.requestJsonAndCheck("GET", "/rate_limit")
        return RateLimit(self.__requester, headers, data["resources"], True)

    @property
    def oauth_scopes(self) -> list[str] | None:
        """
        :type: list of string
        """
        return self.__requester.oauth_scopes

    def get_license(self, key: Opt[str] = NotSet) -> License:
        """
        :calls: `GET /license/{license} <https://docs.github.com/en/rest/reference/licenses#get-a-license>`_
        """

        assert isinstance(key, str), key
        headers, data = self.__requester.requestJsonAndCheck("GET", f"/licenses/{key}")
        return github.License.License(self.__requester, headers, data, completed=True)

    def get_licenses(self) -> PaginatedList[License]:
        """
        :calls: `GET /licenses <https://docs.github.com/en/rest/reference/licenses#get-all-commonly-used-licenses>`_
        """

        url_parameters: dict[str, Any] = {}

        return PaginatedList(github.License.License, self.__requester, "/licenses", url_parameters)

    def get_events(self) -> PaginatedList[Event]:
        """
        :calls: `GET /events <https://docs.github.com/en/rest/reference/activity#list-public-events>`_
        """

        return PaginatedList(github.Event.Event, self.__requester, "/events", None)

    def get_user(self, login: Opt[str] = NotSet) -> NamedUser | AuthenticatedUser:
        """
        :calls: `GET /users/{user} <https://docs.github.com/en/rest/reference/users>`_ or `GET /user <https://docs.github.com/en/rest/reference/users>`_
        """
        assert login is NotSet or isinstance(login, str), login
        if login is NotSet:
            return github.AuthenticatedUser.AuthenticatedUser(self.__requester, {}, {"url": "/user"}, completed=False)
        else:
            headers, data = self.__requester.requestJsonAndCheck("GET", f"/users/{login}")
            return github.NamedUser.NamedUser(self.__requester, headers, data, completed=True)

    def get_user_by_id(self, user_id: int) -> NamedUser:
        """
        :calls: `GET /user/{id} <https://docs.github.com/en/rest/reference/users>`_
        :param user_id: int
        :rtype: :class:`github.NamedUser.NamedUser`
        """
        assert isinstance(user_id, int), user_id
        headers, data = self.__requester.requestJsonAndCheck("GET", f"/user/{user_id}")
        return github.NamedUser.NamedUser(self.__requester, headers, data, completed=True)

    def get_users(self, since: Opt[int] = NotSet) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /users <https://docs.github.com/en/rest/reference/users>`_
        """
        assert since is NotSet or isinstance(since, int), since
        url_parameters = dict()
        if since is not NotSet:
            url_parameters["since"] = since
        return PaginatedList(github.NamedUser.NamedUser, self.__requester, "/users", url_parameters)

    def get_organization(self, login: str) -> Organization:
        """
        :calls: `GET /orgs/{org} <https://docs.github.com/en/rest/reference/orgs>`_
        """
        assert isinstance(login, str), login
        headers, data = self.__requester.requestJsonAndCheck("GET", f"/orgs/{login}")
        return github.Organization.Organization(self.__requester, headers, data, completed=True)

    def get_organizations(self, since: Opt[int] = NotSet) -> PaginatedList[Organization]:
        """
        :calls: `GET /organizations <https://docs.github.com/en/rest/reference/orgs#list-organizations>`_
        """
        assert since is NotSet or isinstance(since, int), since
        url_parameters = dict()
        if since is not NotSet:
            url_parameters["since"] = since
        return PaginatedList(
            github.Organization.Organization,
            self.__requester,
            "/organizations",
            url_parameters,
        )

    def get_enterprise(self, enterprise: str) -> github.Enterprise.Enterprise:
        """
        :calls: `GET /enterprises/{enterprise} <https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin>`_
        :param enterprise: string
        :rtype: :class:`Enterprise`
        """
        assert isinstance(enterprise, str), enterprise
        # There is no native "/enterprises/{enterprise}" api, so this function is a hub for apis that start with "/enterprise/{enterprise}".
        return github.Enterprise.Enterprise(self.__requester, enterprise)

    def get_repo(self, full_name_or_id: int | str, lazy: bool = False) -> Repository:
        """
        :calls: `GET /repos/{owner}/{repo} <https://docs.github.com/en/rest/reference/repos>`_ or `GET /repositories/{id} <https://docs.github.com/en/rest/reference/repos>`_
        """
        assert isinstance(full_name_or_id, (str, int)), full_name_or_id
        url_base = "/repositories/" if isinstance(full_name_or_id, int) else "/repos/"
        url = f"{url_base}{full_name_or_id}"
        if lazy:
            return github.Repository.Repository(self.__requester, {}, {"url": url}, completed=False)
        headers, data = self.__requester.requestJsonAndCheck("GET", url)
        return github.Repository.Repository(self.__requester, headers, data, completed=True)

    def get_repos(
        self,
        since: Opt[int] = NotSet,
        visibility: Opt[str] = NotSet,
    ) -> PaginatedList[Repository]:
        """
        :calls: `GET /repositories <https://docs.github.com/en/rest/reference/repos#list-public-repositories>`_
        :param since: integer
        :param visibility: string ('all','public')
        """
        assert since is NotSet or isinstance(since, int), since
        url_parameters: dict[str, Any] = {}
        if since is not NotSet:
            url_parameters["since"] = since
        if visibility is not NotSet:
            assert visibility in ("public", "all"), visibility
            url_parameters["visibility"] = visibility
        return PaginatedList(
            github.Repository.Repository,
            self.__requester,
            "/repositories",
            url_parameters,
        )

    def get_project(self, id: int) -> Project:
        """
        :calls: `GET /projects/{project_id} <https://docs.github.com/en/rest/reference/projects#get-a-project>`_
        """
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            f"/projects/{id:d}",
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        return github.Project.Project(self.__requester, headers, data, completed=True)

    def get_project_column(self, id: int) -> ProjectColumn:
        """
        :calls: `GET /projects/columns/{column_id} <https://docs.github.com/en/rest/reference/projects#get-a-project-column>`_
        """
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/projects/columns/%d" % id,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        return github.ProjectColumn.ProjectColumn(self.__requester, headers, data, completed=True)

    def get_gist(self, id: str) -> Gist:
        """
        :calls: `GET /gists/{id} <https://docs.github.com/en/rest/reference/gists>`_
        """
        assert isinstance(id, str), id
        headers, data = self.__requester.requestJsonAndCheck("GET", f"/gists/{id}")
        return github.Gist.Gist(self.__requester, headers, data, completed=True)

    def get_gists(self, since: Opt[datetime] = NotSet) -> PaginatedList[Gist]:
        """
        :calls: `GET /gists/public <https://docs.github.com/en/rest/reference/gists>`_
        """
        assert since is NotSet or isinstance(since, datetime), since
        url_parameters = dict()
        if is_defined(since):
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return PaginatedList(github.Gist.Gist, self.__requester, "/gists/public", url_parameters)

    def search_repositories(
        self,
        query: str,
        sort: Opt[str] = NotSet,
        order: Opt[str] = NotSet,
        **qualifiers: Any,
    ) -> PaginatedList[Repository]:
        """
        :calls: `GET /search/repositories <https://docs.github.com/en/rest/reference/search>`_
        :param query: string
        :param sort: string ('stars', 'forks', 'updated')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        """
        assert isinstance(query, str), query
        url_parameters = dict()
        if sort is not NotSet:  # pragma no branch (Should be covered)
            assert sort in ("stars", "forks", "updated"), sort
            url_parameters["sort"] = sort
        if order is not NotSet:  # pragma no branch (Should be covered)
            assert order in ("asc", "desc"), order
            url_parameters["order"] = order

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append(f"{qualifier}:{value}")

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return PaginatedList(
            github.Repository.Repository,
            self.__requester,
            "/search/repositories",
            url_parameters,
        )

    def search_users(
        self,
        query: str,
        sort: Opt[str] = NotSet,
        order: Opt[str] = NotSet,
        **qualifiers: Any,
    ) -> PaginatedList[NamedUser]:
        """
        :calls: `GET /search/users <https://docs.github.com/en/rest/reference/search>`_
        :param query: string
        :param sort: string ('followers', 'repositories', 'joined')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        assert isinstance(query, str), query
        url_parameters = dict()
        if sort is not NotSet:
            assert sort in ("followers", "repositories", "joined"), sort
            url_parameters["sort"] = sort
        if order is not NotSet:
            assert order in ("asc", "desc"), order
            url_parameters["order"] = order

        query_chunks = []
        if query:
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append(f"{qualifier}:{value}")

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return PaginatedList(
            github.NamedUser.NamedUser,
            self.__requester,
            "/search/users",
            url_parameters,
        )

    def search_issues(
        self,
        query: str,
        sort: Opt[str] = NotSet,
        order: Opt[str] = NotSet,
        **qualifiers: Any,
    ) -> PaginatedList[Issue]:
        """
        :calls: `GET /search/issues <https://docs.github.com/en/rest/reference/search>`_
        :param query: string
        :param sort: string ('comments', 'created', 'updated')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`PaginatedList` of :class:`github.Issue.Issue`
        """
        assert isinstance(query, str), query
        url_parameters = dict()
        if sort is not NotSet:
            assert sort in ("comments", "created", "updated"), sort
            url_parameters["sort"] = sort
        if order is not NotSet:
            assert order in ("asc", "desc"), order
            url_parameters["order"] = order

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append(f"{qualifier}:{value}")

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return PaginatedList(github.Issue.Issue, self.__requester, "/search/issues", url_parameters)

    def search_code(
        self,
        query: str,
        sort: Opt[str] = NotSet,
        order: Opt[str] = NotSet,
        highlight: bool = False,
        **qualifiers: Any,
    ) -> PaginatedList[ContentFile]:
        """
        :calls: `GET /search/code <https://docs.github.com/en/rest/reference/search>`_
        :param query: string
        :param sort: string ('indexed')
        :param order: string ('asc', 'desc')
        :param highlight: boolean (True, False)
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`PaginatedList` of :class:`github.ContentFile.ContentFile`
        """
        assert isinstance(query, str), query
        url_parameters = dict()
        if sort is not NotSet:  # pragma no branch (Should be covered)
            assert sort in ("indexed",), sort
            url_parameters["sort"] = sort
        if order is not NotSet:  # pragma no branch (Should be covered)
            assert order in ("asc", "desc"), order
            url_parameters["order"] = order

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append(f"{qualifier}:{value}")

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        headers = {"Accept": Consts.highLightSearchPreview} if highlight else None

        return PaginatedList(
            github.ContentFile.ContentFile,
            self.__requester,
            "/search/code",
            url_parameters,
            headers=headers,
        )

    def search_commits(
        self,
        query: str,
        sort: Opt[str] = NotSet,
        order: Opt[str] = NotSet,
        **qualifiers: Any,
    ) -> PaginatedList[Commit]:
        """
        :calls: `GET /search/commits <https://docs.github.com/en/rest/reference/search>`_
        :param query: string
        :param sort: string ('author-date', 'committer-date')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`PaginatedList` of :class:`github.Commit.Commit`
        """
        assert isinstance(query, str), query
        url_parameters = dict()
        if sort is not NotSet:
            assert sort in ("author-date", "committer-date"), sort
            url_parameters["sort"] = sort
        if order is not NotSet:
            assert order in ("asc", "desc"), order
            url_parameters["order"] = order

        query_chunks = []
        if query:
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append(f"{qualifier}:{value}")

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return PaginatedList(
            github.Commit.Commit,
            self.__requester,
            "/search/commits",
            url_parameters,
            headers={"Accept": Consts.mediaTypeCommitSearchPreview},
        )

    def search_topics(self, query: str, **qualifiers: Any) -> PaginatedList[Topic]:
        """
        :calls: `GET /search/topics <https://docs.github.com/en/rest/reference/search>`_
        :param query: string
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`PaginatedList` of :class:`github.Topic.Topic`
        """
        assert isinstance(query, str), query
        url_parameters = dict()

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append(f"{qualifier}:{value}")

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return PaginatedList(
            github.Topic.Topic,
            self.__requester,
            "/search/topics",
            url_parameters,
            headers={"Accept": Consts.mediaTypeTopicsPreview},
        )

    def render_markdown(self, text: str, context: Opt[Repository] = NotSet) -> str:
        """
        :calls: `POST /markdown <https://docs.github.com/en/rest/reference/markdown>`_
        :param text: string
        :param context: :class:`github.Repository.Repository`
        :rtype: string
        """
        assert isinstance(text, str), text
        assert context is NotSet or isinstance(context, github.Repository.Repository), context
        post_parameters = {"text": text}
        if is_defined(context):
            post_parameters["mode"] = "gfm"
            post_parameters["context"] = context._identity
        status, headers, data = self.__requester.requestJson("POST", "/markdown", input=post_parameters)
        return data

    def get_hook(self, name: str) -> HookDescription:
        """
        :calls: `GET /hooks/{name} <https://docs.github.com/en/rest/reference/repos#webhooks>`_
        """
        assert isinstance(name, str), name
        headers, attributes = self.__requester.requestJsonAndCheck("GET", f"/hooks/{name}")
        return HookDescription(self.__requester, headers, attributes, completed=True)

    def get_hooks(self) -> list[HookDescription]:
        """
        :calls: `GET /hooks <https://docs.github.com/en/rest/reference/repos#webhooks>`_
        :rtype: list of :class:`github.HookDescription.HookDescription`
        """
        headers, data = self.__requester.requestJsonAndCheck("GET", "/hooks")
        return [HookDescription(self.__requester, headers, attributes, completed=True) for attributes in data]

    def get_hook_delivery(self, hook_id: int, delivery_id: int) -> HookDelivery:
        """
        :calls: `GET /hooks/{hook_id}/deliveries/{delivery_id} <https://docs.github.com/en/rest/reference/repos#webhooks>`_
        :param hook_id: integer
        :param delivery_id: integer
        :rtype: :class:`HookDelivery`
        """
        assert isinstance(hook_id, int), hook_id
        assert isinstance(delivery_id, int), delivery_id
        headers, attributes = self.__requester.requestJsonAndCheck("GET", f"/hooks/{hook_id}/deliveries/{delivery_id}")
        return HookDelivery(self.__requester, headers, attributes, completed=True)

    def get_hook_deliveries(self, hook_id: int) -> list[HookDeliverySummary]:
        """
        :calls: `GET /hooks/{hook_id}/deliveries <https://docs.github.com/en/rest/reference/repos#webhooks>`_
        :param hook_id: integer
        :rtype: list of :class:`HookDeliverySummary`
        """
        assert isinstance(hook_id, int), hook_id
        headers, data = self.__requester.requestJsonAndCheck("GET", f"/hooks/{hook_id}/deliveries")
        return [HookDeliverySummary(self.__requester, headers, attributes, completed=True) for attributes in data]

    def get_gitignore_templates(self) -> list[str]:
        """
        :calls: `GET /gitignore/templates <https://docs.github.com/en/rest/reference/gitignore>`_
        """
        headers, data = self.__requester.requestJsonAndCheck("GET", "/gitignore/templates")
        return data

    def get_gitignore_template(self, name: str) -> GitignoreTemplate:
        """
        :calls: `GET /gitignore/templates/{name} <https://docs.github.com/en/rest/reference/gitignore>`_
        """
        assert isinstance(name, str), name
        headers, attributes = self.__requester.requestJsonAndCheck("GET", f"/gitignore/templates/{name}")
        return github.GitignoreTemplate.GitignoreTemplate(self.__requester, headers, attributes, completed=True)

    def get_emojis(self) -> dict[str, str]:
        """
        :calls: `GET /emojis <https://docs.github.com/en/rest/reference/emojis>`_
        :rtype: dictionary of type => url for emoji`
        """
        headers, attributes = self.__requester.requestJsonAndCheck("GET", "/emojis")
        return attributes

    def create_from_raw_data(
        self, klass: type[TGithubObject], raw_data: dict[str, Any], headers: dict[str, str | int] | None = None
    ) -> TGithubObject:
        """
        Creates an object from raw_data previously obtained by :attr:`GithubObject.raw_data`,
        and optionally headers previously obtained by :attr:`GithubObject.raw_headers`.

        :param klass: the class of the object to create
        :param raw_data: dict
        :param headers: dict
        :rtype: instance of class ``klass``
        """
        if headers is None:
            headers = {}

        return klass(self.__requester, headers, raw_data, completed=True)

    def dump(self, obj: GithubObject, file: BinaryIO, protocol: int = 0) -> None:
        """
        Dumps (pickles) a PyGithub object to a file-like object.
        Some effort is made to not pickle sensitive information like the Github credentials used in the :class:`Github` instance.
        But NO EFFORT is made to remove sensitive information from the object's attributes.

        :param obj: the object to pickle
        :param file: the file-like object to pickle to
        :param protocol: the `pickling protocol <https://python.readthedocs.io/en/latest/library/pickle.html#data-stream-format>`_
        """
        pickle.dump((obj.__class__, obj.raw_data, obj.raw_headers), file, protocol)

    def load(self, f: BinaryIO) -> Any:
        """
        Loads (unpickles) a PyGithub object from a file-like object.

        :param f: the file-like object to unpickle from
        :return: the unpickled object
        """
        return self.create_from_raw_data(*pickle.load(f))

    def get_oauth_application(self, client_id: str, client_secret: str) -> ApplicationOAuth:
        return github.ApplicationOAuth.ApplicationOAuth(
            self.__requester,
            headers={},
            attributes={"client_id": client_id, "client_secret": client_secret},
            completed=False,
        )

    def get_app(self, slug: Opt[str] = NotSet) -> GithubApp:
        """
        :calls: `GET /apps/{slug} <https://docs.github.com/en/rest/reference/apps>`_ or `GET /app <https://docs.github.com/en/rest/reference/apps>`_
        """
        assert slug is NotSet or isinstance(slug, str), slug

        if slug is NotSet:
            # with no slug given, calling /app returns the authenticated app,
            # including the actual /apps/{slug}
            warnings.warn(
                "Argument slug is mandatory, calling this method without the slug argument is deprecated, please use "
                "github.GithubIntegration(auth=github.Auth.AppAuth(...)).get_app() instead",
                category=DeprecationWarning,
            )
            return GithubIntegration(**self.__requester.kwargs).get_app()
        else:
            # with a slug given, we can lazily load the GithubApp
            return github.GithubApp.GithubApp(self.__requester, {}, {"url": f"/apps/{slug}"}, completed=False)
