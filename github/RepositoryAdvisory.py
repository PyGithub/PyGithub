############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Jonathan Leitschuh <Jonathan.Leitschuh@gmail.com>             #
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
from typing import TYPE_CHECKING, Any, Iterable

import github.NamedUser
from github.CWE import CWE
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet, Opt
from github.RepositoryAdvisoryCredit import Credit, RepositoryAdvisoryCredit
from github.RepositoryAdvisoryCreditDetailed import RepositoryAdvisoryCreditDetailed
from github.RepositoryAdvisoryVulnerability import AdvisoryVulnerability, RepositoryAdvisoryVulnerability

if TYPE_CHECKING:
    from github.NamedUser import NamedUser


class RepositoryAdvisory(NonCompletableGithubObject):
    """
    This class represents a RepositoryAdvisory.
    The reference can be found here https://docs.github.com/en/rest/security-advisories/repository-advisories
    """

    def _initAttributes(self) -> None:
        self._author: Attribute[NamedUser] = NotSet
        self._closed_at: Attribute[datetime] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._credits: Attribute[list[RepositoryAdvisoryCredit]] = NotSet
        self._credits_detailed: Attribute[list[RepositoryAdvisoryCreditDetailed]] = NotSet
        self._cve_id: Attribute[str] = NotSet
        self._cwe_ids: Attribute[list[str]] = NotSet
        self._cwes: Attribute[list[CWE]] = NotSet
        self._description: Attribute[str] = NotSet
        self._ghsa_id: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._published_at: Attribute[datetime] = NotSet
        self._severity: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._summary: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._vulnerabilities: Attribute[list[RepositoryAdvisoryVulnerability]] = NotSet
        self._withdrawn_at: Attribute[datetime] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"ghsa_id": self.ghsa_id, "summary": self.summary})

    @property
    def author(self) -> NamedUser:
        return self._author.value

    @property
    def closed_at(self) -> datetime:
        return self._closed_at.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def credits(
        self,
    ) -> list[RepositoryAdvisoryCredit]:
        return self._credits.value

    @property
    def credits_detailed(
        self,
    ) -> list[RepositoryAdvisoryCreditDetailed]:
        return self._credits_detailed.value

    @property
    def cve_id(self) -> str:
        return self._cve_id.value

    @property
    def cwe_ids(self) -> list[str]:
        return self._cwe_ids.value

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
    def published_at(self) -> datetime:
        return self._published_at.value

    @property
    def severity(self) -> str:
        return self._severity.value

    @property
    def state(self) -> str:
        return self._state.value

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
    def vulnerabilities(self) -> list[RepositoryAdvisoryVulnerability]:
        return self._vulnerabilities.value

    @property
    def withdrawn_at(self) -> datetime:
        return self._withdrawn_at.value

    def add_vulnerability(
        self,
        ecosystem: str,
        package_name: str | None = None,
        vulnerable_version_range: str | None = None,
        patched_versions: str | None = None,
        vulnerable_functions: list[str] | None = None,
    ) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`\
        """
        return self.add_vulnerabilities(
            [
                {
                    "package": {
                        "ecosystem": ecosystem,
                        "name": package_name,
                    },
                    "vulnerable_version_range": vulnerable_version_range,
                    "patched_versions": patched_versions,
                    "vulnerable_functions": vulnerable_functions,
                }
            ]
        )

    def add_vulnerabilities(self, vulnerabilities: Iterable[AdvisoryVulnerability]) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`
        """
        assert isinstance(vulnerabilities, Iterable), vulnerabilities
        for vulnerability in vulnerabilities:
            github.RepositoryAdvisoryVulnerability.RepositoryAdvisoryVulnerability._validate_vulnerability(
                vulnerability
            )

        post_parameters = {
            "vulnerabilities": [
                github.RepositoryAdvisoryVulnerability.RepositoryAdvisoryVulnerability._to_github_dict(vulnerability)
                for vulnerability in (self.vulnerabilities + list(vulnerabilities))
            ]
        }
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters,
        )
        self._useAttributes(data)

    def offer_credit(
        self,
        login_or_user: str | github.NamedUser.NamedUser,
        credit_type: str,
    ) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`
        Offers credit to a user for a vulnerability in a repository.
        Unless you are giving credit to yourself, the user having credit offered will need to explicitly accept the credit.
        """
        self.offer_credits([{"login": login_or_user, "type": credit_type}])

    def offer_credits(
        self,
        credited: Iterable[Credit],
    ) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`
        Offers credit to a list of users for a vulnerability in a repository.
        Unless you are giving credit to yourself, the user having credit offered will need to explicitly accept the credit.
        :param credited: iterable of dict with keys "login" and "type"
        """
        assert isinstance(credited, Iterable), credited
        for credit in credited:
            RepositoryAdvisoryCredit._validate_credit(credit)

        patch_parameters = {
            "credits": [RepositoryAdvisoryCredit._to_github_dict(credit) for credit in (self.credits + list(credited))]
        }
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
        )
        self._useAttributes(data)

    def revoke_credit(self, login_or_user: str | github.NamedUser.NamedUser) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`_
        """
        assert isinstance(login_or_user, (str, github.NamedUser.NamedUser)), login_or_user
        if isinstance(login_or_user, github.NamedUser.NamedUser):
            login_or_user = login_or_user.login
        patch_parameters = {
            "credits": [
                dict(login=credit.login, type=credit.type) for credit in self.credits if credit.login != login_or_user
            ]
        }
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
        )
        self._useAttributes(data)

    def clear_credits(self) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`_
        """
        patch_parameters: dict[str, Any] = {"credits": []}
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
        )
        self._useAttributes(data)

    def edit(
        self,
        summary: Opt[str] = NotSet,
        description: Opt[str] = NotSet,
        severity_or_cvss_vector_string: Opt[str] = NotSet,
        cve_id: Opt[str] = NotSet,
        vulnerabilities: Opt[Iterable[AdvisoryVulnerability]] = NotSet,
        cwe_ids: Opt[Iterable[str]] = NotSet,
        credits: Opt[Iterable[Credit]] = NotSet,
        state: Opt[str] = NotSet,
    ) -> RepositoryAdvisory:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`_
        """
        assert summary is NotSet or isinstance(summary, str), summary
        assert description is NotSet or isinstance(description, str), description
        assert severity_or_cvss_vector_string is NotSet or isinstance(
            severity_or_cvss_vector_string, str
        ), severity_or_cvss_vector_string
        assert cve_id is NotSet or isinstance(cve_id, str), cve_id
        assert vulnerabilities is NotSet or isinstance(vulnerabilities, Iterable), vulnerabilities
        if isinstance(vulnerabilities, Iterable):
            for vulnerability in vulnerabilities:
                github.RepositoryAdvisoryVulnerability.RepositoryAdvisoryVulnerability._validate_vulnerability(
                    vulnerability
                )
        assert cwe_ids is NotSet or (
            isinstance(cwe_ids, Iterable) and all(isinstance(element, str) for element in cwe_ids)
        ), cwe_ids
        if isinstance(credits, Iterable):
            for credit in credits:
                github.RepositoryAdvisoryCredit.RepositoryAdvisoryCredit._validate_credit(credit)
        assert state is NotSet or isinstance(state, str), state
        patch_parameters: dict[str, Any] = {}
        if summary is not NotSet:
            patch_parameters["summary"] = summary
        if description is not NotSet:
            patch_parameters["description"] = description
        if isinstance(severity_or_cvss_vector_string, str):
            if severity_or_cvss_vector_string.startswith("CVSS:"):
                patch_parameters["cvss_vector_string"] = severity_or_cvss_vector_string
            else:
                patch_parameters["severity"] = severity_or_cvss_vector_string
        if cve_id is not NotSet:
            patch_parameters["cve_id"] = cve_id
        if isinstance(vulnerabilities, Iterable):
            patch_parameters["vulnerabilities"] = [
                github.RepositoryAdvisoryVulnerability.RepositoryAdvisoryVulnerability._to_github_dict(vulnerability)
                for vulnerability in vulnerabilities
            ]
        if isinstance(cwe_ids, Iterable):
            patch_parameters["cwe_ids"] = list(cwe_ids)
        if isinstance(credits, Iterable):
            patch_parameters["credits"] = [
                github.RepositoryAdvisoryCredit.RepositoryAdvisoryCredit._to_github_dict(credit) for credit in credits
            ]
        if state is not NotSet:
            patch_parameters["state"] = state
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
        )
        self._useAttributes(data)
        return self

    def accept_report(self) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`
        Accepts the advisory reported from an external reporter via private vulnerability reporting.
        """
        patch_parameters = {"state": "draft"}
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
        )
        self._useAttributes(data)

    def publish(self) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`
        Publishes the advisory.
        """
        patch_parameters = {"state": "published"}
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
        )
        self._useAttributes(data)

    def close(self) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`
        Closes the advisory.
        """
        patch_parameters = {"state": "closed"}
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
        )
        self._useAttributes(data)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "author" in attributes:  # pragma no branch
            self._author = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["author"])
        if "closed_at" in attributes:  # pragma no branch
            assert attributes["closed_at"] is None or isinstance(attributes["closed_at"], str), attributes["closed_at"]
            self._closed_at = self._makeDatetimeAttribute(attributes["closed_at"])
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], str), attributes[
                "created_at"
            ]
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "credits" in attributes:  # pragma no branch
            self._credits = self._makeListOfClassesAttribute(
                RepositoryAdvisoryCredit,
                attributes["credits"],
            )
        if "credits_detailed" in attributes:  # pragma no branch
            self._credits_detailed = self._makeListOfClassesAttribute(
                RepositoryAdvisoryCreditDetailed,
                attributes["credits_detailed"],
            )
        if "cve_id" in attributes:  # pragma no branch
            self._cve_id = self._makeStringAttribute(attributes["cve_id"])
        if "cwe_ids" in attributes:  # pragma no branch
            self._cwe_ids = self._makeListOfStringsAttribute(attributes["cwe_ids"])
        if "cwes" in attributes:  # pragma no branch
            self._cwes = self._makeListOfClassesAttribute(CWE, attributes["cwes"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "ghsa_id" in attributes:  # pragma no branch
            self._ghsa_id = self._makeStringAttribute(attributes["ghsa_id"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "published_at" in attributes:  # pragma no branch
            assert attributes["published_at"] is None or isinstance(attributes["published_at"], str), attributes[
                "published_at"
            ]
            self._published_at = self._makeDatetimeAttribute(attributes["published_at"])
        if "severity" in attributes:  # pragma no branch
            self._severity = self._makeStringAttribute(attributes["severity"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
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
                RepositoryAdvisoryVulnerability,
                attributes["vulnerabilities"],
            )
        if "withdrawn_at" in attributes:  # pragma no branch
            assert attributes["withdrawn_at"] is None or isinstance(attributes["withdrawn_at"], str), attributes[
                "withdrawn_at"
            ]
            self._withdrawn_at = self._makeDatetimeAttribute(attributes["withdrawn_at"])
