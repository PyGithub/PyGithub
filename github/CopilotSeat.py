############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Pasha Fateev <pasha@autokitteh.com>                           #
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

from datetime import datetime
from typing import TYPE_CHECKING, Any

import github.NamedUser
import github.Organization
import github.Team
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet, _NotSetType

if TYPE_CHECKING:
    from github.Organization import Organization


class CopilotSeat(NonCompletableGithubObject):
    """
    This class represents CopilotSeat.

    The reference can be found here
    https://docs.github.com/en/rest/copilot/copilot-user-management

    The OpenAPI schema can be found at

    - /components/schemas/copilot-seat-details

    """

    def _initAttributes(self) -> None:
        self._assignee: Attribute[github.NamedUser.NamedUser] | _NotSetType = NotSet
        self._assigning_team: Attribute[github.Team.Team] | _NotSetType = NotSet
        self._created_at: Attribute[datetime] | _NotSetType = NotSet
        self._last_activity_at: Attribute[datetime] | _NotSetType = NotSet
        self._last_activity_editor: Attribute[str] | _NotSetType = NotSet
        self._last_authenticated_at: Attribute[datetime] = NotSet
        self._organization: Attribute[Organization] = NotSet
        self._pending_cancellation_date: Attribute[datetime] | _NotSetType = NotSet
        self._plan_type: Attribute[str] | _NotSetType = NotSet
        self._updated_at: Attribute[datetime] | _NotSetType = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"assignee": self._assignee.value})

    @property
    def assignee(self) -> github.NamedUser.NamedUser:
        return self._assignee.value

    @property
    def assigning_team(self) -> github.Team.Team:
        return self._assigning_team.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def last_activity_at(self) -> datetime:
        return self._last_activity_at.value

    @property
    def last_activity_editor(self) -> str:
        return self._last_activity_editor.value

    @property
    def last_authenticated_at(self) -> datetime:
        return self._last_authenticated_at.value

    @property
    def organization(self) -> Organization:
        return self._organization.value

    @property
    def pending_cancellation_date(self) -> datetime:
        return self._pending_cancellation_date.value

    @property
    def plan_type(self) -> str:
        return self._plan_type.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "assignee" in attributes:
            self._assignee = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["assignee"])
        if "assigning_team" in attributes:
            self._assigning_team = self._makeClassAttribute(github.Team.Team, attributes["assigning_team"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "last_activity_at" in attributes:
            self._last_activity_at = self._makeDatetimeAttribute(attributes["last_activity_at"])
        if "last_activity_editor" in attributes:
            self._last_activity_editor = self._makeStringAttribute(attributes["last_activity_editor"])
        if "last_authenticated_at" in attributes:  # pragma no branch
            self._last_authenticated_at = self._makeDatetimeAttribute(attributes["last_authenticated_at"])
        if "organization" in attributes:  # pragma no branch
            self._organization = self._makeClassAttribute(github.Organization.Organization, attributes["organization"])
        if "pending_cancellation_date" in attributes:
            self._pending_cancellation_date = self._makeDatetimeAttribute(attributes["pending_cancellation_date"])
        if "plan_type" in attributes:
            self._plan_type = self._makeStringAttribute(attributes["plan_type"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
