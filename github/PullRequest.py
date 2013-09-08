# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Michael Stead <michael.stead@gmail.com>                       #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
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

import github.GithubObject
import github.PaginatedList

import github.PullRequestMergeStatus
import github.NamedUser
import github.PullRequestPart
import github.PullRequestComment
import github.File
import github.IssueComment
import github.Commit


class PullRequest(github.GithubObject.CompletableGithubObject):
    """
    This class represents PullRequests. The reference can be found here http://developer.github.com/v3/pulls/
    """

    @property
    def additions(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._additions)
        return self._NoneIfNotSet(self._additions)

    @property
    def assignee(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._assignee)
        return self._NoneIfNotSet(self._assignee)

    @property
    def base(self):
        """
        :type: :class:`github.PullRequestPart.PullRequestPart`
        """
        self._completeIfNotSet(self._base)
        return self._NoneIfNotSet(self._base)

    @property
    def body(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._body)
        return self._NoneIfNotSet(self._body)

    @property
    def changed_files(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._changed_files)
        return self._NoneIfNotSet(self._changed_files)

    @property
    def closed_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._closed_at)
        return self._NoneIfNotSet(self._closed_at)

    @property
    def comments(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._comments)
        return self._NoneIfNotSet(self._comments)

    @property
    def comments_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._comments_url)
        return self._NoneIfNotSet(self._comments_url)

    @property
    def commits(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._commits)
        return self._NoneIfNotSet(self._commits)

    @property
    def commits_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._commits_url)
        return self._NoneIfNotSet(self._commits_url)

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def deletions(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._deletions)
        return self._NoneIfNotSet(self._deletions)

    @property
    def diff_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._diff_url)
        return self._NoneIfNotSet(self._diff_url)

    @property
    def head(self):
        """
        :type: :class:`github.PullRequestPart.PullRequestPart`
        """
        self._completeIfNotSet(self._head)
        return self._NoneIfNotSet(self._head)

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def issue_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._issue_url)
        return self._NoneIfNotSet(self._issue_url)

    @property
    def merge_commit_sha(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._merge_commit_sha)
        return self._NoneIfNotSet(self._merge_commit_sha)

    @property
    def mergeable(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._mergeable)
        return self._NoneIfNotSet(self._mergeable)

    @property
    def mergeable_state(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._mergeable_state)
        return self._NoneIfNotSet(self._mergeable_state)

    @property
    def merged(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._merged)
        return self._NoneIfNotSet(self._merged)

    @property
    def merged_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._merged_at)
        return self._NoneIfNotSet(self._merged_at)

    @property
    def merged_by(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._merged_by)
        return self._NoneIfNotSet(self._merged_by)

    @property
    def milestone(self):
        """
        :type: :class:`github.Milestone.Milestone`
        """
        self._completeIfNotSet(self._milestone)
        return self._NoneIfNotSet(self._milestone)

    @property
    def number(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._number)
        return self._NoneIfNotSet(self._number)

    @property
    def patch_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._patch_url)
        return self._NoneIfNotSet(self._patch_url)

    @property
    def review_comment_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._review_comment_url)
        return self._NoneIfNotSet(self._review_comment_url)

    @property
    def review_comments(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._review_comments)
        return self._NoneIfNotSet(self._review_comments)

    @property
    def review_comments_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._review_comments_url)
        return self._NoneIfNotSet(self._review_comments_url)

    @property
    def state(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._state)
        return self._NoneIfNotSet(self._state)

    @property
    def title(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._title)
        return self._NoneIfNotSet(self._title)

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._NoneIfNotSet(self._updated_at)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def user(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._user)
        return self._NoneIfNotSet(self._user)

    def create_comment(self, body, commit_id, path, position):
        """
        :calls: `POST /repos/:owner/:repo/pulls/:number/comments <http://developer.github.com/v3/pulls/comments>`_
        :param body: string
        :param commit_id: :class:`github.Commit.Commit`
        :param path: string
        :param position: integer
        :rtype: :class:`github.PullRequestComment.PullRequestComment`
        """
        return self.create_review_comment(body, commit_id, path, position)

    def create_review_comment(self, body, commit_id, path, position):
        """
        :calls: `POST /repos/:owner/:repo/pulls/:number/comments <http://developer.github.com/v3/pulls/comments>`_
        :param body: string
        :param commit_id: :class:`github.Commit.Commit`
        :param path: string
        :param position: integer
        :rtype: :class:`github.PullRequestComment.PullRequestComment`
        """
        assert isinstance(body, (str, unicode)), body
        assert isinstance(commit_id, github.Commit.Commit), commit_id
        assert isinstance(path, (str, unicode)), path
        assert isinstance(position, (int, long)), position
        post_parameters = {
            "body": body,
            "commit_id": commit_id._identity,
            "path": path,
            "position": position,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/comments",
            input=post_parameters
        )
        return github.PullRequestComment.PullRequestComment(self._requester, headers, data, completed=True)

    def create_issue_comment(self, body):
        """
        :calls: `POST /repos/:owner/:repo/issues/:number/comments <http://developer.github.com/v3/issues/comments>`_
        :param body: string
        :rtype: :class:`github.IssueComment.IssueComment`
        """
        assert isinstance(body, (str, unicode)), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self._parentUrl(self._parentUrl(self.url)) + "/issues/" + str(self.number) + "/comments",
            input=post_parameters
        )
        return github.IssueComment.IssueComment(self._requester, headers, data, completed=True)

    def edit(self, title=github.GithubObject.NotSet, body=github.GithubObject.NotSet, state=github.GithubObject.NotSet):
        """
        :calls: `PATCH /repos/:owner/:repo/pulls/:number <http://developer.github.com/v3/pulls>`_
        :param title: string
        :param body: string
        :param state: string
        :rtype: None
        """
        assert title is github.GithubObject.NotSet or isinstance(title, (str, unicode)), title
        assert body is github.GithubObject.NotSet or isinstance(body, (str, unicode)), body
        assert state is github.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        post_parameters = dict()
        if title is not github.GithubObject.NotSet:
            post_parameters["title"] = title
        if body is not github.GithubObject.NotSet:
            post_parameters["body"] = body
        if state is not github.GithubObject.NotSet:
            post_parameters["state"] = state
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        self._useAttributes(data)

    def get_comment(self, id):
        """
        :calls: `GET /repos/:owner/:repo/pulls/comments/:number <http://developer.github.com/v3/pulls/comments>`_
        :param id: integer
        :rtype: :class:`github.PullRequestComment.PullRequestComment`
        """
        return self.get_review_comment(id)

    def get_review_comment(self, id):
        """
        :calls: `GET /repos/:owner/:repo/pulls/comments/:number <http://developer.github.com/v3/pulls/comments>`_
        :param id: integer
        :rtype: :class:`github.PullRequestComment.PullRequestComment`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self._parentUrl(self.url) + "/comments/" + str(id)
        )
        return github.PullRequestComment.PullRequestComment(self._requester, headers, data, completed=True)

    def get_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/comments <http://developer.github.com/v3/pulls/comments>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestComment.PullRequestComment`
        """
        return self.get_review_comments()

    def get_review_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/comments <http://developer.github.com/v3/pulls/comments>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestComment.PullRequestComment`
        """
        return github.PaginatedList.PaginatedList(
            github.PullRequestComment.PullRequestComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_commits(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/commits <http://developer.github.com/v3/pulls>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Commit.Commit`
        """
        return github.PaginatedList.PaginatedList(
            github.Commit.Commit,
            self._requester,
            self.url + "/commits",
            None
        )

    def get_files(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/files <http://developer.github.com/v3/pulls>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.File.File`
        """
        return github.PaginatedList.PaginatedList(
            github.File.File,
            self._requester,
            self.url + "/files",
            None
        )

    def get_issue_comment(self, id):
        """
        :calls: `GET /repos/:owner/:repo/issues/comments/:id <http://developer.github.com/v3/issues/comments>`_
        :param id: integer
        :rtype: :class:`github.IssueComment.IssueComment`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self._parentUrl(self._parentUrl(self.url)) + "/issues/comments/" + str(id)
        )
        return github.IssueComment.IssueComment(self._requester, headers, data, completed=True)

    def get_issue_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/issues/:number/comments <http://developer.github.com/v3/issues/comments>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.IssueComment.IssueComment`
        """
        return github.PaginatedList.PaginatedList(
            github.IssueComment.IssueComment,
            self._requester,
            self._parentUrl(self._parentUrl(self.url)) + "/issues/" + str(self.number) + "/comments",
            None
        )

    def is_merged(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/merge <http://developer.github.com/v3/pulls>`_
        :rtype: bool
        """
        status, headers, data = self._requester.requestJson(
            "GET",
            self.url + "/merge"
        )
        return status == 204

    def merge(self, commit_message=github.GithubObject.NotSet):
        """
        :calls: `PUT /repos/:owner/:repo/pulls/:number/merge <http://developer.github.com/v3/pulls>`_
        :param commit_message: string
        :rtype: :class:`github.PullRequestMergeStatus.PullRequestMergeStatus`
        """
        assert commit_message is github.GithubObject.NotSet or isinstance(commit_message, (str, unicode)), commit_message
        post_parameters = dict()
        if commit_message is not github.GithubObject.NotSet:
            post_parameters["commit_message"] = commit_message
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/merge",
            input=post_parameters
        )
        return github.PullRequestMergeStatus.PullRequestMergeStatus(self._requester, headers, data, completed=True)

    def _initAttributes(self):
        self._additions = github.GithubObject.NotSet
        self._assignee = github.GithubObject.NotSet
        self._base = github.GithubObject.NotSet
        self._body = github.GithubObject.NotSet
        self._changed_files = github.GithubObject.NotSet
        self._closed_at = github.GithubObject.NotSet
        self._comments = github.GithubObject.NotSet
        self._comments_url = github.GithubObject.NotSet
        self._commits = github.GithubObject.NotSet
        self._commits_url = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._deletions = github.GithubObject.NotSet
        self._diff_url = github.GithubObject.NotSet
        self._head = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._issue_url = github.GithubObject.NotSet
        self._merge_commit_sha = github.GithubObject.NotSet
        self._mergeable = github.GithubObject.NotSet
        self._mergeable_state = github.GithubObject.NotSet
        self._merged = github.GithubObject.NotSet
        self._merged_at = github.GithubObject.NotSet
        self._merged_by = github.GithubObject.NotSet
        self._milestone = github.GithubObject.NotSet
        self._number = github.GithubObject.NotSet
        self._patch_url = github.GithubObject.NotSet
        self._review_comment_url = github.GithubObject.NotSet
        self._review_comments = github.GithubObject.NotSet
        self._review_comments_url = github.GithubObject.NotSet
        self._state = github.GithubObject.NotSet
        self._title = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._user = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "additions" in attributes:  # pragma no branch
            assert attributes["additions"] is None or isinstance(attributes["additions"], (int, long)), attributes["additions"]
            self._additions = attributes["additions"]
        if "assignee" in attributes:  # pragma no branch
            assert attributes["assignee"] is None or isinstance(attributes["assignee"], dict), attributes["assignee"]
            self._assignee = None if attributes["assignee"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["assignee"], completed=False)
        if "base" in attributes:  # pragma no branch
            assert attributes["base"] is None or isinstance(attributes["base"], dict), attributes["base"]
            self._base = None if attributes["base"] is None else github.PullRequestPart.PullRequestPart(self._requester, self._headers, attributes["base"], completed=False)
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
        if "comments_url" in attributes:  # pragma no branch
            assert attributes["comments_url"] is None or isinstance(attributes["comments_url"], (str, unicode)), attributes["comments_url"]
            self._comments_url = attributes["comments_url"]
        if "commits" in attributes:  # pragma no branch
            assert attributes["commits"] is None or isinstance(attributes["commits"], (int, long)), attributes["commits"]
            self._commits = attributes["commits"]
        if "commits_url" in attributes:  # pragma no branch
            assert attributes["commits_url"] is None or isinstance(attributes["commits_url"], (str, unicode)), attributes["commits_url"]
            self._commits_url = attributes["commits_url"]
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
            self._head = None if attributes["head"] is None else github.PullRequestPart.PullRequestPart(self._requester, self._headers, attributes["head"], completed=False)
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "issue_url" in attributes:  # pragma no branch
            assert attributes["issue_url"] is None or isinstance(attributes["issue_url"], (str, unicode)), attributes["issue_url"]
            self._issue_url = attributes["issue_url"]
        if "merge_commit_sha" in attributes:  # pragma no branch
            assert attributes["merge_commit_sha"] is None or isinstance(attributes["merge_commit_sha"], (str, unicode)), attributes["merge_commit_sha"]
            self._merge_commit_sha = attributes["merge_commit_sha"]
        if "mergeable" in attributes:  # pragma no branch
            assert attributes["mergeable"] is None or isinstance(attributes["mergeable"], bool), attributes["mergeable"]
            self._mergeable = attributes["mergeable"]
        if "mergeable_state" in attributes:  # pragma no branch
            assert attributes["mergeable_state"] is None or isinstance(attributes["mergeable_state"], (str, unicode)), attributes["mergeable_state"]
            self._mergeable_state = attributes["mergeable_state"]
        if "merged" in attributes:  # pragma no branch
            assert attributes["merged"] is None or isinstance(attributes["merged"], bool), attributes["merged"]
            self._merged = attributes["merged"]
        if "merged_at" in attributes:  # pragma no branch
            assert attributes["merged_at"] is None or isinstance(attributes["merged_at"], (str, unicode)), attributes["merged_at"]
            self._merged_at = self._parseDatetime(attributes["merged_at"])
        if "merged_by" in attributes:  # pragma no branch
            assert attributes["merged_by"] is None or isinstance(attributes["merged_by"], dict), attributes["merged_by"]
            self._merged_by = None if attributes["merged_by"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["merged_by"], completed=False)
        if "milestone" in attributes:  # pragma no branch
            assert attributes["milestone"] is None or isinstance(attributes["milestone"], dict), attributes["milestone"]
            self._milestone = None if attributes["milestone"] is None else github.Milestone.Milestone(self._requester, self._headers, attributes["milestone"], completed=False)
        if "number" in attributes:  # pragma no branch
            assert attributes["number"] is None or isinstance(attributes["number"], (int, long)), attributes["number"]
            self._number = attributes["number"]
        if "patch_url" in attributes:  # pragma no branch
            assert attributes["patch_url"] is None or isinstance(attributes["patch_url"], (str, unicode)), attributes["patch_url"]
            self._patch_url = attributes["patch_url"]
        if "review_comment_url" in attributes:  # pragma no branch
            assert attributes["review_comment_url"] is None or isinstance(attributes["review_comment_url"], (str, unicode)), attributes["review_comment_url"]
            self._review_comment_url = attributes["review_comment_url"]
        if "review_comments" in attributes:  # pragma no branch
            assert attributes["review_comments"] is None or isinstance(attributes["review_comments"], (int, long)), attributes["review_comments"]
            self._review_comments = attributes["review_comments"]
        if "review_comments_url" in attributes:  # pragma no branch
            assert attributes["review_comments_url"] is None or isinstance(attributes["review_comments_url"], (str, unicode)), attributes["review_comments_url"]
            self._review_comments_url = attributes["review_comments_url"]
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
            self._user = None if attributes["user"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["user"], completed=False)
