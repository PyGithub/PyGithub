# -*- coding: utf-8 -*-

# Copyright 2013 Peter Golm
# golm.peter@gmail.com

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import datetime

import github.GithubObject
import github.PaginatedList

import github.Repository


class Notification(github.GithubObject.GithubObject):
    """
    http://developer.github.com/v3/todo
    """

    @property
    def id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def repository(self):
        """
        :type: class: `github.Repository.Repository`
        """
        self._completeIfNotSet(self._repository)
        return self._NoneIfNotSet(self._repository)

    @property
    def subject(self):
        """
        :type: class: `github.Notification.NotificationSubject`
        """
        self._completeIfNotSet(self._subject)
        return self._NoneIfNotSet(self._subject)

    @property
    def reason(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._reason)
        return self._NoneIfNotSet(self._reason)

    @property
    def unread(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._unread)
        return self._NoneIfNotSet(self._unread)

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

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._repository = github.GithubObject.NotSet
        self._reason = github.GithubObject.NotSet
        self._unread = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:
            assert attributes["id"] is None or isinstance(attributes["id"], (str, unicode)), attributes["id"]
            self._id = attributes["id"]
        if "repository" in attributes:
            assert attributes["repository"] is None or isinstance(attributes["repository"], (dict)), attributes["repository"]
            self._repository = None if attributes["repository"] is None else github.Repository.Repository(self._requester, attributes["repository"], completed=False)
        if "subject" in attributes:
            assert attributes["subject"] is None or isinstance(attributes["subject"], (dict)), attributes["subject"]
            self._subject = None if attributes["subject"] is None else NotificationSubject(self._requester, attributes["subject"], completed=False)
        if "reason" in attributes:
            assert attributes["reason"] is None or isinstance(attributes["reason"], (str, unicode)), attributes["reason"]
            self._reason = attributes["reason"]
        if "unread" in attributes:
            assert attributes["unread"] is None or isinstance(attributes["unread"], (bool,)), attributes["unread"]
            self._unread = attributes["unread"]
        if "updated_at" in attributes:
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = datetime.datetime.strptime(attributes["updated_at"], "%Y-%m-%dT%H:%M:%SZ");
        if "url" in attributes:
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]

class NotificationSubject(github.GithubObject.GithubObject):
    """
    http://developer.github.com/v3/todo
    """

    @property
    def title(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._title)
        return self._NoneIfNotSet(self._title)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def latest_comment_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._latest_comment_url)
        return self._NoneIfNotSet(self._latest_comment_url)

    @property
    def type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._type)
        return self._NoneIfNotSet(self._type)

    def _initAttributes(self):
        self._title = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._latest_comment_url = github.GithubObject.NotSet
        self._type = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "title" in attributes:  # pragma no branch
            assert attributes["title"] is None or isinstance(attributes["title"], (str, unicode)), attributes["title"]
            self._title = attributes["title"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
        if "latest_comment_url" in attributes:  # pragma no branch
            assert attributes["latest_comment_url"] is None or isinstance(attributes["latest_comment_url"], (str, unicode)), attributes["latest_comment_url"]
            self._latest_comment_url = attributes["latest_comment_url"]
        if "type" in attributes:  # pragma no branch
            assert attributes["type"] is None or isinstance(attributes["type"], (str, unicode)), attributes["type"]
            self._type = attributes["type"]