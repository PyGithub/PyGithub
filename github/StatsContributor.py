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

from datetime import datetime
from typing import TYPE_CHECKING

import github.GithubObject
import github.NamedUser
from github.GithubObject import Attribute

if TYPE_CHECKING:
    from github.NamedUser import NamedUser


class Week(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents weekly statistics of a contributor.
    """

    @property
    def w(self) -> datetime:
        """
        :type: datetime.datetime
        """
        return self._w.value

    @property
    def a(self) -> int:
        """
        :type: int
        """
        return self._a.value

    @property
    def d(self) -> int:
        """
        :type: int
        """
        return self._d.value

    @property
    def c(self) -> int:
        """
        :type: int
        """
        return self._c.value

    def _initAttributes(self) -> None:
        self._w: Attribute[datetime] = github.GithubObject.NotSet
        self._a: Attribute[int] = github.GithubObject.NotSet
        self._d: Attribute[int] = github.GithubObject.NotSet
        self._c: Attribute[int] = github.GithubObject.NotSet

    def _useAttributes(self, attributes) -> None:
        if "w" in attributes:  # pragma no branch
            self._w = self._makeTimestampAttribute(attributes["w"])
        if "a" in attributes:  # pragma no branch
            self._a = self._makeIntAttribute(attributes["a"])
        if "d" in attributes:  # pragma no branch
            self._d = self._makeIntAttribute(attributes["d"])
        if "c" in attributes:  # pragma no branch
            self._c = self._makeIntAttribute(attributes["c"])


class StatsContributor(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents StatsContributors. The reference can be found here https://docs.github.com/en/rest/reference/repos#get-all-contributor-commit-activity
    """

    Week: type[Week] = Week

    @property
    def author(self) -> NamedUser:
        return self._author.value

    @property
    def total(self) -> int:
        return self._total.value

    @property
    def weeks(self) -> list[Week]:
        return self._weeks.value

    def _initAttributes(self) -> None:
        self._author: Attribute[NamedUser] = github.GithubObject.NotSet
        self._total: Attribute[int] = github.GithubObject.NotSet
        self._weeks: Attribute[list[Week]] = github.GithubObject.NotSet

    def _useAttributes(self, attributes) -> None:
        if "author" in attributes:  # pragma no branch
            self._author = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["author"]
            )
        if "total" in attributes:  # pragma no branch
            self._total = self._makeIntAttribute(attributes["total"])
        if "weeks" in attributes:  # pragma no branch
            self._weeks = self._makeListOfClassesAttribute(
                self.Week, attributes["weeks"]
            )
