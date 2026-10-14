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


class ActionsRepositoryPermissions(NonCompletableGithubObject):
    """
    This class represents the GitHub Actions permissions of a repository.

    The reference can be found here
    https://docs.github.com/en/rest/actions/permissions#get-github-actions-permissions-for-a-repository

    The OpenAPI schema can be found at

    - /components/schemas/actions-repository-permissions

    """

    def _initAttributes(self) -> None:
        self._allowed_actions: Attribute[str] = NotSet
        self._enabled: Attribute[bool] = NotSet
        self._selected_actions_url: Attribute[str] = NotSet
        self._sha_pinning_required: Attribute[bool] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"enabled": self._enabled.value, "allowed_actions": self._allowed_actions.value})

    @property
    def allowed_actions(self) -> str:
        return self._allowed_actions.value

    @property
    def enabled(self) -> bool:
        return self._enabled.value

    @property
    def selected_actions_url(self) -> str:
        return self._selected_actions_url.value

    @property
    def sha_pinning_required(self) -> bool:
        return self._sha_pinning_required.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "allowed_actions" in attributes:  # pragma no branch
            self._allowed_actions = self._makeStringAttribute(attributes["allowed_actions"])
        if "enabled" in attributes:  # pragma no branch
            self._enabled = self._makeBoolAttribute(attributes["enabled"])
        if "selected_actions_url" in attributes:  # pragma no branch
            self._selected_actions_url = self._makeStringAttribute(attributes["selected_actions_url"])
        if "sha_pinning_required" in attributes:  # pragma no branch
            self._sha_pinning_required = self._makeBoolAttribute(attributes["sha_pinning_required"])
