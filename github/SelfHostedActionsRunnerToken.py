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

from datetime import datetime
from typing import TYPE_CHECKING, Any

import github.Repository
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.Repository import Repository


class SelfHostedActionsRunnerToken(NonCompletableGithubObject):
    """
    This class represents Self-hosted GitHub Actions Runners Token.

    The reference can be found at
    https://docs.github.com/en/free-pro-team@latest/rest/reference/actions#self-hosted-runners

    The OpenAPI schema can be found at
    - /components/schemas/authentication-token

    """

    def _initAttributes(self) -> None:
        self._expires_at: Attribute[datetime] = NotSet
        self._permissions: Attribute[dict[str, Any]] = NotSet
        self._repositories: Attribute[list[Repository]] = NotSet
        self._repository_selection: Attribute[str] = NotSet
        self._single_file: Attribute[str] = NotSet
        self._token: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"token": self._token.value})

    @property
    def expires_at(self) -> datetime:
        return self._expires_at.value

    @property
    def permissions(self) -> dict[str, Any]:
        return self._permissions.value

    @property
    def repositories(self) -> list[Repository]:
        return self._repositories.value

    @property
    def repository_selection(self) -> str:
        return self._repository_selection.value

    @property
    def single_file(self) -> str:
        return self._single_file.value

    @property
    def token(self) -> str:
        return self._token.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "expires_at" in attributes:  # pragma no branch
            self._expires_at = self._makeDatetimeAttribute(attributes["expires_at"])
        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeDictAttribute(attributes["permissions"])
        if "repositories" in attributes:  # pragma no branch
            self._repositories = self._makeListOfClassesAttribute(
                github.Repository.Repository, attributes["repositories"]
            )
        if "repository_selection" in attributes:  # pragma no branch
            self._repository_selection = self._makeStringAttribute(attributes["repository_selection"])
        if "single_file" in attributes:  # pragma no branch
            self._single_file = self._makeStringAttribute(attributes["single_file"])
        if "token" in attributes:
            self._token = self._makeStringAttribute(attributes["token"])
