# -*- coding: utf-8 -*-

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
# Copyright 2018 Gilad Shefer <gshefer@redhat.com>                             #
# Copyright 2018 Martin Monperrus <monperrus@users.noreply.github.com>         #
# Copyright 2018 Matt Babineau <9685860+babineaum@users.noreply.github.com>    #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Thibault Jamet <tjamet@users.noreply.github.com>              #
# Copyright 2018 per1234 <accounts@perglass.com>                               #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

import datetime
import urllib.parse

import github.Commit
import github.File
import github.GithubObject
import github.IssueComment
import github.NamedUser
import github.PaginatedList
import github.PullRequestComment
import github.PullRequestMergeStatus
import github.PullRequestPart
import github.PullRequestReview

from . import Consts


class PullRequest(github.GithubObject.CompletableGithubObject):
    """
    This class represents PullRequests. The reference can be found here http://developer.github.com/v3/pulls/
    """

    def __repr__(self):
        return self.get__repr__(
            {"number": self._number.value, "title": self._title.value}
        )

    @property
    def additions(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._additions)
        return self._additions.value

    @property
    def assignee(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._assignee)
        return self._assignee.value

    @property
    def assignees(self):
        """
        :type: list of :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._assignees)
        return self._assignees.value

    @property
    def base(self):
        """
        :type: :class:`github.PullRequestPart.PullRequestPart`
        """
        self._completeIfNotSet(self._base)
        return self._base.value

    @property
    def body(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def changed_files(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._changed_files)
        return self._changed_files.value

    @property
    def closed_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._closed_at)
        return self._closed_at.value

    @property
    def comments(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._comments)
        return self._comments.value

    @property
    def comments_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    def commits(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._commits)
        return self._commits.value

    @property
    def commits_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._commits_url)
        return self._commits_url.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def deletions(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._deletions)
        return self._deletions.value

    @property
    def diff_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._diff_url)
        return self._diff_url.value

    @property
    def draft(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._draft)
        return self._draft.value

    @property
    def head(self):
        """
        :type: :class:`github.PullRequestPart.PullRequestPart`
        """
        self._completeIfNotSet(self._head)
        return self._head.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def issue_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._issue_url)
        return self._issue_url.value

    @property
    def labels(self):
        """
        :type: list of :class:`github.Label.Label`
        """
        self._completeIfNotSet(self._labels)
        return self._labels.value

    @property
    def merge_commit_sha(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._merge_commit_sha)
        return self._merge_commit_sha.value

    @property
    def mergeable(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._mergeable)
        return self._mergeable.value

    @property
    def mergeable_state(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._mergeable_state)
        return self._mergeable_state.value

    @property
    def merged(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._merged)
        return self._merged.value

    @property
    def merged_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._merged_at)
        return self._merged_at.value

    @property
    def merged_by(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._merged_by)
        return self._merged_by.value

    @property
    def milestone(self):
        """
        :type: :class:`github.Milestone.Milestone`
        """
        self._completeIfNotSet(self._milestone)
        return self._milestone.value

    @property
    def number(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._number)
        return self._number.value

    @property
    def patch_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._patch_url)
        return self._patch_url.value

    @property
    def review_comment_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._review_comment_url)
        return self._review_comment_url.value

    @property
    def review_comments(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._review_comments)
        return self._review_comments.value

    @property
    def review_comments_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._review_comments_url)
        return self._review_comments_url.value

    @property
    def state(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def title(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._title)
        return self._title.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def user(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._user)
        return self._user.value

    def as_issue(self):
        """
        :calls: `GET /repos/:owner/:repo/issues/:number <http://developer.github.com/v3/issues>`_
        :rtype: :class:`github.Issue.Issue`
        """
        headers, data = self._requester.requestJsonAndCheck("GET", self.issue_url)
        return github.Issue.Issue(self._requester, headers, data, completed=True)

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
        assert isinstance(body, str), body
        assert isinstance(commit_id, github.Commit.Commit), commit_id
        assert isinstance(path, str), path
        assert isinstance(position, int), position
        post_parameters = {
            "body": body,
            "commit_id": commit_id._identity,
            "path": path,
            "position": position,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST", self.url + "/comments", input=post_parameters
        )
        return github.PullRequestComment.PullRequestComment(
            self._requester, headers, data, completed=True
        )

    def create_review_comment_reply(self, comment_id, body):
        """
        :calls: `POST /repos/:owner/:repo/pulls/:pull_number/comments/:comment_id/replies <http://developer.github.com/v3/pulls/comments>`_
        :param comment_id: int
        :param body: string
        :rtype: :class:`github.PullRequestComment.PullRequestComment`
        """
        assert isinstance(comment_id, int), comment_id
        assert isinstance(body, str), body
        post_parameters = {"body": body}
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/comments/" + str(comment_id) + "/replies",
            input=post_parameters,
        )
        return github.PullRequestComment.PullRequestComment(
            self._requester, headers, data, completed=True
        )

    def create_issue_comment(self, body):
        """
        :calls: `POST /repos/:owner/:repo/issues/:number/comments <http://developer.github.com/v3/issues/comments>`_
        :param body: string
        :rtype: :class:`github.IssueComment.IssueComment`
        """
        assert isinstance(body, str), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST", self.issue_url + "/comments", input=post_parameters
        )
        return github.IssueComment.IssueComment(
            self._requester, headers, data, completed=True
        )

    def create_review(
        self,
        commit=github.GithubObject.NotSet,
        body=github.GithubObject.NotSet,
        event=github.GithubObject.NotSet,
        comments=github.GithubObject.NotSet,
    ):
        """
        :calls: `POST /repos/:owner/:repo/pulls/:number/reviews <https://developer.github.com/v3/pulls/reviews/>`_
        :param commit: github.Commit.Commit
        :param body: string
        :param event: string
        :param comments: list
        :rtype: :class:`github.PullRequestReview.PullRequestReview`
        """
        assert commit is github.GithubObject.NotSet or isinstance(
            commit, github.Commit.Commit
        ), commit
        assert body is github.GithubObject.NotSet or isinstance(body, str), body
        assert event is github.GithubObject.NotSet or isinstance(event, str), event
        assert comments is github.GithubObject.NotSet or isinstance(
            comments, list
        ), comments
        post_parameters = dict()
        if commit is not github.GithubObject.NotSet:
            post_parameters["commit_id"] = commit.sha
        if body is not github.GithubObject.NotSet:
            post_parameters["body"] = body
        post_parameters["event"] = (
            "COMMENT" if event == github.GithubObject.NotSet else event
        )
        if comments is github.GithubObject.NotSet:
            post_parameters["comments"] = []
        else:
            post_parameters["comments"] = comments
        headers, data = self._requester.requestJsonAndCheck(
            "POST", self.url + "/reviews", input=post_parameters
        )
        return github.PullRequestReview.PullRequestReview(
            self._requester, headers, data, completed=True
        )

    def create_review_request(
        self,
        reviewers=github.GithubObject.NotSet,
        team_reviewers=github.GithubObject.NotSet,
    ):
        """
        :calls: `POST /repos/:owner/:repo/pulls/:number/requested_reviewers <https://developer.github.com/v3/pulls/review_requests/>`_
        :param reviewers: list of strings
        :param team_reviewers: list of strings
        :rtype: None
        """
        post_parameters = dict()
        if reviewers is not github.GithubObject.NotSet:
            assert all(isinstance(element, str) for element in reviewers), reviewers
            post_parameters["reviewers"] = reviewers
        if team_reviewers is not github.GithubObject.NotSet:
            assert all(
                isinstance(element, str) for element in team_reviewers
            ), team_reviewers
            post_parameters["team_reviewers"] = team_reviewers
        headers, data = self._requester.requestJsonAndCheck(
            "POST", self.url + "/requested_reviewers", input=post_parameters
        )

    def delete_review_request(
        self,
        reviewers=github.GithubObject.NotSet,
        team_reviewers=github.GithubObject.NotSet,
    ):
        """
        :calls: `DELETE /repos/:owner/:repo/pulls/:number/requested_reviewers <https://developer.github.com/v3/pulls/review_requests/>`_
        :param reviewers: list of strings
        :param team_reviewers: list of strings
        :rtype: None
        """
        post_parameters = dict()
        if reviewers is not github.GithubObject.NotSet:
            assert all(isinstance(element, str) for element in reviewers), reviewers
            post_parameters["reviewers"] = reviewers
        if team_reviewers is not github.GithubObject.NotSet:
            assert all(
                isinstance(element, str) for element in team_reviewers
            ), team_reviewers
            post_parameters["team_reviewers"] = team_reviewers
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", self.url + "/requested_reviewers", input=post_parameters
        )

    def edit(
        self,
        title=github.GithubObject.NotSet,
        body=github.GithubObject.NotSet,
        state=github.GithubObject.NotSet,
        base=github.GithubObject.NotSet,
    ):
        """
        :calls: `PATCH /repos/:owner/:repo/pulls/:number <http://developer.github.com/v3/pulls>`_
        :param title: string
        :param body: string
        :param state: string
        :param base: string
        :rtype: None
        """
        assert title is github.GithubObject.NotSet or isinstance(title, str), title
        assert body is github.GithubObject.NotSet or isinstance(body, str), body
        assert state is github.GithubObject.NotSet or isinstance(state, str), state
        assert base is github.GithubObject.NotSet or isinstance(base, str), base
        post_parameters = dict()
        if title is not github.GithubObject.NotSet:
            post_parameters["title"] = title
        if body is not github.GithubObject.NotSet:
            post_parameters["body"] = body
        if state is not github.GithubObject.NotSet:
            post_parameters["state"] = state
        if base is not github.GithubObject.NotSet:
            post_parameters["base"] = base
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH", self.url, input=post_parameters
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
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET", self._parentUrl(self.url) + "/comments/" + str(id)
        )
        return github.PullRequestComment.PullRequestComment(
            self._requester, headers, data, completed=True
        )

    def get_comments(self):
        """
        Warning: this only returns review comments. For normal conversation comments, use get_issue_comments.

        :calls: `GET /repos/:owner/:repo/pulls/:number/comments <http://developer.github.com/v3/pulls/comments>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestComment.PullRequestComment`
        """
        return self.get_review_comments()

    def get_review_comments(self, since=github.GithubObject.NotSet):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/comments <http://developer.github.com/v3/pulls/comments>`_
        :param since: datetime.datetime format YYYY-MM-DDTHH:MM:SSZ
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestComment.PullRequestComment`
        """
        assert since is github.GithubObject.NotSet or isinstance(
            since, datetime.datetime
        ), since
        url_parameters = dict()
        if since is not github.GithubObject.NotSet:
            url_parameters["since"] = since.strftime("%Y-%m-%dT%H:%M:%SZ")
        return github.PaginatedList.PaginatedList(
            github.PullRequestComment.PullRequestComment,
            self._requester,
            self.url + "/comments",
            url_parameters,
        )

    def get_single_review_comments(self, id):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/review/:id/comments <https://developer.github.com/v3/pulls/reviews/>`_
        :param id: integer
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestComment.PullRequestComment`
        """
        assert isinstance(id, int), id
        return github.PaginatedList.PaginatedList(
            github.PullRequestComment.PullRequestComment,
            self._requester,
            self.url + "/reviews/" + str(id) + "/comments",
            None,
        )

    def get_commits(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/commits <http://developer.github.com/v3/pulls>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Commit.Commit`
        """
        return github.PaginatedList.PaginatedList(
            github.Commit.Commit, self._requester, self.url + "/commits", None
        )

    def get_files(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/files <http://developer.github.com/v3/pulls>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.File.File`
        """
        return github.PaginatedList.PaginatedList(
            github.File.File, self._requester, self.url + "/files", None
        )

    def get_issue_comment(self, id):
        """
        :calls: `GET /repos/:owner/:repo/issues/comments/:id <http://developer.github.com/v3/issues/comments>`_
        :param id: integer
        :rtype: :class:`github.IssueComment.IssueComment`
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET", self._parentUrl(self.issue_url) + "/comments/" + str(id)
        )
        return github.IssueComment.IssueComment(
            self._requester, headers, data, completed=True
        )

    def get_issue_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/issues/:number/comments <http://developer.github.com/v3/issues/comments>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.IssueComment.IssueComment`
        """
        return github.PaginatedList.PaginatedList(
            github.IssueComment.IssueComment,
            self._requester,
            self.issue_url + "/comments",
            None,
        )

    def get_issue_events(self):
        """
        :calls: `GET /repos/:owner/:repo/issues/:issue_number/events <http://developer.github.com/v3/issues/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.IssueEvent.IssueEvent`
        """
        return github.PaginatedList.PaginatedList(
            github.IssueEvent.IssueEvent,
            self._requester,
            self.issue_url + "/events",
            None,
            headers={"Accept": Consts.mediaTypeLockReasonPreview},
        )

    def get_review(self, id):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/reviews/:id <https://developer.github.com/v3/pulls/reviews>`_
        :param id: integer
        :rtype: :class:`github.PullRequestReview.PullRequestReview`
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET", self.url + "/reviews/" + str(id),
        )
        return github.PullRequestReview.PullRequestReview(
            self._requester, headers, data, completed=True
        )

    def get_reviews(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/reviews <https://developer.github.com/v3/pulls/reviews/>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PullRequestReview.PullRequestReview`
        """
        return github.PaginatedList.PaginatedList(
            github.PullRequestReview.PullRequestReview,
            self._requester,
            self.url + "/reviews",
            None,
        )

    def get_review_requests(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/requested_reviewers <https://developer.github.com/v3/pulls/review_requests/>`_
        :rtype: tuple of :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedUser.NamedUser` and of :class:`github.PaginatedList.PaginatedList` of :class:`github.Team.Team`
        """
        return (
            github.PaginatedList.PaginatedList(
                github.NamedUser.NamedUser,
                self._requester,
                self.url + "/requested_reviewers",
                None,
                list_item="users",
            ),
            github.PaginatedList.PaginatedList(
                github.Team.Team,
                self._requester,
                self.url + "/requested_reviewers",
                None,
                list_item="teams",
            ),
        )

    def get_labels(self):
        """
        :calls: `GET /repos/:owner/:repo/issues/:number/labels <http://developer.github.com/v3/issues/labels>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Label.Label`
        """
        return github.PaginatedList.PaginatedList(
            github.Label.Label, self._requester, self.issue_url + "/labels", None
        )

    def add_to_labels(self, *labels):
        """
        :calls: `POST /repos/:owner/:repo/issues/:number/labels <http://developer.github.com/v3/issues/labels>`_
        :param label: :class:`github.Label.Label` or string
        :rtype: None
        """
        assert all(
            isinstance(element, (github.Label.Label, str)) for element in labels
        ), labels
        post_parameters = [
            label.name if isinstance(label, github.Label.Label) else label
            for label in labels
        ]
        headers, data = self._requester.requestJsonAndCheck(
            "POST", self.issue_url + "/labels", input=post_parameters
        )

    def delete_labels(self):
        """
        :calls: `DELETE /repos/:owner/:repo/issues/:number/labels <http://developer.github.com/v3/issues/labels>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", self.issue_url + "/labels"
        )

    def remove_from_labels(self, label):
        """
        :calls: `DELETE /repos/:owner/:repo/issues/:number/labels/:name <http://developer.github.com/v3/issues/labels>`_
        :param label: :class:`github.Label.Label` or string
        :rtype: None
        """
        assert isinstance(label, (github.Label.Label, str)), label
        if isinstance(label, github.Label.Label):
            label = label._identity
        else:
            label = urllib.parse.quote(label)
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", self.issue_url + "/labels/" + label
        )

    def set_labels(self, *labels):
        """
        :calls: `PUT /repos/:owner/:repo/issues/:number/labels <http://developer.github.com/v3/issues/labels>`_
        :param labels: list of :class:`github.Label.Label` or strings
        :rtype: None
        """
        assert all(
            isinstance(element, (github.Label.Label, str)) for element in labels
        ), labels
        post_parameters = [
            label.name if isinstance(label, github.Label.Label) else label
            for label in labels
        ]
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", self.issue_url + "/labels", input=post_parameters
        )

    def is_merged(self):
        """
        :calls: `GET /repos/:owner/:repo/pulls/:number/merge <http://developer.github.com/v3/pulls>`_
        :rtype: bool
        """
        status, headers, data = self._requester.requestJson("GET", self.url + "/merge")
        return status == 204

    def merge(
        self,
        commit_message=github.GithubObject.NotSet,
        commit_title=github.GithubObject.NotSet,
        merge_method=github.GithubObject.NotSet,
        sha=github.GithubObject.NotSet,
    ):
        """
        :calls: `PUT /repos/:owner/:repo/pulls/:number/merge <http://developer.github.com/v3/pulls>`_
        :param commit_message: string
        :rtype: :class:`github.PullRequestMergeStatus.PullRequestMergeStatus`
        """
        assert commit_message is github.GithubObject.NotSet or isinstance(
            commit_message, str
        ), commit_message
        assert commit_title is github.GithubObject.NotSet or isinstance(
            commit_title, str
        ), commit_title
        assert merge_method is github.GithubObject.NotSet or isinstance(
            merge_method, str
        ), merge_method
        assert sha is github.GithubObject.NotSet or isinstance(sha, str), sha
        post_parameters = dict()
        if commit_message is not github.GithubObject.NotSet:
            post_parameters["commit_message"] = commit_message
        if commit_title is not github.GithubObject.NotSet:
            post_parameters["commit_title"] = commit_title
        if merge_method is not github.GithubObject.NotSet:
            post_parameters["merge_method"] = merge_method
        if sha is not github.GithubObject.NotSet:
            post_parameters["sha"] = sha
        headers, data = self._requester.requestJsonAndCheck(
            "PUT", self.url + "/merge", input=post_parameters
        )
        return github.PullRequestMergeStatus.PullRequestMergeStatus(
            self._requester, headers, data, completed=True
        )

    def add_to_assignees(self, *assignees):
        """
        :calls: `POST /repos/:owner/:repo/issues/:number/assignees <https://developer.github.com/v3/issues/assignees>`_
        :param assignees: list of :class:`github.NamedUser.NamedUser` or string
        :rtype: None
        """
        assert all(
            isinstance(element, (github.NamedUser.NamedUser, str))
            for element in assignees
        ), assignees
        post_parameters = {
            "assignees": [
                assignee.login
                if isinstance(assignee, github.NamedUser.NamedUser)
                else assignee
                for assignee in assignees
            ]
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST", self.issue_url + "/assignees", input=post_parameters
        )
        # Only use the assignees attribute, since we call this PR as an issue
        self._useAttributes({"assignees": data["assignees"]})

    def remove_from_assignees(self, *assignees):
        """
        :calls: `DELETE /repos/:owner/:repo/issues/:number/assignees <https://developer.github.com/v3/issues/assignees>`_
        :param assignees: list of :class:`github.NamedUser.NamedUser` or string
        :rtype: None
        """
        assert all(
            isinstance(element, (github.NamedUser.NamedUser, str))
            for element in assignees
        ), assignees
        post_parameters = {
            "assignees": [
                assignee.login
                if isinstance(assignee, github.NamedUser.NamedUser)
                else assignee
                for assignee in assignees
            ]
        }
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", self.issue_url + "/assignees", input=post_parameters
        )
        # Only use the assignees attribute, since we call this PR as an issue
        self._useAttributes({"assignees": data["assignees"]})

    def update_branch(self, expected_head_sha=github.GithubObject.NotSet):
        """
        :calls `PUT /repos/:owner/:repo/pulls/:pull_number/update-branch <https://developer.github.com/v3/pulls>`_
        :param expected_head_sha: string
        :rtype: bool
        """
        assert expected_head_sha is github.GithubObject.NotSet or isinstance(
            expected_head_sha, str
        ), expected_head_sha
        post_parameters = {}
        if expected_head_sha is not github.GithubObject.NotSet:
            post_parameters["expected_head_sha"] = expected_head_sha
        status, headers, data = self._requester.requestJson(
            "PUT",
            self.url + "/update-branch",
            input=post_parameters,
            headers={"Accept": Consts.updateBranchPreview},
        )
        return status == 202

    def _initAttributes(self):
        self._additions = github.GithubObject.NotSet
        self._assignee = github.GithubObject.NotSet
        self._assignees = github.GithubObject.NotSet
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
        self._draft = github.GithubObject.NotSet
        self._head = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._issue_url = github.GithubObject.NotSet
        self._labels = github.GithubObject.NotSet
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
            self._additions = self._makeIntAttribute(attributes["additions"])
        if "assignee" in attributes:  # pragma no branch
            self._assignee = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["assignee"]
            )
        if "assignees" in attributes:  # pragma no branch
            self._assignees = self._makeListOfClassesAttribute(
                github.NamedUser.NamedUser, attributes["assignees"]
            )
        elif "assignee" in attributes:
            if attributes["assignee"] is not None:
                self._assignees = self._makeListOfClassesAttribute(
                    github.NamedUser.NamedUser, [attributes["assignee"]]
                )
            else:
                self._assignees = self._makeListOfClassesAttribute(
                    github.NamedUser.NamedUser, []
                )
        if "base" in attributes:  # pragma no branch
            self._base = self._makeClassAttribute(
                github.PullRequestPart.PullRequestPart, attributes["base"]
            )
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
            self._head = self._makeClassAttribute(
                github.PullRequestPart.PullRequestPart, attributes["head"]
            )
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "issue_url" in attributes:  # pragma no branch
            self._issue_url = self._makeStringAttribute(attributes["issue_url"])
        if "labels" in attributes:  # pragma no branch
            self._labels = self._makeListOfClassesAttribute(
                github.Label.Label, attributes["labels"]
            )
        if "merge_commit_sha" in attributes:  # pragma no branch
            self._merge_commit_sha = self._makeStringAttribute(
                attributes["merge_commit_sha"]
            )
        if "mergeable" in attributes:  # pragma no branch
            self._mergeable = self._makeBoolAttribute(attributes["mergeable"])
        if "mergeable_state" in attributes:  # pragma no branch
            self._mergeable_state = self._makeStringAttribute(
                attributes["mergeable_state"]
            )
        if "merged" in attributes:  # pragma no branch
            self._merged = self._makeBoolAttribute(attributes["merged"])
        if "merged_at" in attributes:  # pragma no branch
            self._merged_at = self._makeDatetimeAttribute(attributes["merged_at"])
        if "merged_by" in attributes:  # pragma no branch
            self._merged_by = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["merged_by"]
            )
        if "milestone" in attributes:  # pragma no branch
            self._milestone = self._makeClassAttribute(
                github.Milestone.Milestone, attributes["milestone"]
            )
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "patch_url" in attributes:  # pragma no branch
            self._patch_url = self._makeStringAttribute(attributes["patch_url"])
        if "review_comment_url" in attributes:  # pragma no branch
            self._review_comment_url = self._makeStringAttribute(
                attributes["review_comment_url"]
            )
        if "review_comments" in attributes:  # pragma no branch
            self._review_comments = self._makeIntAttribute(
                attributes["review_comments"]
            )
        if "review_comments_url" in attributes:  # pragma no branch
            self._review_comments_url = self._makeStringAttribute(
                attributes["review_comments_url"]
            )
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "title" in attributes:  # pragma no branch
            self._title = self._makeStringAttribute(attributes["title"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["user"]
            )
