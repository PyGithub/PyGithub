############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Eric Nieuwland <eric.nieuwland@gmail.com>                     #
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

import github.DependabotAlertDependencyPackage
import github.GithubObject
import github.PaginatedList


class DependabotAlertDependency(github.GithubObject.NonCompletableGithubObject):
    def __repr__(self) -> str: ...

    @property
    def manifest_path(self) -> str: ...

    @property
    def scope(self) -> str: ...

    @property
    def package(
            self,
    ) -> github.DependabotAlertDependencyPackage.DependabotAlertDependencyPackage: ...

    def _initAttributes(self) -> None: ...

    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
