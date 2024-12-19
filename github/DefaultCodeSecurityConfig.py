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

from typing import Any

import github.CodeSecurityConfig
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class DefaultCodeSecurityConfig(NonCompletableGithubObject):
    """
    This class represents a Default Configurations for Code Security.

    The reference can be found here
    https://docs.github.com/en/rest/code-security/configurations.

    """

    def _initAttributes(self) -> None:
        self._configuration: Attribute[github.CodeSecurityConfig.CodeSecurityConfig] = NotSet
        self._default_for_new_repos: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "default_for_new_repos": self.default_for_new_repos,
            }
        )

    @property
    def configuration(self) -> github.CodeSecurityConfig.CodeSecurityConfig:
        return self._configuration.value

    @property
    def default_for_new_repos(self) -> str:
        return self._default_for_new_repos.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "configuration" in attributes:  # pragma no branch
            self._configuration = self._makeClassAttribute(
                github.CodeSecurityConfig.CodeSecurityConfig, attributes["configuration"]
            )
        if "default_for_new_repos" in attributes:  # pragma no branch
            self._default_for_new_repos = self._makeStringAttribute(attributes["default_for_new_repos"])
