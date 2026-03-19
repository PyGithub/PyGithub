# FILE AUTO GENERATED DO NOT TOUCH
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
# Copyright 2018 Aaron L. Levine <allevin@sandia.gov>                          #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 per1234 <accounts@perglass.com>                               #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Filipe Laíns <filipe.lains@gmail.com>                         #
# Copyright 2019 Nick Campbell <nicholas.j.campbell@gmail.com>                 #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Huan-Cheng Chang <changhc84@gmail.com>                        #
# Copyright 2020 Huw Jones <huwcbjones@outlook.com>                            #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Nicolas Schweitzer <nicolas.schweitzer@datadoghq.com>         #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Malik Shahzad Muzaffar <shahzad.malik.muzaffar@cern.ch>       #
# Copyright 2025 Changyong Um <e7217@naver.com>                                #
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

import urllib.parse
import warnings
from datetime import datetime
from typing import Any

from typing_extensions import deprecated

import github
from github import Consts

from . import (
    GithubApp,
    GithubObject,
    IssueComment,
    IssueDependenciesSummary,
    IssueEvent,
    IssuePullRequest,
    IssueType,
    Label,
    Milestone,
    NamedUser,
    PullRequest,
    Reaction,
    Repository,
    SubIssueSummary,
    TimelineEvent,
)
from .GithubObject import (
    Attribute,
    CompletableGithubObject,
    NotSet,
    Opt,
    is_defined,
    is_optional,
    is_optional_list,
    is_undefined,
)
from .PaginatedList import PaginatedList


