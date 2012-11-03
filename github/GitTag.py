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

import GitAuthor
import GitObject


class GitTag(GithubObject.GithubObject):
    @property
    def message(self):
        self._completeIfNotSet(self._message)
        return self._NoneIfNotSet(self._message)

    @property
    def object(self):
        self._completeIfNotSet(self._object)
        return self._NoneIfNotSet(self._object)

    @property
    def sha(self):
        self._completeIfNotSet(self._sha)
        return self._NoneIfNotSet(self._sha)

    @property
    def tag(self):
        self._completeIfNotSet(self._tag)
        return self._NoneIfNotSet(self._tag)

    @property
    def tagger(self):
        self._completeIfNotSet(self._tagger)
        return self._NoneIfNotSet(self._tagger)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def _initAttributes(self):
        self._message = GithubObject.NotSet
        self._object = GithubObject.NotSet
        self._sha = GithubObject.NotSet
        self._tag = GithubObject.NotSet
        self._tagger = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "message" in attributes:  # pragma no branch
            assert attributes["message"] is None or isinstance(attributes["message"], (str, unicode)), attributes["message"]
            self._message = attributes["message"]
        if "object" in attributes:  # pragma no branch
            assert attributes["object"] is None or isinstance(attributes["object"], dict), attributes["object"]
            self._object = None if attributes["object"] is None else GitObject.GitObject(self._requester, attributes["object"], completed=False)
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "tag" in attributes:  # pragma no branch
            assert attributes["tag"] is None or isinstance(attributes["tag"], (str, unicode)), attributes["tag"]
            self._tag = attributes["tag"]
        if "tagger" in attributes:  # pragma no branch
            assert attributes["tagger"] is None or isinstance(attributes["tagger"], dict), attributes["tagger"]
            self._tagger = None if attributes["tagger"] is None else GitAuthor.GitAuthor(self._requester, attributes["tagger"], completed=False)
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
