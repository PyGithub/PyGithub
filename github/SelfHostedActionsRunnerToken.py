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

from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class SelfHostedActionsRunnerToken(NonCompletableGithubObject):
    """
    This class represents Self-hosted GitHub Actions Runners Token.

    The reference can be found at
    https://docs.github.com/en/free-pro-team@latest/rest/reference/actions#self-hosted-runners

    The OpenAPI schema can be found at
    - /components/schemas/authentication-token

    """

    def _initAttributes(self) -> None:
        self._expires_at: Attribute[str] = NotSet
        self._token: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"token": self._token.value})

    @property
    def expires_at(self) -> str:
        return self._expires_at.value

    @property
    def token(self) -> str:
        return self._token.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "token" in attributes:
            self._token = self._makeStringAttribute(attributes["token"])
        if "expires_at" in attributes:  # pragma no branch
            self._expires_at = self._makeStringAttribute(attributes["expires_at"])
