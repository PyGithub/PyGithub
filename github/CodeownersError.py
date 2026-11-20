############################ Copyrights and license ############################
#                                                                              #
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


class CodeownersError(NonCompletableGithubObject):
    """
    This class represents a syntax error detected in the CODEOWNERS file of a repository.

    The reference can be found here
    https://docs.github.com/en/rest/repos/repos#list-codeowners-errors

    The OpenAPI schema can be found at

    - /components/schemas/codeowners-errors/properties/errors/items

    """

    def _initAttributes(self) -> None:
        self._column: Attribute[int] = NotSet
        self._kind: Attribute[str] = NotSet
        self._line: Attribute[int] = NotSet
        self._message: Attribute[str] = NotSet
        self._path: Attribute[str] = NotSet
        self._source: Attribute[str] = NotSet
        self._suggestion: Attribute[str | None] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"path": self._path.value, "line": self._line.value, "kind": self._kind.value})

    @property
    def column(self) -> int:
        return self._column.value

    @property
    def kind(self) -> str:
        return self._kind.value

    @property
    def line(self) -> int:
        return self._line.value

    @property
    def message(self) -> str:
        return self._message.value

    @property
    def path(self) -> str:
        return self._path.value

    @property
    def source(self) -> str:
        return self._source.value

    @property
    def suggestion(self) -> str | None:
        return self._suggestion.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "column" in attributes:  # pragma no branch
            self._column = self._makeIntAttribute(attributes["column"])
        if "kind" in attributes:  # pragma no branch
            self._kind = self._makeStringAttribute(attributes["kind"])
        if "line" in attributes:  # pragma no branch
            self._line = self._makeIntAttribute(attributes["line"])
        if "message" in attributes:  # pragma no branch
            self._message = self._makeStringAttribute(attributes["message"])
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
        if "source" in attributes:  # pragma no branch
            self._source = self._makeStringAttribute(attributes["source"])
        if "suggestion" in attributes:  # pragma no branch
            self._suggestion = self._makeStringAttribute(attributes["suggestion"])
