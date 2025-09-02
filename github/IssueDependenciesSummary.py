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

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class IssueDependenciesSummary(NonCompletableGithubObject):
    """
    This class represents IssueDependenciesSummary.

    The reference can be found here
    https://docs.github.com/en/rest/issues/issues

    The OpenAPI schema can be found at

    - /components/schemas/issue-dependencies-summary

    """

    def _initAttributes(self) -> None:
        self._blocked_by: Attribute[int] = NotSet
        self._blocking: Attribute[int] = NotSet
        self._total_blocked_by: Attribute[int] = NotSet
        self._total_blocking: Attribute[int] = NotSet

    @property
    def blocked_by(self) -> int:
        return self._blocked_by.value

    @property
    def blocking(self) -> int:
        return self._blocking.value

    @property
    def total_blocked_by(self) -> int:
        return self._total_blocked_by.value

    @property
    def total_blocking(self) -> int:
        return self._total_blocking.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "blocked_by" in attributes:  # pragma no branch
            self._blocked_by = self._makeIntAttribute(attributes["blocked_by"])
        if "blocking" in attributes:  # pragma no branch
            self._blocking = self._makeIntAttribute(attributes["blocking"])
        if "total_blocked_by" in attributes:  # pragma no branch
            self._total_blocked_by = self._makeIntAttribute(attributes["total_blocked_by"])
        if "total_blocking" in attributes:  # pragma no branch
            self._total_blocking = self._makeIntAttribute(attributes["total_blocking"])
