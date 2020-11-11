# -*- coding: utf-8 -*-

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
import pickle
import time
import warnings

import jwt
import requests
import urllib3

import github.ApplicationOAuth
import github.Event
import github.Gist
import github.GithubObject
import github.License
import github.NamedUser
import github.PaginatedList
import github.Topic

from . import (
    AuthenticatedUser,
    Consts,
    GithubApp,
    GithubException,
    GitignoreTemplate,
    HookDescription,
    Installation,
    InstallationAuthorization,
    RateLimit,
    Repository,
)
from .Requester import Requester

DEFAULT_BASE_URL = "https://api.github.com"
DEFAULT_STATUS_URL = "https://status.github.com"
# As of 2018-05-17, Github imposes a 10s limit for completion of API requests.
# Thus, the timeout should be slightly > 10s to account for network/front-end
# latency.
DEFAULT_TIMEOUT = 15
DEFAULT_PER_PAGE = 30


class Github(object):
    """
    This is the main class you instantiate to access the Github API v3. Optional parameters allow different authentication methods.
    """

    def __init__(
        self,
        login_or_token=None,
        password=None,
        jwt=None,
        base_url=DEFAULT_BASE_URL,
        timeout=DEFAULT_TIMEOUT,
        client_id=None,
        client_secret=None,
        user_agent="PyGithub/Python",
        per_page=DEFAULT_PER_PAGE,
        verify=True,
        retry=None,
    ):
        """
        :param login_or_token: string
        :param password: string
        :param base_url: string
        :param timeout: integer
        :param client_id: string
        :param client_secret: string
        :param user_agent: string
        :param per_page: int
        :param verify: boolean or string
        :param retry: int or urllib3.util.retry.Retry object
        """

        assert login_or_token is None or isinstance(login_or_token, str), login_or_token
        assert password is None or isinstance(password, str), password
        assert jwt is None or isinstance(jwt, str), jwt
        assert isinstance(base_url, str), base_url
        assert isinstance(timeout, int), timeout
        assert client_id is None or isinstance(client_id, str), client_id
        assert client_secret is None or isinstance(client_secret, str), client_secret
        assert user_agent is None or isinstance(user_agent, str), user_agent
        assert (
            retry is None
            or isinstance(retry, (int))
            or isinstance(retry, (urllib3.util.Retry))
        )
        if client_id is not None or client_secret is not None:
            warnings.warn(
                "client_id and client_secret are deprecated and will be removed in a future release, switch to token authentication",
                FutureWarning,
                stacklevel=2,
            )
        self.__requester = Requester(
            login_or_token,
            password,
            jwt,
            base_url,
            timeout,
            client_id,
            client_secret,
            user_agent,
            per_page,
            verify,
            retry,
        )

    def __get_FIX_REPO_GET_GIT_REF(self):
        """
        :type: bool
        """
        return self.__requester.FIX_REPO_GET_GIT_REF

    def __set_FIX_REPO_GET_GIT_REF(self, value):
        self.__requester.FIX_REPO_GET_GIT_REF = value

    FIX_REPO_GET_GIT_REF = property(
        __get_FIX_REPO_GET_GIT_REF, __set_FIX_REPO_GET_GIT_REF
    )

    def __get_per_page(self):
        """
        :type: int
        """
        return self.__requester.per_page

    def __set_per_page(self, value):
        self.__requester.per_page = value

    # v2: Remove this property? Why should it be necessary to read/modify it after construction
    per_page = property(__get_per_page, __set_per_page)

    # v2: Provide a unified way to access values of headers of last response
    # v2: (and add/keep ad hoc properties for specific useful headers like rate limiting, oauth scopes, etc.)
    # v2: Return an instance of a class: using a tuple did not allow to add a field "resettime"
    @property
    def rate_limiting(self):
        """
        First value is requests remaining, second value is request limit.

        :type: (int, int)
        """
        remaining, limit = self.__requester.rate_limiting
        if limit < 0:
            self.get_rate_limit()
        return self.__requester.rate_limiting

    @property
    def rate_limiting_resettime(self):
        """
        Unix timestamp indicating when rate limiting will reset.

        :type: int
        """
        if self.__requester.rate_limiting_resettime == 0:
            self.get_rate_limit()
        return self.__requester.rate_limiting_resettime

    def get_rate_limit(self):
        """
        Rate limit status for different resources (core/search/graphql).

        :calls: `GET /rate_limit <http://developer.github.com/v3/rate_limit>`_
        :rtype: :class:`github.RateLimit.RateLimit`
        """
        headers, data = self.__requester.requestJsonAndCheck("GET", "/rate_limit")
        return RateLimit.RateLimit(self.__requester, headers, data["resources"], True)

    @property
    def oauth_scopes(self):
        """
        :type: list of string
        """
        return self.__requester.oauth_scopes

    def get_license(self, key=github.GithubObject.NotSet):
        """
        :calls: `GET /license/:license <https://developer.github.com/v3/licenses/#get-an-individual-license>`_
        :param key: string
        :rtype: :class:`github.License.License`
        """

        assert isinstance(key, str), key
        headers, data = self.__requester.requestJsonAndCheck("GET", "/licenses/" + key)
        return github.License.License(self.__requester, headers, data, completed=True)

    def get_licenses(self):
        """
        :calls: `GET /licenses <https://developer.github.com/v3/licenses/#list-all-licenses>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.License.License`
        """

        url_parameters = dict()

        return github.PaginatedList.PaginatedList(
            github.License.License, self.__requester, "/licenses", url_parameters
        )

    def get_events(self):
        """
        :calls: `GET /events <https://developer.github.com/v3/activity/events/#list-public-events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Event.Event`
        """

        return github.PaginatedList.PaginatedList(
            github.Event.Event, self.__requester, "/events", None
        )

    def get_user(self, login=github.GithubObject.NotSet):
        """
        :calls: `GET /users/:user <http://developer.github.com/v3/users>`_ or `GET /user <http://developer.github.com/v3/users>`_
        :param login: string
        :rtype: :class:`github.NamedUser.NamedUser` or :class:`github.AuthenticatedUser.AuthenticatedUser`
        """
        assert login is github.GithubObject.NotSet or isinstance(login, str), login
        if login is github.GithubObject.NotSet:
            return AuthenticatedUser.AuthenticatedUser(
                self.__requester, {}, {"url": "/user"}, completed=False
            )
        else:
            headers, data = self.__requester.requestJsonAndCheck(
                "GET", "/users/" + login
            )
            return github.NamedUser.NamedUser(
                self.__requester, headers, data, completed=True
            )

    def get_user_by_id(self, user_id):
        """
        :calls: `GET /user/:id <http://developer.github.com/v3/users>`_
        :param user_id: int
        :rtype: :class:`github.NamedUser.NamedUser`
        """
        assert isinstance(user_id, int), user_id
        headers, data = self.__requester.requestJsonAndCheck(
            "GET", "/user/" + str(user_id)
        )
        return github.NamedUser.NamedUser(
            self.__requester, headers, data, completed=True
        )

    def get_users(self, since=github.GithubObject.NotSet):
        """
        :calls: `GET /users <http://developer.github.com/v3/users>`_
        :param since: integer
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        assert since is github.GithubObject.NotSet or isinstance(since, int), since
        url_parameters = dict()
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser, self.__requester, "/users", url_parameters
        )

    def get_organization(self, login):
        """
        :calls: `GET /orgs/:org <http://developer.github.com/v3/orgs>`_
        :param login: string
        :rtype: :class:`github.Organization.Organization`
        """
        assert isinstance(login, str), login
        headers, data = self.__requester.requestJsonAndCheck("GET", "/orgs/" + login)
        return github.Organization.Organization(
            self.__requester, headers, data, completed=True
        )

    def get_organizations(self, since=github.GithubObject.NotSet):
        """
        :calls: `GET /organizations <http://developer.github.com/v3/orgs#list-all-organizations>`_
        :param since: integer
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Organization.Organization`
        """
        assert since is github.GithubObject.NotSet or isinstance(since, int), since
        url_parameters = dict()
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since
        return github.PaginatedList.PaginatedList(
            github.Organization.Organization,
            self.__requester,
            "/organizations",
            url_parameters,
        )

    def get_repo(self, full_name_or_id, lazy=False):
        """
        :calls: `GET /repos/:owner/:repo <http://developer.github.com/v3/repos>`_ or `GET /repositories/:id <http://developer.github.com/v3/repos>`_
        :rtype: :class:`github.Repository.Repository`
        """
        assert isinstance(full_name_or_id, (str, int)), full_name_or_id
        url_base = "/repositories/" if isinstance(full_name_or_id, int) else "/repos/"
        url = "%s%s" % (url_base, full_name_or_id)
        if lazy:
            return Repository.Repository(
                self.__requester, {}, {"url": url}, completed=False
            )
        headers, data = self.__requester.requestJsonAndCheck(
            "GET", "%s%s" % (url_base, full_name_or_id)
        )
        return Repository.Repository(self.__requester, headers, data, completed=True)

    def get_repos(
        self, since=github.GithubObject.NotSet, visibility=github.GithubObject.NotSet
    ):
        """
        :calls: `GET /repositories <http://developer.github.com/v3/repos/#list-all-public-repositories>`_
        :param since: integer
        :param visibility: string ('all','public')
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        assert since is github.GithubObject.NotSet or isinstance(since, int), since
        url_parameters = dict()
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since
        if visibility is not github.GithubObject.NotSet:
            assert visibility in ("public", "all"), visibility
            url_parameters["visibility"] = visibility
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self.__requester,
            "/repositories",
            url_parameters,
        )

    def get_project(self, id):
        """
        :calls: `GET /projects/:project_id <https://developer.github.com/v3/projects/#get-a-project>`_
        :rtype: :class:`github.Project.Project`
        :param id: integer
        """
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/projects/%d" % (id),
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        return github.Project.Project(self.__requester, headers, data, completed=True)

    def get_project_column(self, id):
        """
        :calls: `GET /projects/columns/:column_id <https://developer.github.com/v3/projects/columns/#get-a-project-column>`_
        :rtype: :class:`github.ProjectColumn.ProjectColumn`
        :param id: integer
        """
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/projects/columns/%d" % id,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        return github.ProjectColumn.ProjectColumn(
            self.__requester, headers, data, completed=True
        )

    def get_gist(self, id):
        """
        :calls: `GET /gists/:id <http://developer.github.com/v3/gists>`_
        :param id: string
        :rtype: :class:`github.Gist.Gist`
        """
        assert isinstance(id, str), id
        headers, data = self.__requester.requestJsonAndCheck("GET", "/gists/" + id)
        return github.Gist.Gist(self.__requester, headers, data, completed=True)

    def get_gists(self, since=github.GithubObject.NotSet):
        """
        :calls: `GET /gists/public <http://developer.github.com/v3/gists>`_
        :param since: datetime.datetime format YYYY-MM-DDTHH:MM:SSZ
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Gist.Gist`
        """
        assert since is github.GithubObject.NotSet or isinstance(
            since, datetime.datetime
        ), since
        url_parameters = dict()
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.Gist.Gist, self.__requester, "/gists/public", url_parameters
        )

    def search_repositories(
        self,
        query,
        sort=github.GithubObject.NotSet,
        order=github.GithubObject.NotSet,
        **qualifiers
    ):
        """
        :calls: `GET /search/repositories <http://developer.github.com/v3/search>`_
        :param query: string
        :param sort: string ('stars', 'forks', 'updated')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        assert isinstance(query, str), query
        url_parameters = dict()
        if (
            sort is not github.GithubObject.NotSet
        ):  # pragma no branch (Should be covered)
            assert sort in ("stars", "forks", "updated"), sort
            url_parameters["sort"] = sort
        if (
            order is not github.GithubObject.NotSet
        ):  # pragma no branch (Should be covered)
            assert order in ("asc", "desc"), order
            url_parameters["order"] = order

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append("%s:%s" % (qualifier, value))

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self.__requester,
            "/search/repositories",
            url_parameters,
        )

    def search_users(
        self,
        query,
        sort=github.GithubObject.NotSet,
        order=github.GithubObject.NotSet,
        **qualifiers
    ):
        """
        :calls: `GET /search/users <http://developer.github.com/v3/search>`_
        :param query: string
        :param sort: string ('followers', 'repositories', 'joined')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        assert isinstance(query, str), query
        url_parameters = dict()
        if sort is not github.GithubObject.NotSet:
            assert sort in ("followers", "repositories", "joined"), sort
            url_parameters["sort"] = sort
        if order is not github.GithubObject.NotSet:
            assert order in ("asc", "desc"), order
            url_parameters["order"] = order

        query_chunks = []
        if query:
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append("%s:%s" % (qualifier, value))

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self.__requester,
            "/search/users",
            url_parameters,
        )

    def search_issues(
        self,
        query,
        sort=github.GithubObject.NotSet,
        order=github.GithubObject.NotSet,
        **qualifiers
    ):
        """
        :calls: `GET /search/issues <http://developer.github.com/v3/search>`_
        :param query: string
        :param sort: string ('comments', 'created', 'updated')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        """
        assert isinstance(query, str), query
        url_parameters = dict()
        if sort is not github.GithubObject.NotSet:
            assert sort in ("comments", "created", "updated"), sort
            url_parameters["sort"] = sort
        if order is not github.GithubObject.NotSet:
            assert order in ("asc", "desc"), order
            url_parameters["order"] = order

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append("%s:%s" % (qualifier, value))

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return github.PaginatedList.PaginatedList(
            github.Issue.Issue, self.__requester, "/search/issues", url_parameters
        )

    def search_code(
        self,
        query,
        sort=github.GithubObject.NotSet,
        order=github.GithubObject.NotSet,
        highlight=False,
        **qualifiers
    ):
        """
        :calls: `GET /search/code <http://developer.github.com/v3/search>`_
        :param query: string
        :param sort: string ('indexed')
        :param order: string ('asc', 'desc')
        :param highlight: boolean (True, False)
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.ContentFile.ContentFile`
        """
        assert isinstance(query, str), query
        url_parameters = dict()
        if (
            sort is not github.GithubObject.NotSet
        ):  # pragma no branch (Should be covered)
            assert sort in ("indexed",), sort
            url_parameters["sort"] = sort
        if (
            order is not github.GithubObject.NotSet
        ):  # pragma no branch (Should be covered)
            assert order in ("asc", "desc"), order
            url_parameters["order"] = order

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append("%s:%s" % (qualifier, value))

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        headers = {"Accept": Consts.highLightSearchPreview} if highlight else None

        return github.PaginatedList.PaginatedList(
            github.ContentFile.ContentFile,
            self.__requester,
            "/search/code",
            url_parameters,
            headers=headers,
        )

    def search_commits(
        self,
        query,
        sort=github.GithubObject.NotSet,
        order=github.GithubObject.NotSet,
        **qualifiers
    ):
        """
        :calls: `GET /search/commits <http://developer.github.com/v3/search>`_
        :param query: string
        :param sort: string ('author-date', 'committer-date')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Commit.Commit`
        """
        assert isinstance(query, str), query
        url_parameters = dict()
        if (
            sort is not github.GithubObject.NotSet
        ):  # pragma no branch (Should be covered)
            assert sort in ("author-date", "committer-date"), sort
            url_parameters["sort"] = sort
        if (
            order is not github.GithubObject.NotSet
        ):  # pragma no branch (Should be covered)
            assert order in ("asc", "desc"), order
            url_parameters["order"] = order

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append("%s:%s" % (qualifier, value))

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return github.PaginatedList.PaginatedList(
            github.Commit.Commit,
            self.__requester,
            "/search/commits",
            url_parameters,
            headers={"Accept": Consts.mediaTypeCommitSearchPreview},
        )

    def search_topics(self, query, **qualifiers):
        """
        :calls: `GET /search/topics <http://developer.github.com/v3/search>`_
        :param query: string
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Topic.Topic`
        """
        assert isinstance(query, str), query
        url_parameters = dict()

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append("%s:%s" % (qualifier, value))

        url_parameters["q"] = " ".join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return github.PaginatedList.PaginatedList(
            github.Topic.Topic,
            self.__requester,
            "/search/topics",
            url_parameters,
            headers={"Accept": Consts.mediaTypeTopicsPreview},
        )

    def render_markdown(self, text, context=github.GithubObject.NotSet):
        """
        :calls: `POST /markdown <http://developer.github.com/v3/markdown>`_
        :param text: string
        :param context: :class:`github.Repository.Repository`
        :rtype: string
        """
        assert isinstance(text, str), text
        assert context is github.GithubObject.NotSet or isinstance(
            context, github.Repository.Repository
        ), context
        post_parameters = {"text": text}
        if context is not github.GithubObject.NotSet:
            post_parameters["mode"] = "gfm"
            post_parameters["context"] = context._identity
        status, headers, data = self.__requester.requestJson(
            "POST", "/markdown", input=post_parameters
        )
        return data

    def get_hook(self, name):
        """
        :calls: `GET /hooks/:name <http://developer.github.com/v3/repos/hooks/>`_
        :param name: string
        :rtype: :class:`github.HookDescription.HookDescription`
        """
        assert isinstance(name, str), name
        headers, attributes = self.__requester.requestJsonAndCheck(
            "GET", "/hooks/" + name
        )
        return HookDescription.HookDescription(
            self.__requester, headers, attributes, completed=True
        )

    def get_hooks(self):
        """
        :calls: `GET /hooks <http://developer.github.com/v3/repos/hooks/>`_
        :rtype: list of :class:`github.HookDescription.HookDescription`
        """
        headers, data = self.__requester.requestJsonAndCheck("GET", "/hooks")
        return [
            HookDescription.HookDescription(
                self.__requester, headers, attributes, completed=True
            )
            for attributes in data
        ]

    def get_gitignore_templates(self):
        """
        :calls: `GET /gitignore/templates <http://developer.github.com/v3/gitignore>`_
        :rtype: list of string
        """
        headers, data = self.__requester.requestJsonAndCheck(
            "GET", "/gitignore/templates"
        )
        return data

    def get_gitignore_template(self, name):
        """
        :calls: `GET /gitignore/templates/:name <http://developer.github.com/v3/gitignore>`_
        :rtype: :class:`github.GitignoreTemplate.GitignoreTemplate`
        """
        assert isinstance(name, str), name
        headers, attributes = self.__requester.requestJsonAndCheck(
            "GET", "/gitignore/templates/" + name
        )
        return GitignoreTemplate.GitignoreTemplate(
            self.__requester, headers, attributes, completed=True
        )

    def get_emojis(self):
        """
        :calls: `GET /emojis <http://developer.github.com/v3/emojis/>`_
        :rtype: dictionary of type => url for emoji`
        """
        headers, attributes = self.__requester.requestJsonAndCheck("GET", "/emojis")
        return attributes

    def create_from_raw_data(self, klass, raw_data, headers={}):
        """
        Creates an object from raw_data previously obtained by :attr:`github.GithubObject.GithubObject.raw_data`,
        and optionally headers previously obtained by :attr:`github.GithubObject.GithubObject.raw_headers`.

        :param klass: the class of the object to create
        :param raw_data: dict
        :param headers: dict
        :rtype: instance of class ``klass``
        """
        return klass(self.__requester, headers, raw_data, completed=True)

    def dump(self, obj, file, protocol=0):
        """
        Dumps (pickles) a PyGithub object to a file-like object.
        Some effort is made to not pickle sensitive information like the Github credentials used in the :class:`Github` instance.
        But NO EFFORT is made to remove sensitive information from the object's attributes.

        :param obj: the object to pickle
        :param file: the file-like object to pickle to
        :param protocol: the `pickling protocol <http://docs.python.org/2.7/library/pickle.html#data-stream-format>`_
        """
        pickle.dump((obj.__class__, obj.raw_data, obj.raw_headers), file, protocol)

    def load(self, f):
        """
        Loads (unpickles) a PyGithub object from a file-like object.

        :param f: the file-like object to unpickle from
        :return: the unpickled object
        """
        return self.create_from_raw_data(*pickle.load(f))

    def get_oauth_application(self, client_id, client_secret):
        return github.ApplicationOAuth.ApplicationOAuth(
            self.__requester,
            headers={},
            attributes={"client_id": client_id, "client_secret": client_secret},
            completed=False,
        )

    def get_app(self, slug=github.GithubObject.NotSet):
        """
        :calls: `GET /apps/:slug <https://docs.github.com/en/rest/reference/apps>`_ or `GET /app <https://docs.github.com/en/rest/reference/apps>`_
        :param slug: string
        :rtype: :class:`github.GithubApp.GithubApp`
        """
        assert slug is github.GithubObject.NotSet or isinstance(slug, str), slug
        if slug is github.GithubObject.NotSet:
            return GithubApp.GithubApp(
                self.__requester, {}, {"url": "/app"}, completed=False
            )
        else:
            headers, data = self.__requester.requestJsonAndCheck("GET", "/apps/" + slug)
            return GithubApp.GithubApp(self.__requester, headers, data, completed=True)


