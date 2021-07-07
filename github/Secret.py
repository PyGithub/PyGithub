############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Denis Blanchette <dblanchette@coveo.com>                      #
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


class Secret(github.GithubObject.NonCompletableGithubObject):
    def __repr__(self):
        return self.get__repr__({"": self._name.value})

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        return self._created_at.value

    @property
    def name(self):
        """
        :type: string
        """
        return self._name.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        return self._updated_at.value

    @property
    def visibility(self):
        """
        :type: string
        """
        return self._visibility.value

    def _initAttributes(self):
        self._created_at = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._visibility = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(
                attributes["created_at"], str
            ), attributes["created_at"]
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(
                attributes["updated_at"], str
            ), attributes["updated_at"]
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "visibility" in attributes:  # pragma no branch
            self._visibility = self._makeStringAttribute(attributes["visibility"])
