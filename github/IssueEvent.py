############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Aaron L. Levine <allevin@sandia.gov>                          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

import github.GithubApp
import github.GithubObject
import github.Issue
import github.Label
import github.Milestone
import github.NamedUser
import github.Team
from github.GithubObject import Attribute, CompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.GithubApp import GithubApp
    from github.Issue import Issue
    from github.Label import Label
    from github.Milestone import Milestone
    from github.NamedUser import NamedUser
    from github.Team import Team


class IssueEvent(CompletableGithubObject):
    """
    This class represents IssueEvents.

    The reference can be found here
    https://docs.github.com/en/rest/reference/issues#events

    The OpenAPI schema can be found at
    - /components/schemas/issue-event
    - /components/schemas/issue-event-for-issue

    """

    def _initAttributes(self) -> None:
        self._actor: Attribute[NamedUser] = NotSet
        self._assignee: Attribute[NamedUser] = NotSet
        self._assigner: Attribute[NamedUser] = NotSet
        self._author_association: Attribute[dict[str, Any]] = NotSet
        self._commit_id: Attribute[str] = NotSet
        self._commit_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._dismissed_review: Attribute[dict] = NotSet
        self._event: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._issue: Attribute[Issue] = NotSet
        self._label: Attribute[Label] = NotSet
        self._lock_reason: Attribute[str] = NotSet
        self._milestone: Attribute[Milestone] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._performed_via_github_app: Attribute[GithubApp] = NotSet
        self._project_card: Attribute[dict[str, Any]] = NotSet
        self._rename: Attribute[dict] = NotSet
        self._requested_reviewer: Attribute[NamedUser] = NotSet
        self._requested_team: Attribute[Team] = NotSet
        self._review_requester: Attribute[NamedUser] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def actor(self) -> NamedUser:
        self._completeIfNotSet(self._actor)
        return self._actor.value

    @property
    def assignee(self) -> NamedUser:
        self._completeIfNotSet(self._assignee)
        return self._assignee.value

    @property
    def assigner(self) -> NamedUser:
        self._completeIfNotSet(self._assigner)
        return self._assigner.value

    @property
    def author_association(self) -> dict[str, Any]:
        self._completeIfNotSet(self._author_association)
        return self._author_association.value

    @property
    def commit_id(self) -> str:
        self._completeIfNotSet(self._commit_id)
        return self._commit_id.value

    @property
    def commit_url(self) -> str:
        self._completeIfNotSet(self._commit_url)
        return self._commit_url.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def dismissed_review(self) -> dict:
        self._completeIfNotSet(self._dismissed_review)
        return self._dismissed_review.value

    @property
    def event(self) -> str:
        self._completeIfNotSet(self._event)
        return self._event.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def issue(self) -> Issue:
        self._completeIfNotSet(self._issue)
        return self._issue.value

    @property
    def label(self) -> Label:
        self._completeIfNotSet(self._label)
        return self._label.value

    @property
    def lock_reason(self) -> str:
        self._completeIfNotSet(self._lock_reason)
        return self._lock_reason.value

    @property
    def milestone(self) -> Milestone:
        self._completeIfNotSet(self._milestone)
        return self._milestone.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def performed_via_github_app(self) -> GithubApp:
        self._completeIfNotSet(self._performed_via_github_app)
        return self._performed_via_github_app.value

    @property
    def project_card(self) -> dict[str, Any]:
        self._completeIfNotSet(self._project_card)
        return self._project_card.value

    @property
    def rename(self) -> dict:
        self._completeIfNotSet(self._rename)
        return self._rename.value

    @property
    def requested_reviewer(self) -> NamedUser:
        self._completeIfNotSet(self._requested_reviewer)
        return self._requested_reviewer.value

    @property
    def requested_team(self) -> Team:
        self._completeIfNotSet(self._requested_team)
        return self._requested_team.value

    @property
    def review_requester(self) -> NamedUser:
        self._completeIfNotSet(self._review_requester)
        return self._review_requester.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "actor" in attributes:  # pragma no branch
            self._actor = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["actor"])
        if "assignee" in attributes:  # pragma no branch
            self._assignee = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["assignee"])
        if "assigner" in attributes:  # pragma no branch
            self._assigner = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["assigner"])
        if "author_association" in attributes:  # pragma no branch
            self._author_association = self._makeDictAttribute(attributes["author_association"])
        if "commit_id" in attributes:  # pragma no branch
            self._commit_id = self._makeStringAttribute(attributes["commit_id"])
        if "commit_url" in attributes:  # pragma no branch
            self._commit_url = self._makeStringAttribute(attributes["commit_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "dismissed_review" in attributes:  # pragma no branch
            self._dismissed_review = self._makeDictAttribute(attributes["dismissed_review"])
        if "event" in attributes:  # pragma no branch
            self._event = self._makeStringAttribute(attributes["event"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "issue" in attributes:  # pragma no branch
            self._issue = self._makeClassAttribute(github.Issue.Issue, attributes["issue"])
        if "label" in attributes:  # pragma no branch
            self._label = self._makeClassAttribute(github.Label.Label, attributes["label"])
        if "lock_reason" in attributes:  # pragma no branch
            self._lock_reason = self._makeStringAttribute(attributes["lock_reason"])
        if "milestone" in attributes:  # pragma no branch
            self._milestone = self._makeClassAttribute(github.Milestone.Milestone, attributes["milestone"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "performed_via_github_app" in attributes:  # pragma no branch
            self._performed_via_github_app = self._makeClassAttribute(
                github.GithubApp.GithubApp, attributes["performed_via_github_app"]
            )
        if "project_card" in attributes:  # pragma no branch
            self._project_card = self._makeDictAttribute(attributes["project_card"])
        if "rename" in attributes:  # pragma no branch
            self._rename = self._makeDictAttribute(attributes["rename"])
        if "requested_reviewer" in attributes:  # pragma no branch
            self._requested_reviewer = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["requested_reviewer"]
            )
        if "requested_team" in attributes:  # pragma no branch
            self._requested_team = self._makeClassAttribute(github.Team.Team, attributes["requested_team"])
        if "review_requester" in attributes:  # pragma no branch
            self._review_requester = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["review_requester"]
            )
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
