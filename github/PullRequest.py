############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Michael Stead <michael.stead@gmail.com>                       #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 @tmshn <tmshn@r.recruit.co.jp>                                #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Aaron Levine <allevin@sandia.gov>                             #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Ben Yohay <ben@lightricks.com>                                #
# Copyright 2018 Brian J. Murrell <brian@interlinx.bc.ca>                      #
# Copyright 2018 Gilad Shefer <gshefer@redhat.com>                             #
# Copyright 2018 Martin Monperrus <monperrus@users.noreply.github.com>         #
# Copyright 2018 Matt Babineau <9685860+babineaum@users.noreply.github.com>    #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Thibault Jamet <tjamet@users.noreply.github.com>              #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 per1234 <accounts@perglass.com>                               #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 MarcoFalke <falke.marco@gmail.com>                            #
# Copyright 2019 Mark Browning <mark@cerebras.net>                             #
# Copyright 2019 MurphyZhao <d2014zjt@163.com>                                 #
# Copyright 2019 Olof-Joachim Frahm (欧雅福) <olof@macrolet.net>                  #
# Copyright 2019 Pavan Kunisetty <nagapavan@users.noreply.github.com>          #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Tim Gates <tim.gates@iress.com>                               #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Alice GIRARD <bouhahah@gmail.com>                             #
# Copyright 2020 Florent Clarret <florent.clarret@gmail.com>                   #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 tison <wander4096@gmail.com>                                  #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Heitor Polidoro <14806300+heitorpolidoro@users.noreply.github.com>#
# Copyright 2023 Heitor Polidoro <heitor.polidoro@gmail.com>                   #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 sd-kialo <138505487+sd-kialo@users.noreply.github.com>        #
# Copyright 2023 vanya20074 <vanya20074@gmail.com>                             #
# Copyright 2024 Austin Sasko <austintyler0239@yahoo.com>                      #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Kobbi Gal <85439776+kgal-pan@users.noreply.github.com>        #
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

from typing_extensions import NotRequired, TypedDict

import github.Commit
import github.File
import github.IssueComment
import github.IssueEvent
import github.Label
import github.Milestone
import github.NamedUser
import github.PaginatedList
import github.PullRequestComment
import github.PullRequestMergeStatus
import github.PullRequestPart
import github.PullRequestReview
import github.Team
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
from github.Issue import Issue
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.GitRef import GitRef
    from github.NamedUser import NamedUser


class ReviewComment(TypedDict):
    path: str
    position: NotRequired[int]
    body: str
    line: NotRequired[int]
    side: NotRequired[str]
    start_line: NotRequired[int]
    start_side: NotRequired[str]


