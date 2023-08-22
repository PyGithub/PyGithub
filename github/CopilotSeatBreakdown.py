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

from typing import Any, Dict
from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class CopilotSeatBreakdown(CompletableGithubObject):
    """
    This class represents a Copilot for Business License. The reference can
    be found here https://docs.github.com/en/rest/copilot/copilot-for-business
    """

    def __repr__(self) -> str:
        return self.get__repr__({})

    def _initAttributes(self) -> None:
        self._active_this_cycle: Attribute[int] = NotSet
        self._added_this_cycle: Attribute[int] = NotSet
        self._inactive_this_cycle: Attribute[int] = NotSet
        self._pending_cancellation: Attribute[int] = NotSet
        self._pending_invitation: Attribute[int] = NotSet
        self._total: Attribute[int] = NotSet

    @property
    def active_this_cycle(self) -> int:
        self._completeIfNotSet(self._active_this_cycle)
        return self._active_this_cycle.value

    @property
    def added_this_cycle(self) -> int:
        self._completeIfNotSet(self._added_this_cycle)
        return self._added_this_cycle.value

    @property
    def inactive_this_cycle(self) -> int:
        self._completeIfNotSet(self._inactive_this_cycle)
        return self._inactive_this_cycle.value

    @property
    def pending_cancellation(self) -> int:
        self._completeIfNotSet(self._pending_cancellation)
        return self._pending_cancellation.value

    @property
    def pending_invitation(self) -> int:
        self._completeIfNotSet(self._pending_invitation)
        return self._pending_invitation.value

    @property
    def total(self) -> int:
        self._completeIfNotSet(self._total)
        return self._total.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "active_this_cycle" in attributes:  # pragma no branch
            self._active_this_cycle = self._makeIntAttribute(attributes["active_this_cycle"])
        if "added_this_cycle" in attributes:  # pragma no branch
            self._added_this_cycle = self._makeIntAttribute(attributes["added_this_cycle"])
        if "inactive_this_cycle" in attributes:  # pragma no branch
            self._inactive_this_cycle = self._makeIntAttribute(attributes["inactive_this_cycle"])
        if "pending_cancellation" in attributes:  # pragma no branch
            self._pending_cancellation = self._makeIntAttribute(attributes["pending_cancellation"])
        if "pending_invitation" in attributes:  # pragma no branch
            self._pending_invitation = self._makeIntAttribute(attributes["pending_invitation"])
        if "total" in attributes:  # pragma no branch
            self._total = self._makeIntAttribute(attributes["total"])
