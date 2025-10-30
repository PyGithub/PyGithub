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

from typing import TYPE_CHECKING, Any

import github.Rate
import github.RateLimit
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.Rate import Rate
    from github.RateLimit import RateLimit


class RateLimitOverview(NonCompletableGithubObject):
    """
    This class represents RateLimitOverview.

    The reference can be found here
    https://docs.github.com/en/rest/reference/rate-limit

    The OpenAPI schema can be found at

    - /components/schemas/rate-limit-overview

    """

    def _initAttributes(self) -> None:
        self._rate: Attribute[Rate] = NotSet
        self._resources: Attribute[RateLimit] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"rate": self._rate.value})

    @property
    def rate(self) -> Rate:
        return self._rate.value

    @property
    def resources(self) -> RateLimit:
        return self._resources.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "rate" in attributes:  # pragma no branch
            self._rate = self._makeClassAttribute(github.Rate.Rate, attributes["rate"])
        if "resources" in attributes:  # pragma no branch
            self._resources = self._makeClassAttribute(github.RateLimit.RateLimit, attributes["resources"])
