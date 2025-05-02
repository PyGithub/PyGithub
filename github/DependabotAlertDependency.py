############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

from github.AdvisoryVulnerabilityPackage import AdvisoryVulnerabilityPackage
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class DependabotAlertDependency(NonCompletableGithubObject):
    """
    This class represents a DependabotAlertDependency.

    The reference can be found here
    https://docs.github.com/en/rest/dependabot/alerts

    The OpenAPI schema can be found at
    - /components/schemas/dependabot-alert/properties/dependency

    """

    def _initAttributes(self) -> None:
        self._manifest_path: Attribute[str] = NotSet
        self._package: Attribute[AdvisoryVulnerabilityPackage] = NotSet
        self._scope: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "package": self.package,
                "manifest_path": self.manifest_path,
            }
        )

    @property
    def manifest_path(self) -> str:
        return self._manifest_path.value

    @property
    def package(self) -> AdvisoryVulnerabilityPackage:
        return self._package.value

    @property
    def scope(self) -> str:
        return self._scope.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "manifest_path" in attributes:
            self._manifest_path = self._makeStringAttribute(attributes["manifest_path"])
        if "package" in attributes:
            self._package = self._makeClassAttribute(
                AdvisoryVulnerabilityPackage,
                attributes["package"],
            )
        if "scope" in attributes:
            self._scope = self._makeStringAttribute(attributes["scope"])
