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

import NamedUser
import CommitStats


class GistHistoryState(GithubObject.GithubObject):
    @property
    def change_status(self):
        self._completeIfNotSet(self._change_status)
        return self._NoneIfNotSet(self._change_status)

    @property
    def committed_at(self):
        self._completeIfNotSet(self._committed_at)
        return self._NoneIfNotSet(self._committed_at)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def user(self):
        self._completeIfNotSet(self._user)
        return self._NoneIfNotSet(self._user)

    @property
    def version(self):
        self._completeIfNotSet(self._version)
        return self._NoneIfNotSet(self._version)

    def _initAttributes(self):
        self._change_status = GithubObject.NotSet
        self._committed_at = GithubObject.NotSet
        self._url = GithubObject.NotSet
        self._user = GithubObject.NotSet
        self._version = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "change_status" in attributes:  # pragma no branch
            assert attributes["change_status"] is None or isinstance(attributes["change_status"], dict), attributes["change_status"]
            self._change_status = None if attributes["change_status"] is None else CommitStats.CommitStats(self._requester, attributes["change_status"], completed=False)
        if "committed_at" in attributes:  # pragma no branch
            assert attributes["committed_at"] is None or isinstance(attributes["committed_at"], (str, unicode)), attributes["committed_at"]
            self._committed_at = self._parseDatetime(attributes["committed_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
        if "user" in attributes:  # pragma no branch
            assert attributes["user"] is None or isinstance(attributes["user"], dict), attributes["user"]
            self._user = None if attributes["user"] is None else NamedUser.NamedUser(self._requester, attributes["user"], completed=False)
        if "version" in attributes:  # pragma no branch
            assert attributes["version"] is None or isinstance(attributes["version"], (str, unicode)), attributes["version"]
            self._version = attributes["version"]
