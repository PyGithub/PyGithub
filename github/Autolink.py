############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Marco Köpcke  <hello@parakoopa.de>                            #
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


from typing import Any, Dict, List
from github.GithubObject import NonCompletableGithubObject
class Autolink(github.GithubObject.NonCompletableGithubObject):
    def __repr__(self):
        return self.get__repr__({"id": self._id.value})

    @property
    def id(self) -> int:
        """
        :type: integer
        """
        return self._id.value

    @property
    def key_prefix(self) -> str:
        """
        :type: string
        """
        return self._key_prefix.value

    @property
    def url_template(self) -> str:
        """
        :type: string
        """
        return self._url_template.value

    def _initAttributes(self) -> None:
        self._id = github.GithubObject.NotSet
        self._key_prefix = github.GithubObject.NotSet
        self._url_template = github.GithubObject.NotSet

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "key_prefix" in attributes:  # pragma no branch
            self._key_prefix = self._makeStringAttribute(attributes["key_prefix"])
        if "url_template" in attributes:  # pragma no branch
            self._url_template = self._makeStringAttribute(attributes["url_template"])
