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

import Repository
import NamedUser


class PullRequestPart(GithubObject.BasicGithubObject):
    @property
    def label(self):
        return self._NoneIfNotSet(self._label)

    @property
    def ref(self):
        return self._NoneIfNotSet(self._ref)

    @property
    def repo(self):
        return self._NoneIfNotSet(self._repo)

    @property
    def sha(self):
        return self._NoneIfNotSet(self._sha)

    @property
    def user(self):
        return self._NoneIfNotSet(self._user)

    def _initAttributes(self):
        self._label = GithubObject.NotSet
        self._ref = GithubObject.NotSet
        self._repo = GithubObject.NotSet
        self._sha = GithubObject.NotSet
        self._user = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "label" in attributes:  # pragma no branch
            assert attributes["label"] is None or isinstance(attributes["label"], (str, unicode)), attributes["label"]
            self._label = attributes["label"]
        if "ref" in attributes:  # pragma no branch
            assert attributes["ref"] is None or isinstance(attributes["ref"], (str, unicode)), attributes["ref"]
            self._ref = attributes["ref"]
        if "repo" in attributes:  # pragma no branch
            assert attributes["repo"] is None or isinstance(attributes["repo"], dict), attributes["repo"]
            self._repo = None if attributes["repo"] is None else Repository.Repository(self._requester, attributes["repo"], completed=False)
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "user" in attributes:  # pragma no branch
            assert attributes["user"] is None or isinstance(attributes["user"], dict), attributes["user"]
            self._user = None if attributes["user"] is None else NamedUser.NamedUser(self._requester, attributes["user"], completed=False)
