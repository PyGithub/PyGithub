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


class Plan(GithubObject.BasicGithubObject):
    @property
    def collaborators(self):
        return self._NoneIfNotSet(self._collaborators)

    @property
    def name(self):
        return self._NoneIfNotSet(self._name)

    @property
    def private_repos(self):
        return self._NoneIfNotSet(self._private_repos)

    @property
    def space(self):
        return self._NoneIfNotSet(self._space)

    def _initAttributes(self):
        self._collaborators = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._private_repos = GithubObject.NotSet
        self._space = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "collaborators" in attributes:  # pragma no branch
            assert attributes["collaborators"] is None or isinstance(attributes["collaborators"], (int, long)), attributes["collaborators"]
            self._collaborators = attributes["collaborators"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "private_repos" in attributes:  # pragma no branch
            assert attributes["private_repos"] is None or isinstance(attributes["private_repos"], (int, long)), attributes["private_repos"]
            self._private_repos = attributes["private_repos"]
        if "space" in attributes:  # pragma no branch
            assert attributes["space"] is None or isinstance(attributes["space"], (int, long)), attributes["space"]
            self._space = attributes["space"]
