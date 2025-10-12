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

from typing import TYPE_CHECKING, Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.GithubObject import NonCompletableGithubObject


class SecurityAdvisoryEpss(NonCompletableGithubObject):
    """
    This class represents SecurityAdvisoryEpss.

    The reference can be found here
    https://docs.github.com/en/rest

    The OpenAPI schema can be found at
    - /components/schemas/security-advisory-epss

    """

    def _initAttributes(self) -> None:
        # TODO: remove if parent does not implement this
        super()._initAttributes()
        self._percentage: Attribute[float] = NotSet
        self._percentile: Attribute[float] = NotSet

    def __repr__(self) -> str:
        # TODO: replace "some_attribute" with uniquely identifying attributes in the dict, then run:
        return self.get__repr__({"some_attribute": self._some_attribute.value})

    @property
    def percentage(self) -> float:
        return self._percentage.value

    @property
    def percentile(self) -> float:
        return self._percentile.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        # TODO: remove if parent does not implement this
        super()._useAttributes(attributes)
        if "percentage" in attributes:  # pragma no branch
            self._percentage = self._makeFloatAttribute(attributes["percentage"])
        if "percentile" in attributes:  # pragma no branch
            self._percentile = self._makeFloatAttribute(attributes["percentile"])
