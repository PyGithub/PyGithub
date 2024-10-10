############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Eric Nieuwland <eric.nieuwland@gmail.com>                     #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CodeScanAlertInstanceLocation(NonCompletableGithubObject):
    """
    This class represents code scanning alert instance locations.

    The reference can be found here
    https://docs.github.com/en/rest/reference/code-scanning.

    """

    def _initAttributes(self) -> None:
        self._path: Attribute[str] = NotSet
        self._start_line: Attribute[int] = NotSet
        self._start_column: Attribute[int] = NotSet
        self._end_line: Attribute[int] = NotSet
        self._end_column: Attribute[int] = NotSet

    def __str__(self) -> str:
        return f"{self.path} @ l{self.start_line}:c{self.start_column}-l{self.end_line}:c{self.end_column}"

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "path": self.path,
                "start_line": self.start_line,
                "start_column": self.start_column,
                "end_line": self.end_line,
                "end_column": self.end_column,
            }
        )

    @property
    def path(self) -> str:
        return self._path.value

    @property
    def start_line(self) -> int:
        return self._start_line.value

    @property
    def start_column(self) -> int:
        return self._start_column.value

    @property
    def end_line(self) -> int:
        return self._end_line.value

    @property
    def end_column(self) -> int:
        return self._end_column.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
        if "start_line" in attributes:  # pragma no branch
            self._start_line = self._makeIntAttribute(attributes["start_line"])
        if "start_column" in attributes:  # pragma no branch
            self._start_column = self._makeIntAttribute(attributes["start_column"])
        if "end_line" in attributes:  # pragma no branch
            self._end_line = self._makeIntAttribute(attributes["end_line"])
        if "end_column" in attributes:  # pragma no branch
            self._end_column = self._makeIntAttribute(attributes["end_column"])
