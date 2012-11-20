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


class GistFile(GithubObject.BasicGithubObject):
    @property
    def content(self):
        return self._NoneIfNotSet(self._content)

    @property
    def filename(self):
        return self._NoneIfNotSet(self._filename)

    @property
    def language(self):
        return self._NoneIfNotSet(self._language)

    @property
    def raw_url(self):
        return self._NoneIfNotSet(self._raw_url)

    @property
    def size(self):
        return self._NoneIfNotSet(self._size)

    def _initAttributes(self):
        self._content = GithubObject.NotSet
        self._filename = GithubObject.NotSet
        self._language = GithubObject.NotSet
        self._raw_url = GithubObject.NotSet
        self._size = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "content" in attributes:  # pragma no branch
            assert attributes["content"] is None or isinstance(attributes["content"], (str, unicode)), attributes["content"]
            self._content = attributes["content"]
        if "filename" in attributes:  # pragma no branch
            assert attributes["filename"] is None or isinstance(attributes["filename"], (str, unicode)), attributes["filename"]
            self._filename = attributes["filename"]
        if "language" in attributes:  # pragma no branch
            assert attributes["language"] is None or isinstance(attributes["language"], (str, unicode)), attributes["language"]
            self._language = attributes["language"]
        if "raw_url" in attributes:  # pragma no branch
            assert attributes["raw_url"] is None or isinstance(attributes["raw_url"], (str, unicode)), attributes["raw_url"]
            self._raw_url = attributes["raw_url"]
        if "size" in attributes:  # pragma no branch
            assert attributes["size"] is None or isinstance(attributes["size"], (int, long)), attributes["size"]
            self._size = attributes["size"]
