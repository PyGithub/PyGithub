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

import github.GithubObject

import github.Organization
import github.Repository
import github.NamedUser


class Event(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Events. The reference can be found here http://developer.github.com/v3/activity/events/
    """

    @property
    def actor(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        return self._NoneIfNotSet(self._actor)

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        return self._NoneIfNotSet(self._created_at)

    @property
    def id(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._id)

    @property
    def org(self):
        """
        :type: :class:`github.Organization.Organization`
        """
        return self._NoneIfNotSet(self._org)

    @property
    def payload(self):
        """
        :type: dict
        """
        return self._NoneIfNotSet(self._payload)

    @property
    def public(self):
        """
        :type: bool
        """
        return self._NoneIfNotSet(self._public)

    @property
    def repo(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        return self._NoneIfNotSet(self._repo)

    @property
    def type(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._type)

    def _initAttributes(self):
        self._actor = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._org = github.GithubObject.NotSet
        self._payload = github.GithubObject.NotSet
        self._public = github.GithubObject.NotSet
        self._repo = github.GithubObject.NotSet
        self._type = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "actor" in attributes:  # pragma no branch
            assert attributes["actor"] is None or isinstance(attributes["actor"], dict), attributes["actor"]
            self._actor = None if attributes["actor"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["actor"], completed=False)
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (str, unicode)), attributes["id"]
            self._id = attributes["id"]
        if "org" in attributes:  # pragma no branch
            assert attributes["org"] is None or isinstance(attributes["org"], dict), attributes["org"]
            self._org = None if attributes["org"] is None else github.Organization.Organization(self._requester, self._headers, attributes["org"], completed=False)
        if "payload" in attributes:  # pragma no branch
            assert attributes["payload"] is None or isinstance(attributes["payload"], dict), attributes["payload"]
            self._payload = attributes["payload"]
        if "public" in attributes:  # pragma no branch
            assert attributes["public"] is None or isinstance(attributes["public"], bool), attributes["public"]
            self._public = attributes["public"]
        if "repo" in attributes:  # pragma no branch
            assert attributes["repo"] is None or isinstance(attributes["repo"], dict), attributes["repo"]
            self._repo = None if attributes["repo"] is None else github.Repository.Repository(self._requester, self._headers, attributes["repo"], completed=False)
        if "type" in attributes:  # pragma no branch
            assert attributes["type"] is None or isinstance(attributes["type"], (str, unicode)), attributes["type"]
            self._type = attributes["type"]
