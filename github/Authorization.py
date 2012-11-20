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

import AuthorizationApplication


class Authorization(GithubObject.GithubObject):
    @property
    def app(self):
        self._completeIfNotSet(self._app)
        return self._NoneIfNotSet(self._app)

    @property
    def created_at(self):
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def id(self):
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def note(self):
        self._completeIfNotSet(self._note)
        return self._NoneIfNotSet(self._note)

    @property
    def note_url(self):
        self._completeIfNotSet(self._note_url)
        return self._NoneIfNotSet(self._note_url)

    @property
    def scopes(self):
        self._completeIfNotSet(self._scopes)
        return self._NoneIfNotSet(self._scopes)

    @property
    def token(self):
        self._completeIfNotSet(self._token)
        return self._NoneIfNotSet(self._token)

    @property
    def updated_at(self):
        self._completeIfNotSet(self._updated_at)
        return self._NoneIfNotSet(self._updated_at)

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

    def edit(self, scopes=GithubObject.NotSet, add_scopes=GithubObject.NotSet, remove_scopes=GithubObject.NotSet, note=GithubObject.NotSet, note_url=GithubObject.NotSet):
        assert scopes is GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in scopes), scopes
        assert add_scopes is GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in add_scopes), add_scopes
        assert remove_scopes is GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in remove_scopes), remove_scopes
        assert note is GithubObject.NotSet or isinstance(note, (str, unicode)), note
        assert note_url is GithubObject.NotSet or isinstance(note_url, (str, unicode)), note_url
        post_parameters = dict()
        if scopes is not GithubObject.NotSet:
            post_parameters["scopes"] = scopes
        if add_scopes is not GithubObject.NotSet:
            post_parameters["add_scopes"] = add_scopes
        if remove_scopes is not GithubObject.NotSet:
            post_parameters["remove_scopes"] = remove_scopes
        if note is not GithubObject.NotSet:
            post_parameters["note"] = note
        if note_url is not GithubObject.NotSet:
            post_parameters["note_url"] = note_url
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def _initAttributes(self):
        self._app = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._note = GithubObject.NotSet
        self._note_url = GithubObject.NotSet
        self._scopes = GithubObject.NotSet
        self._token = GithubObject.NotSet
        self._updated_at = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "app" in attributes:  # pragma no branch
            assert attributes["app"] is None or isinstance(attributes["app"], dict), attributes["app"]
            self._app = None if attributes["app"] is None else AuthorizationApplication.AuthorizationApplication(self._requester, attributes["app"], completed=False)
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "note" in attributes:  # pragma no branch
            assert attributes["note"] is None or isinstance(attributes["note"], (str, unicode)), attributes["note"]
            self._note = attributes["note"]
        if "note_url" in attributes:  # pragma no branch
            assert attributes["note_url"] is None or isinstance(attributes["note_url"], (str, unicode)), attributes["note_url"]
            self._note_url = attributes["note_url"]
        if "scopes" in attributes:  # pragma no branch
            assert attributes["scopes"] is None or all(isinstance(element, (str, unicode)) for element in attributes["scopes"]), attributes["scopes"]
            self._scopes = attributes["scopes"]
        if "token" in attributes:  # pragma no branch
            assert attributes["token"] is None or isinstance(attributes["token"], (str, unicode)), attributes["token"]
            self._token = attributes["token"]
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
