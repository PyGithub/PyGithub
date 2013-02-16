# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import urllib

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


DEFAULT_BASE_URL = "https://api.github.com"
DEFAULT_TIMEOUT = 10


class Github(object):
    """
    This is the main class you instanciate to access the Github API v3. Optional parameters allow different authentication methods.
    """

    def __init__(self, login_or_token=None, password=None, base_url=DEFAULT_BASE_URL, timeout=DEFAULT_TIMEOUT, client_id=None, client_secret=None, user_agent=None):
        """
        :param login_or_token: string
        :param password: string
        :param base_url: string
        :param timeout: integer
        :param client_id: string
        :param client_secret: string
        :param user_agent: string
        """

        assert login_or_token is None or isinstance(login_or_token, (str, unicode)), login_or_token
        assert password is None or isinstance(password, (str, unicode)), password
        assert isinstance(base_url, (str, unicode)), base_url
        assert isinstance(timeout, (int, long)), timeout
        assert client_id is None or isinstance(client_id, (str, unicode)), client_id
        assert client_secret is None or isinstance(client_secret, (str, unicode)), client_secret
        assert user_agent is None or isinstance(user_agent, (str, unicode)), user_agent
        self.__requester = Requester(login_or_token, password, base_url, timeout, client_id, client_secret, user_agent)

    def __get_FIX_REPO_GET_GIT_REF(self):
        return self.__requester.FIX_REPO_GET_GIT_REF

    def __set_FIX_REPO_GET_GIT_REF(self, value):
        self.__requester.FIX_REPO_GET_GIT_REF = value

    FIX_REPO_GET_GIT_REF = property(__get_FIX_REPO_GET_GIT_REF, __set_FIX_REPO_GET_GIT_REF)

    @property
    def rate_limiting(self):
        """
        :type: (int, int)
        """
        return self.__requester.rate_limiting

    @property
    def oauth_scopes(self):
        """
        :type: list of string
        """
        return self.__requester.oauth_scopes

    def get_user(self, login=github.GithubObject.NotSet):
        """
        :calls: `GET /users/:user <http://developer.github.com/v3/todo>`_
        :param login: string
        :rtype: :class:`github.NamedUser.NamedUser`
        """
        assert login is github.GithubObject.NotSet or isinstance(login, (str, unicode)), login
        if login is github.GithubObject.NotSet:
            return AuthenticatedUser.AuthenticatedUser(self.__requester, {"url": "/user"}, completed=False)
        else:
            headers, data = self.__requester.requestJsonAndCheck(
                "GET",
                "/users/" + login,
                None,
                None
            )
            return github.NamedUser.NamedUser(self.__requester, data, completed=True)

    def get_organization(self, login):
        """
        :calls: `GET /orgs/:org <http://developer.github.com/v3/todo>`_
        :param login: string
        :rtype: :class:`github.Organization.Organization`
        """
        assert isinstance(login, (str, unicode)), login
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/orgs/" + login,
            None,
            None
        )
        return github.Organization.Organization(self.__requester, data, completed=True)

    def get_repo(self, full_name):
        """
        :calls: `GET /repos/:user/:repo <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.Repository.Repository`
        """
        assert isinstance(full_name, (str, unicode)), full_name
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/repos/" + full_name,
            None,
            None
        )
        return Repository.Repository(self.__requester, data, completed=True)

    def get_gist(self, id):
        """
        :calls: `GET /gists/:id <http://developer.github.com/v3/todo>`_
        :param id: string
        :rtype: :class:`github.Gist.Gist`
        """
        assert isinstance(id, (str, unicode)), id
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/gists/" + id,
            None,
            None
        )
        return github.Gist.Gist(self.__requester, data, completed=True)

    def get_gists(self):
        """
        :calls: `GET /gists/public <http://developer.github.com/v3/todo>`_
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
        :calls: `GET /legacy/repos/search/:keyword <http://developer.github.com/v3/todo>`_
        :param keyword: string
        :param language: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        assert isinstance(keyword, (str, unicode)), keyword
        assert language is github.GithubObject.NotSet or isinstance(language, (str, unicode)), language
        args = {} if language is github.GithubObject.NotSet else {"language": language}
        return Legacy.PaginatedList(
            "/legacy/repos/search/" + urllib.quote(keyword),
            args,
            self.__requester,
            "repositories",
            Legacy.convertRepo,
            github.Repository.Repository,
        )

    def legacy_search_users(self, keyword):
        """
        :calls: `GET /legacy/user/search/:keyword <http://developer.github.com/v3/todo>`_
        :param keyword: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        assert isinstance(keyword, (str, unicode)), keyword
        return Legacy.PaginatedList(
            "/legacy/user/search/" + urllib.quote(keyword),
            {},
            self.__requester,
            "users",
            Legacy.convertUser,
            github.NamedUser.NamedUser,
        )

    def legacy_search_user_by_email(self, email):
        """
        :calls: `GET /legacy/user/email/:email <http://developer.github.com/v3/todo>`_
        :param email: string
        :rtype: :class:`github.NamedUser.NamedUser`
        """
        assert isinstance(email, (str, unicode)), email
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/legacy/user/email/" + email,
            None,
            None
        )
        return github.NamedUser.NamedUser(self.__requester, Legacy.convertUser(data["user"]), completed=False)

    def render_markdown(self, text, context=github.GithubObject.NotSet):
        """
        :calls: `POST /markdown <http://developer.github.com/v3/todo>`_
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
            None,
            post_parameters
        )
        return data

    def get_hooks(self):
        """
        :calls: `GET /hooks <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.HookDescription.HookDescription`
        """
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/hooks",
            None,
            None
        )
        return [HookDescription.HookDescription(self.__requester, attributes, completed=True) for attributes in data]

    def get_gitignore_templates(self):
        """
        :calls: `GET /gitignore/templates <http://developer.github.com/v3/todo>`_
        :rtype: list of string
        """
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/gitignore/templates",
            None,
            None
        )
        return data

    def get_gitignore_template(self, name):
        """
        :calls: `GET /gitignore/templates/:name <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.GitignoreTemplate.GitignoreTemplate`
        """
        assert isinstance(name, (str, unicode)), name
        headers, attributes = self.__requester.requestJsonAndCheck(
            "GET",
            "/gitignore/templates/" + name,
            None,
            None
        )
        return GitignoreTemplate.GitignoreTemplate(self.__requester, attributes, completed=True)
