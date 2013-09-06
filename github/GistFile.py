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


class GistFile(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents GistFiles as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def content(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._content)

    @property
    def filename(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._filename)

    @property
    def language(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._language)

    @property
    def raw_url(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._raw_url)

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

    def _initAttributes(self):
        self._content = github.GithubObject.NotSet
        self._filename = github.GithubObject.NotSet
        self._language = github.GithubObject.NotSet
        self._raw_url = github.GithubObject.NotSet
        self._size = github.GithubObject.NotSet
        self._type = github.GithubObject.NotSet

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
        if "type" in attributes:  # pragma no branch
            assert attributes["type"] is None or isinstance(attributes["type"], (str, unicode)), attributes["type"]
            self._type = attributes["type"]
