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

import github.Repository
import github.NamedUser


class PullRequestPart(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents PullRequestParts as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def label(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._label)

    @property
    def ref(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._ref)

    @property
    def repo(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        return self._NoneIfNotSet(self._repo)

    @property
    def sha(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._sha)

    @property
    def user(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        return self._NoneIfNotSet(self._user)

    def _initAttributes(self):
        self._label = github.GithubObject.NotSet
        self._ref = github.GithubObject.NotSet
        self._repo = github.GithubObject.NotSet
        self._sha = github.GithubObject.NotSet
        self._user = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "label" in attributes:  # pragma no branch
            assert attributes["label"] is None or isinstance(attributes["label"], (str, unicode)), attributes["label"]
            self._label = attributes["label"]
        if "ref" in attributes:  # pragma no branch
            assert attributes["ref"] is None or isinstance(attributes["ref"], (str, unicode)), attributes["ref"]
            self._ref = attributes["ref"]
        if "repo" in attributes:  # pragma no branch
            assert attributes["repo"] is None or isinstance(attributes["repo"], dict), attributes["repo"]
            self._repo = None if attributes["repo"] is None else github.Repository.Repository(self._requester, self._headers, attributes["repo"], completed=False)
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "user" in attributes:  # pragma no branch
            assert attributes["user"] is None or isinstance(attributes["user"], dict), attributes["user"]
            self._user = None if attributes["user"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["user"], completed=False)
