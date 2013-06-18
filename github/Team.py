# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques vincent@vincent-jacques.net
# Copyright 2012 Zearin zearin@gonk.net
# Copyright 2013 Vincent Jacques vincent@vincent-jacques.net
# Copyright 2013 martinqt m.ki2@laposte.net

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import github.GithubObject
import github.PaginatedList

import github.Repository
import github.NamedUser


class Team(github.GithubObject.CompletableGithubObject):
    """
    This class represents Teams. The reference can be found here http://developer.github.com/v3/orgs/teams/
    """

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def members_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._members_count)
        return self._NoneIfNotSet(self._members_count)

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._NoneIfNotSet(self._name)

    @property
    def permission(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._permission)
        return self._NoneIfNotSet(self._permission)

    @property
    def repos_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._repos_count)
        return self._NoneIfNotSet(self._repos_count)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def add_to_members(self, member):
        """
        :calls: `PUT /teams/:id/members/:user <http://developer.github.com/v3/todo>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/members/" + member._identity,
            None,
            None
        )

    def add_to_repos(self, repo):
        """
        :calls: `PUT /teams/:id/repos/:user/:repo <http://developer.github.com/v3/todo>`_
        :param repo: :class:`github.Repository.Repository`
        :rtype: None
        """
        assert isinstance(repo, github.Repository.Repository), repo
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/repos/" + repo._identity,
            None,
            None
        )

    def delete(self):
        """
        :calls: `DELETE /teams/:id <http://developer.github.com/v3/todo>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def edit(self, name, permission=github.GithubObject.NotSet):
        """
        :calls: `PATCH /teams/:id <http://developer.github.com/v3/todo>`_
        :param name: string
        :param permission: string
        :rtype: None
        """
        assert isinstance(name, (str, unicode)), name
        assert permission is github.GithubObject.NotSet or isinstance(permission, (str, unicode)), permission
        post_parameters = {
            "name": name,
        }
        if permission is not github.GithubObject.NotSet:
            post_parameters["permission"] = permission
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def get_members(self):
        """
        :calls: `GET /teams/:id/members <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser`
        """
        return github.PaginatedList.PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self.url + "/members",
            None
        )

    def get_repos(self):
        """
        :calls: `GET /teams/:id/repos <http://developer.github.com/v3/todo>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self._requester,
            self.url + "/repos",
            None
        )

    def has_in_members(self, member):
        """
        :calls: `GET /teams/:id/members/:user <http://developer.github.com/v3/todo>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: bool
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/members/" + member._identity,
            None,
            None
        )
        return status == 204

    def has_in_repos(self, repo):
        """
        :calls: `GET /teams/:id/repos/:user/:repo <http://developer.github.com/v3/todo>`_
        :param repo: :class:`github.Repository.Repository`
        :rtype: bool
        """
        assert isinstance(repo, github.Repository.Repository), repo
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/repos/" + repo._identity,
            None,
            None
        )
        return status == 204

    def remove_from_members(self, member):
        """
        :calls: `DELETE /teams/:id/members/:user <http://developer.github.com/v3/todo>`_
        :param member: :class:`github.NamedUser.NamedUser`
        :rtype: None
        """
        assert isinstance(member, github.NamedUser.NamedUser), member
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/members/" + member._identity,
            None,
            None
        )

    def remove_from_repos(self, repo):
        """
        :calls: `DELETE /teams/:id/repos/:user/:repo <http://developer.github.com/v3/todo>`_
        :param repo: :class:`github.Repository.Repository`
        :rtype: None
        """
        assert isinstance(repo, github.Repository.Repository), repo
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/repos/" + repo._identity,
            None,
            None
        )

    @property
    def _identity(self):
        return self.id

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._members_count = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._permission = github.GithubObject.NotSet
        self._repos_count = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "members_count" in attributes:  # pragma no branch
            assert attributes["members_count"] is None or isinstance(attributes["members_count"], (int, long)), attributes["members_count"]
            self._members_count = attributes["members_count"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "permission" in attributes:  # pragma no branch
            assert attributes["permission"] is None or isinstance(attributes["permission"], (str, unicode)), attributes["permission"]
            self._permission = attributes["permission"]
        if "repos_count" in attributes:  # pragma no branch
            assert attributes["repos_count"] is None or isinstance(attributes["repos_count"], (int, long)), attributes["repos_count"]
            self._repos_count = attributes["repos_count"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
