# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

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
import PaginatedList
import Repository
import Legacy
import GithubObject
import HookDescription


DEFAULT_BASE_URL = "https://api.github.com"
DEFAULT_TIMEOUT = 10


class Github(object):
    def __init__(self, login_or_token=None, password=None, base_url=DEFAULT_BASE_URL, timeout=DEFAULT_TIMEOUT, client_id=None, client_secret=None, user_agent=None):
        self.__requester = Requester(login_or_token, password, base_url, timeout, client_id, client_secret, user_agent)

    def get_FIX_REPO_GET_GIT_REF(self):
        return self.__requester.FIX_REPO_GET_GIT_REF

    def set_FIX_REPO_GET_GIT_REF(self, value):
        self.__requester.FIX_REPO_GET_GIT_REF = value

    FIX_REPO_GET_GIT_REF = property(get_FIX_REPO_GET_GIT_REF, set_FIX_REPO_GET_GIT_REF)

    @property
    def rate_limiting(self):
        return self.__requester.rate_limiting

    def get_user(self, login=GithubObject.NotSet):
        assert login is GithubObject.NotSet or isinstance(login, (str, unicode)), login
        if login is GithubObject.NotSet:
            return AuthenticatedUser.AuthenticatedUser(self.__requester, {"url": "/user"}, completed=False)
        else:
            headers, data = self.__requester.requestAndCheck(
                "GET",
                "/users/" + login,
                None,
                None
            )
            return NamedUser.NamedUser(self.__requester, data, completed=True)

    def get_organization(self, login):
        assert isinstance(login, (str, unicode)), login
        headers, data = self.__requester.requestAndCheck(
            "GET",
            "/orgs/" + login,
            None,
            None
        )
        return Organization.Organization(self.__requester, data, completed=True)

    def get_gist(self, id):
        assert isinstance(id, (str, unicode)), id
        headers, data = self.__requester.requestAndCheck(
            "GET",
            "/gists/" + id,
            None,
            None
        )
        return Gist.Gist(self.__requester, data, completed=True)

    def get_gists(self):
        return PaginatedList.PaginatedList(
            Gist.Gist,
            self.__requester,
            "/gists/public",
            None
        )

    def legacy_search_repos(self, keyword, language=GithubObject.NotSet):
        assert isinstance(keyword, (str, unicode)), keyword
        assert language is GithubObject.NotSet or isinstance(language, (str, unicode)), language
        args = {} if language is GithubObject.NotSet else {"language": language}
        return Legacy.PaginatedList(
            "/legacy/repos/search/" + urllib.quote(keyword),
            args,
            self.__requester,
            "repositories",
            Legacy.convertRepo,
            Repository.Repository,
        )

    def legacy_search_users(self, keyword):
        assert isinstance(keyword, (str, unicode)), keyword
        return Legacy.PaginatedList(
            "/legacy/user/search/" + urllib.quote(keyword),
            {},
            self.__requester,
            "users",
            Legacy.convertUser,
            NamedUser.NamedUser,
        )

    def legacy_search_user_by_email(self, email):
        assert isinstance(email, (str, unicode)), email
        headers, data = self.__requester.requestAndCheck(
            "GET",
            "/legacy/user/email/" + email,
            None,
            None
        )
        return NamedUser.NamedUser(self.__requester, Legacy.convertUser(data["user"]), completed=False)

    def render_markdown(self, text, context=GithubObject.NotSet):
        assert isinstance(text, (str, unicode)), text
        assert context is GithubObject.NotSet or isinstance(context, Repository.Repository), context
        post_parameters = {
            "text": text
        }
        if context is not GithubObject.NotSet:
            post_parameters["mode"] = "gfm"
            post_parameters["context"] = context._identity
        status, headers, data = self.__requester.requestRaw(
            "POST",
            "/markdown",
            None,
            post_parameters
        )
        return data

    def get_hooks(self):
        headers, data = self.__requester.requestAndCheck(
            "GET",
            "/hooks",
            None,
            None
        )
        return [HookDescription.HookDescription(self.__requester, attributes, completed=True) for attributes in data]
