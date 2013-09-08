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


class HookDescription(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents HookDescriptions as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def events(self):
        """
        :type: list of string
        """
        return self._NoneIfNotSet(self._events)

    @property
    def name(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._name)

    @property
    def schema(self):
        """
        :type: list of list of string
        """
        return self._NoneIfNotSet(self._schema)

    @property
    def supported_events(self):
        """
        :type: list of string
        """
        return self._NoneIfNotSet(self._supported_events)

    def _initAttributes(self):
        self._events = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._schema = github.GithubObject.NotSet
        self._supported_events = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "events" in attributes:  # pragma no branch
            assert attributes["events"] is None or all(isinstance(element, (str, unicode)) for element in attributes["events"]), attributes["events"]
            self._events = attributes["events"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "schema" in attributes:  # pragma no branch
            assert attributes["schema"] is None or all(isinstance(element, list) for element in attributes["schema"]), attributes["schema"]
            self._schema = attributes["schema"]
        if "supported_events" in attributes:  # pragma no branch
            assert attributes["supported_events"] is None or all(isinstance(element, (str, unicode)) for element in attributes["supported_events"]), attributes["supported_events"]
            self._supported_events = attributes["supported_events"]
