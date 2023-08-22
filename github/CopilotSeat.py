############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Colby Gallup <colbygallup@gmail.com>                          #
# Copyright 2020 Pascal Hofmann <mail@pascalhofmann.de>                        #
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
from typing import Any, Dict

from github.GithubObject import Attribute, CompletableGithubObject, NotSet
from github.NamedUser import NamedUser
from github.Team import Team


class CopilotSeat(CompletableGithubObject):
    """
    This class represents a Copilot for Business License. The reference can
    be found here https://docs.github.com/en/rest/copilot/copilot-for-business
    """

    def __repr__(self) -> str:
        return self.get__repr__({})

    def _initAttributes(self) -> None:
        self._assignee: Attribute[NamedUser] = NotSet
        self._assigning_team: Attribute['Team'] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._last_activity_at: Attribute[datetime] = NotSet
        self._last_activity_editor: Attribute[str] = NotSet
        self._pending_cancellation_date: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet

    @property
    def assignee(self) -> NamedUser:
        self._completeIfNotSet(self._assignee)
        return self._assignee.value

    @property
    def assigning_team(self) -> 'Team':
        self._completeIfNotSet(self._assigning_team)
        return self._assigning_team.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def last_activity_at(self) -> datetime:
        self._completeIfNotSet(self._last_activity_at)
        return self._last_activity_at.value

    @property
    def last_activity_editor(self) -> str:
        self._completeIfNotSet(self._last_activity_editor)
        return self._last_activity_editor.value

    @property
    def pending_cancellation_date(self) -> datetime:
        self._completeIfNotSet(self._pending_cancellation_date)
        return self._pending_cancellation_date.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "assignee" in attributes:  # pragma no branch
            self._assignee = self._makeClassAttribute(NamedUser, attributes["assignee"])
        if "assigning_team" in attributes:  # pragma no branch
            self._assigning_team = self._makeClassAttribute(Team, attributes["assigning_team"])
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], str), attributes["created_at"]
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "last_activity_at" in attributes:  # pragma no branch
            assert attributes["last_activity_at"] is None or isinstance(attributes["last_activity_at"], str), attributes["last_activity_at"]
            self._last_activity_at = self._makeDatetimeAttribute(attributes["last_activity_at"])
        if "last_activity_editor" in attributes:  # pragma no branch
            self._last_activity_editor = self._makeStringAttribute(attributes["last_activity_editor"])
        if "pending_cancellation_date" in attributes:  # pragma no branch
            assert attributes["pending_cancellation_date"] is None or isinstance(attributes["pending_cancellation_date"], str), attributes["pending_cancellation_date"]
            self._pending_cancellation_date = self._makeDatetimeAttribute(attributes["pending_cancellation_date"])
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], str), attributes["updated_at"]
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
