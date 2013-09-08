# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
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


class NotificationSubject(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Subjects of Notifications as returned for example by http://developer.github.com/v3/activity/notifications/#list-your-notifications
    """

    @property
    def title(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._title)

    @property
    def url(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._url)

    @property
    def latest_comment_url(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._latest_comment_url)

    @property
    def type(self):
        """
        :type: string
        """
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
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]  # pragma no cover (but should be investigated)
            self._url = attributes["url"]  # pragma no cover (but should be investigated)
        if "latest_comment_url" in attributes:  # pragma no branch
            assert attributes["latest_comment_url"] is None or isinstance(attributes["latest_comment_url"], (str, unicode)), attributes["latest_comment_url"]  # pragma no cover (but should be investigated)
            self._latest_comment_url = attributes["latest_comment_url"]  # pragma no cover (but should be investigated)
        if "type" in attributes:  # pragma no branch
            assert attributes["type"] is None or isinstance(attributes["type"], (str, unicode)), attributes["type"]
            self._type = attributes["type"]
