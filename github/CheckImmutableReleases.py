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

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CheckImmutableReleases(NonCompletableGithubObject):
    """
    This class represents CheckImmutableReleases.

    The reference can be found here
    https://docs.github.com/en/rest

    The OpenAPI schema can be found at

    - /components/schemas/check-immutable-releases

    """

    def _initAttributes(self) -> None:
        self._enabled: Attribute[bool] = NotSet
        self._enforced_by_owner: Attribute[bool] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "enabled": self._enabled.value,
                "enforced_by_owner": self._enforced_by_owner.value,
            }
        )

    @property
    def enabled(self) -> bool:
        return self._enabled.value

    @property
    def enforced_by_owner(self) -> bool:
        return self._enforced_by_owner.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "enabled" in attributes:  # pragma no branch
            self._enabled = self._makeBoolAttribute(attributes["enabled"])
        if "enforced_by_owner" in attributes:  # pragma no branch
            self._enforced_by_owner = self._makeBoolAttribute(attributes["enforced_by_owner"])
