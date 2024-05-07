############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
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
from typing import TYPE_CHECKING, Any

import github.AdvisoryVulnerabilityPackage
import github.DependabotAlertAdvisory
import github.DependabotAlertDependency
import github.DependabotAlertVulnerability
import github.NamedUser
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.DependabotAlertAdvisory import DependabotAlertAdvisory
    from github.DependabotAlertDependency import DependabotAlertDependency
    from github.DependabotAlertVulnerability import DependabotAlertVulnerability
    from github.NamedUser import NamedUser


class DependabotAlert(NonCompletableGithubObject):
    """
    This class represents a DependabotAlert.

    The reference can be found here
    https://docs.github.com/en/rest/dependabot/alerts

    """

    def _initAttributes(self) -> None:
        self._number: Attribute[int] = NotSet
        self._state: Attribute[str] = NotSet
        self._dependency: Attribute[DependabotAlertDependency] = NotSet
        self._security_advisory: Attribute[DependabotAlertAdvisory] = NotSet
        self._security_vulnerability: Attribute[DependabotAlertVulnerability] = NotSet
        self._url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._dismissed_at: Attribute[datetime | None] = NotSet
        self._dismissed_by: Attribute[NamedUser | None] = NotSet
        self._dismissed_reason: Attribute[str | None] = NotSet
        self._dismissed_comment: Attribute[str | None] = NotSet
        self._fixed_at: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self.number, "ghsa_id": self.security_advisory.ghsa_id})

    @property
    def number(self) -> int:
        return self._number.value

    @property
    def state(self) -> str:
        return self._state.value

    @property
    def dependency(self) -> DependabotAlertDependency:
        return self._dependency.value

    @property
    def security_advisory(self) -> DependabotAlertAdvisory:
        return self._security_advisory.value

    @property
    def security_vulnerability(self) -> DependabotAlertVulnerability:
        return self._security_vulnerability.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def dismissed_at(self) -> datetime | None:
        return self._dismissed_at.value

    @property
    def dismissed_by(self) -> NamedUser | None:
        return self._dismissed_by.value

    @property
    def dismissed_reason(self) -> str | None:
        return self._dismissed_reason.value

    @property
    def dismissed_comment(self) -> str | None:
        return self._dismissed_comment.value

    @property
    def fixed_at(self) -> str | None:
        return self._fixed_at.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "number" in attributes:
            self._number = self._makeIntAttribute(attributes["number"])
        if "state" in attributes:
            self._state = self._makeStringAttribute(attributes["state"])
        if "dependency" in attributes:
            self._dependency = self._makeClassAttribute(
                github.DependabotAlertDependency.DependabotAlertDependency, attributes["dependency"]
            )
        if "security_advisory" in attributes:
            self._security_advisory = self._makeClassAttribute(
                github.DependabotAlertAdvisory.DependabotAlertAdvisory, attributes["security_advisory"]
            )
        if "security_vulnerability" in attributes:
            self._security_vulnerability = self._makeClassAttribute(
                github.DependabotAlertVulnerability.DependabotAlertVulnerability, attributes["security_vulnerability"]
            )
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
        if "html_url" in attributes:
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "dismissed_at" in attributes:
            self._dismissed_at = self._makeDatetimeAttribute(attributes["dismissed_at"])
        if "dismissed_by" in attributes:
            self._dismissed_by = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["dismissed_by"])
        if "dismissed_reason" in attributes:
            self._dismissed_reason = self._makeStringAttribute(attributes["dismissed_reason"])
        if "dismissed_comment" in attributes:
            self._dismissed_comment = self._makeStringAttribute(attributes["dismissed_comment"])
        if "fixed_at" in attributes:
            self._fixed_at = self._makeStringAttribute(attributes["fixed_at"])
