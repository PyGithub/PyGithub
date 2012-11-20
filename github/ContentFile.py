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


class ContentFile(GithubObject.BasicGithubObject):
    @property
    def content(self):
        return self._NoneIfNotSet(self._content)

    @property
    def encoding(self):
        return self._NoneIfNotSet(self._encoding)

    @property
    def name(self):
        return self._NoneIfNotSet(self._name)

    @property
    def path(self):
        return self._NoneIfNotSet(self._path)

    @property
    def sha(self):
        return self._NoneIfNotSet(self._sha)

    @property
    def size(self):
        return self._NoneIfNotSet(self._size)

    @property
    def type(self):
        return self._NoneIfNotSet(self._type)

    def _initAttributes(self):
        self._content = GithubObject.NotSet
        self._encoding = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._path = GithubObject.NotSet
        self._sha = GithubObject.NotSet
        self._size = GithubObject.NotSet
        self._type = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "content" in attributes:  # pragma no branch
            assert attributes["content"] is None or isinstance(attributes["content"], (str, unicode)), attributes["content"]
            self._content = attributes["content"]
        if "encoding" in attributes:  # pragma no branch
            assert attributes["encoding"] is None or isinstance(attributes["encoding"], (str, unicode)), attributes["encoding"]
            self._encoding = attributes["encoding"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "path" in attributes:  # pragma no branch
            assert attributes["path"] is None or isinstance(attributes["path"], (str, unicode)), attributes["path"]
            self._path = attributes["path"]
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "size" in attributes:  # pragma no branch
            assert attributes["size"] is None or isinstance(attributes["size"], (int, long)), attributes["size"]
            self._size = attributes["size"]
        if "type" in attributes:  # pragma no branch
            assert attributes["type"] is None or isinstance(attributes["type"], (str, unicode)), attributes["type"]
            self._type = attributes["type"]
