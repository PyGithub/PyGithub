# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import GithubObject
import PaginatedList

import PullRequestMergeStatus
import NamedUser
import PullRequestPart
import PullRequestComment
import File
import IssueComment
import Commit


class PullRequest(GithubObject.GithubObject):
    @property
    def additions(self):
        self._completeIfNotSet(self._additions)
        return self._NoneIfNotSet(self._additions)

    @property
    def assignee(self):
        self._completeIfNotSet(self._assignee)
        return self._NoneIfNotSet(self._assignee)

    @property
    def base(self):
        self._completeIfNotSet(self._base)
        return self._NoneIfNotSet(self._base)

    @property
    def body(self):
        self._completeIfNotSet(self._body)
        return self._NoneIfNotSet(self._body)

    @property
    def changed_files(self):
        self._completeIfNotSet(self._changed_files)
        return self._NoneIfNotSet(self._changed_files)

    @property
    def closed_at(self):
        self._completeIfNotSet(self._closed_at)
        return self._NoneIfNotSet(self._closed_at)

    @property
    def comments(self):
        self._completeIfNotSet(self._comments)
        return self._NoneIfNotSet(self._comments)

    @property
    def commits(self):
        self._completeIfNotSet(self._commits)
        return self._NoneIfNotSet(self._commits)

    @property
    def created_at(self):
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def deletions(self):
        self._completeIfNotSet(self._deletions)
        return self._NoneIfNotSet(self._deletions)

    @property
    def diff_url(self):
        self._completeIfNotSet(self._diff_url)
        return self._NoneIfNotSet(self._diff_url)

    @property
    def head(self):
        self._completeIfNotSet(self._head)
        return self._NoneIfNotSet(self._head)

    @property
    def html_url(self):
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def id(self):
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def issue_url(self):
        self._completeIfNotSet(self._issue_url)
        return self._NoneIfNotSet(self._issue_url)

    @property
    def mergeable(self):
        self._completeIfNotSet(self._mergeable)
        return self._NoneIfNotSet(self._mergeable)

    @property
    def merged(self):
        self._completeIfNotSet(self._merged)
        return self._NoneIfNotSet(self._merged)

    @property
    def merged_at(self):
        self._completeIfNotSet(self._merged_at)
        return self._NoneIfNotSet(self._merged_at)

    @property
    def merged_by(self):
        self._completeIfNotSet(self._merged_by)
        return self._NoneIfNotSet(self._merged_by)

    @property
    def number(self):
        self._completeIfNotSet(self._number)
        return self._NoneIfNotSet(self._number)

    @property
    def patch_url(self):
        self._completeIfNotSet(self._patch_url)
        return self._NoneIfNotSet(self._patch_url)

    @property
    def review_comments(self):
        self._completeIfNotSet(self._review_comments)
        return self._NoneIfNotSet(self._review_comments)

    @property
    def state(self):
        self._completeIfNotSet(self._state)
        return self._NoneIfNotSet(self._state)

    @property
    def title(self):
        self._completeIfNotSet(self._title)
        return self._NoneIfNotSet(self._title)

    @property
    def updated_at(self):
        self._completeIfNotSet(self._updated_at)
        return self._NoneIfNotSet(self._updated_at)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def user(self):
        self._completeIfNotSet(self._user)
        return self._NoneIfNotSet(self._user)

    def create_comment(self, body, commit_id, path, position):
        return self.create_review_comment(body, commit_id, path, position)

    def create_review_comment(self, body, commit_id, path, position):
        assert isinstance(body, (str, unicode)), body
        assert isinstance(commit_id, Commit.Commit), commit_id
        assert isinstance(path, (str, unicode)), path
        assert isinstance(position, (int, long)), position
        post_parameters = {
            "body": body,
            "commit_id": commit_id._identity,
            "path": path,
            "position": position,
        }
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/comments",
            None,
            post_parameters
        )
        return PullRequestComment.PullRequestComment(self._requester, data, completed=True)

    def create_issue_comment(self, body):
        assert isinstance(body, (str, unicode)), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestAndCheck(
            "POST",
            self._parentUrl(self._parentUrl(self.url)) + "/issues/" + str(self.number) + "/comments",
            None,
            post_parameters
        )
        return IssueComment.IssueComment(self._requester, data, completed=True)

    def edit(self, title=GithubObject.NotSet, body=GithubObject.NotSet, state=GithubObject.NotSet):
        assert title is GithubObject.NotSet or isinstance(title, (str, unicode)), title
        assert body is GithubObject.NotSet or isinstance(body, (str, unicode)), body
        assert state is GithubObject.NotSet or isinstance(state, (str, unicode)), state
        post_parameters = dict()
        if title is not GithubObject.NotSet:
            post_parameters["title"] = title
        if body is not GithubObject.NotSet:
            post_parameters["body"] = body
        if state is not GithubObject.NotSet:
            post_parameters["state"] = state
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def get_comment(self, id):
        return self.get_review_comment(id)

    def get_review_comment(self, id):
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestAndCheck(
            "GET",
            self._parentUrl(self.url) + "/comments/" + str(id),
            None,
            None
        )
        return PullRequestComment.PullRequestComment(self._requester, data, completed=True)

    def get_comments(self):
        return self.get_review_comments()

    def get_review_comments(self):
        return PaginatedList.PaginatedList(
            PullRequestComment.PullRequestComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_commits(self):
        return PaginatedList.PaginatedList(
            Commit.Commit,
            self._requester,
            self.url + "/commits",
            None
        )

    def get_files(self):
        return PaginatedList.PaginatedList(
            File.File,
            self._requester,
            self.url + "/files",
            None
        )

    def get_issue_comment(self, id):
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestAndCheck(
            "GET",
            self._parentUrl(self._parentUrl(self.url)) + "/issues/comments/" + str(id),
            None,
            None
        )
        return IssueComment.IssueComment(self._requester, data, completed=True)

    def get_issue_comments(self):
        return PaginatedList.PaginatedList(
            IssueComment.IssueComment,
            self._requester,
            self._parentUrl(self._parentUrl(self.url)) + "/issues/" + str(self.number) + "/comments",
            None
        )

    def is_merged(self):
        status, headers, data = self._requester.requestRaw(
            "GET",
            self.url + "/merge",
            None,
            None
        )
        return status == 204

    def merge(self, commit_message=GithubObject.NotSet):
        assert commit_message is GithubObject.NotSet or isinstance(commit_message, (str, unicode)), commit_message
        post_parameters = dict()
        if commit_message is not GithubObject.NotSet:
            post_parameters["commit_message"] = commit_message
        headers, data = self._requester.requestAndCheck(
            "PUT",
            self.url + "/merge",
            None,
            post_parameters
        )
        return PullRequestMergeStatus.PullRequestMergeStatus(self._requester, data, completed=True)

    def _initAttributes(self):
        self._additions = GithubObject.NotSet
        self._assignee = GithubObject.NotSet
        self._base = GithubObject.NotSet
        self._body = GithubObject.NotSet
        self._changed_files = GithubObject.NotSet
        self._closed_at = GithubObject.NotSet
        self._comments = GithubObject.NotSet
        self._commits = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._deletions = GithubObject.NotSet
        self._diff_url = GithubObject.NotSet
        self._head = GithubObject.NotSet
        self._html_url = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._issue_url = GithubObject.NotSet
        self._mergeable = GithubObject.NotSet
        self._merged = GithubObject.NotSet
        self._merged_at = GithubObject.NotSet
        self._merged_by = GithubObject.NotSet
        self._number = GithubObject.NotSet
        self._patch_url = GithubObject.NotSet
        self._review_comments = GithubObject.NotSet
        self._state = GithubObject.NotSet
        self._title = GithubObject.NotSet
        self._updated_at = GithubObject.NotSet
        self._url = GithubObject.NotSet
        self._user = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "additions" in attributes:  # pragma no branch
            assert attributes["additions"] is None or isinstance(attributes["additions"], (int, long)), attributes["additions"]
            self._additions = attributes["additions"]
        if "assignee" in attributes:  # pragma no branch
            assert attributes["assignee"] is None or isinstance(attributes["assignee"], dict), attributes["assignee"]
            self._assignee = None if attributes["assignee"] is None else NamedUser.NamedUser(self._requester, attributes["assignee"], completed=False)
        if "base" in attributes:  # pragma no branch
            assert attributes["base"] is None or isinstance(attributes["base"], dict), attributes["base"]
            self._base = None if attributes["base"] is None else PullRequestPart.PullRequestPart(self._requester, attributes["base"], completed=False)
        if "body" in attributes:  # pragma no branch
            assert attributes["body"] is None or isinstance(attributes["body"], (str, unicode)), attributes["body"]
            self._body = attributes["body"]
        if "changed_files" in attributes:  # pragma no branch
            assert attributes["changed_files"] is None or isinstance(attributes["changed_files"], (int, long)), attributes["changed_files"]
            self._changed_files = attributes["changed_files"]
        if "closed_at" in attributes:  # pragma no branch
            assert attributes["closed_at"] is None or isinstance(attributes["closed_at"], (str, unicode)), attributes["closed_at"]
            self._closed_at = self._parseDatetime(attributes["closed_at"])
        if "comments" in attributes:  # pragma no branch
            assert attributes["comments"] is None or isinstance(attributes["comments"], (int, long)), attributes["comments"]
            self._comments = attributes["comments"]
        if "commits" in attributes:  # pragma no branch
            assert attributes["commits"] is None or isinstance(attributes["commits"], (int, long)), attributes["commits"]
            self._commits = attributes["commits"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "deletions" in attributes:  # pragma no branch
            assert attributes["deletions"] is None or isinstance(attributes["deletions"], (int, long)), attributes["deletions"]
            self._deletions = attributes["deletions"]
        if "diff_url" in attributes:  # pragma no branch
            assert attributes["diff_url"] is None or isinstance(attributes["diff_url"], (str, unicode)), attributes["diff_url"]
            self._diff_url = attributes["diff_url"]
        if "head" in attributes:  # pragma no branch
            assert attributes["head"] is None or isinstance(attributes["head"], dict), attributes["head"]
            self._head = None if attributes["head"] is None else PullRequestPart.PullRequestPart(self._requester, attributes["head"], completed=False)
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "issue_url" in attributes:  # pragma no branch
            assert attributes["issue_url"] is None or isinstance(attributes["issue_url"], (str, unicode)), attributes["issue_url"]
            self._issue_url = attributes["issue_url"]
        if "mergeable" in attributes:  # pragma no branch
            assert attributes["mergeable"] is None or isinstance(attributes["mergeable"], bool), attributes["mergeable"]
            self._mergeable = attributes["mergeable"]
        if "merged" in attributes:  # pragma no branch
            assert attributes["merged"] is None or isinstance(attributes["merged"], bool), attributes["merged"]
            self._merged = attributes["merged"]
        if "merged_at" in attributes:  # pragma no branch
            assert attributes["merged_at"] is None or isinstance(attributes["merged_at"], (str, unicode)), attributes["merged_at"]
            self._merged_at = self._parseDatetime(attributes["merged_at"])
        if "merged_by" in attributes:  # pragma no branch
            assert attributes["merged_by"] is None or isinstance(attributes["merged_by"], dict), attributes["merged_by"]
            self._merged_by = None if attributes["merged_by"] is None else NamedUser.NamedUser(self._requester, attributes["merged_by"], completed=False)
        if "number" in attributes:  # pragma no branch
            assert attributes["number"] is None or isinstance(attributes["number"], (int, long)), attributes["number"]
            self._number = attributes["number"]
        if "patch_url" in attributes:  # pragma no branch
            assert attributes["patch_url"] is None or isinstance(attributes["patch_url"], (str, unicode)), attributes["patch_url"]
            self._patch_url = attributes["patch_url"]
        if "review_comments" in attributes:  # pragma no branch
            assert attributes["review_comments"] is None or isinstance(attributes["review_comments"], (int, long)), attributes["review_comments"]
            self._review_comments = attributes["review_comments"]
        if "state" in attributes:  # pragma no branch
            assert attributes["state"] is None or isinstance(attributes["state"], (str, unicode)), attributes["state"]
            self._state = attributes["state"]
        if "title" in attributes:  # pragma no branch
            assert attributes["title"] is None or isinstance(attributes["title"], (str, unicode)), attributes["title"]
            self._title = attributes["title"]
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
        if "user" in attributes:  # pragma no branch
            assert attributes["user"] is None or isinstance(attributes["user"], dict), attributes["user"]
            self._user = None if attributes["user"] is None else NamedUser.NamedUser(self._requester, attributes["user"], completed=False)
