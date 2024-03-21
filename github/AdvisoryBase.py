############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Joseph Henrich <crimsonknave@gmail.com>                       #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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
from typing import Any

from github.CVSS import CVSS
from github.CWE import CWE
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class AdvisoryBase(NonCompletableGithubObject):
    """
    This class represents a the shared attributes between GlobalAdvisory, RepositoryAdvisory and DependabotAdvisory
    https://docs.github.com/en/rest/security-advisories/global-advisories
    https://docs.github.com/en/rest/security-advisories/repository-advisories
    https://docs.github.com/en/rest/dependabot/alerts
    """

    def _initAttributes(self) -> None:
        self._cve_id: Attribute[str] = NotSet
        self._cvss: Attribute[CVSS] = NotSet
        self._cwes: Attribute[list[CWE]] = NotSet
        self._description: Attribute[str] = NotSet
        self._ghsa_id: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._identifiers: Attribute[list[dict]] = NotSet
        self._published_at: Attribute[datetime] = NotSet
        self._severity: Attribute[str] = NotSet
        self._summary: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._withdrawn_at: Attribute[datetime] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"ghsa_id": self.ghsa_id, "summary": self.summary})

    @property
    def cve_id(self) -> str:
        return self._cve_id.value

    @property
    def cvss(self) -> CVSS:
        return self._cvss.value

    @property
    def cwes(self) -> list[CWE]:
        return self._cwes.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def ghsa_id(self) -> str:
        return self._ghsa_id.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def identifiers(self) -> list[dict]:
        return self._identifiers.value

    @property
    def published_at(self) -> datetime:
        return self._published_at.value

    @property
    def severity(self) -> str:
        return self._severity.value

    @property
    def summary(self) -> str:
        return self._summary.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def withdrawn_at(self) -> datetime:
        return self._withdrawn_at.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "cve_id" in attributes:  # pragma no branch
            self._cve_id = self._makeStringAttribute(attributes["cve_id"])
        if "cvss" in attributes:  # pragma no branch
            self._cvss = self._makeClassAttribute(CVSS, attributes["cvss"])
        if "cwes" in attributes:  # pragma no branch
            self._cwes = self._makeListOfClassesAttribute(CWE, attributes["cwes"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "ghsa_id" in attributes:  # pragma no branch
            self._ghsa_id = self._makeStringAttribute(attributes["ghsa_id"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "identifiers" in attributes:  # pragma no branch
            self._identifiers = self._makeListOfDictsAttribute(attributes["identifiers"])
        if "published_at" in attributes:  # pragma no branch
            assert attributes["published_at"] is None or isinstance(attributes["published_at"], str), attributes[
                "published_at"
            ]
            self._published_at = self._makeDatetimeAttribute(attributes["published_at"])
        if "severity" in attributes:  # pragma no branch
            self._severity = self._makeStringAttribute(attributes["severity"])
        if "summary" in attributes:  # pragma no branch
            self._summary = self._makeStringAttribute(attributes["summary"])
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], str), attributes[
                "updated_at"
            ]
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "withdrawn_at" in attributes:  # pragma no branch
            assert attributes["withdrawn_at"] is None or isinstance(attributes["withdrawn_at"], str), attributes[
                "withdrawn_at"
            ]
            self._withdrawn_at = self._makeDatetimeAttribute(attributes["withdrawn_at"])
