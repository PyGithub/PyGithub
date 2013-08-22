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

import github.GitTreeElement


class GitTree(github.GithubObject.CompletableGithubObject):
    """
    This class represents GitTrees as returned for example by http://developer.github.com/v3/todo
    """

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
        :type: list of :class:`github.GitTreeElement.GitTreeElement`
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
        self._sha = github.GithubObject.NotSet
        self._tree = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "tree" in attributes:  # pragma no branch
            assert attributes["tree"] is None or all(isinstance(element, dict) for element in attributes["tree"]), attributes["tree"]
            self._tree = None if attributes["tree"] is None else [
                github.GitTreeElement.GitTreeElement(self._requester, self._headers, element, completed=False)
                for element in attributes["tree"]
            ]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
