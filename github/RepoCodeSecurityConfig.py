############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Bill Napier <napier@pobox.com>                                #
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

import github.CodeSecurityConfig
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    pass


class RepoCodeSecurityConfig(NonCompletableGithubObject):
    """
    This class represents Configurations for Code Security for a Repository.

    The reference can be found here
    https://docs.github.com/en/rest/code-security/configurations.

    """

    def _initAttributes(self) -> None:
        self._configuration: Attribute[github.CodeSecurityConfig.CodeSecurityConfig] = NotSet
        self._status: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "configuration": self.configuration,
            }
        )

    @property
    def configuration(self) -> github.CodeSecurityConfig.CodeSecurityConfig:
        return self._configuration.value

    @property
    def status(self) -> str:
        return self._status.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "configuration" in attributes:  # pragma no branch
            self._configuration = self._makeClassAttribute(
                github.CodeSecurityConfig.CodeSecurityConfig, attributes["configuration"]
            )
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
