# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Peter Golm <golm.peter@gmail.com>                             #
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

import github.Repository
import github.NotificationSubject


class Notification(github.GithubObject.CompletableGithubObject):
    """
    This class represents Notifications. The reference can be found here http://developer.github.com/v3/activity/notifications/
    """

    @property
    def id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def last_read_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._last_read_at)
        return self._NoneIfNotSet(self._last_read_at)

    @property
    def repository(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        self._completeIfNotSet(self._repository)
        return self._NoneIfNotSet(self._repository)

    @property
    def subject(self):
        """
        :type: :class:`github.NotificationSubject.NotificationSubject`
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
    def subscription_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._subscription_url)
        return self._NoneIfNotSet(self._subscription_url)

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
        self._last_read_at = github.GithubObject.NotSet
        self._repository = github.GithubObject.NotSet
        self._reason = github.GithubObject.NotSet
        self._subscription_url = github.GithubObject.NotSet
        self._unread = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (str, unicode)), attributes["id"]
            self._id = attributes["id"]
        if "last_read_at" in attributes:  # pragma no branch
            assert attributes["last_read_at"] is None or isinstance(attributes["last_read_at"], (str, unicode)), attributes["last_read_at"]
            self._last_read_at = self._parseDatetime(attributes["last_read_at"])
        if "repository" in attributes:  # pragma no branch
            assert attributes["repository"] is None or isinstance(attributes["repository"], dict), attributes["repository"]
            self._repository = None if attributes["repository"] is None else github.Repository.Repository(self._requester, self._headers, attributes["repository"], completed=False)
        if "subject" in attributes:  # pragma no branch
            assert attributes["subject"] is None or isinstance(attributes["subject"], dict), attributes["subject"]
            self._subject = None if attributes["subject"] is None else github.NotificationSubject.NotificationSubject(self._requester, self._headers, attributes["subject"], completed=False)
        if "reason" in attributes:  # pragma no branch
            assert attributes["reason"] is None or isinstance(attributes["reason"], (str, unicode)), attributes["reason"]
            self._reason = attributes["reason"]
        if "subscription_url" in attributes:  # pragma no branch
            assert attributes["subscription_url"] is None or isinstance(attributes["subscription_url"], (str, unicode)), attributes["subscription_url"]
            self._subscription_url = attributes["subscription_url"]
        if "unread" in attributes:  # pragma no branch
            assert attributes["unread"] is None or isinstance(attributes["unread"], bool), attributes["unread"]
            self._unread = attributes["unread"]
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]  # pragma no cover (but should be investigated)
            self._url = attributes["url"]  # pragma no cover (but should be investigated)
