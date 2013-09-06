# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
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

import datetime

import github.GithubObject
import github.PaginatedList

import github.NamedUser
import github.Label


class Milestone(github.GithubObject.CompletableGithubObject):
    """
    This class represents Milestones. The reference can be found here http://developer.github.com/v3/issues/milestones/
    """

    @property
    def closed_issues(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._closed_issues)
        return self._NoneIfNotSet(self._closed_issues)

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def creator(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._creator)
        return self._NoneIfNotSet(self._creator)

    @property
    def description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._NoneIfNotSet(self._description)

    @property
    def due_on(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._due_on)
        return self._NoneIfNotSet(self._due_on)

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def labels_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._labels_url)
        return self._NoneIfNotSet(self._labels_url)

    @property
    def number(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._number)
        return self._NoneIfNotSet(self._number)

    @property
    def open_issues(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._open_issues)
        return self._NoneIfNotSet(self._open_issues)

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

    def delete(self):
        """
        :calls: `DELETE /repos/:owner/:repo/milestones/:number <http://developer.github.com/v3/issues/milestones>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url
        )

    def edit(self, title, state=github.GithubObject.NotSet, description=github.GithubObject.NotSet, due_on=github.GithubObject.NotSet):
        """
        :calls: `PATCH /repos/:owner/:repo/milestones/:number <http://developer.github.com/v3/issues/milestones>`_
        :param title: string
        :param state: string
        :param description: string
        :param due_on: date
        :rtype: None
        """
        assert isinstance(title, (str, unicode)), title
        assert state is github.GithubObject.NotSet or isinstance(state, (str, unicode)), state
        assert description is github.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        assert due_on is github.GithubObject.NotSet or isinstance(due_on, datetime.date), due_on
        post_parameters = {
            "title": title,
        }
        if state is not github.GithubObject.NotSet:
            post_parameters["state"] = state
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        if due_on is not github.GithubObject.NotSet:
            post_parameters["due_on"] = due_on.strftime("%Y-%m-%d")
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        self._useAttributes(data)

    def get_labels(self):
        """
        :calls: `GET /repos/:owner/:repo/milestones/:number/labels <http://developer.github.com/v3/issues/labels>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Label.Label`
        """
        return github.PaginatedList.PaginatedList(
            github.Label.Label,
            self._requester,
            self.url + "/labels",
            None
        )

    @property
    def _identity(self):
        return self.number

    def _initAttributes(self):
        self._closed_issues = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._creator = github.GithubObject.NotSet
        self._description = github.GithubObject.NotSet
        self._due_on = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._labels_url = github.GithubObject.NotSet
        self._number = github.GithubObject.NotSet
        self._open_issues = github.GithubObject.NotSet
        self._state = github.GithubObject.NotSet
        self._title = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "closed_issues" in attributes:  # pragma no branch
            assert attributes["closed_issues"] is None or isinstance(attributes["closed_issues"], (int, long)), attributes["closed_issues"]
            self._closed_issues = attributes["closed_issues"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "creator" in attributes:  # pragma no branch
            assert attributes["creator"] is None or isinstance(attributes["creator"], dict), attributes["creator"]
            self._creator = None if attributes["creator"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["creator"], completed=False)
        if "description" in attributes:  # pragma no branch
            assert attributes["description"] is None or isinstance(attributes["description"], (str, unicode)), attributes["description"]
            self._description = attributes["description"]
        if "due_on" in attributes:  # pragma no branch
            assert attributes["due_on"] is None or isinstance(attributes["due_on"], (str, unicode)), attributes["due_on"]
            self._due_on = self._parseDatetime(attributes["due_on"])
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "labels_url" in attributes:  # pragma no branch
            assert attributes["labels_url"] is None or isinstance(attributes["labels_url"], (str, unicode)), attributes["labels_url"]
            self._labels_url = attributes["labels_url"]
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
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
