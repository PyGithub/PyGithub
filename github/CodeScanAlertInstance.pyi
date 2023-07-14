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

from __future__ import annotations

from typing import Any, Dict

import github.CodeScanAlertInstanceLocation
import github.GithubObject

class CodeScanAlertInstance(github.GithubObject.NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    @property
    def ref(self) -> str: ...
    @property
    def analysis_key(self) -> str: ...
    @property
    def environment(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def commit_sha(self) -> str: ...
    @property
    def message(self) -> str: ...
    @property
    def location(
        self,
    ) -> github.CodeScanAlertInstanceLocation.CodeScanAlertInstanceLocation: ...
    @property
    def classifications(self) -> list[str]: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
