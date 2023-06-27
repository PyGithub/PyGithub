############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Victor Zeng <zacker150@hotmail.com>                           #
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

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class SelfHostedActionsRunner(NonCompletableGithubObject):
    """
    This class represents Self-hosted GitHub Actions Runners. The reference can be found at
    https://docs.github.com/en/free-pro-team@latest/rest/reference/actions#self-hosted-runners
    """

    def __repr__(self):
        return self.get__repr__({"name": self._name.value})

    _id: Attribute[int]
    _name: Attribute[str]
    _os: Attribute[str]
    _status: Attribute[str]
    _busy: Attribute[bool]
    _labels: Attribute[list[dict[str, int | str]]]

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def os(self) -> str:
        return self._os.value

    @property
    def status(self) -> str:
        return self._status.value

    @property
    def busy(self) -> bool:
        return self._busy.value

    def labels(self) -> list[dict[str, int | str]]:
        return self._labels.value

    def _initAttributes(self):
        self._id = NotSet
        self._name = NotSet
        self._os = NotSet
        self._status = NotSet
        self._busy = NotSet
        self._labels = []

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "os" in attributes:  # pragma no branch
            self._os = self._makeStringAttribute(attributes["os"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
        if "busy" in attributes:
            self._busy = self._makeBoolAttribute(attributes["busy"])
        if "labels" in attributes:
            self._labels = self._makeListOfDictsAttribute(attributes["labels"])
