############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Nick Campbell <nicholas.j.campbell@gmail.com>                 #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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

import github.GithubObject
import github.NamedUser
import github.TimelineEventSource
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class TimelineEvent(NonCompletableGithubObject):
    """
    This class represents IssueTimelineEvents. The reference can be found here https://docs.github.com/en/rest/reference/issues#timeline
    """

    def _initAttributes(self) -> None:
        self._actor: Attribute[github.NamedUser.NamedUser] = NotSet
        self._commit_id: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._event: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._commit_url: Attribute[str] = NotSet
        self._source: Attribute[github.TimelineEventSource.TimelineEventSource] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def actor(self) -> github.NamedUser.NamedUser:
        return self._actor.value

    @property
    def commit_id(self) -> str:
        return self._commit_id.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def event(self) -> str:
        return self._event.value

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def node_id(self) -> str:
        return self._node_id.value

    @property
    def commit_url(self) -> str:
        return self._commit_url.value

    @property
    def source(self) -> github.TimelineEventSource.TimelineEventSource | None:
        # only available on `cross-referenced` events.
        if self.event == "cross-referenced" and self._source is not NotSet:
            return self._source.value
        return None

    @property
    def body(self) -> str | None:
        if self.event == "commented" and self._body is not NotSet:
            return self._body.value
        return None

    @property
    def author_association(self) -> str | None:
        if self.event == "commented" and self._author_association is not NotSet:
            return self._author_association.value
        return None

    @property
    def url(self) -> str:
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "actor" in attributes:  # pragma no branch
            self._actor = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["actor"])
        if "commit_id" in attributes:  # pragma no branch
            self._commit_id = self._makeStringAttribute(attributes["commit_id"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "event" in attributes:  # pragma no branch
            self._event = self._makeStringAttribute(attributes["event"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "commit_url" in attributes:  # pragma no branch
            self._commit_url = self._makeStringAttribute(attributes["commit_url"])
        if "source" in attributes:  # pragma no branch
            self._source = self._makeClassAttribute(
                github.TimelineEventSource.TimelineEventSource, attributes["source"]
            )
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "author_association" in attributes:  # pragma no branch
            self._author_association = self._makeStringAttribute(attributes["author_association"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
