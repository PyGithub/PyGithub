from __future__ import annotations

from typing import Any

import github.NamedUser
import github.Team
from github.GithubObject import NonCompletableGithubObject, NotSet


class CopilotSeat(NonCompletableGithubObject):
    def _initAttributes(self) -> None:
        self._created_at = NotSet
        self._updated_at = NotSet
        self._pending_cancellation_date = NotSet
        self._last_activity_at = NotSet
        self._last_activity_editor = NotSet
        self._plan_type = NotSet
        self._assignee = NotSet
        self._assigning_team = NotSet

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "pending_cancellation_date" in attributes:
            self._pending_cancellation_date = self._makeDatetimeAttribute(attributes["pending_cancellation_date"])
        if "last_activity_at" in attributes:
            self._last_activity_at = self._makeDatetimeAttribute(attributes["last_activity_at"])
        if "last_activity_editor" in attributes:
            self._last_activity_editor = self._makeStringAttribute(attributes["last_activity_editor"])
        if "plan_type" in attributes:
            self._plan_type = self._makeStringAttribute(attributes["plan_type"])
        if "assignee" in attributes:
            self._assignee = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["assignee"])
        if "assigning_team" in attributes:
            self._assigning_team = self._makeClassAttribute(github.Team.Team, attributes["assigning_team"])

    def __repr__(self) -> str:
        return self.get__repr__({"assignee": self._assignee.value})

    @property
    def created_at(self) -> str:
        return self._created_at.value

    @property
    def updated_at(self) -> str:
        return self._updated_at.value

    @property
    def pending_cancellation_date(self) -> str:
        return self._pending_cancellation_date.value

    @property
    def last_activity_at(self) -> str:
        return self._last_activity_at.value

    @property
    def last_activity_editor(self) -> str:
        return self._last_activity_editor.value

    @property
    def plan_type(self) -> str:
        return self._plan_type.value

    @property
    def assignee(self) -> github.NamedUser.NamedUser:
        return self._assignee.value

    @property
    def assigning_team(self) -> github.Team.Team:
        return self._assigning_team.value
