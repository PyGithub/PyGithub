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


class PullRequestMergeStatus(GithubObject.BasicGithubObject):
    @property
    def merged(self):
        return self._NoneIfNotSet(self._merged)

    @property
    def message(self):
        return self._NoneIfNotSet(self._message)

    @property
    def sha(self):
        return self._NoneIfNotSet(self._sha)

    def _initAttributes(self):
        self._merged = GithubObject.NotSet
        self._message = GithubObject.NotSet
        self._sha = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "merged" in attributes:  # pragma no branch
            assert attributes["merged"] is None or isinstance(attributes["merged"], bool), attributes["merged"]
            self._merged = attributes["merged"]
        if "message" in attributes:  # pragma no branch
            assert attributes["message"] is None or isinstance(attributes["message"], (str, unicode)), attributes["message"]
            self._message = attributes["message"]
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
