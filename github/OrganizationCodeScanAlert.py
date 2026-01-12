############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Matthew Davis <35502728+matt-davis27@users.noreply.github.com>#
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

from github.CodeScanAlert import CodeScanAlert
from github.GithubObject import Attribute, NotSet
from github.Repository import Repository


class OrganizationCodeScanAlert(CodeScanAlert):
    """
    This class represents a Code Scan Alerts for an organization.

    The reference can be found here
    https://docs.github.com/en/rest/code-scanning/code-scanning#list-code-scanning-alerts-for-an-organization

    The OpenAPI schema can be found at

    - /components/schemas/code-scanning-organization-alert-items

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._repository: Attribute[Repository] = NotSet

    @property
    def repository(self) -> Repository:
        return self._repository.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "repository" in attributes:
            self._repository = self._makeClassAttribute(Repository, attributes["repository"])

