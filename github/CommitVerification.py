############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 timgates42 <tim.gates@gmail.com>                              #
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


class CommitVerification(NonCompletableGithubObject):
    """
    This class represents CommitVerifications.

    The reference can be found here
    https://docs.github.com/en/rest/commits/commits

    """

    def _initAttributes(self) -> None:
        self._verified: Attribute[bool] = NotSet
        self._verified_at: Attribute[datetime] = NotSet
        self._reason: Attribute[str] = NotSet
        self._signature: Attribute[str] = NotSet
        self._payload: Attribute[str] = NotSet

    @property
    def verified(self) -> bool:
        return self._verified.value

    @property
    def verified_at(self) -> datetime:
        return self._verified_at.value

    @property
    def reason(self) -> str:
        return self._reason.value

    @property
    def signature(self) -> str:
        return self._signature.value

    @property
    def payload(self) -> str:
        return self._payload.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "verified" in attributes:  # pragma no branch
            self._verified = self._makeBoolAttribute(attributes["verified"])
        if "verified_at" in attributes:  # pragma no branch
            self._verified_at = self._makeDatetimeAttribute(attributes["verified_at"])
        if "reason" in attributes:  # pragma no branch
            self._reason = self._makeStringAttribute(attributes["reason"])
        if "signature" in attributes:  # pragma no branch
            self._signature = self._makeStringAttribute(attributes["signature"])
        if "payload" in attributes:  # pragma no branch
            self._payload = self._makeStringAttribute(attributes["payload"])
