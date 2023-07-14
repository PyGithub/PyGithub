############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Andrew Bettison <andrewb@zip.com.au>                          #
# Copyright 2012 Philip Kimmey <philip@rover.com>                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 David Farr <david.farr@sap.com>                               #
# Copyright 2013 Stuart Glaser <stuglaser@gmail.com>                           #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Raja Reddy Karri <klnrajareddy@gmail.com>                     #
# Copyright 2016 @tmshn <tmshn@r.recruit.co.jp>                                #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Matt Babineau <babineaum@users.noreply.github.com>            #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Nicolas Agustín Torres <nicolastrres@gmail.com>               #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 per1234 <accounts@perglass.com>                               #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Nick Campbell <nicholas.j.campbell@gmail.com>                 #
# Copyright 2020 Huan-Cheng Chang <changhc84@gmail.com>                        #
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

import urllib.parse
from datetime import datetime
from typing import TYPE_CHECKING, Any

import github.GithubObject
import github.IssueComment
import github.IssueEvent
import github.IssuePullRequest
import github.Label
import github.Milestone
import github.NamedUser
import github.PullRequest
import github.Reaction
import github.Repository
import github.TimelineEvent
from github import Consts
from github.GithubObject import (
    Attribute,
    CompletableGithubObject,
    NotSet,
    Opt,
    is_defined,
    is_optional,
    is_optional_list,
    is_undefined,
)
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.IssueComment import IssueComment
    from github.IssueEvent import IssueEvent
    from github.IssuePullRequest import IssuePullRequest
    from github.Label import Label
    from github.Milestone import Milestone
    from github.NamedUser import NamedUser
    from github.PullRequest import PullRequest
    from github.Reaction import Reaction
    from github.Repository import Repository
    from github.TimelineEvent import TimelineEvent


