############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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


class StatsParticipation(NonCompletableGithubObject):
    """
    This class represents StatsParticipations. The reference can be found here https://docs.github.com/en/rest/reference/repos#get-the-weekly-commit-count
    """

    def _initAttributes(self) -> None:
        self._all: Attribute[list[int]] = NotSet
        self._owner: Attribute[list[int]] = NotSet

    @property
    def all(self) -> list[int]:
        return self._all.value

    @property
    def owner(self) -> list[int]:
        return self._owner.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "all" in attributes:  # pragma no branch
            self._all = self._makeListOfIntsAttribute(attributes["all"])
        if "owner" in attributes:  # pragma no branch
            self._owner = self._makeListOfIntsAttribute(attributes["owner"])
