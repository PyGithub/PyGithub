############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
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

import github.AdvisoryBase
import github.DependabotAlertVulnerability
from github.GithubObject import Attribute, NotSet

if TYPE_CHECKING:
    from github.DependabotAlertVulnerability import DependabotAlertVulnerability


class DependabotAlertAdvisory(github.AdvisoryBase.AdvisoryBase):
    """
    This class represents a package flagged by a Dependabot alert that is vulnerable to a parent SecurityAdvisory.
    The reference can be found here https://docs.github.com/en/rest/dependabot/alerts
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._references: Attribute[list[dict]] = NotSet
        self._vulnerabilities: Attribute[list[DependabotAlertVulnerability]] = NotSet

    @property
    def references(self) -> list[dict]:
        return self._references.value

    @property
    def vulnerabilities(self) -> list[DependabotAlertVulnerability]:
        return self._vulnerabilities.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "references" in attributes:
            self._references = self._makeListOfDictsAttribute(
                attributes["references"],
            )
        if "vulnerabilities" in attributes:
            self._vulnerabilities = self._makeListOfClassesAttribute(
                github.DependabotAlertVulnerability.DependabotAlertVulnerability,
                attributes["vulnerabilities"],
            )
        super()._useAttributes(attributes)
