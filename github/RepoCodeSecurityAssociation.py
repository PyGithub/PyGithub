############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Bill Napier <napier@pobox.com>                                #
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

import github.Repository
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.Repository import Repository


class RepoCodeSecurityAssociation(NonCompletableGithubObject):
    """
    Repositories associated with a code security configuration and attachment status.

    The reference can be found here
    https://docs.github.com/en/rest/code-security/configurations?apiVersion=2022-11-28#get-repositories-associated-with-a-code-security-configuration

    """

    def _initAttributes(self) -> None:
        self._repository: Attribute[Repository] = NotSet
        self._status: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"repo": self._repository.value, "status": self._status.value})

    @property
    def repository(self) -> Repository:
        return self._repository.value

    @property
    def status(self) -> str:
        return self._status.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
