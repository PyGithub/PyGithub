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


class GitTreeElement(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents GitTreeElements as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def mode(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._mode)

    @property
    def path(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._path)

    @property
    def sha(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._sha)

    @property
    def size(self):
        """
        :type: integer
        """
        return self._NoneIfNotSet(self._size)

    @property
    def type(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._type)

    @property
    def url(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._url)

    def _initAttributes(self):
        self._mode = github.GithubObject.NotSet
        self._path = github.GithubObject.NotSet
        self._sha = github.GithubObject.NotSet
        self._size = github.GithubObject.NotSet
        self._type = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "mode" in attributes:  # pragma no branch
            assert attributes["mode"] is None or isinstance(attributes["mode"], (str, unicode)), attributes["mode"]
            self._mode = attributes["mode"]
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
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
