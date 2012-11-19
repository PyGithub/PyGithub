# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import GithubObject

import Organization
import Repository
import NamedUser


class Event(GithubObject.BasicGithubObject):
    @property
    def actor(self):
        return self._NoneIfNotSet(self._actor)

    @property
    def created_at(self):
        return self._NoneIfNotSet(self._created_at)

    @property
    def id(self):
        return self._NoneIfNotSet(self._id)

    @property
    def org(self):
        return self._NoneIfNotSet(self._org)

    @property
    def payload(self):
        return self._NoneIfNotSet(self._payload)

    @property
    def public(self):
        return self._NoneIfNotSet(self._public)

    @property
    def repo(self):
        return self._NoneIfNotSet(self._repo)

    @property
    def type(self):
        return self._NoneIfNotSet(self._type)

    def _initAttributes(self):
        self._actor = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._org = GithubObject.NotSet
        self._payload = GithubObject.NotSet
        self._public = GithubObject.NotSet
        self._repo = GithubObject.NotSet
        self._type = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "actor" in attributes:  # pragma no branch
            assert attributes["actor"] is None or isinstance(attributes["actor"], dict), attributes["actor"]
            self._actor = None if attributes["actor"] is None else NamedUser.NamedUser(self._requester, attributes["actor"], completed=False)
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (str, unicode)), attributes["id"]
            self._id = attributes["id"]
        if "org" in attributes:  # pragma no branch
            assert attributes["org"] is None or isinstance(attributes["org"], dict), attributes["org"]
            self._org = None if attributes["org"] is None else Organization.Organization(self._requester, attributes["org"], completed=False)
        if "payload" in attributes:  # pragma no branch
            assert attributes["payload"] is None or isinstance(attributes["payload"], dict), attributes["payload"]
            self._payload = attributes["payload"]
        if "public" in attributes:  # pragma no branch
            assert attributes["public"] is None or isinstance(attributes["public"], bool), attributes["public"]
            self._public = attributes["public"]
        if "repo" in attributes:  # pragma no branch
            assert attributes["repo"] is None or isinstance(attributes["repo"], dict), attributes["repo"]
            self._repo = None if attributes["repo"] is None else Repository.Repository(self._requester, attributes["repo"], completed=False)
        if "type" in attributes:  # pragma no branch
            assert attributes["type"] is None or isinstance(attributes["type"], (str, unicode)), attributes["type"]
            self._type = attributes["type"]
