############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
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

import github.Repository
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.Repository import Repository


class RepositoryPreferences(NonCompletableGithubObject):
    """
    This class represents repository preferences.
    The reference can be found here https://docs.github.com/en/free-pro-team@latest/rest/reference/checks#update-repository-preferences-for-check-suites
    """

    def _initAttributes(self) -> None:
        self._preferences: Attribute[dict[str, list[dict[str, bool | int]]]] = NotSet
        self._repository: Attribute[Repository] = NotSet

    @property
    def preferences(self) -> dict[str, list[dict[str, bool | int]]]:
        return self._preferences.value

    @property
    def repository(self) -> Repository:
        return self._repository.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "preferences" in attributes:  # pragma no branch
            self._preferences = self._makeDictAttribute(attributes["preferences"])
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
