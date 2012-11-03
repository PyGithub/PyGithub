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
import GitCommit
import GitTree


class GitCommit(GithubObject.GithubObject):
    @property
    def author(self):
        self._completeIfNotSet(self._author)
        return self._NoneIfNotSet(self._author)

    @property
    def committer(self):
        self._completeIfNotSet(self._committer)
        return self._NoneIfNotSet(self._committer)

    @property
    def message(self):
        self._completeIfNotSet(self._message)
        return self._NoneIfNotSet(self._message)

    @property
    def parents(self):
        self._completeIfNotSet(self._parents)
        return self._NoneIfNotSet(self._parents)

    @property
    def sha(self):
        self._completeIfNotSet(self._sha)
        return self._NoneIfNotSet(self._sha)

    @property
    def tree(self):
        self._completeIfNotSet(self._tree)
        return self._NoneIfNotSet(self._tree)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def _identity(self):
        return self.sha

    def _initAttributes(self):
        self._author = GithubObject.NotSet
        self._committer = GithubObject.NotSet
        self._message = GithubObject.NotSet
        self._parents = GithubObject.NotSet
        self._sha = GithubObject.NotSet
        self._tree = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "author" in attributes:  # pragma no branch
            assert attributes["author"] is None or isinstance(attributes["author"], dict), attributes["author"]
            self._author = None if attributes["author"] is None else GitAuthor.GitAuthor(self._requester, attributes["author"], completed=False)
        if "committer" in attributes:  # pragma no branch
            assert attributes["committer"] is None or isinstance(attributes["committer"], dict), attributes["committer"]
            self._committer = None if attributes["committer"] is None else GitAuthor.GitAuthor(self._requester, attributes["committer"], completed=False)
        if "message" in attributes:  # pragma no branch
            assert attributes["message"] is None or isinstance(attributes["message"], (str, unicode)), attributes["message"]
            self._message = attributes["message"]
        if "parents" in attributes:  # pragma no branch
            assert attributes["parents"] is None or all(isinstance(element, dict) for element in attributes["parents"]), attributes["parents"]
            self._parents = None if attributes["parents"] is None else [
                GitCommit(self._requester, element, completed=False)
                for element in attributes["parents"]
            ]
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "tree" in attributes:  # pragma no branch
            assert attributes["tree"] is None or isinstance(attributes["tree"], dict), attributes["tree"]
            self._tree = None if attributes["tree"] is None else GitTree.GitTree(self._requester, attributes["tree"], completed=False)
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
