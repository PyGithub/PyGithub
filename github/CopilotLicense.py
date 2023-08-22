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

from typing import Any, Dict

from github.GithubObject import Attribute, CompletableGithubObject, NotSet
from github.CopilotSeatBreakdown import CopilotSeatBreakdown


class CopilotLicense(CompletableGithubObject):
    """
    This class represents a Copilot for Business License. The reference can
    be found here https://docs.github.com/en/rest/copilot/copilot-for-business
    """

    def __repr__(self) -> str:
        return self.get__repr__({})

    def _initAttributes(self) -> None:
        self._seat_breakdown: CopilotSeatBreakdown = NotSet
        self._seat_management_setting: Attribute[str] = NotSet

    @property
    def seat_breakdown(self) -> CopilotSeatBreakdown:
        self._completeIfNotSet(self._seat_breakdown)
        return self._seat_breakdown.value

    @property
    def seat_management_setting(self) -> str:
        self._completeIfNotSet(self._seat_management_setting)
        return self._seat_management_setting.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "seat_breakdown" in attributes:  # pragma no branch
            self._seat_breakdown = self._makeClassAttribute(CopilotSeatBreakdown, attributes["seat_breakdown"])
        if "seat_management_setting" in attributes:  # pragma no branch
            self._seat_management_setting = self._makeStringAttribute(attributes["seat_management_setting"])