class Issue(CompletableGithubObject):
    """
    This class represents Issues.

    The reference can be found here
    https://docs.github.com/en/rest/reference/issues

    The OpenAPI schema can be found at

    - /components/schemas/issue
    - /components/schemas/nullable-issue

    """

    def _initAttributes(self) -> None:
        self._active_lock_reason: Attribute[str | None] = NotSet
        self._assignee: Attribute[NamedUser | None] = NotSet
        self._assignees: Attribute[list[NamedUser]] = NotSet
        self._author_association: Attribute[str] = NotSet
        self._body: Attribute[str] = NotSet
        self._body_html: Attribute[str] = NotSet
        self._body_text: Attribute[str] = NotSet
        self._closed_at: Attribute[datetime] = NotSet
        self._closed_by: Attribute[NamedUser] = NotSet
        self._comments: Attribute[int] = NotSet
        self._comments_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._draft: Attribute[bool] = NotSet
        self._events_url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._issue_dependencies_summary: Attribute[IssueDependenciesSummary] = NotSet
        self._labels: Attribute[list[Label]] = NotSet
        self._labels_url: Attribute[str] = NotSet
        self._locked: Attribute[bool] = NotSet
        self._milestone: Attribute[Milestone] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._number: Attribute[int] = NotSet
        self._parent_issue_url: Attribute[str] = NotSet
        self._performed_via_github_app: Attribute[GithubApp] = NotSet
        self._pull_request: Attribute[IssuePullRequest] = NotSet
        self._reactions: Attribute[dict] = NotSet
        self._repository: Attribute[Repository] = NotSet
        self._repository_url: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._state_reason: Attribute[str | None] = NotSet
        self._sub_issues_summary: Attribute[SubIssueSummary] = NotSet
        self._text_matches: Attribute[dict[str, Any]] = NotSet
        self._timeline_url: Attribute[str] = NotSet
        self._title: Attribute[str] = NotSet
        self._type: Attribute[IssueType] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._user: Attribute[NamedUser] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self._number.value, "title": self._title.value})

    @property
    async def _identity(self) -> int:
        return await self.number

    @property
    async def active_lock_reason(self) -> str | None:
        await self._completeIfNotSet(self._active_lock_reason)
        return self._active_lock_reason.value

    @property
    @deprecated("Use assignees instead")
    async def assignee(self) -> NamedUser | None:
        await self._completeIfNotSet(self._assignee)
        return self._assignee.value

    @property
    async def assignees(self) -> list[NamedUser]:
        await self._completeIfNotSet(self._assignees)
        return self._assignees.value

    @property
    async def author_association(self) -> str:
        await self._completeIfNotSet(self._author_association)
        return self._author_association.value

    @property
    async def body(self) -> str:
        await self._completeIfNotSet(self._body)
        return self._body.value

    @property
    async def body_html(self) -> str:
        await self._completeIfNotSet(self._body_html)
        return self._body_html.value

    @property
    async def body_text(self) -> str:
        await self._completeIfNotSet(self._body_text)
        return self._body_text.value

    @property
    async def closed_at(self) -> datetime:
        await self._completeIfNotSet(self._closed_at)
        return self._closed_at.value

    @property
    async def closed_by(self) -> NamedUser | None:
        await self._completeIfNotSet(self._closed_by)
        return self._closed_by.value

    @property
    async def comments(self) -> int:
        await self._completeIfNotSet(self._comments)
        return self._comments.value

    @property
    async def comments_url(self) -> str:
        await self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    async def created_at(self) -> datetime:
        await self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    async def draft(self) -> bool:
        await self._completeIfNotSet(self._draft)
        return self._draft.value

    @property
    async def events_url(self) -> str:
        await self._completeIfNotSet(self._events_url)
        return self._events_url.value

    @property
    async def html_url(self) -> str:
        await self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    async def id(self) -> int:
        await self._completeIfNotSet(self._id)
        return self._id.value

    @property
    async def issue_dependencies_summary(self) -> IssueDependenciesSummary:
        await self._completeIfNotSet(self._issue_dependencies_summary)
        return self._issue_dependencies_summary.value

    @property
    async def labels(self) -> list[Label]:
        await self._completeIfNotSet(self._labels)
        return self._labels.value

    @property
    async def labels_url(self) -> str:
        await self._completeIfNotSet(self._labels_url)
        return self._labels_url.value

    @property
    async def locked(self) -> bool:
        await self._completeIfNotSet(self._locked)
        return self._locked.value

    @property
    async def milestone(self) -> Milestone:
        await self._completeIfNotSet(self._milestone)
        return self._milestone.value

    @property
    async def node_id(self) -> str:
        await self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    async def number(self) -> int:
        await self._completeIfNotSet(self._number)
        return self._number.value

    @property
    async def parent_issue_url(self) -> str:
        await self._completeIfNotSet(self._parent_issue_url)
        return self._parent_issue_url.value

    @property
    async def performed_via_github_app(self) -> GithubApp:
        await self._completeIfNotSet(self._performed_via_github_app)
        return self._performed_via_github_app.value

    @property
    async def pull_request(self) -> IssuePullRequest | None:
        await self._completeIfNotSet(self._pull_request)
        return self._pull_request.value

    @property
    async def reactions(self) -> dict:
        await self._completeIfNotSet(self._reactions)
        return self._reactions.value

    @property
    async def repository(self) -> Repository:
        await self._completeIfNotSet(self._repository)
        if is_undefined(self._repository):
            # The repository was not set automatically, so it must be looked up by url.
            repo_url = "/".join((await self.url).split("/")[:-2])
            self._repository = GithubObject._ValuedAttribute(
                Repository.Repository(self._requester, self._headers, {"url": repo_url}, completed=False)
            )
        return self._repository.value

    @property
    async def repository_url(self) -> str:
        await self._completeIfNotSet(self._repository_url)
        return self._repository_url.value

    @property
    async def state(self) -> str:
        await self._completeIfNotSet(self._state)
        return self._state.value

    @property
    async def state_reason(self) -> str | None:
        await self._completeIfNotSet(self._state_reason)
        return self._state_reason.value

    @property
    async def sub_issues_summary(self) -> SubIssueSummary:
        await self._completeIfNotSet(self._sub_issues_summary)
        return self._sub_issues_summary.value

    @property
    async def text_matches(self) -> dict[str, Any]:
        await self._completeIfNotSet(self._text_matches)
        return self._text_matches.value

    @property
    async def timeline_url(self) -> str:
        await self._completeIfNotSet(self._timeline_url)
        return self._timeline_url.value

    @property
    async def title(self) -> str:
        await self._completeIfNotSet(self._title)
        return self._title.value

    @property
    async def type(self) -> IssueType:
        await self._completeIfNotSet(self._type)
        return self._type.value

    @property
    async def updated_at(self) -> datetime:
        await self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    async def url(self) -> str:
        await self._completeIfNotSet(self._url)
        return self._url.value

    @property
    async def user(self) -> NamedUser:
        await self._completeIfNotSet(self._user)
        return self._user.value

    async def as_pull_request(self) -> PullRequest:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{pull_number} <https://docs.github.com/en/rest/reference/pulls>`_
        """
        url = "/pulls/".join((await self.url).rsplit("/issues/", 1))
        return PullRequest.PullRequest(self._requester, url=url)

    async def add_to_assignees(self, *assignees: NamedUser | str) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{issue_number}/assignees <https://docs.github.com/en/rest/reference/issues#assignees>`_
        """
        assert all(
            isinstance(element, (NamedUser.NamedUser, github.NamedUser.NamedUser, str)) for element in assignees
        ), assignees
        post_parameters = {
            "assignees": [
                (await assignee.login)
                if isinstance(assignee, (NamedUser.NamedUser, github.NamedUser.NamedUser))
                else assignee
                for assignee in assignees
            ]
        }
        headers, data = await self._requester.requestJsonAndCheck(
            "POST", f"{await self.url}/assignees", input=post_parameters
        )
        self._useAttributes(data)
        self._set_complete()

    async def add_to_labels(self, *labels: Label | str) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{issue_number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        assert all(isinstance(element, (Label.Label, github.Label.Label, str)) for element in labels), labels
        post_parameters = [
            (await label.name) if isinstance(label, (Label.Label, github.Label.Label)) else label for label in labels
        ]
        headers, data = await self._requester.requestJsonAndCheck(
            "POST", f"{await self.url}/labels", input=post_parameters
        )

    async def create_comment(self, body: str) -> IssueComment:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{issue_number}/comments <https://docs.github.com/en/rest/reference/issues#comments>`_
        """
        assert isinstance(body, str), body
        post_parameters = {
            "body": body,
        }
        headers, data = await self._requester.requestJsonAndCheck(
            "POST", f"{await self.url}/comments", input=post_parameters
        )
        return IssueComment.IssueComment(self._requester, headers, data, completed=True)

    async def delete_labels(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{issue_number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        headers, data = await self._requester.requestJsonAndCheck("DELETE", f"{await self.url}/labels")

    # breaking change: remove deprecated assignee
    async def edit(
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
        :calls: `PATCH /repos/{owner}/{repo}/issues/{issue_number} <https://docs.github.com/en/rest/reference/issues>`_
        :param assignee: deprecated, use `assignees` instead. `assignee=None` means to remove current assignee.
        :param milestone: `milestone=None` means to remove current milestone.
        """
        assert is_optional(title, str), title
        assert is_optional(body, str), body
        assert assignee is None or is_optional(assignee, (NamedUser.NamedUser, str)), assignee
        assert is_optional_list(assignees, (NamedUser.NamedUser, str)), assignees
        assert is_optional(state, str), state
        assert milestone is None or is_optional(milestone, Milestone.Milestone), milestone
        assert is_optional_list(labels, str), labels

        if assignee is None or is_defined(assignee):
            warnings.warn(
                "Argument assignee is deprecated, please use assignees=[assignee] instead",
                category=DeprecationWarning,
            )
            if is_undefined(assignees):
                assignees = [assignee] if assignee is not None else []  # type: ignore
        if is_defined(assignees):
            assignees = [
                (await element._identity)
                if isinstance(element, (NamedUser.NamedUser, github.NamedUser.NamedUser))
                else element
                for element in assignees
            ]

        post_parameters = NotSet.remove_unset_items(
            {
                "title": title,
                "body": body,
                "state": state,
                "state_reason": state_reason,
                "labels": labels,
                "assignees": assignees,
                "milestone": milestone._identity
                if isinstance(milestone, (Milestone.Milestone, github.Milestone.Milestone))
                else (milestone or ""),
            }
        )

        headers, data = await self._requester.requestJsonAndCheck("PATCH", await self.url, input=post_parameters)
        self._useAttributes(data)
        self._set_complete()

    async def lock(self, lock_reason: str) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/issues/{issue_number}/lock <https://docs.github.com/en/rest/reference/issues>`_
        """
        assert isinstance(lock_reason, str), lock_reason
        put_parameters = {"lock_reason": lock_reason}
        headers, data = await self._requester.requestJsonAndCheck(
            "PUT",
            f"{await self.url}/lock",
            input=put_parameters,
            headers={"Accept": Consts.mediaTypeLockReasonPreview},
        )

    async def unlock(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{issue_number}/lock <https://docs.github.com/en/rest/reference/issues>`_
        """
        headers, data = await self._requester.requestJsonAndCheck("DELETE", f"{await self.url}/lock")

    async def get_comment(self, id: int) -> IssueComment:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/comments/{comment_id} <https://docs.github.com/en/rest/reference/issues#comments>`_
        """
        assert isinstance(id, int), id
        url = f"{self._parentUrl(await self.url)}/comments/{id}"
        return IssueComment.IssueComment(self._requester, url=url)

    async def get_comments(self, since: Opt[datetime] = NotSet) -> PaginatedList[IssueComment]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{issue_number}/comments <https://docs.github.com/en/rest/reference/issues#comments>`_
        """
        url_parameters = {}
        if is_defined(since):
            assert isinstance(since, datetime), since
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")

        return PaginatedList(
            IssueComment.IssueComment,
            self._requester,
            f"{await self.url}/comments",
            url_parameters,
        )

    async def get_events(self) -> PaginatedList[IssueEvent]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{issue_number}/events <https://docs.github.com/en/rest/reference/issues#events>`_
        """
        return PaginatedList(
            IssueEvent.IssueEvent,
            self._requester,
            f"{await self.url}/events",
            None,
            headers={"Accept": Consts.mediaTypeLockReasonPreview},
        )

    async def get_labels(self) -> PaginatedList[Label]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{issue_number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        return PaginatedList(Label.Label, self._requester, f"{await self.url}/labels", None)

    async def remove_from_assignees(self, *assignees: NamedUser | str) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{issue_number}/assignees <https://docs.github.com/en/rest/reference/issues#assignees>`_
        """
        assert all(
            isinstance(element, (NamedUser.NamedUser, github.NamedUser.NamedUser, str)) for element in assignees
        ), assignees
        post_parameters = {
            "assignees": [
                (await assignee.login)
                if isinstance(assignee, (NamedUser.NamedUser, github.NamedUser.NamedUser))
                else assignee
                for assignee in assignees
            ]
        }
        headers, data = await self._requester.requestJsonAndCheck(
            "DELETE", f"{await self.url}/assignees", input=post_parameters
        )
        self._useAttributes(data)
        self._set_complete()

    async def remove_from_labels(self, label: Label | str) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{issue_number}/labels/{name} <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        assert isinstance(label, (Label.Label, github.Label.Label, str)), label
        if isinstance(label, (Label.Label, github.Label.Label)):
            label = await label._identity
        else:
            label = urllib.parse.quote(label)
        headers, data = await self._requester.requestJsonAndCheck("DELETE", f"{await self.url}/labels/{label}")

    async def set_labels(self, *labels: Label | str) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/issues/{issue_number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        assert all(isinstance(element, (Label.Label, github.Label.Label, str)) for element in labels), labels
        post_parameters = [
            (await label.name) if isinstance(label, (Label.Label, github.Label.Label)) else label for label in labels
        ]
        headers, data = await self._requester.requestJsonAndCheck(
            "PUT", f"{await self.url}/labels", input=post_parameters
        )

    async def get_reactions(self) -> PaginatedList[Reaction]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{issue_number}/reactions <https://docs.github.com/en/rest/reference/reactions#list-reactions-for-an-issue>`_
        """
        return PaginatedList(
            Reaction.Reaction,
            self._requester,
            f"{await self.url}/reactions",
            None,
            headers={"Accept": Consts.mediaTypeReactionsPreview},
        )

    async def get_sub_issues(self) -> PaginatedList[SubIssue]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{issue_number}/sub_issues <https://docs.github.com/en/rest/issues/sub-issues?apiVersion=2022-11-28>`_
        :rtype: :class:`PaginatedList` of :class:`Issue`
        """
        return PaginatedList(
            SubIssue,
            self._requester,
            f"{await self.url}/sub_issues",
            None,
            headers={"Accept": Consts.mediaType},
        )

    async def add_sub_issue(self, sub_issue: int | Issue) -> SubIssue:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{issue_number}/sub_issues <https://docs.github.com/en/rest/issues/sub-issues>`_
        :param sub_issue: int (sub-issue ID) or Issue object. Note: Use sub_issue.id, not sub_issue.number
        :rtype: :class:`Issue.SubIssue`
        """
        assert isinstance(sub_issue, (int, Issue)), sub_issue

        sub_issue_id = sub_issue
        if isinstance(sub_issue, Issue):
            sub_issue_id = await sub_issue.id

        post_parameters: dict[str, Any] = {
            "sub_issue_id": sub_issue_id,
        }
        headers, data = await self._requester.requestJsonAndCheck(
            "POST",
            f"{await self.url}/sub_issues",
            input=post_parameters,
            headers={"Accept": Consts.mediaType},
        )
        return SubIssue(self._requester, headers, data, completed=True)

    async def remove_sub_issue(self, sub_issue: int | Issue) -> SubIssue:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{issue_number}/sub_issue <https://docs.github.com/en/rest/issues/sub-issues>`_
        :param sub_issue: int (sub-issue ID) or Issue object. Note: Use sub_issue.id, not sub_issue.number
        :rtype: :class:`Issue.SubIssue`
        """
        assert isinstance(sub_issue, (int, Issue)), sub_issue

        sub_issue_id = sub_issue
        if isinstance(sub_issue, Issue):
            sub_issue_id = await sub_issue.id

        post_parameters: dict[str, Any] = {
            "sub_issue_id": sub_issue_id,
        }
        headers, data = await self._requester.requestJsonAndCheck(
            "DELETE",
            f"{await self.url}/sub_issue",
            input=post_parameters,
            headers={"Accept": Consts.mediaType},
        )
        return SubIssue(self._requester, headers, data, completed=True)

    async def prioritize_sub_issue(self, sub_issue: int | Issue, after_sub_issue: int | Issue | None) -> SubIssue:
        """
        :calls: `PATCH /repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priority <https://docs.github.com/en/rest/issues/sub-issues>`_
        :param sub_issue: int (sub-issue ID) or Issue object. Note: Use sub_issue.id, not sub_issue.number
        :param after_sub_issue: int (sub-issue ID) or Issue object. Note: Use sub_issue.id, not sub_issue.number
        :rtype: :class:`Issue.SubIssue`
        """
        assert isinstance(sub_issue, (int, Issue)), sub_issue
        assert after_sub_issue is None or isinstance(after_sub_issue, (int, Issue)), after_sub_issue

        sub_issue_id = sub_issue
        if isinstance(sub_issue, Issue):
            sub_issue_id = await sub_issue.id
        after_sub_issue_id = after_sub_issue
        if isinstance(after_sub_issue, Issue):
            after_sub_issue_id = await after_sub_issue.id

        patch_parameters = {"sub_issue_id": sub_issue_id, "after_id": after_sub_issue_id}
        headers, data = await self._requester.requestJsonAndCheck(
            "PATCH",
            f"{await self.url}/sub_issues/priority",
            input=patch_parameters,
            headers={"Accept": Consts.mediaType},
        )
        return SubIssue(self._requester, headers, data, completed=True)

    async def create_reaction(self, reaction_type: str) -> Reaction:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{issue_number}/reactions <https://docs.github.com/en/rest/reference/reactions>`_
        """
        assert isinstance(reaction_type, str), reaction_type
        post_parameters = {
            "content": reaction_type,
        }
        headers, data = await self._requester.requestJsonAndCheck(
            "POST",
            f"{await self.url}/reactions",
            input=post_parameters,
            headers={"Accept": Consts.mediaTypeReactionsPreview},
        )
        return Reaction.Reaction(self._requester, headers, data)

    async def delete_reaction(self, reaction_id: int) -> bool:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id} <https://docs.github.com/en/rest/reference/reactions#delete-an-issue-reaction>`_
        """
        assert isinstance(reaction_id, int), reaction_id
        status, _, _ = await self._requester.requestJson(
            "DELETE",
            f"{await self.url}/reactions/{reaction_id}",
            headers={"Accept": Consts.mediaTypeReactionsPreview},
        )
        return status == 204

    async def get_timeline(self) -> PaginatedList[TimelineEvent]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{issue_number}/timeline <https://docs.github.com/en/rest/reference/issues#list-timeline-events-for-an-issue>`_
        """
        return PaginatedList(
            TimelineEvent.TimelineEvent,
            self._requester,
            f"{await self.url}/timeline",
            None,
            headers={"Accept": Consts.issueTimelineEventsPreview},
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "active_lock_reason" in attributes:  # pragma no branch
            self._active_lock_reason = self._makeStringAttribute(attributes["active_lock_reason"])
        if "assignee" in attributes:  # pragma no branch
            self._assignee = self._makeClassAttribute(NamedUser.NamedUser, attributes["assignee"])
        if "assignees" in attributes:  # pragma no branch
            self._assignees = self._makeListOfClassesAttribute(NamedUser.NamedUser, attributes["assignees"])
        elif "assignee" in attributes:
            if attributes["assignee"] is not None:
                self._assignees = self._makeListOfClassesAttribute(NamedUser.NamedUser, [attributes["assignee"]])
            else:
                self._assignees = self._makeListOfClassesAttribute(NamedUser.NamedUser, [])
        if "author_association" in attributes:  # pragma no branch
            self._author_association = self._makeStringAttribute(attributes["author_association"])
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "body_html" in attributes:  # pragma no branch
            self._body_html = self._makeStringAttribute(attributes["body_html"])
        if "body_text" in attributes:  # pragma no branch
            self._body_text = self._makeStringAttribute(attributes["body_text"])
        if "closed_at" in attributes:  # pragma no branch
            self._closed_at = self._makeDatetimeAttribute(attributes["closed_at"])
        if "closed_by" in attributes:  # pragma no branch
            self._closed_by = self._makeClassAttribute(NamedUser.NamedUser, attributes["closed_by"])
        if "comments" in attributes:  # pragma no branch
            self._comments = self._makeIntAttribute(attributes["comments"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "draft" in attributes:  # pragma no branch
            self._draft = self._makeBoolAttribute(attributes["draft"])
        if "events_url" in attributes:  # pragma no branch
            self._events_url = self._makeStringAttribute(attributes["events_url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "issue_dependencies_summary" in attributes:  # pragma no branch
            self._issue_dependencies_summary = self._makeClassAttribute(
                IssueDependenciesSummary.IssueDependenciesSummary, attributes["issue_dependencies_summary"]
            )
        if "labels" in attributes:  # pragma no branch
            self._labels = self._makeListOfClassesAttribute(Label.Label, attributes["labels"])
        if "labels_url" in attributes:  # pragma no branch
            self._labels_url = self._makeStringAttribute(attributes["labels_url"])
        if "locked" in attributes:  # pragma no branch
            self._locked = self._makeBoolAttribute(attributes["locked"])
        if "milestone" in attributes:  # pragma no branch
            self._milestone = self._makeClassAttribute(Milestone.Milestone, attributes["milestone"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        elif "url" in attributes:
            number = attributes["url"].split("/")[-1]
            if number.isnumeric():
                self._number = self._makeIntAttribute(int(number))
        if "parent_issue_url" in attributes:  # pragma no branch
            self._parent_issue_url = self._makeStringAttribute(attributes["parent_issue_url"])
        if "performed_via_github_app" in attributes:  # pragma no branch
            self._performed_via_github_app = self._makeClassAttribute(
                GithubApp.GithubApp, attributes["performed_via_github_app"]
            )
        if "pull_request" in attributes:  # pragma no branch
            self._pull_request = self._makeClassAttribute(IssuePullRequest.IssuePullRequest, attributes["pull_request"])
        if "reactions" in attributes:
            self._reactions = self._makeDictAttribute(attributes["reactions"])
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(Repository.Repository, attributes["repository"])
        if "repository_url" in attributes:  # pragma no branch
            self._repository_url = self._makeStringAttribute(attributes["repository_url"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "state_reason" in attributes:  # pragma no branch
            self._state_reason = self._makeStringAttribute(attributes["state_reason"])
        if "sub_issues_summary" in attributes:  # pragma no branch
            self._sub_issues_summary = self._makeClassAttribute(
                SubIssueSummary.SubIssueSummary, attributes["sub_issues_summary"]
            )
        if "text_matches" in attributes:  # pragma no branch
            self._text_matches = self._makeDictAttribute(attributes["text_matches"])
        if "timeline_url" in attributes:  # pragma no branch
            self._timeline_url = self._makeStringAttribute(attributes["timeline_url"])
        if "title" in attributes:  # pragma no branch
            self._title = self._makeStringAttribute(attributes["title"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeClassAttribute(IssueType.IssueType, attributes["type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(NamedUser.NamedUser, attributes["user"])


class IssueSearchResult(Issue):
    """
    This class represents IssueSearchResult.

    The reference can be found here
    https://docs.github.com/en/rest/reference/search#search-issues-and-pull-requests

    The OpenAPI schema can be found at

    - /components/schemas/issue-search-result-item

    """

    def _initAttributes(self) -> None:
        # TODO: remove if parent does not implement this
        super()._initAttributes()
        self._score: Attribute[float] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self._number.value, "title": self._title.value, "score": self._score.value})

    @property
    async def score(self) -> float:
        await self._completeIfNotSet(self._score)
        return self._score.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        # TODO: remove if parent does not implement this
        super()._useAttributes(attributes)
        if "score" in attributes:  # pragma no branch
            self._score = self._makeFloatAttribute(attributes["score"])


class SubIssue(Issue):
    """
    This class represents a Sub-issue in GitHub's REST API. Sub-issues are issues that are linked to a parent issue.

    See https://docs.github.com/en/rest/issues/sub-issues for more details.

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        # Sub-issue specific attributes
        self._parent_issue: Attribute[Issue] = NotSet
        self._priority_position: Attribute[int] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self._number.value, "title": self._title.value})

    @property
    async def parent_issue(self) -> Issue:
        """
        :type: :class:`Issue`
        """
        await self._completeIfNotSet(self._parent_issue)
        return self._parent_issue.value

    @property
    async def priority_position(self) -> int:
        """
        :type: int
        """
        await self._completeIfNotSet(self._priority_position)
        return self._priority_position.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        # Process sub-issue specific attributes
        if "parent_issue" in attributes:
            self._parent_issue = self._makeClassAttribute(Issue, attributes["parent_issue"])
        if "priority_position" in attributes:
            self._priority_position = self._makeIntAttribute(attributes["priority_position"])
