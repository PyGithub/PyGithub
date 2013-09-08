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

import github.GitObject


class GitRef(github.GithubObject.CompletableGithubObject):
    """
    This class represents GitRefs as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def object(self):
        """
        :type: :class:`github.GitObject.GitObject`
        """
        self._completeIfNotSet(self._object)
        return self._NoneIfNotSet(self._object)

    @property
    def ref(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._ref)
        return self._NoneIfNotSet(self._ref)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def delete(self):
        """
        :calls: `DELETE /repos/:owner/:repo/git/refs/:ref <http://developer.github.com/v3/git/refs>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url
        )

    def edit(self, sha, force=github.GithubObject.NotSet):
        """
        :calls: `PATCH /repos/:owner/:repo/git/refs/:ref <http://developer.github.com/v3/git/refs>`_
        :param sha: string
        :param force: bool
        :rtype: None
        """
        assert isinstance(sha, (str, unicode)), sha
        assert force is github.GithubObject.NotSet or isinstance(force, bool), force
        post_parameters = {
            "sha": sha,
        }
        if force is not github.GithubObject.NotSet:
            post_parameters["force"] = force
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        self._useAttributes(data)

    def _initAttributes(self):
        self._object = github.GithubObject.NotSet
        self._ref = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "object" in attributes:  # pragma no branch
            assert attributes["object"] is None or isinstance(attributes["object"], dict), attributes["object"]
            self._object = None if attributes["object"] is None else github.GitObject.GitObject(self._requester, self._headers, attributes["object"], completed=False)
        if "ref" in attributes:  # pragma no branch
            assert attributes["ref"] is None or isinstance(attributes["ref"], (str, unicode)), attributes["ref"]
            self._ref = attributes["ref"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
