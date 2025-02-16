############################ Copyrights and license ############################
#                                                                              #
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

from github.GithubObject import NonCompletableGithubObject
from github.GithubObject import Attribute, NotSet
import github.RateLimit
import github.Rate


class RateLimitOverview(NonCompletableGithubObject):
    """
    This class represents RateLimitOverview.

    The reference can be found here
    https://docs.github.com/en/rest/reference/rate-limit

    The OpenAPI schema can be found at
    - /components/schemas/rate-limit-overview

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._rate: Attribute[Rate] = NotSet
        self._resources: Attribute[RateLimit] = NotSet

    def __repr__(self) -> str:
        # TODO: replace "some_attribute" with uniquely identifying attributes in the dict, then run:
        #   pre-commit run --all-files
        return self.get__repr__({"some_attribute": self._some_attribute.value})

    @property
    def rate(self) -> Rate:
        return self._rate.value

    @property
    def resources(self) -> RateLimit:
        return self._resources.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "rate" in attributes:  # pragma no branch
            self._rate = self._makeClassAttribute(github.Rate.Rate, attributes["rate"])
        if "resources" in attributes:  # pragma no branch
            self._resources = self._makeClassAttribute(github.RateLimit.RateLimit, attributes["resources"])

