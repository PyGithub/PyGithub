############################ Copyrights and license ############################
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
from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class AuthorizationOrganization(NonCompletableGithubObject):
    """
    This class represents credential authorizations for an organization that uses SAML single sign-on.

    The reference can be found here
    https://docs.github.com/enterprise-cloud@latest//rest/orgs/orgs#list-saml-sso-authorizations-for-an-organization

    The OpenAPI schema can be found at
    - /components/schemas/credential-authorization

    """

    def _initAttributes(self) -> None:
        self._authorized_credential_expires_at: Attribute[datetime | None] = NotSet
        self._authorized_credential_id: Attribute[int | None] = NotSet
        self._authorized_credential_note: Attribute[str | None] = NotSet
        self._authorized_credential_title: Attribute[str | None] = NotSet
        self._credential_accessed_at: Attribute[datetime | None] = NotSet
        self._credential_authorized_at: Attribute[datetime] = NotSet
        self._credential_id: Attribute[int] = NotSet
        self._credential_type: Attribute[str] = NotSet
        self._fingerprint: Attribute[str | None] = NotSet
        self._login: Attribute[str] = NotSet
        self._scopes: Attribute[list[str]] = NotSet
        self._token_last_eight: Attribute[str | None] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"credential_id": self._credential_id.value})

    @property
    def authorized_credential_expires_at(self) -> datetime | None:
        return self._authorized_credential_expires_at.value

    @property
    def authorized_credential_id(self) -> int | None:
        return self._authorized_credential_id.value

    @property
    def authorized_credential_note(self) -> str | None:
        return self._authorized_credential_note.value

    @property
    def authorized_credential_title(self) -> str | None:
        return self._authorized_credential_title.value

    @property
    def credential_accessed_at(self) -> datetime | None:
        return self._credential_accessed_at.value

    @property
    def credential_authorized_at(self) -> datetime:
        return self._credential_authorized_at.value

    @property
    def credential_id(self) -> int:
        return self._credential_id.value

    @property
    def credential_type(self) -> str:
        return self._credential_type.value

    @property
    def fingerprint(self) -> str | None:
        return self._fingerprint.value

    @property
    def login(self) -> str:
        return self._login.value

    @property
    def scopes(self) -> list[str]:
        return self._scopes.value

    @property
    def token_last_eight(self) -> str | None:
        return self._token_last_eight.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "authorized_credential_expires_at" in attributes:  # pragma no branch
            self._authorized_credential_expires_at = self._makeDatetimeAttribute(
                attributes["authorized_credential_expires_at"]
            )
        if "authorized_credential_id" in attributes:  # pragma no branch
            self._authorized_credential_id = self._makeIntAttribute(attributes["authorized_credential_id"])
        if "authorized_credential_note" in attributes:  # pragma no branch
            self._authorized_credential_note = self._makeStringAttribute(attributes["authorized_credential_note"])
        if "authorized_credential_title" in attributes:  # pragma no branch
            self._authorized_credential_title = self._makeStringAttribute(attributes["authorized_credential_title"])
        if "credential_accessed_at" in attributes:  # pragma no branch
            self._credential_accessed_at = self._makeDatetimeAttribute(attributes["credential_accessed_at"])
        if "credential_authorized_at" in attributes:  # pragma no branch
            self._credential_authorized_at = self._makeDatetimeAttribute(attributes["credential_authorized_at"])
        if "credential_id" in attributes:  # pragma no branch
            self._credential_id = self._makeIntAttribute(attributes["credential_id"])
        if "credential_type" in attributes:  # pragma no branch
            self._credential_type = self._makeStringAttribute(attributes["credential_type"])
        if "fingerprint" in attributes:  # pragma no branch
            self._fingerprint = self._makeStringAttribute(attributes["fingerprint"])
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "scopes" in attributes:  # pragma no branch
            self._scopes = self._makeListOfStringsAttribute(attributes["scopes"])
        if "token_last_eight" in attributes:  # pragma no branch
            self._token_last_eight = self._makeStringAttribute(attributes["token_last_eight"])
