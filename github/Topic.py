# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
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


class Topic(github.GithubObject.CompletableGithubObject):
    """
    This class represents topics as used by https://github.com/topics. The object refereence can be found here https://developer.github.com/v3/search/#search-topics
    """

    def __repr__(self):
        return self.get__repr__({"name": self._name.value})

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def display_name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._display_name)
        return self._display_name.value

    @property
    def short_description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._short_description)
        return self._short_description.value

    @property
    def description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._description.value

    def _initAttributes(self):
        self._name = github.GithubObject.NotSet
        self._display_name = github.GithubObject.NotSet
        self._short_description = github.GithubObject.NotSet
        self._description = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "display_name" in attributes:  # pragma no branch
            self._display_name = self._makeStringAttribute(attributes["display_name"])
        if "short_description" in attributes:  # pragma no branch
            self._short_description = self._makeStringAttribute(attributes["short_description"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
