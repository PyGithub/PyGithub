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

from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_optional


class ActionsRepositoryPermissions(CompletableGithubObject):
    """
    This class represents the GitHub Actions permissions of a repository.

    The reference can be found here
    https://docs.github.com/en/rest/actions/permissions#get-github-actions-permissions-for-a-repository

    The OpenAPI schema can be found at

    - /components/schemas/actions-repository-permissions

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._allowed_actions: Attribute[str] = NotSet
        self._enabled: Attribute[bool] = NotSet
        self._selected_actions_url: Attribute[str] = NotSet
        self._sha_pinning_required: Attribute[bool] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"enabled": self._enabled.value, "allowed_actions": self._allowed_actions.value})

    @property
    def allowed_actions(self) -> str:
        self._completeIfNotSet(self._allowed_actions)
        return self._allowed_actions.value

    @property
    def enabled(self) -> bool:
        self._completeIfNotSet(self._enabled)
        return self._enabled.value

    @property
    def selected_actions_url(self) -> str:
        self._completeIfNotSet(self._selected_actions_url)
        return self._selected_actions_url.value

    @property
    def sha_pinning_required(self) -> bool:
        self._completeIfNotSet(self._sha_pinning_required)
        return self._sha_pinning_required.value

    def edit(
        self,
        *,
        enabled: bool,
        allowed_actions: Opt[str] = NotSet,
        sha_pinning_required: Opt[bool] = NotSet,
    ) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/actions/permissions <https://docs.github.com/en/rest/actions/permissions#set-github-actions-permissions-for-a-repository>`_
        :param enabled: bool
        :param allowed_actions: string, one of "all", "local_only" or "selected"
        :param sha_pinning_required: bool
        :rtype: None
        """
        assert isinstance(enabled, bool), enabled
        assert is_optional(allowed_actions, str), allowed_actions
        assert is_optional(sha_pinning_required, bool), sha_pinning_required
        put_parameters = NotSet.remove_unset_items(
            {
                "enabled": enabled,
                "allowed_actions": allowed_actions,
                "sha_pinning_required": sha_pinning_required,
            }
        )
        self._requester.requestJsonAndCheck("PUT", self.url, input=put_parameters)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "allowed_actions" in attributes:  # pragma no branch
            self._allowed_actions = self._makeStringAttribute(attributes["allowed_actions"])
        if "enabled" in attributes:  # pragma no branch
            self._enabled = self._makeBoolAttribute(attributes["enabled"])
        if "selected_actions_url" in attributes:  # pragma no branch
            self._selected_actions_url = self._makeStringAttribute(attributes["selected_actions_url"])
        if "sha_pinning_required" in attributes:  # pragma no branch
            self._sha_pinning_required = self._makeBoolAttribute(attributes["sha_pinning_required"])
