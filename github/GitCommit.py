# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import github.GithubObject

import github.GitAuthor
import github.GitTree


class GitCommit(github.GithubObject.CompletableGithubObject):
    """
    This class represents GitCommits as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def author(self):
        """
        :type: :class:`github.GitAuthor.GitAuthor`
        """
        self._completeIfNotSet(self._author)
        return self._NoneIfNotSet(self._author)

    @property
    def committer(self):
        """
        :type: :class:`github.GitAuthor.GitAuthor`
        """
        self._completeIfNotSet(self._committer)
        return self._NoneIfNotSet(self._committer)

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def message(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._message)
        return self._NoneIfNotSet(self._message)

    @property
    def parents(self):
        """
        :type: list of :class:`github.GitCommit.GitCommit`
        """
        self._completeIfNotSet(self._parents)
        return self._NoneIfNotSet(self._parents)

    @property
    def sha(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._sha)
        return self._NoneIfNotSet(self._sha)

    @property
    def tree(self):
        """
        :type: :class:`github.GitTree.GitTree`
        """
        self._completeIfNotSet(self._tree)
        return self._NoneIfNotSet(self._tree)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def _identity(self):
        return self.sha

    def _initAttributes(self):
        self._author = github.GithubObject.NotSet
        self._committer = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._message = github.GithubObject.NotSet
        self._parents = github.GithubObject.NotSet
        self._sha = github.GithubObject.NotSet
        self._tree = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "author" in attributes:  # pragma no branch
            assert attributes["author"] is None or isinstance(attributes["author"], dict), attributes["author"]
            self._author = None if attributes["author"] is None else github.GitAuthor.GitAuthor(self._requester, self._headers, attributes["author"], completed=False)
        if "committer" in attributes:  # pragma no branch
            assert attributes["committer"] is None or isinstance(attributes["committer"], dict), attributes["committer"]
            self._committer = None if attributes["committer"] is None else github.GitAuthor.GitAuthor(self._requester, self._headers, attributes["committer"], completed=False)
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "message" in attributes:  # pragma no branch
            assert attributes["message"] is None or isinstance(attributes["message"], (str, unicode)), attributes["message"]
            self._message = attributes["message"]
        if "parents" in attributes:  # pragma no branch
            assert attributes["parents"] is None or all(isinstance(element, dict) for element in attributes["parents"]), attributes["parents"]
            self._parents = None if attributes["parents"] is None else [
                GitCommit(self._requester, self._headers, element, completed=False)
                for element in attributes["parents"]
            ]
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "tree" in attributes:  # pragma no branch
            assert attributes["tree"] is None or isinstance(attributes["tree"], dict), attributes["tree"]
            self._tree = None if attributes["tree"] is None else github.GitTree.GitTree(self._requester, self._headers, attributes["tree"], completed=False)
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
