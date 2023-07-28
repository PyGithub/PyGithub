from __future__ import annotations

from datetime import datetime
from typing import Any

from github.AdvisoryVulnerability import AdvisoryVulnerability
from github.CVSS import CVSS
from github.CWE import CWE
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class AdvisoryBase(NonCompletableGithubObject):
    """
    This class represents a the shared attributes between GlobalAdvisory and RepositoryAdvisory
    https://docs.github.com/en/rest/security-advisories/global-advisories
    https://docs.github.com/en/rest/security-advisories/repository-advisories
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
        self._vulnerabilities: Attribute[list[AdvisoryVulnerability]] = NotSet
        self._withdrawn_at: Attribute[datetime] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"ghsa_id": self.ghsa_id, "summary": self.summary})

    @property
    def cve_id(self) -> str:
        return self._cve_id.value

    @property
    def cvss(self) -> str:
        return self._cvss.value

    @property
    def cwes(self) -> list[CWE]:
        return self._cwes.value

    @property
    def closed_at(self) -> datetime:
        return self._closed_at.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

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
    def identifiers(self) -> str:
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
    def vulnerabilities(self) -> list[AdvisoryVulnerability]:
        return self._vulnerabilities.value

    @property
    def withdrawn_at(self) -> datetime:
        return self._withdrawn_at.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "cve_id" in attributes:  # pragma no branch
            self._cve_id = self._makeStringAttribute(attributes["cve_id"])
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
        if "vulnerabilities" in attributes:  # pragma no branch
            self._vulnerabilities = self._makeListOfClassesAttribute(
                AdvisoryVulnerability,
                attributes["vulnerabilities"],
            )
        if "withdrawn_at" in attributes:  # pragma no branch
            assert attributes["withdrawn_at"] is None or isinstance(attributes["withdrawn_at"], str), attributes[
                "withdrawn_at"
            ]
            self._withdrawn_at = self._makeDatetimeAttribute(attributes["withdrawn_at"])
