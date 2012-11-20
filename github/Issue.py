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

import Repository
import IssueEvent
import Label
import NamedUser
import Milestone
import IssueComment
import IssuePullRequest


class Issue(GithubObject.GithubObject):
    @property
    def assignee(self):
        self._completeIfNotSet(self._assignee)
        return self._NoneIfNotSet(self._assignee)

    @property
    def body(self):
        self._completeIfNotSet(self._body)
        return self._NoneIfNotSet(self._body)

    @property
    def closed_at(self):
        self._completeIfNotSet(self._closed_at)
        return self._NoneIfNotSet(self._closed_at)

    @property
    def closed_by(self):
        self._completeIfNotSet(self._closed_by)
        return self._NoneIfNotSet(self._closed_by)

    @property
    def comments(self):
        self._completeIfNotSet(self._comments)
        return self._NoneIfNotSet(self._comments)

    @property
    def created_at(self):
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def html_url(self):
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def id(self):
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def labels(self):
        self._completeIfNotSet(self._labels)
        return self._NoneIfNotSet(self._labels)

    @property
    def milestone(self):
        self._completeIfNotSet(self._milestone)
        return self._NoneIfNotSet(self._milestone)

    @property
    def number(self):
        self._completeIfNotSet(self._number)
        return self._NoneIfNotSet(self._number)

    @property
    def pull_request(self):
        self._completeIfNotSet(self._pull_request)
        return self._NoneIfNotSet(self._pull_request)

    @property
    def repository(self):
        self._completeIfNotSet(self._repository)
        return self._NoneIfNotSet(self._repository)

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

    def add_to_labels(self, *labels):
        assert all(isinstance(element, Label.Label) for element in labels), labels
        post_parameters = [label.name for label in labels]
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/labels",
            None,
            post_parameters
        )

    def create_comment(self, body):
        assert isinstance(body, (str, unicode)), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/comments",
            None,
            post_parameters
        )
        return IssueComment.IssueComment(self._requester, data, completed=True)

    def delete_labels(self):
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url + "/labels",
            None,
            None
        )

    def edit(self, title=GithubObject.NotSet, body=GithubObject.NotSet, assignee=GithubObject.NotSet, state=GithubObject.NotSet, milestone=GithubObject.NotSet, labels=GithubObject.NotSet):
        assert title is GithubObject.NotSet or isinstance(title, (str, unicode)), title
        assert body is GithubObject.NotSet or isinstance(body, (str, unicode)), body
        assert assignee is GithubObject.NotSet or assignee is None or isinstance(assignee, NamedUser.NamedUser), assignee
        assert state is GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert milestone is GithubObject.NotSet or milestone is None or isinstance(milestone, Milestone.Milestone), milestone
        assert labels is GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in labels), labels
        post_parameters = dict()
        if title is not GithubObject.NotSet:
            post_parameters["title"] = title
        if body is not GithubObject.NotSet:
            post_parameters["body"] = body
        if assignee is not GithubObject.NotSet:
            post_parameters["assignee"] = assignee._identity if assignee else ''
        if state is not GithubObject.NotSet:
            post_parameters["state"] = state
        if milestone is not GithubObject.NotSet:
            post_parameters["milestone"] = milestone._identity if milestone else ''
        if labels is not GithubObject.NotSet:
            post_parameters["labels"] = labels
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def get_comment(self, id):
        assert isinstance(id, (int, long)), id
        headers, data = self._requester.requestAndCheck(
            "GET",
            self._parentUrl(self.url) + "/comments/" + str(id),
            None,
            None
        )
        return IssueComment.IssueComment(self._requester, data, completed=True)

    def get_comments(self):
        return PaginatedList.PaginatedList(
            IssueComment.IssueComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_events(self):
        return PaginatedList.PaginatedList(
            IssueEvent.IssueEvent,
            self._requester,
            self.url + "/events",
            None
        )

    def get_labels(self):
        return PaginatedList.PaginatedList(
            Label.Label,
            self._requester,
            self.url + "/labels",
            None
        )

    def remove_from_labels(self, label):
        assert isinstance(label, Label.Label), label
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url + "/labels/" + label._identity,
            None,
            None
        )

    def set_labels(self, *labels):
        assert all(isinstance(element, Label.Label) for element in labels), labels
        post_parameters = [label.name for label in labels]
        headers, data = self._requester.requestAndCheck(
            "PUT",
            self.url + "/labels",
            None,
            post_parameters
        )

    @property
    def _identity(self):
        return self.number

    def _initAttributes(self):
        self._assignee = GithubObject.NotSet
        self._body = GithubObject.NotSet
        self._closed_at = GithubObject.NotSet
        self._closed_by = GithubObject.NotSet
        self._comments = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._html_url = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._labels = GithubObject.NotSet
        self._milestone = GithubObject.NotSet
        self._number = GithubObject.NotSet
        self._pull_request = GithubObject.NotSet
        self._repository = GithubObject.NotSet
        self._state = GithubObject.NotSet
        self._title = GithubObject.NotSet
        self._updated_at = GithubObject.NotSet
        self._url = GithubObject.NotSet
        self._user = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "assignee" in attributes:  # pragma no branch
            assert attributes["assignee"] is None or isinstance(attributes["assignee"], dict), attributes["assignee"]
            self._assignee = None if attributes["assignee"] is None else NamedUser.NamedUser(self._requester, attributes["assignee"], completed=False)
        if "body" in attributes:  # pragma no branch
            assert attributes["body"] is None or isinstance(attributes["body"], (str, unicode)), attributes["body"]
            self._body = attributes["body"]
        if "closed_at" in attributes:  # pragma no branch
            assert attributes["closed_at"] is None or isinstance(attributes["closed_at"], (str, unicode)), attributes["closed_at"]
            self._closed_at = self._parseDatetime(attributes["closed_at"])
        if "closed_by" in attributes:  # pragma no branch
            assert attributes["closed_by"] is None or isinstance(attributes["closed_by"], dict), attributes["closed_by"]
            self._closed_by = None if attributes["closed_by"] is None else NamedUser.NamedUser(self._requester, attributes["closed_by"], completed=False)
        if "comments" in attributes:  # pragma no branch
            assert attributes["comments"] is None or isinstance(attributes["comments"], (int, long)), attributes["comments"]
            self._comments = attributes["comments"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "labels" in attributes:  # pragma no branch
            assert attributes["labels"] is None or all(isinstance(element, dict) for element in attributes["labels"]), attributes["labels"]
            self._labels = None if attributes["labels"] is None else [
                Label.Label(self._requester, element, completed=False)
                for element in attributes["labels"]
            ]
        if "milestone" in attributes:  # pragma no branch
            assert attributes["milestone"] is None or isinstance(attributes["milestone"], dict), attributes["milestone"]
            self._milestone = None if attributes["milestone"] is None else Milestone.Milestone(self._requester, attributes["milestone"], completed=False)
        if "number" in attributes:  # pragma no branch
            assert attributes["number"] is None or isinstance(attributes["number"], (int, long)), attributes["number"]
            self._number = attributes["number"]
        if "pull_request" in attributes:  # pragma no branch
            assert attributes["pull_request"] is None or isinstance(attributes["pull_request"], dict), attributes["pull_request"]
            self._pull_request = None if attributes["pull_request"] is None else IssuePullRequest.IssuePullRequest(self._requester, attributes["pull_request"], completed=False)
        if "repository" in attributes:  # pragma no branch
            assert attributes["repository"] is None or isinstance(attributes["repository"], dict), attributes["repository"]
            self._repository = None if attributes["repository"] is None else Repository.Repository(self._requester, attributes["repository"], completed=False)
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
