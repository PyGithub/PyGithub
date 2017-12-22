# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2017 Jessime Kirk <jessime.kirk@gmail.com>                         #
#                                                                              #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.github.io/PyGithub/v1/index.html                             #
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
# ##############################################################################

import github.GithubObject

class Clones(github.GithubObject.CompletableGithubObject):
    """Represents clone traffic for a repository
    
    https://developer.github.com/v3/repos/traffic/clones
    """

    def __repr__(self):
        return self.get__repr__({"count": self._count.value,
                                 "uniques": self._uniques.value})
    @property
    def count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._count)
        return self._count.value
    
    @property
    def uniques(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._uniques)
        return self._uniques.value
    
    @property
    def clones(self):
        """
        :type: list
        """
        self._completeIfNotSet(self._clones)
        return self._clones.value
    
    def _initAttributes(self):
        self._count = github.GithubObject.NotSet
        self._uniques = github.GithubObject.NotSet
        self._clones = github.GithubObject.NotSet

    def _useAttributes(self, attributes):      
        if "count" in attributes:  # pragma no branch
            self._count = self._makeIntAttribute(attributes["count"])
        if "uniques" in attributes:  # pragma no branch
            self._uniques = self._makeIntAttribute(attributes["uniques"])
        if "clones" in attributes:
            self._clones = self._GithubObject__makeSimpleListAttribute(attributes["clones"], dict)
            

            

class Views(github.GithubObject.CompletableGithubObject):
    """Represents view traffic for a repository
    
    https://developer.github.com/v3/repos/traffic/clones
    """
    
    def __repr__(self):
        return self.get__repr__({"count": self._count.value,
                                 "uniques": self._uniques.value})
    @property
    def count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._count)
        return self._count.value
    
    @property
    def uniques(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._uniques)
        return self._uniques.value
    
    @property
    def views(self):
        """
        :type: list
        """
        self._completeIfNotSet(self._views)
        return self._views.value
    
    def _initAttributes(self):
        self._count = github.GithubObject.NotSet
        self._uniques = github.GithubObject.NotSet
        self._views = github.GithubObject.NotSet

    def _useAttributes(self, attributes):      
        if "count" in attributes:  # pragma no branch
            self._count = self._makeIntAttribute(attributes["count"])
        if "uniques" in attributes:  # pragma no branch
            self._uniques = self._makeIntAttribute(attributes["uniques"])
        if "views" in attributes:
            print('self: ', self.__class__)
            self._views = self._GithubObject__makeSimpleListAttribute(attributes["views"], dict)