class GithubIntegration(object):
    """
    Main class to obtain tokens for a GitHub integration.
    """

    def __init__(self, integration_id, private_key, base_url=DEFAULT_BASE_URL):
        """
        :param base_url: string
        :param integration_id: int
        :param private_key: string
        """
        self.base_url = base_url
        self.integration_id = integration_id
        self.private_key = private_key
        assert isinstance(base_url, str), base_url

    def create_jwt(self, expiration=60):
        """
        Creates a signed JWT, valid for 60 seconds by default.
        The expiration can be extended beyond this, to a maximum of 600 seconds.

        :param expiration: int
        :return string:
        """
        now = int(time.time())
        payload = {"iat": now, "exp": now + expiration, "iss": self.integration_id}
        encrypted = jwt.encode(payload, key=self.private_key, algorithm="RS256")

        if isinstance(encrypted, bytes):
            encrypted = encrypted.decode("utf-8")

        return encrypted

    def get_access_token(self, installation_id, user_id=None):
        """
        Get an access token for the given installation id.
        POSTs https://api.github.com/app/installations/<installation_id>/access_tokens
        :param user_id: int
        :param installation_id: int
        :return: :class:`github.InstallationAuthorization.InstallationAuthorization`
        """
        body = {}
        if user_id:
            body = {"user_id": user_id}
        response = requests.post(
            "{}/app/installations/{}/access_tokens".format(
                self.base_url, installation_id
            ),
            headers={
                "Authorization": "Bearer {}".format(self.create_jwt()),
                "Accept": Consts.mediaTypeIntegrationPreview,
                "User-Agent": "PyGithub/Python",
            },
            json=body,
        )

        if response.status_code == 201:
            return InstallationAuthorization.InstallationAuthorization(
                requester=None,  # not required, this is a NonCompletableGithubObject
                headers={},  # not required, this is a NonCompletableGithubObject
                attributes=response.json(),
                completed=True,
            )
        elif response.status_code == 403:
            raise GithubException.BadCredentialsException(
                status=response.status_code, data=response.text
            )
        elif response.status_code == 404:
            raise GithubException.UnknownObjectException(
                status=response.status_code, data=response.text
            )
        raise GithubException.GithubException(
            status=response.status_code, data=response.text
        )

    def get_installation(self, owner, repo):
        """
        :calls: `GET /repos/:owner/:repo/installation <https://developer.github.com/v3/apps/#get-a-repository-installation>`_
        :param owner: str
        :param repo: str
        :rtype: :class:`github.Installation.Installation`
        """
        headers = {
            "Authorization": "Bearer {}".format(self.create_jwt()),
            "Accept": Consts.mediaTypeIntegrationPreview,
            "User-Agent": "PyGithub/Python",
        }

        response = requests.get(
            "{}/repos/{}/{}/installation".format(self.base_url, owner, repo),
            headers=headers,
        )
        response_dict = response.json()
        return Installation.Installation(None, headers, response_dict, True)
