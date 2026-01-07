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

from typing import Any, TYPE_CHECKING

from github.GithubObject import NonCompletableGithubObject
from github.GithubObject import Attribute, NotSet

if TYPE_CHECKING:
    from github.GithubObject import NonCompletableGithubObject


class RepositoryRulesetBypassActor(NonCompletableGithubObject):
    """
    This class represents RepositoryRulesetBypassActor.

    The reference can be found here
    https://docs.github.com/en/rest/repos/rules

    The OpenAPI schema can be found at

    - /components/schemas/repository-ruleset-bypass-actor

    """

    def _initAttributes(self) -> None:
        self._actor_id: Attribute[int] = NotSet
        self._actor_type: Attribute[str] = NotSet
        self._bypass_mode: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"actor_id": self._actor_id.value, "actor_type": self._actor_type.value, "bypass_mode": self._bypass_mode.value})

    @property
    def actor_id(self) -> int:
        return self._actor_id.value

    @property
    def actor_type(self) -> str:
        return self._actor_type.value

    @property
    def bypass_mode(self) -> str:
        return self._bypass_mode.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "actor_id" in attributes:  # pragma no branch
            self._actor_id = self._makeIntAttribute(attributes["actor_id"])
        if "actor_type" in attributes:  # pragma no branch
            self._actor_type = self._makeStringAttribute(attributes["actor_type"])
        if "bypass_mode" in attributes:  # pragma no branch
            self._bypass_mode = self._makeStringAttribute(attributes["bypass_mode"])

