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


class HookResponse(GithubObject.BasicGithubObject):
    @property
    def code(self):
        return self._NoneIfNotSet(self._code)

    @property
    def message(self):
        return self._NoneIfNotSet(self._message)

    @property
    def status(self):
        return self._NoneIfNotSet(self._status)

    def _initAttributes(self):
        self._code = GithubObject.NotSet
        self._message = GithubObject.NotSet
        self._status = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "code" in attributes:  # pragma no branch
            assert attributes["code"] is None or isinstance(attributes["code"], (int, long)), attributes["code"]
            self._code = attributes["code"]
        if "message" in attributes:  # pragma no branch
            assert attributes["message"] is None or isinstance(attributes["message"], (str, unicode)), attributes["message"]
            self._message = attributes["message"]
        if "status" in attributes:  # pragma no branch
            assert attributes["status"] is None or isinstance(attributes["status"], (str, unicode)), attributes["status"]
            self._status = attributes["status"]
