# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
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

import github.NamedUser


class CommitStatus(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents CommitStatuss as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        return self._NoneIfNotSet(self._created_at)

    @property
    def creator(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        return self._NoneIfNotSet(self._creator)

    @property
    def description(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._description)

    @property
    def id(self):
        """
        :type: integer
        """
        return self._NoneIfNotSet(self._id)

    @property
    def state(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._state)

    @property
    def target_url(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._target_url)

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        return self._NoneIfNotSet(self._updated_at)

    @property
    def url(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._url)

    def _initAttributes(self):
        self._created_at = github.GithubObject.NotSet
        self._creator = github.GithubObject.NotSet
        self._description = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._state = github.GithubObject.NotSet
        self._target_url = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "creator" in attributes:  # pragma no branch
            assert attributes["creator"] is None or isinstance(attributes["creator"], dict), attributes["creator"]
            self._creator = None if attributes["creator"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["creator"], completed=False)
        if "description" in attributes:  # pragma no branch
            assert attributes["description"] is None or isinstance(attributes["description"], (str, unicode)), attributes["description"]
            self._description = attributes["description"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "state" in attributes:  # pragma no branch
            assert attributes["state"] is None or isinstance(attributes["state"], (str, unicode)), attributes["state"]
            self._state = attributes["state"]
        if "target_url" in attributes:  # pragma no branch
            assert attributes["target_url"] is None or isinstance(attributes["target_url"], (str, unicode)), attributes["target_url"]
            self._target_url = attributes["target_url"]
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
