############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Eric Nieuwland <eric.nieuwland@gmail.com>                     #
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
from __future__ import annotations

from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CodeScanRule(NonCompletableGithubObject):
    """
    This class represents Alerts from code scanning.
    The reference can be found here https://docs.github.com/en/rest/reference/code-scanning.
    """

    def _initAttributes(self) -> None:
        self._id: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._severity: Attribute[str] = NotSet
        self._security_severity_level: Attribute[str] = NotSet
        self._description: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self.id, "name": self.name})

    @property
    def id(self) -> str:
        return self._id.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def severity(self) -> str:
        return self._severity.value

    @property
    def security_severity_level(self) -> str:
        return self._security_severity_level.value

    @property
    def description(self) -> str:
        return self._description.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "severity" in attributes:  # pragma no branch
            self._severity = self._makeStringAttribute(attributes["severity"])
        if "security_severity_level" in attributes:  # pragma no branch
            self._security_severity_level = self._makeStringAttribute(attributes["security_severity_level"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
