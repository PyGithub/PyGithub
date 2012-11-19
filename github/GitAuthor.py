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


class GitAuthor(GithubObject.BasicGithubObject):
    @property
    def date(self):
        return self._NoneIfNotSet(self._date)

    @property
    def email(self):
        return self._NoneIfNotSet(self._email)

    @property
    def name(self):
        return self._NoneIfNotSet(self._name)

    def _initAttributes(self):
        self._date = GithubObject.NotSet
        self._email = GithubObject.NotSet
        self._name = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "date" in attributes:  # pragma no branch
            assert attributes["date"] is None or isinstance(attributes["date"], (str, unicode)), attributes["date"]
            self._date = self._parseDatetime(attributes["date"])
        if "email" in attributes:  # pragma no branch
            assert attributes["email"] is None or isinstance(attributes["email"], (str, unicode)), attributes["email"]
            self._email = attributes["email"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
