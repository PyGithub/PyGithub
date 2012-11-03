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


class Permissions(GithubObject.BasicGithubObject):
    @property
    def admin(self):
        return self._NoneIfNotSet(self._admin)

    @property
    def pull(self):
        return self._NoneIfNotSet(self._pull)

    @property
    def push(self):
        return self._NoneIfNotSet(self._push)

    def _initAttributes(self):
        self._admin = GithubObject.NotSet
        self._pull = GithubObject.NotSet
        self._push = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "admin" in attributes:  # pragma no branch
            assert attributes["admin"] is None or isinstance(attributes["admin"], bool), attributes["admin"]
            self._admin = attributes["admin"]
        if "pull" in attributes:  # pragma no branch
            assert attributes["pull"] is None or isinstance(attributes["pull"], bool), attributes["pull"]
            self._pull = attributes["pull"]
        if "push" in attributes:  # pragma no branch
            assert attributes["push"] is None or isinstance(attributes["push"], bool), attributes["push"]
            self._push = attributes["push"]