class Issue(CompletableGithubObject):
    """
    This class represents Issues. The reference can be found here https://docs.github.com/en/rest/reference/issues
    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._active_lock_reason: Attribute[str | None] = NotSet
        self._assignee: Attribute[NamedUser | None] = NotSet
        self._assignees: Attribute[list[NamedUser]] = NotSet
        self._body: Attribute[str] = NotSet
        self._closed_at: Attribute[datetime] = NotSet
        self._closed_by: Attribute[NamedUser] = NotSet
        self._comments: Attribute[int] = NotSet
        self._comments_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._events_url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._labels: Attribute[list[Label]] = NotSet
        self._labels_url: Attribute[str] = NotSet
        self._locked: Attribute[bool] = NotSet
        self._milestone: Attribute[Milestone] = NotSet
        self._number: Attribute[int] = NotSet
        self._pull_request: Attribute[IssuePullRequest] = NotSet
        self._repository: Attribute[Repository] = NotSet
        self._state: Attribute[str] = NotSet
        self._state_reason: Attribute[str | None] = NotSet
        self._title: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._user: Attribute[NamedUser] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self._number.value, "title": self._title.value})

    @property
    def assignee(self) -> NamedUser | None:
        self._completeIfNotSet(self._assignee)
        return self._assignee.value

    @property
    def assignees(self) -> list[NamedUser]:
        self._completeIfNotSet(self._assignees)
        return self._assignees.value

    @property
    def body(self) -> str:
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def closed_at(self) -> datetime:
        self._completeIfNotSet(self._closed_at)
        return self._closed_at.value

    @property
    def closed_by(self) -> NamedUser | None:
        self._completeIfNotSet(self._closed_by)
        return self._closed_by.value

    @property
    def comments(self) -> int:
        self._completeIfNotSet(self._comments)
        return self._comments.value

    @property
    def comments_url(self) -> str:
        self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def events_url(self) -> str:
        self._completeIfNotSet(self._events_url)
        return self._events_url.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def labels(self) -> list[Label]:
        self._completeIfNotSet(self._labels)
        return self._labels.value

    @property
    def labels_url(self) -> str:
        self._completeIfNotSet(self._labels_url)
        return self._labels_url.value

    @property
    def milestone(self) -> Milestone:
        self._completeIfNotSet(self._milestone)
        return self._milestone.value

    @property
    def number(self) -> int:
        self._completeIfNotSet(self._number)
        return self._number.value

    @property
    def pull_request(self) -> IssuePullRequest | None:
        self._completeIfNotSet(self._pull_request)
        return self._pull_request.value

    @property
    def repository(self) -> Repository:
        self._completeIfNotSet(self._repository)
        if is_undefined(self._repository):
            # The repository was not set automatically, so it must be looked up by url.
            repo_url = "/".join(self.url.split("/")[:-2])
            self._repository = github.GithubObject._ValuedAttribute(
                github.Repository.Repository(self._requester, self._headers, {"url": repo_url}, completed=False)
            )
        return self._repository.value

    @property
    def state(self) -> str:
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def state_reason(self) -> str | None:
        self._completeIfNotSet(self._state_reason)
        return self._state_reason.value

    @property
    def title(self) -> str:
        self._completeIfNotSet(self._title)
        return self._title.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def user(self) -> NamedUser:
        self._completeIfNotSet(self._user)
        return self._user.value

    @property
    def locked(self) -> bool:
        self._completeIfNotSet(self._locked)
        return self._locked.value

    @property
    def active_lock_reason(self) -> str | None:
        self._completeIfNotSet(self._active_lock_reason)
        return self._active_lock_reason.value

    def as_pull_request(self) -> PullRequest:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{number} <https://docs.github.com/en/rest/reference/pulls>`_
        """
        headers, data = self._requester.requestJsonAndCheck("GET", "/pulls/".join(self.url.rsplit("/issues/", 1)))
        return github.PullRequest.PullRequest(self._requester, headers, data, completed=True)

    def add_to_assignees(self, *assignees: NamedUser | str) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{number}/assignees <https://docs.github.com/en/rest/reference/issues#assignees>`_
        """
        assert all(isinstance(element, (github.NamedUser.NamedUser, str)) for element in assignees), assignees
        post_parameters = {
            "assignees": [
                assignee.login if isinstance(assignee, github.NamedUser.NamedUser) else assignee
                for assignee in assignees
            ]
        }
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/assignees", input=post_parameters)
        self._useAttributes(data)

    def add_to_labels(self, *labels: Label | str) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        assert all(isinstance(element, (github.Label.Label, str)) for element in labels), labels
        post_parameters = [label.name if isinstance(label, github.Label.Label) else label for label in labels]
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/labels", input=post_parameters)

    def create_comment(self, body: str) -> IssueComment:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{number}/comments <https://docs.github.com/en/rest/reference/issues#comments>`_
        """
        assert isinstance(body, str), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/comments", input=post_parameters)
        return github.IssueComment.IssueComment(self._requester, headers, data, completed=True)

    def delete_labels(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/labels")

    def edit(
        self,
        title: Opt[str] = NotSet,
        body: Opt[str] = NotSet,
        assignee: Opt[str | NamedUser | None] = NotSet,
        state: Opt[str] = NotSet,
        milestone: Opt[Milestone | None] = NotSet,
        labels: Opt[list[str]] = NotSet,
        assignees: Opt[list[NamedUser | str]] = NotSet,
        state_reason: Opt[str] = NotSet,
    ) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/issues/{number} <https://docs.github.com/en/rest/reference/issues>`_
        :param assignee: deprecated, use `assignees` instead. `assignee=None` means to remove current assignee.
        :param milestone: `milestone=None` means to remove current milestone.
        """
        assert is_optional(title, str), title
        assert is_optional(body, str), body
        assert assignee is None or is_optional(assignee, (github.NamedUser.NamedUser, str)), assignee
        assert is_optional_list(assignees, (github.NamedUser.NamedUser, str)), assignees
        assert is_optional(state, str), state
        assert milestone is None or is_optional(milestone, github.Milestone.Milestone), milestone
        assert is_optional_list(labels, str), labels

        post_parameters = NotSet.remove_unset_items(
            {
                "title": title,
                "body": body,
                "state": state,
                "state_reason": state_reason,
                "labels": labels,
                "assignee": assignee._identity
                if isinstance(assignee, github.NamedUser.NamedUser)
                else (assignee or ""),
                "milestone": milestone._identity
                if isinstance(milestone, github.Milestone.Milestone)
                else (milestone or ""),
            }
        )

        if is_defined(assignees):
            post_parameters["assignees"] = [
                element._identity if isinstance(element, github.NamedUser.NamedUser) else element
                for element in assignees
            ]

        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        self._useAttributes(data)

    def lock(self, lock_reason: str) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/issues/{issue_number}/lock <https://docs.github.com/en/rest/reference/issues>`_
        """
        assert isinstance(lock_reason, str), lock_reason
        put_parameters = {"lock_reason": lock_reason}
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            f"{self.url}/lock",
            input=put_parameters,
            headers={"Accept": Consts.mediaTypeLockReasonPreview},
        )

    def unlock(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{issue_number}/lock <https://docs.github.com/en/rest/reference/issues>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/lock")

    def get_comment(self, id: int) -> IssueComment:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/comments/{id} <https://docs.github.com/en/rest/reference/issues#comments>`_
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self._parentUrl(self.url)}/comments/{id}")
        return github.IssueComment.IssueComment(self._requester, headers, data, completed=True)

    def get_comments(self, since: Opt[datetime] = NotSet) -> PaginatedList[IssueComment]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{number}/comments <https://docs.github.com/en/rest/reference/issues#comments>`_
        """
        url_parameters = {}
        if is_defined(since):
            assert isinstance(since, datetime), since
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")

        return PaginatedList(
            github.IssueComment.IssueComment,
            self._requester,
            f"{self.url}/comments",
            url_parameters,
        )

    def get_events(self) -> PaginatedList[IssueEvent]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{issue_number}/events <https://docs.github.com/en/rest/reference/issues#events>`_
        """
        return PaginatedList(
            github.IssueEvent.IssueEvent,
            self._requester,
            f"{self.url}/events",
            None,
            headers={"Accept": Consts.mediaTypeLockReasonPreview},
        )

    def get_labels(self) -> PaginatedList[Label]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        return PaginatedList(github.Label.Label, self._requester, f"{self.url}/labels", None)

    def remove_from_assignees(self, *assignees: NamedUser | str) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{number}/assignees <https://docs.github.com/en/rest/reference/issues#assignees>`_
        """
        assert all(isinstance(element, (github.NamedUser.NamedUser, str)) for element in assignees), assignees
        post_parameters = {
            "assignees": [
                assignee.login if isinstance(assignee, github.NamedUser.NamedUser) else assignee
                for assignee in assignees
            ]
        }
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/assignees", input=post_parameters)
        self._useAttributes(data)

    def remove_from_labels(self, label: Label | str) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{number}/labels/{name} <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        assert isinstance(label, (github.Label.Label, str)), label
        if isinstance(label, github.Label.Label):
            label = label._identity
        else:
            label = urllib.parse.quote(label)
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/labels/{label}")

    def set_labels(self, *labels: Label | str) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/issues/{number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        assert all(isinstance(element, (github.Label.Label, str)) for element in labels), labels
        post_parameters = [label.name if isinstance(label, github.Label.Label) else label for label in labels]
        headers, data = self._requester.requestJsonAndCheck("PUT", f"{self.url}/labels", input=post_parameters)

    def get_reactions(self) -> PaginatedList[Reaction]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{number}/reactions <https://docs.github.com/en/rest/reference/reactions#list-reactions-for-an-issue>`_
        """
        return PaginatedList(
            github.Reaction.Reaction,
            self._requester,
            f"{self.url}/reactions",
            None,
            headers={"Accept": Consts.mediaTypeReactionsPreview},
        )

    def create_reaction(self, reaction_type: str) -> Reaction:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{number}/reactions <https://docs.github.com/en/rest/reference/reactions>`_
        """
        assert isinstance(reaction_type, str), reaction_type
        post_parameters = {
            "content": reaction_type,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"{self.url}/reactions",
            input=post_parameters,
            headers={"Accept": Consts.mediaTypeReactionsPreview},
        )
        return github.Reaction.Reaction(self._requester, headers, data, completed=True)

    def delete_reaction(self, reaction_id: int) -> bool:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id} <https://docs.github.com/en/rest/reference/reactions#delete-an-issue-reaction>`_
        """
        assert isinstance(reaction_id, int), reaction_id
        status, _, _ = self._requester.requestJson(
            "DELETE",
            f"{self.url}/reactions/{reaction_id}",
            headers={"Accept": Consts.mediaTypeReactionsPreview},
        )
        return status == 204

    def get_timeline(self) -> PaginatedList[TimelineEvent]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{number}/timeline <https://docs.github.com/en/rest/reference/issues#list-timeline-events-for-an-issue>`_
        """
        return PaginatedList(
            github.TimelineEvent.TimelineEvent,
            self._requester,
            f"{self.url}/timeline",
            None,
            headers={"Accept": Consts.issueTimelineEventsPreview},
        )

    @property
    def _identity(self) -> int:
        return self.number

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "active_lock_reason" in attributes:  # pragma no branch
            self._active_lock_reason = self._makeStringAttribute(attributes["active_lock_reason"])
        if "assignee" in attributes:  # pragma no branch
            self._assignee = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["assignee"])
        if "assignees" in attributes:  # pragma no branch
            self._assignees = self._makeListOfClassesAttribute(github.NamedUser.NamedUser, attributes["assignees"])
        elif "assignee" in attributes:
            if attributes["assignee"] is not None:
                self._assignees = self._makeListOfClassesAttribute(github.NamedUser.NamedUser, [attributes["assignee"]])
            else:
                self._assignees = self._makeListOfClassesAttribute(github.NamedUser.NamedUser, [])
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "closed_at" in attributes:  # pragma no branch
            self._closed_at = self._makeDatetimeAttribute(attributes["closed_at"])
        if "closed_by" in attributes:  # pragma no branch
            self._closed_by = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["closed_by"])
        if "comments" in attributes:  # pragma no branch
            self._comments = self._makeIntAttribute(attributes["comments"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "events_url" in attributes:  # pragma no branch
            self._events_url = self._makeStringAttribute(attributes["events_url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "labels" in attributes:  # pragma no branch
            self._labels = self._makeListOfClassesAttribute(github.Label.Label, attributes["labels"])
        if "labels_url" in attributes:  # pragma no branch
            self._labels_url = self._makeStringAttribute(attributes["labels_url"])
        if "locked" in attributes:  # pragma no branch
            self._locked = self._makeBoolAttribute(attributes["locked"])
        if "milestone" in attributes:  # pragma no branch
            self._milestone = self._makeClassAttribute(github.Milestone.Milestone, attributes["milestone"])
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "pull_request" in attributes:  # pragma no branch
            self._pull_request = self._makeClassAttribute(
                github.IssuePullRequest.IssuePullRequest, attributes["pull_request"]
            )
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "state_reason" in attributes:  # pragma no branch
            self._state_reason = self._makeStringAttribute(attributes["state_reason"])
        if "title" in attributes:  # pragma no branch
            self._title = self._makeStringAttribute(attributes["title"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["user"])
