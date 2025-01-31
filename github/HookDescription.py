############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
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

from __future__ import annotations

from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class HookDescription(NonCompletableGithubObject):
    """
    This class represents HookDescriptions.
    """

    def _initAttributes(self) -> None:
        self._events: Attribute[list[str]] = NotSet
        self._name: Attribute[str] = NotSet
        self._schema: Attribute[list[list[str]]] = NotSet
        self._supported_events: Attribute[list[str]] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def events(self) -> list[str]:
        return self._events.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def schema(self) -> list[list[str]]:
        return self._schema.value

    @property
    def supported_events(self) -> list[str]:
        return self._supported_events.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "events" in attributes:  # pragma no branch
            self._events = self._makeListOfStringsAttribute(attributes["events"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "schema" in attributes:  # pragma no branch
            self._schema = self._makeListOfListOfStringsAttribute(attributes["schema"])
        if "supported_events" in attributes:  # pragma no branch
            self._supported_events = self._makeListOfStringsAttribute(attributes["supported_events"])
