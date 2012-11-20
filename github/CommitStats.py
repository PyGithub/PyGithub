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


class CommitStats(GithubObject.BasicGithubObject):
    @property
    def additions(self):
        return self._NoneIfNotSet(self._additions)

    @property
    def deletions(self):
        return self._NoneIfNotSet(self._deletions)

    @property
    def total(self):
        return self._NoneIfNotSet(self._total)

    def _initAttributes(self):
        self._additions = GithubObject.NotSet
        self._deletions = GithubObject.NotSet
        self._total = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "additions" in attributes:  # pragma no branch
            assert attributes["additions"] is None or isinstance(attributes["additions"], (int, long)), attributes["additions"]
            self._additions = attributes["additions"]
        if "deletions" in attributes:  # pragma no branch
            assert attributes["deletions"] is None or isinstance(attributes["deletions"], (int, long)), attributes["deletions"]
            self._deletions = attributes["deletions"]
        if "total" in attributes:  # pragma no branch
            assert attributes["total"] is None or isinstance(attributes["total"], (int, long)), attributes["total"]
            self._total = attributes["total"]
