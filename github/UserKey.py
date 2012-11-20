# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import GithubObject


class UserKey(GithubObject.GithubObject):
    @property
    def id(self):
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def key(self):
        self._completeIfNotSet(self._key)
        return self._NoneIfNotSet(self._key)

    @property
    def title(self):
        self._completeIfNotSet(self._title)
        return self._NoneIfNotSet(self._title)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def verified(self):
        self._completeIfNotSet(self._verified)
        return self._NoneIfNotSet(self._verified)

    def delete(self):
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def edit(self, title=GithubObject.NotSet, key=GithubObject.NotSet):
        assert title is GithubObject.NotSet or isinstance(title, (str, unicode)), title
        assert key is GithubObject.NotSet or isinstance(key, (str, unicode)), key
        post_parameters = dict()
        if title is not GithubObject.NotSet:
            post_parameters["title"] = title
        if key is not GithubObject.NotSet:
            post_parameters["key"] = key
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def _initAttributes(self):
        self._id = GithubObject.NotSet
        self._key = GithubObject.NotSet
        self._title = GithubObject.NotSet
        self._url = GithubObject.NotSet
        self._verified = GithubObject.NotSet

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
