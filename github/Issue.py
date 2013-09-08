# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Andrew Bettison <andrewb@zip.com.au>                          #
# Copyright 2012 Philip Kimmey <philip@rover.com>                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Stuart Glaser <stuglaser@gmail.com>                           #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
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

import github.Repository
import github.IssueEvent
import github.Label
import github.NamedUser
import github.Milestone
import github.IssueComment
import github.IssuePullRequest


class Issue(github.GithubObject.CompletableGithubObject):
    """
    This class represents Issues as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def assignee(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._assignee)
        return self._NoneIfNotSet(self._assignee)

    @property
    def body(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._body)
        return self._NoneIfNotSet(self._body)

    @property
    def closed_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._closed_at)
        return self._NoneIfNotSet(self._closed_at)

    @property
    def closed_by(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._closed_by)
        return self._NoneIfNotSet(self._closed_by)

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
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def events_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._events_url)
        return self._NoneIfNotSet(self._events_url)

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
    def labels(self):
        """
        :type: list of :class:`github.Label.Label`
        """
        self._completeIfNotSet(self._labels)
        return self._NoneIfNotSet(self._labels)

    @property
    def labels_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._labels_url)
        return self._NoneIfNotSet(self._labels_url)

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
    def pull_request(self):
        """
        :type: :class:`github.IssuePullRequest.IssuePullRequest`
        """
        self._completeIfNotSet(self._pull_request)
        return self._NoneIfNotSet(self._pull_request)

    @property
    def repository(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        self._completeIfNotSet(self._repository)
        if self._repository is github.GithubObject.NotSet:
            # The repository was not set automatically, so it must be looked up by url.
            repo_url = "/".join(self.url.split("/")[:-2])
            self._repository = github.Repository.Repository(self._requester, self._headers, {'url': repo_url}, completed=False)
        return self._repository

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

    def add_to_labels(self, *labels):
        """
        :calls: `POST /repos/:owner/:repo/issues/:number/labels <http://developer.github.com/v3/issues/labels>`_
        :param label: :class:`github.Label.Label`
        :rtype: None
        """
        assert all(isinstance(element, github.Label.Label) for element in labels), labels
        post_parameters = [label.name for label in labels]
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/labels",
            input=post_parameters
        )

    def create_comment(self, body):
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
            self.url + "/comments",
            input=post_parameters
        )
        return github.IssueComment.IssueComment(self._requester, headers, data, completed=True)

    def delete_labels(self):
        """
        :calls: `DELETE /repos/:owner/:repo/issues/:number/labels <http://developer.github.com/v3/issues/labels>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/labels"
        )

    def edit(self, title=github.GithubObject.NotSet, body=github.GithubObject.NotSet, assignee=github.GithubObject.NotSet, state=github.GithubObject.NotSet, milestone=github.GithubObject.NotSet, labels=github.GithubObject.NotSet):
        """
        :calls: `PATCH /repos/:owner/:repo/issues/:number <http://developer.github.com/v3/issues>`_
        :param title: string
        :param body: string
        :param assignee: :class:`github.NamedUser.NamedUser` or None
        :param state: string
        :param milestone: :class:`github.Milestone.Milestone` or None
        :param labels: list of string
        :rtype: None
        """
        assert title is github.GithubObject.NotSet or isinstance(title, (str, unicode)), title
        assert body is github.GithubObject.NotSet or isinstance(body, (str, unicode)), body
        assert assignee is github.GithubObject.NotSet or assignee is None or isinstance(assignee, github.NamedUser.NamedUser), assignee
        assert state is github.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert milestone is github.GithubObject.NotSet or milestone is None or isinstance(milestone, github.Milestone.Milestone), milestone
        assert labels is github.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in labels), labels
        post_parameters = dict()
        if title is not github.GithubObject.NotSet:
            post_parameters["title"] = title
        if body is not github.GithubObject.NotSet:
            post_parameters["body"] = body
        if assignee is not github.GithubObject.NotSet:
            post_parameters["assignee"] = assignee._identity if assignee else ''
        if state is not github.GithubObject.NotSet:
            post_parameters["state"] = state
        if milestone is not github.GithubObject.NotSet:
            post_parameters["milestone"] = milestone._identity if milestone else ''
        if labels is not github.GithubObject.NotSet:
            post_parameters["labels"] = labels
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        self._useAttributes(data)

    def get_comment(self, id):
        """
        :calls: `GET /repos/:owner/:repo/issues/comments/:id <http://developer.github.com/v3/issues/comments>`_
        :param id: integer
        :rtype: :class:`github.IssueComment.IssueComment`
        """
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            self._parentUrl(self.url) + "/comments/" + str(id)
        )
        return github.IssueComment.IssueComment(self._requester, headers, data, completed=True)

    def get_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/issues/:number/comments <http://developer.github.com/v3/issues/comments>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.IssueComment.IssueComment`
        """
        return github.PaginatedList.PaginatedList(
            github.IssueComment.IssueComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_events(self):
        """
        :calls: `GET /repos/:owner/:repo/issues/:issue_number/events <http://developer.github.com/v3/issues/events>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.IssueEvent.IssueEvent`
        """
        return github.PaginatedList.PaginatedList(
            github.IssueEvent.IssueEvent,
            self._requester,
            self.url + "/events",
            None
        )

    def get_labels(self):
        """
        :calls: `GET /repos/:owner/:repo/issues/:number/labels <http://developer.github.com/v3/issues/labels>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Label.Label`
        """
        return github.PaginatedList.PaginatedList(
            github.Label.Label,
            self._requester,
            self.url + "/labels",
            None
        )

    def remove_from_labels(self, label):
        """
        :calls: `DELETE /repos/:owner/:repo/issues/:number/labels/:name <http://developer.github.com/v3/issues/labels>`_
        :param label: :class:`github.Label.Label`
        :rtype: None
        """
        assert isinstance(label, github.Label.Label), label
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url + "/labels/" + label._identity
        )

    def set_labels(self, *labels):
        """
        :calls: `PUT /repos/:owner/:repo/issues/:number/labels <http://developer.github.com/v3/issues/labels>`_
        :param label: :class:`github.Label.Label`
        :rtype: None
        """
        assert all(isinstance(element, github.Label.Label) for element in labels), labels
        post_parameters = [label.name for label in labels]
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.url + "/labels",
            input=post_parameters
        )

    @property
    def _identity(self):
        return self.number

    def _initAttributes(self):
        self._assignee = github.GithubObject.NotSet
        self._body = github.GithubObject.NotSet
        self._closed_at = github.GithubObject.NotSet
        self._closed_by = github.GithubObject.NotSet
        self._comments = github.GithubObject.NotSet
        self._comments_url = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._events_url = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._labels = github.GithubObject.NotSet
        self._labels_url = github.GithubObject.NotSet
        self._milestone = github.GithubObject.NotSet
        self._number = github.GithubObject.NotSet
        self._pull_request = github.GithubObject.NotSet
        self._repository = github.GithubObject.NotSet
        self._state = github.GithubObject.NotSet
        self._title = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._user = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "assignee" in attributes:  # pragma no branch
            assert attributes["assignee"] is None or isinstance(attributes["assignee"], dict), attributes["assignee"]
            self._assignee = None if attributes["assignee"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["assignee"], completed=False)
        if "body" in attributes:  # pragma no branch
            assert attributes["body"] is None or isinstance(attributes["body"], (str, unicode)), attributes["body"]
            self._body = attributes["body"]
        if "closed_at" in attributes:  # pragma no branch
            assert attributes["closed_at"] is None or isinstance(attributes["closed_at"], (str, unicode)), attributes["closed_at"]
            self._closed_at = self._parseDatetime(attributes["closed_at"])
        if "closed_by" in attributes:  # pragma no branch
            assert attributes["closed_by"] is None or isinstance(attributes["closed_by"], dict), attributes["closed_by"]
            self._closed_by = None if attributes["closed_by"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["closed_by"], completed=False)
        if "comments" in attributes:  # pragma no branch
            assert attributes["comments"] is None or isinstance(attributes["comments"], (int, long)), attributes["comments"]
            self._comments = attributes["comments"]
        if "comments_url" in attributes:  # pragma no branch
            assert attributes["comments_url"] is None or isinstance(attributes["comments_url"], (str, unicode)), attributes["comments_url"]
            self._comments_url = attributes["comments_url"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "events_url" in attributes:  # pragma no branch
            assert attributes["events_url"] is None or isinstance(attributes["events_url"], (str, unicode)), attributes["events_url"]
            self._events_url = attributes["events_url"]
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "labels" in attributes:  # pragma no branch
            assert attributes["labels"] is None or all(isinstance(element, dict) for element in attributes["labels"]), attributes["labels"]
            self._labels = None if attributes["labels"] is None else [
                github.Label.Label(self._requester, self._headers, element, completed=False)
                for element in attributes["labels"]
            ]
        if "labels_url" in attributes:  # pragma no branch
            assert attributes["labels_url"] is None or isinstance(attributes["labels_url"], (str, unicode)), attributes["labels_url"]
            self._labels_url = attributes["labels_url"]
        if "milestone" in attributes:  # pragma no branch
            assert attributes["milestone"] is None or isinstance(attributes["milestone"], dict), attributes["milestone"]
            self._milestone = None if attributes["milestone"] is None else github.Milestone.Milestone(self._requester, self._headers, attributes["milestone"], completed=False)
        if "number" in attributes:  # pragma no branch
            assert attributes["number"] is None or isinstance(attributes["number"], (int, long)), attributes["number"]
            self._number = attributes["number"]
        if "pull_request" in attributes:  # pragma no branch
            assert attributes["pull_request"] is None or isinstance(attributes["pull_request"], dict), attributes["pull_request"]
            self._pull_request = None if attributes["pull_request"] is None else github.IssuePullRequest.IssuePullRequest(self._requester, self._headers, attributes["pull_request"], completed=False)
        if "repository" in attributes:  # pragma no branch
            assert attributes["repository"] is None or isinstance(attributes["repository"], dict), attributes["repository"]
            self._repository = None if attributes["repository"] is None else github.Repository.Repository(self._requester, self._headers, attributes["repository"], completed=False)
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
