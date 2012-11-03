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


class HookDescription(GithubObject.BasicGithubObject):
    @property
    def events(self):
        return self._NoneIfNotSet(self._events)

    @property
    def name(self):
        return self._NoneIfNotSet(self._name)

    @property
    def schema(self):
        return self._NoneIfNotSet(self._schema)

    @property
    def supported_events(self):
        return self._NoneIfNotSet(self._supported_events)

    def _initAttributes(self):
        self._events = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._schema = GithubObject.NotSet
        self._supported_events = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "events" in attributes:  # pragma no branch
            assert attributes["events"] is None or all(isinstance(element, (str, unicode)) for element in attributes["events"]), attributes["events"]
            self._events = attributes["events"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "schema" in attributes:  # pragma no branch
            assert attributes["schema"] is None or all(isinstance(element, list) for element in attributes["schema"]), attributes["schema"]
            self._schema = attributes["schema"]
        if "supported_events" in attributes:  # pragma no branch
            assert attributes["supported_events"] is None or all(isinstance(element, (str, unicode)) for element in attributes["supported_events"]), attributes["supported_events"]
            self._supported_events = attributes["supported_events"]
