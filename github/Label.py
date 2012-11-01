# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import urllib

import GithubObject


class Label(GithubObject.GithubObject):
    @property
    def color(self):
        self._completeIfNotSet(self._color)
        return self._NoneIfNotSet(self._color)

    @property
    def name(self):
        self._completeIfNotSet(self._name)
        return self._NoneIfNotSet(self._name)

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

    def edit(self, name, color):
        assert isinstance(name, (str, unicode)), name
        assert isinstance(color, (str, unicode)), color
        post_parameters = {
            "name": name,
            "color": color,
        }
        headers, data = self._requester.requestAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    @property
    def _identity(self):
        return urllib.quote(self.name)

    def _initAttributes(self):
        self._color = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "color" in attributes:  # pragma no branch
            assert attributes["color"] is None or isinstance(attributes["color"], (str, unicode)), attributes["color"]
            self._color = attributes["color"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
