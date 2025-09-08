############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Jens Keiner <jens.keiner@gmail.com>                           #
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

from typing import TYPE_CHECKING, Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    pass


class Rule(NonCompletableGithubObject):
    """
    This class represents Rules.

    Rules control how people can interact with selected branches and
    tags in a repository. They are grouped into Rulesets.

    The reference can be found here
    https://docs.github.com/en/rest/repos/rules

    The OpenAPI schema can be found at
    - /components/schemas/repository-rule-detailed

    """

    def _initAttributes(self) -> None:
        self._ruleset_source_type: Attribute[str] = NotSet
        self._ruleset_source: Attribute[str] = NotSet
        self._ruleset_id: Attribute[int] = NotSet
        self._type: Attribute[str] = NotSet
        self._parameters: Attribute[dict[str, Any]] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"type": self._type.value})

    @property
    def ruleset_source_type(self) -> str:
        """
        :type: string
        :return: The type of source for the ruleset that includes this rule (Repository or Organization)
        """
        return self._ruleset_source_type.value

    @property
    def ruleset_source(self) -> str:
        """
        :type: string
        :return: The name of the source of the ruleset that includes this rule
        """
        return self._ruleset_source.value

    @property
    def ruleset_id(self) -> int:
        """
        :type: integer
        :return: The ID of the ruleset that includes this rule
        """
        return self._ruleset_id.value

    @property
    def type(self) -> str:
        """
        :type: string
        :return: The type of the rule (e.g. creation, update, deletion, etc.)
        """
        return self._type.value

    @property
    def parameters(self) -> dict[str, Any]:
        """
        :type: dict
        :return: The parameters specific to this rule type
        """
        return self._parameters.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "ruleset_source_type" in attributes:  # pragma no branch
            self._ruleset_source_type = self._makeStringAttribute(attributes["ruleset_source_type"])
        if "ruleset_source" in attributes:  # pragma no branch
            self._ruleset_source = self._makeStringAttribute(attributes["ruleset_source"])
        if "ruleset_id" in attributes:  # pragma no branch
            self._ruleset_id = self._makeIntAttribute(attributes["ruleset_id"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
        if "parameters" in attributes:  # pragma no branch
            self._parameters = self._makeDictAttribute(attributes["parameters"])
