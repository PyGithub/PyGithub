# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import datetime

import GithubObject
import PaginatedList

import NamedUser
import Label


class Milestone(GithubObject.GithubObject):
    @property
    def closed_issues(self):
        self._completeIfNotSet(self._closed_issues)
        return self._NoneIfNotSet(self._closed_issues)

    @property
    def created_at(self):
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def creator(self):
        self._completeIfNotSet(self._creator)
        return self._NoneIfNotSet(self._creator)

    @property
    def description(self):
        self._completeIfNotSet(self._description)
        return self._NoneIfNotSet(self._description)

    @property
    def due_on(self):
        self._completeIfNotSet(self._due_on)
        return self._NoneIfNotSet(self._due_on)

    @property
    def id(self):
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def number(self):
        self._completeIfNotSet(self._number)
        return self._NoneIfNotSet(self._number)

    @property
    def open_issues(self):
        self._completeIfNotSet(self._open_issues)
        return self._NoneIfNotSet(self._open_issues)

    @property
    def state(self):
        self._completeIfNotSet(self._state)
        return self._NoneIfNotSet(self._state)

    @property
    def title(self):
        self._completeIfNotSet(self._title)
        return self._NoneIfNotSet(self._title)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def delete(self):
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def edit(self, title, state=GithubObject.NotSet, description=GithubObject.NotSet, due_on=GithubObject.NotSet):
        assert isinstance(title, (str, unicode)), title
        assert state is GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert description is GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert due_on is GithubObject.NotSet or isinstance(due_on, datetime.date), due_on
        post_parameters = {
            "title": title,
        }
        if state is not GithubObject.NotSet:
            post_parameters["state"] = state
        if description is not GithubObject.NotSet:
            post_parameters["description"] = description
        if due_on is not GithubObject.NotSet:
            post_parameters["due_on"] = due_on.strftime("%Y-%m-%d")
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def get_labels(self):
        return PaginatedList.PaginatedList(
            Label.Label,
            self._requester,
            self.url + "/labels",
            None
        )

    @property
    def _identity(self):
        return self.number

    def _initAttributes(self):
        self._closed_issues = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._creator = GithubObject.NotSet
        self._description = GithubObject.NotSet
        self._due_on = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._number = GithubObject.NotSet
        self._open_issues = GithubObject.NotSet
        self._state = GithubObject.NotSet
        self._title = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "closed_issues" in attributes:  # pragma no branch
            assert attributes["closed_issues"] is None or isinstance(attributes["closed_issues"], (int, long)), attributes["closed_issues"]
            self._closed_issues = attributes["closed_issues"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "creator" in attributes:  # pragma no branch
            assert attributes["creator"] is None or isinstance(attributes["creator"], dict), attributes["creator"]
            self._creator = None if attributes["creator"] is None else NamedUser.NamedUser(self._requester, attributes["creator"], completed=False)
        if "description" in attributes:  # pragma no branch
            assert attributes["description"] is None or isinstance(attributes["description"], (str, unicode)), attributes["description"]
            self._description = attributes["description"]
        if "due_on" in attributes:  # pragma no branch
            assert attributes["due_on"] is None or isinstance(attributes["due_on"], (str, unicode)), attributes["due_on"]
            self._due_on = self._parseDatetime(attributes["due_on"])
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "number" in attributes:  # pragma no branch
            assert attributes["number"] is None or isinstance(attributes["number"], (int, long)), attributes["number"]
            self._number = attributes["number"]
        if "open_issues" in attributes:  # pragma no branch
            assert attributes["open_issues"] is None or isinstance(attributes["open_issues"], (int, long)), attributes["open_issues"]
            self._open_issues = attributes["open_issues"]
        if "state" in attributes:  # pragma no branch
            assert attributes["state"] is None or isinstance(attributes["state"], (str, unicode)), attributes["state"]
            self._state = attributes["state"]
        if "title" in attributes:  # pragma no branch
            assert attributes["title"] is None or isinstance(attributes["title"], (str, unicode)), attributes["title"]
            self._title = attributes["title"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
