############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Matthew Davis <35502728+matt-davis27@users.noreply.github.com> #
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


class SecretScanAlertInstance(NonCompletableGithubObject):
    """
    This class represents secret scanning alert instances.

    The reference can be found here
    https://docs.github.com/en/rest/reference/secret-scanning.

    """

    def _initAttributes(self) -> None:
        self._blob_sha: Attribute[str] = NotSet
        self._blob_url: Attribute[str] = NotSet
        self._commit_sha: Attribute[str] = NotSet
        self._commit_url: Attribute[str] = NotSet
        self._end_column: Attribute[int] = NotSet
        self._end_line: Attribute[int] = NotSet
        self._path: Attribute[str] = NotSet
        self._start_column: Attribute[int] = NotSet
        self._start_line: Attribute[int] = NotSet

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

    def __str__(self) -> str:
        return f"{self.path} @ l{self.start_line}:c{self.start_column}-l{self.end_line}:c{self.end_column}"

    @property
    def blob_sha(self) -> str:
        return self._blob_sha.value

    @property
    def blob_url(self) -> str:
        return self._blob_url.value

    @property
    def commit_sha(self) -> str:
        return self._commit_sha.value

    @property
    def commit_url(self) -> str:
        return self._commit_url.value

    @property
    def end_column(self) -> int:
        return self._end_column.value

    @property
    def end_line(self) -> int:
        return self._end_line.value

    @property
    def path(self) -> str:
        return self._path.value

    @property
    def start_column(self) -> int:
        return self._start_column.value

    @property
    def start_line(self) -> int:
        return self._start_line.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "blob_sha" in attributes:
            self._blob_sha = self._makeStringAttribute(attributes["blob_sha"])
        if "blob_url" in attributes:
            self._blob_url = self._makeStringAttribute(attributes["blob_url"])
        if "commit_sha" in attributes:
            self._commit_sha = self._makeStringAttribute(attributes["commit_sha"])
        if "commit_url" in attributes:
            self._commit_url = self._makeStringAttribute(attributes["commit_url"])
        if "end_column" in attributes:
            self._end_column = self._makeIntAttribute(attributes["end_column"])
        if "end_line" in attributes:
            self._end_line = self._makeIntAttribute(attributes["end_line"])
        if "path" in attributes:
            self._path = self._makeStringAttribute(attributes["path"])
        if "start_column" in attributes:
            self._start_column = self._makeIntAttribute(attributes["start_column"])
        if "start_line" in attributes:
            self._start_line = self._makeIntAttribute(attributes["start_line"])
