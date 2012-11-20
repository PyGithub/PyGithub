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

import NamedUser


class PullRequestComment(GithubObject.GithubObject):
    @property
    def body(self):
        self._completeIfNotSet(self._body)
        return self._NoneIfNotSet(self._body)

    @property
    def commit_id(self):
        self._completeIfNotSet(self._commit_id)
        return self._NoneIfNotSet(self._commit_id)

    @property
    def created_at(self):
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def id(self):
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def original_commit_id(self):
        self._completeIfNotSet(self._original_commit_id)
        return self._NoneIfNotSet(self._original_commit_id)

    @property
    def original_position(self):
        self._completeIfNotSet(self._original_position)
        return self._NoneIfNotSet(self._original_position)

    @property
    def path(self):
        self._completeIfNotSet(self._path)
        return self._NoneIfNotSet(self._path)

    @property
    def position(self):
        self._completeIfNotSet(self._position)
        return self._NoneIfNotSet(self._position)

    @property
    def updated_at(self):
        self._completeIfNotSet(self._updated_at)
        return self._NoneIfNotSet(self._updated_at)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def user(self):
        self._completeIfNotSet(self._user)
        return self._NoneIfNotSet(self._user)

    def delete(self):
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def edit(self, body):
        assert isinstance(body, (str, unicode)), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def _initAttributes(self):
        self._body = GithubObject.NotSet
        self._commit_id = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._original_commit_id = GithubObject.NotSet
        self._original_position = GithubObject.NotSet
        self._path = GithubObject.NotSet
        self._position = GithubObject.NotSet
        self._updated_at = GithubObject.NotSet
        self._url = GithubObject.NotSet
        self._user = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "body" in attributes:  # pragma no branch
            assert attributes["body"] is None or isinstance(attributes["body"], (str, unicode)), attributes["body"]
            self._body = attributes["body"]
        if "commit_id" in attributes:  # pragma no branch
            assert attributes["commit_id"] is None or isinstance(attributes["commit_id"], (str, unicode)), attributes["commit_id"]
            self._commit_id = attributes["commit_id"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "original_commit_id" in attributes:  # pragma no branch
            assert attributes["original_commit_id"] is None or isinstance(attributes["original_commit_id"], (str, unicode)), attributes["original_commit_id"]
            self._original_commit_id = attributes["original_commit_id"]
        if "original_position" in attributes:  # pragma no branch
            assert attributes["original_position"] is None or isinstance(attributes["original_position"], (int, long)), attributes["original_position"]
            self._original_position = attributes["original_position"]
        if "path" in attributes:  # pragma no branch
            assert attributes["path"] is None or isinstance(attributes["path"], (str, unicode)), attributes["path"]
            self._path = attributes["path"]
        if "position" in attributes:  # pragma no branch
            assert attributes["position"] is None or isinstance(attributes["position"], (int, long)), attributes["position"]
            self._position = attributes["position"]
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
        if "user" in attributes:  # pragma no branch
            assert attributes["user"] is None or isinstance(attributes["user"], dict), attributes["user"]
            self._user = None if attributes["user"] is None else NamedUser.NamedUser(self._requester, attributes["user"], completed=False)
