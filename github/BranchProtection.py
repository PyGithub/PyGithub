############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Benjamin K <53038537+treee111@users.noreply.github.com>       #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

import github.GithubObject
import github.NamedUser
import github.RequiredPullRequestReviews
import github.RequiredStatusChecks
import github.Team
from github.GithubObject import Attribute, NotSet, Opt, is_defined
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.NamedUser import NamedUser
    from github.RequiredPullRequestReviews import RequiredPullRequestReviews
    from github.RequiredStatusChecks import RequiredStatusChecks
    from github.Team import Team


class BranchProtection(github.GithubObject.CompletableGithubObject):
    """
    This class represents Branch Protection.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#get-branch-protection

    The OpenAPI schema can be found at
    - /components/schemas/branch-protection
    - /components/schemas/protected-branch

    """

    def _initAttributes(self) -> None:
        self._allow_deletions: Attribute[bool] = NotSet
        self._allow_force_pushes: Attribute[bool] = NotSet
        self._allow_fork_syncing: Attribute[bool] = NotSet
        self._block_creations: Attribute[bool] = NotSet
        self._enabled: Attribute[bool] = NotSet
        self._enforce_admins: Attribute[bool] = NotSet
        self._lock_branch: Attribute[bool] = NotSet
        self._name: Attribute[str] = NotSet
        self._protection_url: Attribute[str] = NotSet
        self._required_conversation_resolution: Attribute[bool] = NotSet
        self._required_linear_history: Attribute[bool] = github.GithubObject.NotSet
        self._required_pull_request_reviews: Attribute[RequiredPullRequestReviews] = NotSet
        self._required_signatures: Attribute[bool] = NotSet
        self._required_status_checks: Attribute[RequiredStatusChecks] = NotSet
        self._restrictions: Attribute[dict[str, Any]] = NotSet
        self._team_push_restrictions: Opt[str] = NotSet
        self._url: Attribute[str] = NotSet
        self._user_push_restrictions: Opt[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"url": self._url.value})

    @property
    def allow_deletions(self) -> bool:
        self._completeIfNotSet(self._allow_deletions)
        return self._allow_deletions.value

    @property
    def allow_force_pushes(self) -> bool:
        self._completeIfNotSet(self._allow_force_pushes)
        return self._allow_force_pushes.value

    @property
    def allow_fork_syncing(self) -> bool:
        self._completeIfNotSet(self._allow_fork_syncing)
        return self._allow_fork_syncing.value

    @property
    def block_creations(self) -> bool:
        return self._block_creations.value

    @property
    def enabled(self) -> bool:
        return self._enabled.value

    @property
    def enforce_admins(self) -> bool:
        self._completeIfNotSet(self._enforce_admins)
        return self._enforce_admins.value

    @property
    def lock_branch(self) -> bool:
        self._completeIfNotSet(self._lock_branch)
        return self._lock_branch.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def protection_url(self) -> str:
        return self._protection_url.value

    @property
    def required_conversation_resolution(self) -> bool:
        self._completeIfNotSet(self._required_conversation_resolution)
        return self._required_conversation_resolution.value

    @property
    def required_linear_history(self) -> bool:
        self._completeIfNotSet(self._required_linear_history)
        return self._required_linear_history.value

    @property
    def required_pull_request_reviews(self) -> RequiredPullRequestReviews:
        self._completeIfNotSet(self._required_pull_request_reviews)
        return self._required_pull_request_reviews.value

    @property
    def required_signatures(self) -> bool:
        return self._required_signatures.value

    @property
    def required_status_checks(self) -> RequiredStatusChecks:
        self._completeIfNotSet(self._required_status_checks)
        return self._required_status_checks.value

    @property
    def restrictions(self) -> dict[str, Any]:
        return self._restrictions.value

    @property
    def url(self) -> str:
        return self._url.value

    def get_user_push_restrictions(self) -> PaginatedList[NamedUser] | None:
        if not is_defined(self._user_push_restrictions):
            return None
        return PaginatedList(
            github.NamedUser.NamedUser,
            self._requester,
            self._user_push_restrictions,
            None,
        )

    def get_team_push_restrictions(self) -> PaginatedList[Team] | None:
        if not is_defined(self._team_push_restrictions):
            return None
        return github.PaginatedList.PaginatedList(github.Team.Team, self._requester, self._team_push_restrictions, None)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "allow_deletions" in attributes:  # pragma no branch
            self._allow_deletions = self._makeBoolAttribute(attributes["allow_deletions"]["enabled"])
        if "allow_force_pushes" in attributes:  # pragma no branch
            self._allow_force_pushes = self._makeBoolAttribute(attributes["allow_force_pushes"]["enabled"])
        if "allow_fork_syncing" in attributes:  # pragma no branch
            self._allow_fork_syncing = self._makeBoolAttribute(attributes["allow_fork_syncing"]["enabled"])
        if "block_creations" in attributes:  # pragma no branch
            self._block_creations = self._makeBoolAttribute(attributes["block_creations"]["enabled"])
        if "enabled" in attributes:  # pragma no branch
            self._enabled = self._makeBoolAttribute(attributes["enabled"])
        if "enforce_admins" in attributes:  # pragma no branch
            self._enforce_admins = self._makeBoolAttribute(attributes["enforce_admins"]["enabled"])
        if "lock_branch" in attributes:  # pragma no branch
            self._lock_branch = self._makeBoolAttribute(attributes["lock_branch"]["enabled"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "protection_url" in attributes:  # pragma no branch
            self._protection_url = self._makeStringAttribute(attributes["protection_url"])
        if "required_conversation_resolution" in attributes:  # pragma no branch
            self._required_conversation_resolution = self._makeBoolAttribute(
                attributes["required_conversation_resolution"]["enabled"]
            )
        if "required_linear_history" in attributes:  # pragma no branch
            self._required_linear_history = self._makeBoolAttribute(attributes["required_linear_history"]["enabled"])
        if "required_pull_request_reviews" in attributes:  # pragma no branch
            self._required_pull_request_reviews = self._makeClassAttribute(
                github.RequiredPullRequestReviews.RequiredPullRequestReviews,
                attributes["required_pull_request_reviews"],
            )
        if "required_signatures" in attributes:  # pragma no branch
            self._required_signatures = self._makeBoolAttribute(attributes["required_signatures"]["enabled"])
        if "required_status_checks" in attributes:  # pragma no branch
            self._required_status_checks = self._makeClassAttribute(
                github.RequiredStatusChecks.RequiredStatusChecks,
                attributes["required_status_checks"],
            )
        if "restrictions" in attributes:  # pragma no branch
            self._restrictions = attributes["restrictions"]
            self._user_push_restrictions = attributes["restrictions"]["users_url"]
            self._team_push_restrictions = attributes["restrictions"]["teams_url"]
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
