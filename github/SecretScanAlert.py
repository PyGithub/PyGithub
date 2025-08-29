############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Matthew Davis <35502728+matt-davis27@users.noreply.github.com>#
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
import github.SecretScanAlertInstance
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.NamedUser import NamedUser
    from github.SecretScanAlertInstance import SecretScanAlertInstance


class SecretScanAlert(NonCompletableGithubObject):
    """
    This class represents alerts from secret scanning.

    The reference can be found here
    https://docs.github.com/en/rest/reference/secret-scanning.

    The OpenAPI schema can be found at
    - /components/schemas/secret-scanning-alert

    """

    def _initAttributes(self) -> None:
        self._created_at: Attribute[datetime] = NotSet
        self._first_location_detected: Attribute[SecretScanAlertInstance] = NotSet
        self._has_more_locations: Attribute[bool] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._is_base64_encoded: Attribute[bool] = NotSet
        self._locations_url: Attribute[str] = NotSet
        self._multi_repo: Attribute[bool] = NotSet
        self._number: Attribute[int] = NotSet
        self._publicly_leaked: Attribute[bool] = NotSet
        self._push_protection_bypass_request_comment: Attribute[str | None] = NotSet
        self._push_protection_bypass_request_html_url: Attribute[str | None] = NotSet
        self._push_protection_bypass_request_reviewer: Attribute[NamedUser | None] = NotSet
        self._push_protection_bypass_request_reviewer_comment: Attribute[str | None] = NotSet
        self._push_protection_bypassed: Attribute[bool] = NotSet
        self._push_protection_bypassed_at: Attribute[datetime | None] = NotSet
        self._push_protection_bypassed_by: Attribute[NamedUser | None] = NotSet
        self._resolution: Attribute[str | None] = NotSet
        self._resolution_comment: Attribute[str | None] = NotSet
        self._resolved_at: Attribute[datetime | None] = NotSet
        self._resolved_by: Attribute[NamedUser | None] = NotSet
        self._secret: Attribute[str] = NotSet
        self._secret_type: Attribute[str] = NotSet
        self._secret_type_display_name: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._validity: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self.number})

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def first_location_detected(self) -> SecretScanAlertInstance:
        return self._first_location_detected.value

    @property
    def has_more_locations(self) -> bool:
        return self._has_more_locations.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def is_base64_encoded(self) -> bool:
        return self._is_base64_encoded.value

    @property
    def locations_url(self) -> str:
        return self._locations_url.value

    @property
    def multi_repo(self) -> bool:
        return self._multi_repo.value

    @property
    def number(self) -> int:
        return self._number.value

    @property
    def publicly_leaked(self) -> bool:
        return self._publicly_leaked.value

    @property
    def push_protection_bypass_request_comment(self) -> str | None:
        return self._push_protection_bypass_request_comment.value

    @property
    def push_protection_bypass_request_html_url(self) -> str | None:
        return self._push_protection_bypass_request_html_url.value

    @property
    def push_protection_bypass_request_reviewer(self) -> NamedUser | None:
        return self._push_protection_bypass_request_reviewer.value

    @property
    def push_protection_bypass_request_reviewer_comment(self) -> str | None:
        return self._push_protection_bypass_request_reviewer_comment.value

    @property
    def push_protection_bypassed(self) -> bool:
        return self._push_protection_bypassed.value

    @property
    def push_protection_bypassed_at(self) -> datetime | None:
        return self._push_protection_bypassed_at.value

    @property
    def push_protection_bypassed_by(self) -> NamedUser | None:
        return self._push_protection_bypassed_by.value

    @property
    def resolution(self) -> str | None:
        return self._resolution.value

    @property
    def resolution_comment(self) -> str | None:
        return self._resolution_comment.value

    @property
    def resolved_at(self) -> datetime | None:
        return self._resolved_at.value

    @property
    def resolved_by(self) -> NamedUser | None:
        return self._resolved_by.value

    @property
    def secret(self) -> str:
        return self._secret.value

    @property
    def secret_type(self) -> str:
        return self._secret_type.value

    @property
    def secret_type_display_name(self) -> str:
        return self._secret_type_display_name.value

    @property
    def state(self) -> str:
        return self._state.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def validity(self) -> str:
        return self._validity.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "first_location_detected" in attributes:
            self._first_location_detected = self._makeClassAttribute(
                github.SecretScanAlertInstance.SecretScanAlertInstance, attributes["first_location_detected"]
            )
        if "has_more_locations" in attributes:
            self._has_more_locations = self._makeBoolAttribute(attributes["has_more_locations"])
        if "html_url" in attributes:
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "is_base64_encoded" in attributes:
            self._is_base64_encoded = self._makeBoolAttribute(attributes["is_base64_encoded"])
        if "locations_url" in attributes:
            self._locations_url = self._makeStringAttribute(attributes["locations_url"])
        if "multi_repo" in attributes:
            self._multi_repo = self._makeBoolAttribute(attributes["multi_repo"])
        if "number" in attributes:
            self._number = self._makeIntAttribute(attributes["number"])
        if "publicly_leaked" in attributes:
            self._publicly_leaked = self._makeBoolAttribute(attributes["publicly_leaked"])
        if "push_protection_bypass_request_comment" in attributes:
            self._push_protection_bypass_request_comment = self._makeStringAttribute(
                attributes["push_protection_bypass_request_comment"]
            )
        if "push_protection_bypass_request_html_url" in attributes:
            self._push_protection_bypass_request_html_url = self._makeStringAttribute(
                attributes["push_protection_bypass_request_html_url"]
            )
        if "push_protection_bypass_request_reviewer" in attributes:
            self._push_protection_bypass_request_reviewer = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["push_protection_bypass_request_reviewer"]
            )
        if "push_protection_bypass_request_reviewer_comment" in attributes:
            self._push_protection_bypass_request_reviewer_comment = self._makeStringAttribute(
                attributes["push_protection_bypass_request_reviewer_comment"]
            )
        if "push_protection_bypassed" in attributes:
            self._push_protection_bypassed = self._makeBoolAttribute(attributes["push_protection_bypassed"])
        if "push_protection_bypassed_at" in attributes:
            self._push_protection_bypassed_at = self._makeDatetimeAttribute(attributes["push_protection_bypassed_at"])
        if "push_protection_bypassed_by" in attributes:
            self._push_protection_bypassed_by = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["push_protection_bypassed_by"]
            )
        if "resolution" in attributes:
            self._resolution = self._makeStringAttribute(attributes["resolution"])
        if "resolution_comment" in attributes:
            self._resolution_comment = self._makeStringAttribute(attributes["resolution_comment"])
        if "resolved_at" in attributes:
            self._resolved_at = self._makeDatetimeAttribute(attributes["resolved_at"])
        if "resolved_by" in attributes:
            self._resolved_by = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["resolved_by"])
        if "secret" in attributes:
            self._secret = self._makeStringAttribute(attributes["secret"])
        if "secret_type" in attributes:
            self._secret_type = self._makeStringAttribute(attributes["secret_type"])
        if "secret_type_display_name" in attributes:
            self._secret_type_display_name = self._makeStringAttribute(attributes["secret_type_display_name"])
        if "state" in attributes:
            self._state = self._makeStringAttribute(attributes["state"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
        if "validity" in attributes:
            self._validity = self._makeStringAttribute(attributes["validity"])
