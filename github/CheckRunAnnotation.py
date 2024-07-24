############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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


class CheckRunAnnotation(NonCompletableGithubObject):
    """
    This class represents check run annotations.

    The reference can be found here: https://docs.github.com/en/rest/reference/checks#list-check-run-annotations

    """

    def _initAttributes(self) -> None:
        self._annotation_level: Attribute[str] = NotSet
        self._end_column: Attribute[int] = NotSet
        self._end_line: Attribute[int] = NotSet
        self._message: Attribute[str] = NotSet
        self._path: Attribute[str] = NotSet
        self._raw_details: Attribute[str] = NotSet
        self._start_column: Attribute[int] = NotSet
        self._start_line: Attribute[int] = NotSet
        self._title: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"title": self._title.value})

    @property
    def annotation_level(self) -> str:
        return self._annotation_level.value

    @property
    def end_column(self) -> int:
        return self._end_column.value

    @property
    def end_line(self) -> int:
        return self._end_line.value

    @property
    def message(self) -> str:
        return self._message.value

    @property
    def path(self) -> str:
        return self._path.value

    @property
    def raw_details(self) -> str:
        return self._raw_details.value

    @property
    def start_column(self) -> int:
        return self._start_column.value

    @property
    def start_line(self) -> int:
        return self._start_line.value

    @property
    def title(self) -> str:
        return self._title.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "annotation_level" in attributes:  # pragma no branch
            self._annotation_level = self._makeStringAttribute(attributes["annotation_level"])
        if "end_column" in attributes:  # pragma no branch
            self._end_column = self._makeIntAttribute(attributes["end_column"])
        if "end_line" in attributes:  # pragma no branch
            self._end_line = self._makeIntAttribute(attributes["end_line"])
        if "message" in attributes:  # pragma no branch
            self._message = self._makeStringAttribute(attributes["message"])
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
        if "raw_details" in attributes:  # pragma no branch
            self._raw_details = self._makeStringAttribute(attributes["raw_details"])
        if "start_column" in attributes:  # pragma no branch
            self._start_column = self._makeIntAttribute(attributes["start_column"])
        if "start_line" in attributes:  # pragma no branch
            self._start_line = self._makeIntAttribute(attributes["start_line"])
        if "title" in attributes:  # pragma no branch
            self._title = self._makeStringAttribute(attributes["title"])
