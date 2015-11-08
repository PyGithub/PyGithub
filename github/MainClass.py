# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Ed Jackson <ed.jackson@gmail.com>                             #
# Copyright 2013 Jonathan J Hunt <hunt@braincorporation.com>                   #
# Copyright 2013 Peter Golm <golm.peter@gmail.com>                             #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
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
# ##############################################################################

import urllib
import pickle

from Requester import Requester
import AuthenticatedUser
import NamedUser
import Organization
import Gist
import github.PaginatedList
import Repository
import Legacy
import github.GithubObject
import HookDescription
import GitignoreTemplate
import Status
import StatusMessage
import RateLimit


DEFAULT_BASE_URL = "https://api.github.com"
DEFAULT_TIMEOUT = 10
DEFAULT_PER_PAGE = 30


class Github(object):
    """
    This is the main class you instanciate to access the Github API v3. Optional parameters allow different authentication methods.
    """

    def __init__(self, login_or_token=None, password=None, base_url=DEFAULT_BASE_URL, timeout=DEFAULT_TIMEOUT, client_id=None, client_secret=None, user_agent='PyGithub/Python', per_page=DEFAULT_PER_PAGE, api_preview=False):
        """
        :param login_or_token: string
        :param password: string
        :param base_url: string
        :param timeout: integer
        :param client_id: string
        :param client_secret: string
        :param user_agent: string
        :param per_page: int
        """

        assert login_or_token is None or isinstance(login_or_token, (str, unicode)), login_or_token
        assert password is None or isinstance(password, (str, unicode)), password
        assert isinstance(base_url, (str, unicode)), base_url
        assert isinstance(timeout, (int, long)), timeout
        assert client_id is None or isinstance(client_id, (str, unicode)), client_id
        assert client_secret is None or isinstance(client_secret, (str, unicode)), client_secret
        assert user_agent is None or isinstance(user_agent, (str, unicode)), user_agent
        assert isinstance(api_preview, (bool))
        self.__requester = Requester(login_or_token, password, base_url, timeout, client_id, client_secret, user_agent, per_page, api_preview)

    def __get_FIX_REPO_GET_GIT_REF(self):
        """
        :type: bool
        """
        return self.__requester.FIX_REPO_GET_GIT_REF

    def __set_FIX_REPO_GET_GIT_REF(self, value):
        self.__requester.FIX_REPO_GET_GIT_REF = value

    FIX_REPO_GET_GIT_REF = property(__get_FIX_REPO_GET_GIT_REF, __set_FIX_REPO_GET_GIT_REF)

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
        Don't forget you can access the rate limit returned in headers of last Github API v3 response, by :attr:`github.MainClass.Github.rate_limiting` and :attr:`github.MainClass.Github.rate_limiting_resettime`.

        :calls: `GET /rate_limit <http://developer.github.com/v3/rate_limit>`_
        :rtype: :class:`github.RateLimit.RateLimit`
        """
        headers, attributes = self.__requester.requestJsonAndCheck(
            'GET',
            '/rate_limit'
        )
        return RateLimit.RateLimit(self.__requester, headers, attributes, True)

    @property
    def oauth_scopes(self):
        """
        :type: list of string
        """
        return self.__requester.oauth_scopes

    def get_user(self, login=github.GithubObject.NotSet):
        """
        :calls: `GET /users/:user <http://developer.github.com/v3/users>`_ or `GET /user <http://developer.github.com/v3/users>`_
        :param login: string
        :rtype: :class:`github.NamedUser.NamedUser`
        """
        assert login is github.GithubObject.NotSet or isinstance(login, (str, unicode)), login
        if login is github.GithubObject.NotSet:
            return AuthenticatedUser.AuthenticatedUser(self.__requester, {}, {"url": "/user"}, completed=False)
        else:
            headers, data = self.__requester.requestJsonAndCheck(
                "GET",
                "/users/" + login
            )
            return github.NamedUser.NamedUser(self.__requester, headers, data, completed=True)

    def get_users(self, since=github.GithubObject.NotSet):
        """
        :calls: `GET /users <http://developer.github.com/v3/users>`_
        :param since: integer
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        assert since is github.GithubObject.NotSet or isinstance(since, (int, long)), since
        url_parameters = dict()
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self.__requester,
            "/users",
            url_parameters
        )

    def get_organization(self, login):
        """
        :calls: `GET /orgs/:org <http://developer.github.com/v3/orgs>`_
        :param login: string
        :rtype: :class:`github.Organization.Organization`
        """
        assert isinstance(login, (str, unicode)), login
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/orgs/" + login
        )
        return github.Organization.Organization(self.__requester, headers, data, completed=True)

    def get_repo(self, full_name_or_id, lazy=True):
        """
        :calls: `GET /repos/:owner/:repo <http://developer.github.com/v3/repos>`_ or `GET /repositories/:id <http://developer.github.com/v3/repos>`_
        :rtype: :class:`github.Repository.Repository`
        """
        assert isinstance(full_name_or_id, (str, unicode, int, long)), full_name_or_id
        url_base = "/repositories/" if isinstance(full_name_or_id, int) or isinstance(full_name_or_id, long) else "/repos/"
        url = "%s%s" % (url_base, full_name_or_id)
        if lazy:
            return Repository.Repository(self.__requester, {}, {"url": url}, completed=False)
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "%s%s" % (url_base, full_name_or_id)
        )
        return Repository.Repository(self.__requester, headers, data, completed=True)

    def get_repos(self, since=github.GithubObject.NotSet):
        """
        :calls: `GET /repositories <http://developer.github.com/v3/repos/#list-all-public-repositories>`_
        :param since: integer
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        assert since is github.GithubObject.NotSet or isinstance(since, (int, long)), since
        url_parameters = dict()
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self.__requester,
            "/repositories",
            url_parameters
        )

    def get_gist(self, id):
        """
        :calls: `GET /gists/:id <http://developer.github.com/v3/gists>`_
        :param id: string
        :rtype: :class:`github.Gist.Gist`
        """
        assert isinstance(id, (str, unicode)), id
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/gists/" + id
        )
        return github.Gist.Gist(self.__requester, headers, data, completed=True)

    def get_gists(self):
        """
        :calls: `GET /gists/public <http://developer.github.com/v3/gists>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Gist.Gist`
        """
        return github.PaginatedList.PaginatedList(
            github.Gist.Gist,
            self.__requester,
            "/gists/public",
            None
        )

    def legacy_search_repos(self, keyword, language=github.GithubObject.NotSet):
        """
        :calls: `GET /legacy/repos/search/:keyword <http://developer.github.com/v3/search/legacy>`_
        :param keyword: string
        :param language: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        assert isinstance(keyword, (str, unicode)), keyword
        assert language is github.GithubObject.NotSet or isinstance(language, (str, unicode)), language
        args = {} if language is github.GithubObject.NotSet else {"language": language}
        return Legacy.PaginatedList(
            "/legacy/repos/search/" + urllib.quote_plus(keyword, safe='/%:><'),
            args,
            self.__requester,
            "repositories",
            Legacy.convertRepo,
            github.Repository.Repository,
        )

    def legacy_search_users(self, keyword):
        """
        :calls: `GET /legacy/user/search/:keyword <http://developer.github.com/v3/search/legacy>`_
        :param keyword: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        assert isinstance(keyword, (str, unicode)), keyword
        return Legacy.PaginatedList(
            "/legacy/user/search/" + urllib.quote_plus(keyword, safe='/%:><'),
            {},
            self.__requester,
            "users",
            Legacy.convertUser,
            github.NamedUser.NamedUser,
        )

    def legacy_search_user_by_email(self, email):
        """
        :calls: `GET /legacy/user/email/:email <http://developer.github.com/v3/search/legacy>`_
        :param email: string
        :rtype: :class:`github.NamedUser.NamedUser`
        """
        assert isinstance(email, (str, unicode)), email
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/legacy/user/email/" + email
        )
        return github.NamedUser.NamedUser(self.__requester, headers, Legacy.convertUser(data["user"]), completed=False)

    def search_repositories(self, query, sort=github.GithubObject.NotSet, order=github.GithubObject.NotSet, **qualifiers):
        """
        :calls: `GET /search/repositories <http://developer.github.com/v3/search>`_
        :param query: string
        :param sort: string ('stars', 'forks', 'updated')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        assert isinstance(query, (str, unicode)), query
        url_parameters = dict()
        if sort is not github.GithubObject.NotSet:  # pragma no branch (Should be covered)
            assert sort in ('stars', 'forks', 'updated'), sort
            url_parameters["sort"] = sort
        if order is not github.GithubObject.NotSet:  # pragma no branch (Should be covered)
            assert order in ('asc', 'desc'), order
            url_parameters["order"] = order

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append("%s:%s" % (qualifier, value))

        url_parameters["q"] = ' '.join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self.__requester,
            "/search/repositories",
            url_parameters
        )

    def search_users(self, query, sort=github.GithubObject.NotSet, order=github.GithubObject.NotSet, **qualifiers):
        """
        :calls: `GET /search/users <http://developer.github.com/v3/search>`_
        :param query: string
        :param sort: string ('followers', 'repositories', 'joined')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        assert isinstance(query, (str, unicode)), query
        url_parameters = dict()
        if sort is not github.GithubObject.NotSet:
            assert sort in ('followers', 'repositories', 'joined'), sort
            url_parameters["sort"] = sort
        if order is not github.GithubObject.NotSet:
            assert order in ('asc', 'desc'), order
            url_parameters["order"] = order

        query_chunks = []
        if query:
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append("%s:%s" % (qualifier, value))

        url_parameters["q"] = ' '.join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self.__requester,
            "/search/users",
            url_parameters
        )

    def search_issues(self, query, sort=github.GithubObject.NotSet, order=github.GithubObject.NotSet, **qualifiers):
        """
        :calls: `GET /search/issues <http://developer.github.com/v3/search>`_
        :param query: string
        :param sort: string ('comments', 'created', 'updated')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Issue.Issue`
        """
        assert isinstance(query, (str, unicode)), query
        url_parameters = dict()
        if sort is not github.GithubObject.NotSet:
            assert sort in ('comments', 'created', 'updated'), sort
            url_parameters["sort"] = sort
        if order is not github.GithubObject.NotSet:
            assert order in ('asc', 'desc'), order
            url_parameters["order"] = order

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append("%s:%s" % (qualifier, value))

        url_parameters["q"] = ' '.join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return github.PaginatedList.PaginatedList(
            github.Issue.Issue,
            self.__requester,
            "/search/issues",
            url_parameters
        )

    def search_code(self, query, sort=github.GithubObject.NotSet, order=github.GithubObject.NotSet, **qualifiers):
        """
        :calls: `GET /search/code <http://developer.github.com/v3/search>`_
        :param query: string
        :param sort: string ('indexed')
        :param order: string ('asc', 'desc')
        :param qualifiers: keyword dict query qualifiers
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.ContentFile.ContentFile`
        """
        assert isinstance(query, (str, unicode)), query
        url_parameters = dict()
        if sort is not github.GithubObject.NotSet:  # pragma no branch (Should be covered)
            assert sort in ('indexed',), sort
            url_parameters["sort"] = sort
        if order is not github.GithubObject.NotSet:  # pragma no branch (Should be covered)
            assert order in ('asc', 'desc'), order
            url_parameters["order"] = order

        query_chunks = []
        if query:  # pragma no branch (Should be covered)
            query_chunks.append(query)

        for qualifier, value in qualifiers.items():
            query_chunks.append("%s:%s" % (qualifier, value))

        url_parameters["q"] = ' '.join(query_chunks)
        assert url_parameters["q"], "need at least one qualifier"

        return github.PaginatedList.PaginatedList(
            github.ContentFile.ContentFile,
            self.__requester,
            "/search/code",
            url_parameters
        )

    def render_markdown(self, text, context=github.GithubObject.NotSet):
        """
        :calls: `POST /markdown <http://developer.github.com/v3/markdown>`_
        :param text: string
        :param context: :class:`github.Repository.Repository`
        :rtype: string
        """
        assert isinstance(text, (str, unicode)), text
        assert context is github.GithubObject.NotSet or isinstance(context, github.Repository.Repository), context
        post_parameters = {
            "text": text
        }
        if context is not github.GithubObject.NotSet:
            post_parameters["mode"] = "gfm"
            post_parameters["context"] = context._identity
        status, headers, data = self.__requester.requestJson(
            "POST",
            "/markdown",
            input=post_parameters
        )
        return data

    def get_hook(self, name):
        """
        :calls: `GET /hooks/:name <http://developer.github.com/v3/repos/hooks/>`_
        :param name: string
        :rtype: :class:`github.HookDescription.HookDescription`
        """
        assert isinstance(name, (str, unicode)), name
        headers, attributes = self.__requester.requestJsonAndCheck(
            "GET",
            "/hooks/" + name
        )
        return HookDescription.HookDescription(self.__requester, headers, attributes, completed=True)

    def get_hooks(self):
        """
        :calls: `GET /hooks <http://developer.github.com/v3/repos/hooks/>`_
        :rtype: list of :class:`github.HookDescription.HookDescription`
        """
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/hooks"
        )
        return [HookDescription.HookDescription(self.__requester, headers, attributes, completed=True) for attributes in data]

    def get_gitignore_templates(self):
        """
        :calls: `GET /gitignore/templates <http://developer.github.com/v3/gitignore>`_
        :rtype: list of string
        """
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/gitignore/templates"
        )
        return data

    def get_gitignore_template(self, name):
        """
        :calls: `GET /gitignore/templates/:name <http://developer.github.com/v3/gitignore>`_
        :rtype: :class:`github.GitignoreTemplate.GitignoreTemplate`
        """
        assert isinstance(name, (str, unicode)), name
        headers, attributes = self.__requester.requestJsonAndCheck(
            "GET",
            "/gitignore/templates/" + name
        )
        return GitignoreTemplate.GitignoreTemplate(self.__requester, headers, attributes, completed=True)

    def get_emojis(self):
        """
        :calls: `GET /emojis <http://developer.github.com/v3/emojis/>`_
        :rtype: dictionary of type => url for emoji`
        """
        headers, attributes = self.__requester.requestJsonAndCheck(
            "GET",
            "/emojis"
        )
        return attributes

    def create_from_raw_data(self, klass, raw_data, headers={}):
        """
        Creates an object from raw_data previously obtained by :attr:`github.GithubObject.GithubObject.raw_data`,
        and optionaly headers previously obtained by :attr:`github.GithubObject.GithubObject.raw_headers`.

        :param klass: the class of the object to create
        :param raw_data: dict
        :param headers: dict
        :rtype: instance of class ``klass``
        """
        return klass(self.__requester, headers, raw_data, completed=True)

    def dump(self, obj, file, protocol=0):
        """
        Dumps (pickles) a PyGithub object to a file-like object.
        Some effort is made to not pickle sensitive informations like the Github credentials used in the :class:`Github` instance.
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

    def get_api_status(self):
        """
        This doesn't work with a Github Enterprise installation, because it always targets https://status.github.com.

        :calls: `GET /api/status.json <https://status.github.com/api>`_
        :rtype: :class:`github.Status.Status`
        """
        headers, attributes = self.__requester.requestJsonAndCheck(
            "GET",
            "/api/status.json",
            cnx="status"
        )
        return Status.Status(self.__requester, headers, attributes, completed=True)

    def get_last_api_status_message(self):
        """
        This doesn't work with a Github Enterprise installation, because it always targets https://status.github.com.

        :calls: `GET /api/last-message.json <https://status.github.com/api>`_
        :rtype: :class:`github.StatusMessage.StatusMessage`
        """
        headers, attributes = self.__requester.requestJsonAndCheck(
            "GET",
            "/api/last-message.json",
            cnx="status"
        )
        return StatusMessage.StatusMessage(self.__requester, headers, attributes, completed=True)

    def get_api_status_messages(self):
        """
        This doesn't work with a Github Enterprise installation, because it always targets https://status.github.com.

        :calls: `GET /api/messages.json <https://status.github.com/api>`_
        :rtype: list of :class:`github.StatusMessage.StatusMessage`
        """
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/api/messages.json",
            cnx="status"
        )
        return [StatusMessage.StatusMessage(self.__requester, headers, attributes, completed=True) for attributes in data]
