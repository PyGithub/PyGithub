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

from datetime import datetime
from typing import Any, Dict

import github.DependabotAlertDependency
import github.DependabotAlertSecurityAdvisory
import github.DependabotAlertSecurityVulnerability
import github.GithubObject
import github.PaginatedList


class CodeScanAlert(github.GithubObject.NonCompletableGithubObject):
    def __repr__(self) -> str: ...

    @property
    def number(self) -> int: ...

    @property
    def state(self) -> str: ...

    @property
    def created_at(self) -> datetime: ...

    @property
    def updated_at(self) -> datetime: ...

    @property
    def fixed_at(self) -> datetime: ...

    @property
    def dismissed_at(self) -> datetime: ...

    @property
    def dismissed_by(self) -> dict: ...

    @property
    def dismissed_reason(self) -> str: ...

    @property
    def dismissed_comment(self) -> str: ...

    @property
    def url(self) -> str: ...

    @property
    def html_url(self) -> str: ...

    @property
    def dependency(
            self,
    ) -> github.DependabotAlertDependency.DependabotAlertDependency: ...

    @property
    def security_advisory(
            self,
    ) -> github.DependabotAlertSecurityAdvisory.DependabotAlertSecurityAdvisory: ...

    @property
    def security_vulnerability(
            self,
    ) -> github.DependabotAlertSecurityVulnerability.DependabotAlertSecurityVulnerability: ...

    def get_instances(self) -> github.PaginatedList.PaginatedList: ...

    def _initAttributes(self) -> None: ...

    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
