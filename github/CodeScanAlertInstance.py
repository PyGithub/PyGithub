############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Eric Nieuwland <eric.nieuwland@gmail.com>                     #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

from typing import TYPE_CHECKING, Any

import github.CodeScanAlertInstanceLocation
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.CodeScanAlertInstanceLocation import CodeScanAlertInstanceLocation


class CodeScanAlertInstance(NonCompletableGithubObject):
    """
    This class represents code scanning alert instances.

    The reference can be found here
    https://docs.github.com/en/rest/reference/code-scanning.

    """

    def _initAttributes(self) -> None:
        self._analysis_key: Attribute[str] = NotSet
        self._classifications: Attribute[list[str]] = NotSet
        self._commit_sha: Attribute[str] = NotSet
        self._environment: Attribute[str] = NotSet
        self._location: Attribute[CodeScanAlertInstanceLocation] = NotSet
        self._message: Attribute[dict[str, Any]] = NotSet
        self._ref: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"ref": self.ref, "analysis_key": self.analysis_key})

    @property
    def analysis_key(self) -> str:
        return self._analysis_key.value

    @property
    def classifications(self) -> list[str]:
        return self._classifications.value

    @property
    def commit_sha(self) -> str:
        return self._commit_sha.value

    @property
    def environment(self) -> str:
        return self._environment.value

    @property
    def location(self) -> CodeScanAlertInstanceLocation:
        return self._location.value

    @property
    def message(self) -> dict[str, Any]:
        return self._message.value

    @property
    def ref(self) -> str:
        return self._ref.value

    @property
    def state(self) -> str:
        return self._state.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "analysis_key" in attributes:  # pragma no branch
            self._analysis_key = self._makeStringAttribute(attributes["analysis_key"])
        if "classifications" in attributes:  # pragma no branch
            self._classifications = self._makeListOfStringsAttribute(attributes["classifications"])
        if "commit_sha" in attributes:  # pragma no branch
            self._commit_sha = self._makeStringAttribute(attributes["commit_sha"])
        if "environment" in attributes:  # pragma no branch
            self._environment = self._makeStringAttribute(attributes["environment"])
        if "environment" in attributes:  # pragma no branch
            self._environment = self._makeStringAttribute(attributes["environment"])
        if "location" in attributes:  # pragma no branch
            self._location = self._makeClassAttribute(
                github.CodeScanAlertInstanceLocation.CodeScanAlertInstanceLocation,
                attributes["location"],
            )
        if "message" in attributes:  # pragma no branch
            self._message = self._makeDictAttribute(attributes["message"])
        if "ref" in attributes:  # pragma no branch
            self._ref = self._makeStringAttribute(attributes["ref"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
