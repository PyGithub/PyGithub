############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Eric Nieuwland <eric.nieuwland@gmail.com>                     #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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

from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CodeScanTool(NonCompletableGithubObject):
    """
    This class represents code scanning tools.
    The reference can be found here https://docs.github.com/en/rest/reference/code-scanning.
    """

    def _initAttributes(self) -> None:
        self._name: Attribute[str] = NotSet
        self._version: Attribute[str] = NotSet
        self._guid: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "guid": self.guid,
                "name": self.name,
                "version": self.version,
            }
        )

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def version(self) -> str:
        return self._version.value

    @property
    def guid(self) -> str:
        return self._guid.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "version" in attributes:  # pragma no branch
            self._version = self._makeStringAttribute(attributes["version"])
        if "guid" in attributes:  # pragma no branch
            self._guid = self._makeStringAttribute(attributes["guid"])
