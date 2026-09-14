############################ Copyrights and license ############################
#                                                                              #
# Copyright 2026 r1cksync <152320439+r1cksync@users.noreply.github.com>        #
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

from datetime import datetime
from typing import TYPE_CHECKING, Any

import github.Environment
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.Environment import Environment


class PendingDeployment(NonCompletableGithubObject):
    """
    This class represents a pending deployment, i.e. a workflow-run deployment waiting on environment protection rules.

    The reference can be found here
    https://docs.github.com/en/rest/actions/workflow-runs#get-pending-deployments-for-a-workflow-run

    The OpenAPI schema can be found at

    - /components/schemas/pending-deployment

    """

    def _initAttributes(self) -> None:
        self._environment: Attribute[Environment] = NotSet
        self._wait_timer: Attribute[int] = NotSet
        self._wait_timer_started_at: Attribute[datetime] = NotSet
        self._current_user_can_approve: Attribute[bool] = NotSet
        self._reviewers: Attribute[list[dict[str, Any]]] = NotSet

    @property
    def environment(self) -> Environment:
        return self._environment.value

    @property
    def wait_timer(self) -> int:
        return self._wait_timer.value

    @property
    def wait_timer_started_at(self) -> datetime:
        return self._wait_timer_started_at.value

    @property
    def current_user_can_approve(self) -> bool:
        return self._current_user_can_approve.value

    @property
    def reviewers(self) -> list[dict[str, Any]]:
        return self._reviewers.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "environment" in attributes:  # pragma no branch
            self._environment = self._makeClassAttribute(github.Environment.Environment, attributes["environment"])
        if "wait_timer" in attributes:  # pragma no branch
            self._wait_timer = self._makeIntAttribute(attributes["wait_timer"])
        if "wait_timer_started_at" in attributes:  # pragma no branch
            self._wait_timer_started_at = self._makeDatetimeAttribute(attributes["wait_timer_started_at"])
        if "current_user_can_approve" in attributes:  # pragma no branch
            self._current_user_can_approve = self._makeBoolAttribute(attributes["current_user_can_approve"])
        if "reviewers" in attributes:  # pragma no branch
            self._reviewers = self._makeListOfDictsAttribute(attributes["reviewers"])
