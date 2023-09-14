############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
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

from datetime import datetime, timedelta, timezone
from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class AccessToken(NonCompletableGithubObject):
    """This class represents access tokens."""

    _created: datetime

    def _initAttributes(self) -> None:
        self._token: Attribute[str] = NotSet
        self._type: Attribute[str] = NotSet
        self._scope: Attribute[str] = NotSet
        self._expires_in: Attribute[int | None] = NotSet
        self._refresh_token: Attribute[str] = NotSet
        self._refresh_expires_in: Attribute[int | None] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "token": f"{self.token[:5]}...",
                "scope": self.scope,
                "type": self.type,
                "expires_in": self.expires_in,
                "refresh_token": (f"{self.refresh_token[:5]}..." if self.refresh_token else None),
                "refresh_token_expires_in": self.refresh_expires_in,
            }
        )

    @property
    def token(self) -> str:
        """
        :type: string
        """
        return self._token.value

    @property
    def type(self) -> str:
        """
        :type: string
        """
        return self._type.value

    @property
    def scope(self) -> str:
        """
        :type: string
        """
        return self._scope.value

    @property
    def created(self) -> datetime:
        """
        :type: datetime
        """
        return self._created

    @property
    def expires_in(self) -> int | None:
        """
        :type: Optional[int]
        """
        return self._expires_in.value

    @property
    def expires_at(self) -> datetime | None:
        """
        :type: Optional[datetime]
        """
        seconds = self.expires_in
        if seconds is not None:
            return self._created + timedelta(seconds=seconds)
        return None

    @property
    def refresh_token(self) -> str | None:
        """
        :type: Optional[string]
        """
        return self._refresh_token.value

    @property
    def refresh_expires_in(self) -> int | None:
        """
        :type: Optional[int]
        """
        return self._refresh_expires_in.value

    @property
    def refresh_expires_at(self) -> datetime | None:
        """
        :type: Optional[datetime]
        """
        seconds = self.refresh_expires_in
        if seconds is not None:
            return self._created + timedelta(seconds=seconds)
        return None

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        self._created = datetime.now(timezone.utc)
        if "access_token" in attributes:  # pragma no branch
            self._token = self._makeStringAttribute(attributes["access_token"])
        if "token_type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["token_type"])
        if "scope" in attributes:  # pragma no branch
            self._scope = self._makeStringAttribute(attributes["scope"])
        if "expires_in" in attributes:  # pragma no branch
            self._expires_in = self._makeIntAttribute(attributes["expires_in"])
        if "refresh_token" in attributes:  # pragma no branch
            self._refresh_token = self._makeStringAttribute(attributes["refresh_token"])
        if "refresh_token_expires_in" in attributes:  # pragma no branch
            self._refresh_expires_in = self._makeIntAttribute(attributes["refresh_token_expires_in"])
