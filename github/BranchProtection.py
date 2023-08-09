############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
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
    This class represents Branch Protection. The reference can be found here https://docs.github.com/en/rest/reference/repos#get-branch-protection
    """

    def __repr__(self) -> str:
        return self.get__repr__({"url": self._url.value})

    def _initAttributes(self) -> None:
        self._url: Attribute[str] = NotSet
        self._required_status_checks: Attribute[RequiredStatusChecks] = NotSet
        self._enforce_admins: Attribute[bool] = NotSet
        self._required_linear_history: Attribute[bool] = github.GithubObject.NotSet
        self._required_pull_request_reviews: Attribute[RequiredPullRequestReviews] = NotSet
        self._user_push_restrictions: Opt[str] = NotSet
        self._team_push_restrictions: Opt[str] = NotSet

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def required_status_checks(self) -> RequiredStatusChecks:
        self._completeIfNotSet(self._required_status_checks)
        return self._required_status_checks.value

    @property
    def enforce_admins(self) -> bool:
        self._completeIfNotSet(self._enforce_admins)
        return self._enforce_admins.value

    @property
    def required_linear_history(self) -> bool:
        self._completeIfNotSet(self._required_linear_history)
        return self._required_linear_history.value

    @property
    def required_pull_request_reviews(self) -> RequiredPullRequestReviews:
        self._completeIfNotSet(self._required_pull_request_reviews)
        return self._required_pull_request_reviews.value

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
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "required_status_checks" in attributes:  # pragma no branch
            self._required_status_checks = self._makeClassAttribute(
                github.RequiredStatusChecks.RequiredStatusChecks,
                attributes["required_status_checks"],
            )
        if "enforce_admins" in attributes:  # pragma no branch
            self._enforce_admins = self._makeBoolAttribute(attributes["enforce_admins"]["enabled"])
        if "required_pull_request_reviews" in attributes:  # pragma no branch
            self._required_pull_request_reviews = self._makeClassAttribute(
                github.RequiredPullRequestReviews.RequiredPullRequestReviews,
                attributes["required_pull_request_reviews"],
            )
        if "required_linear_history" in attributes:  # pragma no branch
            self._required_linear_history = self._makeBoolAttribute(attributes["required_linear_history"]["enabled"])
        if "restrictions" in attributes:  # pragma no branch
            self._user_push_restrictions = attributes["restrictions"]["users_url"]
            self._team_push_restrictions = attributes["restrictions"]["teams_url"]
