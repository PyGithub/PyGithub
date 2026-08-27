############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 myhelix <https://github.com/myhelix>                          #
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


class AuditLog(NonCompletableGithubObject):
    """
    This class represents an organization audit log event.

    The reference can be found here
    https://docs.github.com/en/rest/orgs/orgs#get-the-audit-log-for-an-organization

    The OpenAPI schema can be found at

    - /components/schemas/audit-log-event

    """

    def _initAttributes(self) -> None:
        self._action: Attribute[str] = NotSet
        self._actor: Attribute[str] = NotSet
        self._actor_id: Attribute[int] = NotSet
        self._actor_ip: Attribute[str] = NotSet
        self._actor_location: Attribute[dict] = NotSet
        self._at: Attribute[int] = NotSet
        self._blocked_user: Attribute[str] = NotSet
        self._business: Attribute[str] = NotSet
        self._config: Attribute[list] = NotSet
        self._config_was: Attribute[list] = NotSet
        self._content_type: Attribute[str] = NotSet
        self._created_at: Attribute[int] = NotSet
        self._deploy_key_fingerprint: Attribute[str] = NotSet
        self._document_id: Attribute[str] = NotSet
        self._emoji: Attribute[str] = NotSet
        self._events: Attribute[list] = NotSet
        self._events_were: Attribute[list] = NotSet
        self._explanation: Attribute[str] = NotSet
        self._fingerprint: Attribute[str] = NotSet
        self._hook_id: Attribute[int] = NotSet
        self._limited_availability: Attribute[bool] = NotSet
        self._message: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._old_user: Attribute[str] = NotSet
        self._openssh_public_key: Attribute[str] = NotSet
        self._org: Attribute[str] = NotSet
        self._org_id: Attribute[int] = NotSet
        self._previous_visibility: Attribute[str] = NotSet
        self._read_only: Attribute[str] = NotSet
        self._repo: Attribute[str] = NotSet
        self._repository: Attribute[str] = NotSet
        self._repository_public: Attribute[bool] = NotSet
        self._target_login: Attribute[str] = NotSet
        self._team: Attribute[str] = NotSet
        self._timestamp: Attribute[int] = NotSet
        self._transport_protocol: Attribute[int] = NotSet
        self._transport_protocol_name: Attribute[str] = NotSet
        self._user: Attribute[str] = NotSet
        self._user_agent: Attribute[str] = NotSet
        self._visibility: Attribute[str] = NotSet

    @property
    def action(self) -> str | None:
        """The action performed, e.g. ``repo.create`` or ``org.add_member``."""
        return self._action.value if self._action is not NotSet else None

    @property
    def actor(self) -> str | None:
        """The GitHub username of the actor who triggered the event."""
        return self._actor.value if self._actor is not NotSet else None

    @property
    def actor_id(self) -> int | None:
        """The numeric ID of the actor."""
        return self._actor_id.value if self._actor_id is not NotSet else None

    @property
    def actor_ip(self) -> str | None:
        """The IP address of the actor at the time of the event."""
        return self._actor_ip.value if self._actor_ip is not NotSet else None

    @property
    def actor_location(self) -> dict | None:
        """Location data for the actor (dict with ``country_name``)."""
        return self._actor_location.value if self._actor_location is not NotSet else None

    @property
    def at(self) -> int | None:
        """Unix timestamp (ms) when the event occurred. Alias for ``timestamp``."""
        return self._at.value if self._at is not NotSet else None

    @property
    def created_at(self) -> int | None:
        """Unix timestamp (ms) when the event was created."""
        return self._created_at.value if self._created_at is not NotSet else None

    @property
    def document_id(self) -> str | None:
        """Unique document identifier for this audit log entry."""
        return self._document_id.value if self._document_id is not NotSet else None

    @property
    def org(self) -> str | None:
        """The organization login name."""
        return self._org.value if self._org is not NotSet else None

    @property
    def org_id(self) -> int | None:
        """The numeric organization ID."""
        return self._org_id.value if self._org_id is not NotSet else None

    @property
    def repo(self) -> str | None:
        """The ``owner/name`` of the repository involved, if applicable."""
        return self._repo.value if self._repo is not NotSet else None

    @property
    def repository(self) -> str | None:
        """Alias for ``repo``."""
        return self._repository.value if self._repository is not NotSet else None

    @property
    def timestamp(self) -> int | None:
        """Unix timestamp (ms) when the event occurred."""
        return self._timestamp.value if self._timestamp is not NotSet else None

    @property
    def user(self) -> str | None:
        """The GitHub username of the user affected by the event."""
        return self._user.value if self._user is not NotSet else None

    @property
    def user_agent(self) -> str | None:
        """The user agent string of the client that triggered the event."""
        return self._user_agent.value if self._user_agent is not NotSet else None

    @property
    def visibility(self) -> str | None:
        """Repository visibility change value, if applicable."""
        return self._visibility.value if self._visibility is not NotSet else None

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "action" in attributes:
            self._action = self._makeStringAttribute(attributes["action"])
        if "actor" in attributes:
            self._actor = self._makeStringAttribute(attributes["actor"])
        if "actor_id" in attributes:
            self._actor_id = self._makeIntAttribute(attributes["actor_id"])
        if "actor_ip" in attributes:
            self._actor_ip = self._makeStringAttribute(attributes["actor_ip"])
        if "actor_location" in attributes:
            self._actor_location = self._makeDictAttribute(attributes["actor_location"])
        if "@timestamp" in attributes:
            self._at = self._makeIntAttribute(attributes["@timestamp"])
        if "blocked_user" in attributes:
            self._blocked_user = self._makeStringAttribute(attributes["blocked_user"])
        if "business" in attributes:
            self._business = self._makeStringAttribute(attributes["business"])
        if "config" in attributes:
            self._config = self._makeListAttribute(attributes["config"])
        if "config_was" in attributes:
            self._config_was = self._makeListAttribute(attributes["config_was"])
        if "content_type" in attributes:
            self._content_type = self._makeStringAttribute(attributes["content_type"])
        if "created_at" in attributes:
            self._created_at = self._makeIntAttribute(attributes["created_at"])
        if "deploy_key_fingerprint" in attributes:
            self._deploy_key_fingerprint = self._makeStringAttribute(attributes["deploy_key_fingerprint"])
        if "_document_id" in attributes:
            self._document_id = self._makeStringAttribute(attributes["_document_id"])
        if "emoji" in attributes:
            self._emoji = self._makeStringAttribute(attributes["emoji"])
        if "events" in attributes:
            self._events = self._makeListAttribute(attributes["events"])
        if "events_were" in attributes:
            self._events_were = self._makeListAttribute(attributes["events_were"])
        if "explanation" in attributes:
            self._explanation = self._makeStringAttribute(attributes["explanation"])
        if "fingerprint" in attributes:
            self._fingerprint = self._makeStringAttribute(attributes["fingerprint"])
        if "hook_id" in attributes:
            self._hook_id = self._makeIntAttribute(attributes["hook_id"])
        if "limited_availability" in attributes:
            self._limited_availability = self._makeBoolAttribute(attributes["limited_availability"])
        if "message" in attributes:
            self._message = self._makeStringAttribute(attributes["message"])
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "old_user" in attributes:
            self._old_user = self._makeStringAttribute(attributes["old_user"])
        if "openssh_public_key" in attributes:
            self._openssh_public_key = self._makeStringAttribute(attributes["openssh_public_key"])
        if "org" in attributes:
            self._org = self._makeStringAttribute(attributes["org"])
        if "org_id" in attributes:
            self._org_id = self._makeIntAttribute(attributes["org_id"])
        if "previous_visibility" in attributes:
            self._previous_visibility = self._makeStringAttribute(attributes["previous_visibility"])
        if "read_only" in attributes:
            self._read_only = self._makeStringAttribute(attributes["read_only"])
        if "repo" in attributes:
            self._repo = self._makeStringAttribute(attributes["repo"])
        if "repository" in attributes:
            self._repository = self._makeStringAttribute(attributes["repository"])
        if "repository_public" in attributes:
            self._repository_public = self._makeBoolAttribute(attributes["repository_public"])
        if "target_login" in attributes:
            self._target_login = self._makeStringAttribute(attributes["target_login"])
        if "team" in attributes:
            self._team = self._makeStringAttribute(attributes["team"])
        if "@timestamp" in attributes:
            self._timestamp = self._makeIntAttribute(attributes["@timestamp"])
        if "transport_protocol" in attributes:
            self._transport_protocol = self._makeIntAttribute(attributes["transport_protocol"])
        if "transport_protocol_name" in attributes:
            self._transport_protocol_name = self._makeStringAttribute(attributes["transport_protocol_name"])
        if "user" in attributes:
            self._user = self._makeStringAttribute(attributes["user"])
        if "user_agent" in attributes:
            self._user_agent = self._makeStringAttribute(attributes["user_agent"])
        if "visibility" in attributes:
            self._visibility = self._makeStringAttribute(attributes["visibility"])

    def __repr__(self) -> str:
        return self.get__repr__({"action": self._action.value if self._action is not NotSet else None})