class PullRequest(CompletableGithubObject):
    """
    This class represents PullRequests.

    The reference can be found here
    https://docs.github.com/en/rest/reference/pulls

    """

    def _initAttributes(self) -> None:
        self._additions: Attribute[int] = NotSet
        self._assignee: Attribute[github.NamedUser.NamedUser] = NotSet
        self._assignees: Attribute[list[NamedUser]] = NotSet
        self._base: Attribute[github.PullRequestPart.PullRequestPart] = NotSet
        self._body: Attribute[str] = NotSet
        self._changed_files: Attribute[int] = NotSet
        self._closed_at: Attribute[datetime | None] = NotSet
        self._comments: Attribute[int] = NotSet
        self._comments_url: Attribute[str] = NotSet
        self._commits: Attribute[int] = NotSet
        self._commits_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._deletions: Attribute[int] = NotSet
        self._diff_url: Attribute[str] = NotSet
        self._draft: Attribute[bool] = NotSet
        self._head: Attribute[github.PullRequestPart.PullRequestPart] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._issue_url: Attribute[str] = NotSet
        self._labels: Attribute[list[github.Label.Label]] = NotSet
        self._merge_commit_sha: Attribute[str] = NotSet
        self._mergeable: Attribute[bool] = NotSet
        self._mergeable_state: Attribute[str] = NotSet
        self._merged: Attribute[bool] = NotSet
        self._merged_at: Attribute[datetime | None] = NotSet
        self._merged_by: Attribute[github.NamedUser.NamedUser] = NotSet
        self._milestone: Attribute[github.Milestone.Milestone] = NotSet
        self._number: Attribute[int] = NotSet
        self._patch_url: Attribute[str] = NotSet
        self._rebaseable: Attribute[bool] = NotSet
        self._requested_reviewers: Attribute[list[NamedUser]] = NotSet
        self._review_comment_url: Attribute[str] = NotSet
        self._review_comments: Attribute[int] = NotSet
        self._review_comments_url: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._title: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime | None] = NotSet
        self._url: Attribute[str] = NotSet
        self._user: Attribute[github.NamedUser.NamedUser] = NotSet
        self._maintainer_can_modify: Attribute[bool] = NotSet
        self._node_id: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self._number.value, "title": self._title.value})

    @property
    def additions(self) -> int:
        self._completeIfNotSet(self._additions)
        return self._additions.value

    @property
    def assignee(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._assignee)
        return self._assignee.value

    @property
    def assignees(self) -> list[github.NamedUser.NamedUser]:
        self._completeIfNotSet(self._assignees)
        return self._assignees.value

    @property
    def base(self) -> github.PullRequestPart.PullRequestPart:
        self._completeIfNotSet(self._base)
        return self._base.value

    @property
    def body(self) -> str:
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def changed_files(self) -> int:
        self._completeIfNotSet(self._changed_files)
        return self._changed_files.value

    @property
    def closed_at(self) -> datetime | None:
        self._completeIfNotSet(self._closed_at)
        return self._closed_at.value

    @property
    def comments(self) -> int:
        self._completeIfNotSet(self._comments)
        return self._comments.value

    @property
    def comments_url(self) -> str:
        self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    def commits(self) -> int:
        self._completeIfNotSet(self._commits)
        return self._commits.value

    @property
    def commits_url(self) -> str:
        self._completeIfNotSet(self._commits_url)
        return self._commits_url.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def deletions(self) -> int:
        self._completeIfNotSet(self._deletions)
        return self._deletions.value

    @property
    def diff_url(self) -> str:
        self._completeIfNotSet(self._diff_url)
        return self._diff_url.value

    @property
    def draft(self) -> bool:
        self._completeIfNotSet(self._draft)
        return self._draft.value

    @property
    def head(self) -> github.PullRequestPart.PullRequestPart:
        self._completeIfNotSet(self._head)
        return self._head.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def issue_url(self) -> str:
        self._completeIfNotSet(self._issue_url)
        return self._issue_url.value

    @property
    def labels(self) -> list[github.Label.Label]:
        self._completeIfNotSet(self._labels)
        return self._labels.value

    @property
    def merge_commit_sha(self) -> str:
        self._completeIfNotSet(self._merge_commit_sha)
        return self._merge_commit_sha.value

    @property
    def mergeable(self) -> bool:
        self._completeIfNotSet(self._mergeable)
        return self._mergeable.value

    @property
    def mergeable_state(self) -> str:
        self._completeIfNotSet(self._mergeable_state)
        return self._mergeable_state.value

    @property
    def merged(self) -> bool:
        self._completeIfNotSet(self._merged)
        return self._merged.value

    @property
    def merged_at(self) -> datetime | None:
        self._completeIfNotSet(self._merged_at)
        return self._merged_at.value

    @property
    def merged_by(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._merged_by)
        return self._merged_by.value

    @property
    def milestone(self) -> github.Milestone.Milestone:
        self._completeIfNotSet(self._milestone)
        return self._milestone.value

    @property
    def number(self) -> int:
        self._completeIfNotSet(self._number)
        return self._number.value

    @property
    def patch_url(self) -> str:
        self._completeIfNotSet(self._patch_url)
        return self._patch_url.value

    @property
    def rebaseable(self) -> bool:
        self._completeIfNotSet(self._rebaseable)
        return self._rebaseable.value

    @property
    def review_comment_url(self) -> str:
        self._completeIfNotSet(self._review_comment_url)
        return self._review_comment_url.value

    @property
    def review_comments(self) -> int:
        self._completeIfNotSet(self._review_comments)
        return self._review_comments.value

    @property
    def review_comments_url(self) -> str:
        self._completeIfNotSet(self._review_comments_url)
        return self._review_comments_url.value

    @property
    def state(self) -> str:
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def title(self) -> str:
        self._completeIfNotSet(self._title)
        return self._title.value

    @property
    def updated_at(self) -> datetime | None:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def requested_reviewers(self) -> list[github.NamedUser.NamedUser]:
        self._completeIfNotSet(self._requested_reviewers)
        return self._requested_reviewers.value

    @property
    def requested_teams(self) -> list[github.Team.Team]:
        self._completeIfNotSet(self._requested_teams)
        return self._requested_teams.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def user(self) -> NamedUser:
        self._completeIfNotSet(self._user)
        return self._user.value

    @property
    def maintainer_can_modify(self) -> bool:
        self._completeIfNotSet(self._maintainer_can_modify)
        return self._maintainer_can_modify.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    def as_issue(self) -> Issue:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{number} <https://docs.github.com/en/rest/reference/issues>`_
        """
        headers, data = self._requester.requestJsonAndCheck("GET", self.issue_url)
        return github.Issue.Issue(self._requester, headers, data, completed=True)

    def create_comment(
        self, body: str, commit: github.Commit.Commit, path: str, position: int
    ) -> github.PullRequestComment.PullRequestComment:
        """
        :calls: `POST /repos/{owner}/{repo}/pulls/{number}/comments <https://docs.github.com/en/rest/reference/pulls#review-comments>`_
        """
        return self.create_review_comment(body, commit, path, position)

    def create_review_comment(
        self,
        body: str,
        commit: github.Commit.Commit,
        path: str,
        # line replaces deprecated position argument, so we put it between path and side
        line: Opt[int] = NotSet,
        side: Opt[str] = NotSet,
        start_line: Opt[int] = NotSet,
        start_side: Opt[int] = NotSet,
        in_reply_to: Opt[int] = NotSet,
        subject_type: Opt[str] = NotSet,
        as_suggestion: bool = False,
    ) -> github.PullRequestComment.PullRequestComment:
        """
        :calls: `POST /repos/{owner}/{repo}/pulls/{number}/comments <https://docs.github.com/en/rest/reference/pulls#review-comments>`_
        """
        assert isinstance(body, str), body
        assert isinstance(commit, github.Commit.Commit), commit
        assert isinstance(path, str), path
        assert is_optional(line, int), line
        assert is_undefined(side) or side in ["LEFT", "RIGHT"], side
        assert is_optional(start_line, int), start_line
        assert is_undefined(start_side) or start_side in [
            "LEFT",
            "RIGHT",
            "side",
        ], start_side
        assert is_optional(in_reply_to, int), in_reply_to
        assert is_undefined(subject_type) or subject_type in [
            "line",
            "file",
        ], subject_type
        assert isinstance(as_suggestion, bool), as_suggestion

        if as_suggestion:
            body = f"```suggestion\n{body}\n```"
        post_parameters = NotSet.remove_unset_items(
            {
                "body": body,
                "commit_id": commit._identity,
                "path": path,
                "line": line,
                "side": side,
                "start_line": start_line,
                "start_side": start_side,
                "in_reply_to": in_reply_to,
                "subject_type": subject_type,
            }
        )

        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/comments", input=post_parameters)
        return github.PullRequestComment.PullRequestComment(self._requester, headers, data, completed=True)

    def create_review_comment_reply(self, comment_id: int, body: str) -> github.PullRequestComment.PullRequestComment:
        """
        :calls: `POST /repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies <https://docs.github.com/en/rest/reference/pulls#review-comments>`_
        """
        assert isinstance(comment_id, int), comment_id
        assert isinstance(body, str), body
        post_parameters = {"body": body}
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"{self.url}/comments/{comment_id}/replies",
            input=post_parameters,
        )
        return github.PullRequestComment.PullRequestComment(self._requester, headers, data, completed=True)

    def create_issue_comment(self, body: str) -> github.IssueComment.IssueComment:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{number}/comments <https://docs.github.com/en/rest/reference/issues#comments>`_
        """
        assert isinstance(body, str), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.issue_url}/comments", input=post_parameters)
        return github.IssueComment.IssueComment(self._requester, headers, data, completed=True)

    def create_review(
        self,
        commit: Opt[github.Commit.Commit] = NotSet,
        body: Opt[str] = NotSet,
        event: Opt[str] = NotSet,
        comments: Opt[list[ReviewComment]] = NotSet,
    ) -> github.PullRequestReview.PullRequestReview:
        """
        :calls: `POST /repos/{owner}/{repo}/pulls/{number}/reviews <https://docs.github.com/en/free-pro-team@latest/rest/pulls/reviews?apiVersion=2022-11-28#create-a-review-for-a-pull-request>`_
        """
        assert is_optional(commit, github.Commit.Commit), commit
        assert is_optional(body, str), body
        assert is_optional(event, str), event
        assert is_optional_list(comments, dict), comments
        post_parameters: dict[str, Any] = NotSet.remove_unset_items({"body": body})
        post_parameters["event"] = "COMMENT" if is_undefined(event) else event
        if is_defined(commit):
            post_parameters["commit_id"] = commit.sha
        if is_defined(comments):
            post_parameters["comments"] = comments
        else:
            post_parameters["comments"] = []
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/reviews", input=post_parameters)
        return github.PullRequestReview.PullRequestReview(self._requester, headers, data, completed=True)

    def create_review_request(
        self,
        reviewers: Opt[list[str] | str] = NotSet,
        team_reviewers: Opt[list[str] | str] = NotSet,
    ) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/pulls/{number}/requested_reviewers <https://docs.github.com/en/rest/reference/pulls#review-requests>`_
        """
        assert is_optional(reviewers, str) or is_optional_list(reviewers, str), reviewers
        assert is_optional(team_reviewers, str) or is_optional_list(team_reviewers, str), team_reviewers

        post_parameters = NotSet.remove_unset_items({"reviewers": reviewers, "team_reviewers": team_reviewers})

        headers, data = self._requester.requestJsonAndCheck(
            "POST", f"{self.url}/requested_reviewers", input=post_parameters
        )

    def delete_review_request(
        self,
        reviewers: Opt[list[str] | str] = NotSet,
        team_reviewers: Opt[list[str] | str] = NotSet,
    ) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/pulls/{number}/requested_reviewers <https://docs.github.com/en/rest/reference/pulls#review-requests>`_
        """
        assert is_optional(reviewers, str) or is_optional_list(reviewers, str), reviewers
        assert is_optional(team_reviewers, str) or is_optional_list(team_reviewers, str), team_reviewers

        post_parameters = NotSet.remove_unset_items({"reviewers": reviewers, "team_reviewers": team_reviewers})

        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", f"{self.url}/requested_reviewers", input=post_parameters
        )

    def edit(
        self,
        title: Opt[str] = NotSet,
        body: Opt[str] = NotSet,
        state: Opt[str] = NotSet,
        base: Opt[str] = NotSet,
        maintainer_can_modify: Opt[bool] = NotSet,
    ) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/pulls/{number} <https://docs.github.com/en/rest/reference/pulls>`_
        """
        assert is_optional(title, str), title
        assert is_optional(body, str), body
        assert is_optional(state, str), state
        assert is_optional(base, str), base
        assert is_optional(maintainer_can_modify, bool), maintainer_can_modify
        post_parameters = NotSet.remove_unset_items(
            {"title": title, "body": body, "state": state, "base": base, "maintainer_can_modify": maintainer_can_modify}
        )

        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        self._useAttributes(data)

    def get_comment(self, id: int) -> github.PullRequestComment.PullRequestComment:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/comments/{number} <https://docs.github.com/en/rest/reference/pulls#review-comments>`_
        """
        return self.get_review_comment(id)

    def get_review_comment(self, id: int) -> github.PullRequestComment.PullRequestComment:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/comments/{number} <https://docs.github.com/en/rest/reference/pulls#review-comments>`_
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self._parentUrl(self.url)}/comments/{id}")
        return github.PullRequestComment.PullRequestComment(self._requester, headers, data, completed=True)

    def get_comments(
        self,
        sort: Opt[str] = NotSet,
        direction: Opt[str] = NotSet,
        since: Opt[datetime] = NotSet,
    ) -> PaginatedList[github.PullRequestComment.PullRequestComment]:
        """
        Warning: this only returns review comments. For normal conversation comments, use get_issue_comments.

        :calls: `GET /repos/{owner}/{repo}/pulls/{number}/comments <https://docs.github.com/en/rest/reference/pulls#review-comments>`_
        :param sort: string 'created' or 'updated'
        :param direction: string 'asc' or 'desc'
        :param since: datetime
        """
        return self.get_review_comments(sort=sort, direction=direction, since=since)

    # v3: remove *, added here to force named parameters because order has changed
    def get_review_comments(
        self,
        *,
        sort: Opt[str] = NotSet,
        direction: Opt[str] = NotSet,
        since: Opt[datetime] = NotSet,
    ) -> PaginatedList[github.PullRequestComment.PullRequestComment]:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{number}/comments <https://docs.github.com/en/rest/reference/pulls#review-comments>`_
        :param sort: string 'created' or 'updated'
        :param direction: string 'asc' or 'desc'
        :param since: datetime
        """
        assert is_optional(sort, str), sort
        assert is_optional(direction, str), direction
        assert is_optional(since, datetime), since

        url_parameters = NotSet.remove_unset_items({"sort": sort, "direction": direction})
        if is_defined(since):
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")

        return PaginatedList(
            github.PullRequestComment.PullRequestComment,
            self._requester,
            f"{self.url}/comments",
            url_parameters,
        )

    def get_single_review_comments(self, id: int) -> PaginatedList[github.PullRequestComment.PullRequestComment]:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{number}/review/{id}/comments <https://docs.github.com/en/rest/reference/pulls#reviews>`_
        """
        assert isinstance(id, int), id
        return PaginatedList(
            github.PullRequestComment.PullRequestComment,
            self._requester,
            f"{self.url}/reviews/{id}/comments",
            None,
        )

    def get_commits(self) -> PaginatedList[github.Commit.Commit]:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{number}/commits <https://docs.github.com/en/rest/reference/pulls>`_
        """
        return PaginatedList(github.Commit.Commit, self._requester, f"{self.url}/commits", None)

    def get_files(self) -> PaginatedList[github.File.File]:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{number}/files <https://docs.github.com/en/rest/reference/pulls>`_
        """
        return PaginatedList(github.File.File, self._requester, f"{self.url}/files", None)

    def get_issue_comment(self, id: int) -> github.IssueComment.IssueComment:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/comments/{id} <https://docs.github.com/en/rest/reference/issues#comments>`_
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self._parentUrl(self.issue_url)}/comments/{id}")
        return github.IssueComment.IssueComment(self._requester, headers, data, completed=True)

    def get_issue_comments(self) -> PaginatedList[github.IssueComment.IssueComment]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{number}/comments <https://docs.github.com/en/rest/reference/issues#comments>`_
        """
        return PaginatedList(
            github.IssueComment.IssueComment,
            self._requester,
            f"{self.issue_url}/comments",
            None,
        )

    def get_issue_events(self) -> PaginatedList[github.IssueEvent.IssueEvent]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{issue_number}/events <https://docs.github.com/en/rest/reference/issues#events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.IssueEvent.IssueEvent`
        """
        return PaginatedList(
            github.IssueEvent.IssueEvent,
            self._requester,
            f"{self.issue_url}/events",
            None,
            headers={"Accept": Consts.mediaTypeLockReasonPreview},
        )

    def get_review(self, id: int) -> github.PullRequestReview.PullRequestReview:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{number}/reviews/{id} <https://docs.github.com/en/rest/reference/pulls#reviews>`_
        :param id: integer
        :rtype: :class:`github.PullRequestReview.PullRequestReview`
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            f"{self.url}/reviews/{id}",
        )
        return github.PullRequestReview.PullRequestReview(self._requester, headers, data, completed=True)

    def get_reviews(self) -> PaginatedList[github.PullRequestReview.PullRequestReview]:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{number}/reviews <https://docs.github.com/en/rest/reference/pulls#reviews>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestReview.PullRequestReview`
        """
        return PaginatedList(
            github.PullRequestReview.PullRequestReview,
            self._requester,
            f"{self.url}/reviews",
            None,
        )

    def get_review_requests(self) -> tuple[PaginatedList[NamedUser], PaginatedList[github.Team.Team]]:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{number}/requested_reviewers <https://docs.github.com/en/rest/reference/pulls#review-requests>`_
        :rtype: tuple of :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser` and of :class:`github.PaginatedList.PaginatedList` of :class:`github.Team.Team`
        """
        return (
            PaginatedList(
                github.NamedUser.NamedUser,
                self._requester,
                f"{self.url}/requested_reviewers",
                None,
                list_item="users",
            ),
            PaginatedList(
                github.Team.Team,
                self._requester,
                f"{self.url}/requested_reviewers",
                None,
                list_item="teams",
            ),
        )

    def get_labels(self) -> PaginatedList[github.Label.Label]:
        """
        :calls: `GET /repos/{owner}/{repo}/issues/{number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        return PaginatedList(github.Label.Label, self._requester, f"{self.issue_url}/labels", None)

    def add_to_labels(self, *labels: github.Label.Label | str) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        assert all(isinstance(element, (github.Label.Label, str)) for element in labels), labels
        post_parameters = [label.name if isinstance(label, github.Label.Label) else label for label in labels]
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.issue_url}/labels", input=post_parameters)

    def delete_labels(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.issue_url}/labels")

    def remove_from_labels(self, label: github.Label.Label | str) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/issues/{number}/labels/{name} <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        assert isinstance(label, (github.Label.Label, str)), label
        if isinstance(label, github.Label.Label):
            label = label._identity
        else:
            label = urllib.parse.quote(label)
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.issue_url}/labels/{label}")

    def set_labels(self, *labels: github.Label.Label | str) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/issues/{number}/labels <https://docs.github.com/en/rest/reference/issues#labels>`_
        """
        assert all(isinstance(element, (github.Label.Label, str)) for element in labels), labels
        post_parameters = [label.name if isinstance(label, github.Label.Label) else label for label in labels]
        headers, data = self._requester.requestJsonAndCheck("PUT", f"{self.issue_url}/labels", input=post_parameters)

    def is_merged(self) -> bool:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{number}/merge <https://docs.github.com/en/rest/reference/pulls>`_
        """
        status, headers, data = self._requester.requestJson("GET", f"{self.url}/merge")
        return status == 204

    def restore_branch(self) -> GitRef:
        """
        Convenience function that calls :meth:`Repository.create_git_ref` :rtype: :class:`github.GitRef.GitRef`
        """
        return self.head.repo.create_git_ref(f"refs/heads/{self.head.ref}", sha=self.head.sha)

    def delete_branch(self, force: bool = False) -> None:
        """
        Convenience function that calls :meth:`GitRef.delete` :rtype: bool.
        """
        if not force:
            remaining_pulls = self.head.repo.get_pulls(head=self.head.ref)
            if remaining_pulls.totalCount > 0:
                raise RuntimeError(
                    "This branch is referenced by open pull requests, set force=True to delete this branch."
                )
        return self.head.repo.get_git_ref(f"heads/{self.head.ref}").delete()

    def enable_automerge(
        self,
        merge_method: Opt[str] = "MERGE",
        author_email: Opt[str] = NotSet,
        client_mutation_id: Opt[str] = NotSet,
        commit_body: Opt[str] = NotSet,
        commit_headline: Opt[str] = NotSet,
        expected_head_oid: Opt[str] = NotSet,
    ) -> dict[str, Any]:
        """
        :calls: `POST /graphql <https://docs.github.com/en/graphql>`_ with a mutation to enable pull request auto merge
        <https://docs.github.com/en/graphql/reference/mutations#enablepullrequestautomerge>
        """
        assert is_optional(author_email, str), author_email
        assert is_optional(client_mutation_id, str), client_mutation_id
        assert is_optional(commit_body, str), commit_body
        assert is_optional(commit_headline, str), commit_headline
        assert is_optional(expected_head_oid, str), expected_head_oid
        assert isinstance(merge_method, str) and merge_method in ["MERGE", "REBASE", "SQUASH"], merge_method

        # Define the variables
        variables = {
            "pullRequestId": self.node_id,
            "authorEmail": author_email,
            "clientMutationId": client_mutation_id,
            "commitBody": commit_body,
            "commitHeadline": commit_headline,
            "expectedHeadOid": expected_head_oid,
            "mergeMethod": merge_method,
        }

        # Make the request
        _, data = self._requester.graphql_named_mutation(
            mutation_name="enable_pull_request_auto_merge",
            variables={"input": NotSet.remove_unset_items(variables)},
            output="actor { avatarUrl login resourcePath url } clientMutationId",
        )
        return data

    def disable_automerge(
        self,
        client_mutation_id: Opt[str] = NotSet,
    ) -> dict[str, Any]:
        """
        :calls: `POST /graphql <https://docs.github.com/en/graphql>`_ with a mutation to disable pull request auto merge
        <https://docs.github.com/en/graphql/reference/mutations#disablepullrequestautomerge>
        """
        assert is_optional(client_mutation_id, str), client_mutation_id

        # Define the variables
        variables = {
            "pullRequestId": self.node_id,
            "clientMutationId": client_mutation_id,
        }

        # Make the request
        _, data = self._requester.graphql_named_mutation(
            mutation_name="disable_pull_request_auto_merge",
            variables={"input": NotSet.remove_unset_items(variables)},
            output="actor { avatarUrl login resourcePath url } clientMutationId",
        )
        return data

    def merge(
        self,
        commit_message: Opt[str] = NotSet,
        commit_title: Opt[str] = NotSet,
        merge_method: Opt[str] = NotSet,
        sha: Opt[str] = NotSet,
        delete_branch: bool = False,
    ) -> github.PullRequestMergeStatus.PullRequestMergeStatus:
        """
        :calls: `PUT /repos/{owner}/{repo}/pulls/{number}/merge <https://docs.github.com/en/rest/reference/pulls>`_
        """
        assert is_optional(commit_message, str), commit_message
        assert is_optional(commit_title, str), commit_title
        assert is_optional(merge_method, str), merge_method
        assert is_optional(sha, str), sha
        post_parameters = NotSet.remove_unset_items(
            {"commit_message": commit_message, "commit_title": commit_title, "merge_method": merge_method, "sha": sha}
        )
        headers, data = self._requester.requestJsonAndCheck("PUT", f"{self.url}/merge", input=post_parameters)
        if delete_branch:
            self.delete_branch()

        return github.PullRequestMergeStatus.PullRequestMergeStatus(self._requester, headers, data, completed=True)

    def add_to_assignees(self, *assignees: github.NamedUser.NamedUser | str) -> None:
        """
        :calls: `POST /repos/{owner}/{repo}/issues/{number}/assignees <https://docs.github.com/en/rest/issues/assignees?apiVersion=2022-11-28#add-assignees-to-an-issue>`_
        """
        assert all(isinstance(element, (github.NamedUser.NamedUser, str)) for element in assignees), assignees
        post_parameters = {
            "assignees": [
                assignee.login if isinstance(assignee, github.NamedUser.NamedUser) else assignee
                for assignee in assignees
            ]
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST", f"{self.issue_url}/assignees", input=post_parameters
        )
        # Only use the assignees attribute, since we call this PR as an issue
        self._useAttributes({"assignees": data["assignees"]})

    def remove_from_assignees(self, *assignees: github.NamedUser.NamedUser | str) -> None:
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
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", f"{self.issue_url}/assignees", input=post_parameters
        )
        # Only use the assignees attribute, since we call this PR as an issue
        self._useAttributes({"assignees": data["assignees"]})

    def update_branch(self, expected_head_sha: Opt[str] = NotSet) -> bool:
        """
        :calls `PUT /repos/{owner}/{repo}/pulls/{pull_number}/update-branch <https://docs.github.com/en/rest/reference/pulls>`_
        """
        assert is_optional(expected_head_sha, str), expected_head_sha
        post_parameters = NotSet.remove_unset_items({"expected_head_sha": expected_head_sha})
        status, headers, data = self._requester.requestJson(
            "PUT",
            f"{self.url}/update-branch",
            input=post_parameters,
            headers={"Accept": Consts.updateBranchPreview},
        )
        return status == 202

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "additions" in attributes:  # pragma no branch
            self._additions = self._makeIntAttribute(attributes["additions"])
        if "assignee" in attributes:  # pragma no branch
            self._assignee = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["assignee"])
        if "assignees" in attributes:  # pragma no branch
            self._assignees = self._makeListOfClassesAttribute(github.NamedUser.NamedUser, attributes["assignees"])
        elif "assignee" in attributes:
            if attributes["assignee"] is not None:
                self._assignees = self._makeListOfClassesAttribute(github.NamedUser.NamedUser, [attributes["assignee"]])
            else:
                self._assignees = self._makeListOfClassesAttribute(github.NamedUser.NamedUser, [])
        if "base" in attributes:  # pragma no branch
            self._base = self._makeClassAttribute(github.PullRequestPart.PullRequestPart, attributes["base"])
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "changed_files" in attributes:  # pragma no branch
            self._changed_files = self._makeIntAttribute(attributes["changed_files"])
        if "closed_at" in attributes:  # pragma no branch
            self._closed_at = self._makeDatetimeAttribute(attributes["closed_at"])
        if "comments" in attributes:  # pragma no branch
            self._comments = self._makeIntAttribute(attributes["comments"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "commits" in attributes:  # pragma no branch
            self._commits = self._makeIntAttribute(attributes["commits"])
        if "commits_url" in attributes:  # pragma no branch
            self._commits_url = self._makeStringAttribute(attributes["commits_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "deletions" in attributes:  # pragma no branch
            self._deletions = self._makeIntAttribute(attributes["deletions"])
        if "diff_url" in attributes:  # pragma no branch
            self._diff_url = self._makeStringAttribute(attributes["diff_url"])
        if "draft" in attributes:  # pragma no branch
            self._draft = self._makeBoolAttribute(attributes["draft"])
        if "head" in attributes:  # pragma no branch
            self._head = self._makeClassAttribute(github.PullRequestPart.PullRequestPart, attributes["head"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "issue_url" in attributes:  # pragma no branch
            self._issue_url = self._makeStringAttribute(attributes["issue_url"])
        if "labels" in attributes:  # pragma no branch
            self._labels = self._makeListOfClassesAttribute(github.Label.Label, attributes["labels"])
        if "maintainer_can_modify" in attributes:  # pragma no branch
            self._maintainer_can_modify = self._makeBoolAttribute(attributes["maintainer_can_modify"])
        if "merge_commit_sha" in attributes:  # pragma no branch
            self._merge_commit_sha = self._makeStringAttribute(attributes["merge_commit_sha"])
        if "mergeable" in attributes:  # pragma no branch
            self._mergeable = self._makeBoolAttribute(attributes["mergeable"])
        if "mergeable_state" in attributes:  # pragma no branch
            self._mergeable_state = self._makeStringAttribute(attributes["mergeable_state"])
        if "merged" in attributes:  # pragma no branch
            self._merged = self._makeBoolAttribute(attributes["merged"])
        if "merged_at" in attributes:  # pragma no branch
            self._merged_at = self._makeDatetimeAttribute(attributes["merged_at"])
        if "merged_by" in attributes:  # pragma no branch
            self._merged_by = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["merged_by"])
        if "milestone" in attributes:  # pragma no branch
            self._milestone = self._makeClassAttribute(github.Milestone.Milestone, attributes["milestone"])
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "patch_url" in attributes:  # pragma no branch
            self._patch_url = self._makeStringAttribute(attributes["patch_url"])
        if "rebaseable" in attributes:  # pragma no branch
            self._rebaseable = self._makeBoolAttribute(attributes["rebaseable"])
        if "review_comment_url" in attributes:  # pragma no branch
            self._review_comment_url = self._makeStringAttribute(attributes["review_comment_url"])
        if "review_comments" in attributes:  # pragma no branch
            self._review_comments = self._makeIntAttribute(attributes["review_comments"])
        if "review_comments_url" in attributes:  # pragma no branch
            self._review_comments_url = self._makeStringAttribute(attributes["review_comments_url"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "title" in attributes:  # pragma no branch
            self._title = self._makeStringAttribute(attributes["title"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["user"])
        if "requested_reviewers" in attributes:
            self._requested_reviewers = self._makeListOfClassesAttribute(
                github.NamedUser.NamedUser, attributes["requested_reviewers"]
            )
        if "requested_teams" in attributes:
            self._requested_teams = self._makeListOfClassesAttribute(github.Team.Team, attributes["requested_teams"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
