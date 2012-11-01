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

import GitObject


class GitRef(GithubObject.GithubObject):
    @property
    def object(self):
        self._completeIfNotSet(self._object)
        return self._NoneIfNotSet(self._object)

    @property
    def ref(self):
        self._completeIfNotSet(self._ref)
        return self._NoneIfNotSet(self._ref)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def delete(self):
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def edit(self, sha, force=GithubObject.NotSet):
        assert isinstance(sha, (str, unicode)), sha
        assert force is GithubObject.NotSet or isinstance(force, bool), force
        post_parameters = {
            "sha": sha,
        }
        if force is not GithubObject.NotSet:
            post_parameters["force"] = force
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def _initAttributes(self):
        self._object = GithubObject.NotSet
        self._ref = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "object" in attributes:  # pragma no branch
            assert attributes["object"] is None or isinstance(attributes["object"], dict), attributes["object"]
            self._object = None if attributes["object"] is None else GitObject.GitObject(self._requester, attributes["object"], completed=False)
        if "ref" in attributes:  # pragma no branch
            assert attributes["ref"] is None or isinstance(attributes["ref"], (str, unicode)), attributes["ref"]
            self._ref = attributes["ref"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
