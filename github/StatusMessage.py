# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
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


class StatusMessage(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents status messages as defined in https://status.github.com/api
    """

    @property
    def body(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._body)

    @property
    def status(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._status)

    @property
    def created_on(self):
        """
        :type: datetime.datetime
        """
        return self._NoneIfNotSet(self._created_on)

    def _initAttributes(self):
        self._status = github.GithubObject.NotSet
        self._created_on = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "body" in attributes:  # pragma no branch
            assert attributes["body"] is None or isinstance(attributes["body"], (str, unicode)), attributes["body"]
            self._body = attributes["body"]
        if "status" in attributes:  # pragma no branch
            assert attributes["status"] is None or isinstance(attributes["status"], (str, unicode)), attributes["status"]
            self._status = attributes["status"]
        if "created_on" in attributes:  # pragma no branch
            assert attributes["created_on"] is None or isinstance(attributes["created_on"], (str, unicode)), attributes["created_on"]
            self._created_on = self._parseDatetime(attributes["created_on"])
