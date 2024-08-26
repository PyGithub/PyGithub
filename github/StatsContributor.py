############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
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

from datetime import datetime
from typing import Any

import github.GithubObject
import github.NamedUser
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class StatsContributor(NonCompletableGithubObject):
    """
    This class represents StatsContributors.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#get-all-contributor-commit-activity

    """

    class Week(NonCompletableGithubObject):
        """
        This class represents weekly statistics of a contributor.
        """

        @property
        def w(self) -> datetime:
            return self._w.value

        @property
        def a(self) -> int:
            return self._a.value

        @property
        def d(self) -> int:
            return self._d.value

        @property
        def c(self) -> int:
            return self._c.value

        def _initAttributes(self) -> None:
            self._w: Attribute[datetime] = NotSet
            self._a: Attribute[int] = NotSet
            self._d: Attribute[int] = NotSet
            self._c: Attribute[int] = NotSet

        def _useAttributes(self, attributes: dict[str, Any]) -> None:
            if "w" in attributes:  # pragma no branch
                self._w = self._makeTimestampAttribute(attributes["w"])
            if "a" in attributes:  # pragma no branch
                self._a = self._makeIntAttribute(attributes["a"])
            if "d" in attributes:  # pragma no branch
                self._d = self._makeIntAttribute(attributes["d"])
            if "c" in attributes:  # pragma no branch
                self._c = self._makeIntAttribute(attributes["c"])

    @property
    def author(self) -> github.NamedUser.NamedUser:
        return self._author.value

    @property
    def total(self) -> int:
        return self._total.value

    @property
    def weeks(self) -> list[Week]:
        return self._weeks.value

    def _initAttributes(self) -> None:
        self._author: Attribute[github.NamedUser.NamedUser] = NotSet
        self._total: Attribute[int] = NotSet
        self._weeks: Attribute[list[StatsContributor.Week]] = NotSet

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "author" in attributes:  # pragma no branch
            self._author = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["author"])
        if "total" in attributes:  # pragma no branch
            self._total = self._makeIntAttribute(attributes["total"])
        if "weeks" in attributes:  # pragma no branch
            self._weeks = self._makeListOfClassesAttribute(self.Week, attributes["weeks"])
