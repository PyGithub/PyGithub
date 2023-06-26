############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Nick Campbell <nicholas.j.campbell@gmail.com>                 #
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

from typing import TYPE_CHECKING

import github.Issue
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.Issue import Issue


class TimelineEventSource(NonCompletableGithubObject):
    """
    This class represents IssueTimelineEventSource. The reference can be found here https://docs.github.com/en/rest/reference/issues#timeline
    """

    def __repr__(self):
        return self.get__repr__({"type": self._type.value})

    _type: Attribute[str]
    _issue: Attribute[Issue]

    @property
    def type(self) -> str:
        return self._type.value

    @property
    def issue(self) -> Issue:
        return self._issue.value

    def _initAttributes(self):
        self._type = NotSet
        self._issue = NotSet

    def _useAttributes(self, attributes):
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
        if "issue" in attributes:  # pragma no branch
            self._issue = self._makeClassAttribute(
                github.Issue.Issue, attributes["issue"]
            )
