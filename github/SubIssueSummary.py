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


class SubIssueSummary(NonCompletableGithubObject):
    """
    This class represents SubIssueSummary.

    The reference can be found here
    https://docs.github.com/en/rest/issues/issues

    The OpenAPI schema can be found at

    - /components/schemas/sub-issues-summary

    """

    def _initAttributes(self) -> None:
        self._completed: Attribute[int] = NotSet
        self._percent_completed: Attribute[int] = NotSet
        self._total: Attribute[int] = NotSet

    @property
    def completed(self) -> int:
        return self._completed.value

    @property
    def percent_completed(self) -> int:
        return self._percent_completed.value

    @property
    def total(self) -> int:
        return self._total.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "completed" in attributes:  # pragma no branch
            self._completed = self._makeIntAttribute(attributes["completed"])
        if "percent_completed" in attributes:  # pragma no branch
            self._percent_completed = self._makeIntAttribute(attributes["percent_completed"])
        if "total" in attributes:  # pragma no branch
            self._total = self._makeIntAttribute(attributes["total"])
