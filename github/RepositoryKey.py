# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques vincent@vincent-jacques.net
# Copyright 2012 Zearin zearin@gonk.net
# Copyright 2013 Vincent Jacques vincent@vincent-jacques.net

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import github.GithubObject


class RepositoryKey(github.GithubObject.CompletableGithubObject):
    """
    This class represents RepositoryKeys as returned for example by http://developer.github.com/v3/keys
    """

    def __init__(self, requester, attributes, completed, repoUrl):
        github.GithubObject.CompletableGithubObject.__init__(self, requester, attributes, completed)
        self.__repoUrl = repoUrl

    @property
    def __customUrl(self):
        return self.__repoUrl + "/keys/" + str(self.id)

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def key(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._key)
        return self._NoneIfNotSet(self._key)

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
    def verified(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._verified)
        return self._NoneIfNotSet(self._verified)

    def delete(self):
        """
        :calls: `DELETE /repos/:user/:repo/keys/:id <http://developer.github.com/v3/keys>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.__customUrl,
            None,
            None
        )

    def edit(self, title=github.GithubObject.NotSet, key=github.GithubObject.NotSet):
        """
        :calls: `PATCH /repos/:user/:repo/keys/:id <http://developer.github.com/v3/keys>`_
        :param title: string
        :param key: string
        :rtype: None
        """
        assert title is github.GithubObject.NotSet or isinstance(title, (str, unicode)), title
        assert key is github.GithubObject.NotSet or isinstance(key, (str, unicode)), key
        post_parameters = dict()
        if title is not github.GithubObject.NotSet:
            post_parameters["title"] = title
        if key is not github.GithubObject.NotSet:
            post_parameters["key"] = key
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.__customUrl,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._key = github.GithubObject.NotSet
        self._title = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._verified = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "key" in attributes:  # pragma no branch
            assert attributes["key"] is None or isinstance(attributes["key"], (str, unicode)), attributes["key"]
            self._key = attributes["key"]
        if "title" in attributes:  # pragma no branch
            assert attributes["title"] is None or isinstance(attributes["title"], (str, unicode)), attributes["title"]
            self._title = attributes["title"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
        if "verified" in attributes:  # pragma no branch
            assert attributes["verified"] is None or isinstance(attributes["verified"], bool), attributes["verified"]
            self._verified = attributes["verified"]
