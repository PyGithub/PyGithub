############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Leitschuh <jonathan.leitschuh@gmail.com>             #
# Copyright 2023 Joseph Henrich <crimsonknave@gmail.com>                       #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
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

from datetime import datetime
from typing import TYPE_CHECKING, Any, Iterable

import github.AdvisoryCredit
import github.AdvisoryCreditDetailed
import github.AdvisoryVulnerability
import github.NamedUser
import github.Repository
import github.Team
from github.AdvisoryBase import AdvisoryBase
from github.GithubObject import Attribute, NotSet, Opt

if TYPE_CHECKING:
    from github.AdvisoryCredit import AdvisoryCredit, Credit
    from github.AdvisoryCreditDetailed import AdvisoryCreditDetailed
    from github.AdvisoryVulnerability import AdvisoryVulnerability, AdvisoryVulnerabilityInput
    from github.NamedUser import NamedUser
    from github.Repository import Repository
    from github.Team import Team


class RepositoryAdvisory(AdvisoryBase):
    """
    This class represents a RepositoryAdvisory.

    The reference can be found here
    https://docs.github.com/en/rest/security-advisories/repository-advisories

    The OpenAPI schema can be found at
    - /components/schemas/repository-advisory

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._author: Attribute[NamedUser] = NotSet
        self._closed_at: Attribute[datetime] = NotSet
        self._collaborating_teams: Attribute[list[Team]] = NotSet
        self._collaborating_users: Attribute[list[NamedUser]] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._credits: Attribute[list[AdvisoryCredit]] = NotSet
        self._credits_detailed: Attribute[list[AdvisoryCreditDetailed]] = NotSet
        self._cwe_ids: Attribute[list[str]] = NotSet
        self._private_fork: Attribute[Repository] = NotSet
        self._publisher: Attribute[NamedUser] = NotSet
        self._state: Attribute[str] = NotSet
        self._submission: Attribute[dict[str, Any]] = NotSet
        self._vulnerabilities: Attribute[list[AdvisoryVulnerability]] = NotSet
        super()._initAttributes()

    @property
    def author(self) -> NamedUser:
        return self._author.value

    @property
    def closed_at(self) -> datetime:
        return self._closed_at.value

    @property
    def collaborating_teams(self) -> list[Team]:
        return self._collaborating_teams.value

    @property
    def collaborating_users(self) -> list[NamedUser]:
        return self._collaborating_users.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def credits(
        self,
    ) -> list[AdvisoryCredit]:
        return self._credits.value

    @property
    def credits_detailed(
        self,
    ) -> list[AdvisoryCreditDetailed]:
        return self._credits_detailed.value

    @property
    def cwe_ids(self) -> list[str]:
        return self._cwe_ids.value

    @property
    def private_fork(self) -> Repository:
        return self._private_fork.value

    @property
    def publisher(self) -> NamedUser:
        return self._publisher.value

    @property
    def state(self) -> str:
        return self._state.value

    @property
    def submission(self) -> dict[str, Any]:
        return self._submission.value

    @property
    def vulnerabilities(self) -> list[AdvisoryVulnerability]:
        return self._vulnerabilities.value

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

    def add_vulnerabilities(self, vulnerabilities: Iterable[AdvisoryVulnerabilityInput]) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`
        """
        assert isinstance(vulnerabilities, Iterable), vulnerabilities
        for vulnerability in vulnerabilities:
            github.AdvisoryVulnerability.AdvisoryVulnerability._validate_vulnerability(vulnerability)

        post_parameters = {
            "vulnerabilities": [
                github.AdvisoryVulnerability.AdvisoryVulnerability._to_github_dict(vulnerability)
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
        Offers credit to a user for a vulnerability in a repository.

        Unless you are giving credit to yourself, the user having credit offered will need to explicitly accept the credit.
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`

        """
        self.offer_credits([{"login": login_or_user, "type": credit_type}])

    def offer_credits(
        self,
        credited: Iterable[Credit],
    ) -> None:
        """
        Offers credit to a list of users for a vulnerability in a repository.

        Unless you are giving credit to yourself, the user having credit offered will need to explicitly accept the credit.
        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`
        :param credited: iterable of dict with keys "login" and "type"

        """
        assert isinstance(credited, Iterable), credited
        for credit in credited:
            github.AdvisoryCredit.AdvisoryCredit._validate_credit(credit)

        patch_parameters = {
            "credits": [
                github.AdvisoryCredit.AdvisoryCredit._to_github_dict(credit)
                for credit in (self.credits + list(credited))
            ]
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
        vulnerabilities: Opt[Iterable[AdvisoryVulnerabilityInput]] = NotSet,
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
                github.AdvisoryVulnerability.AdvisoryVulnerability._validate_vulnerability(vulnerability)
        assert cwe_ids is NotSet or (
            isinstance(cwe_ids, Iterable) and all(isinstance(element, str) for element in cwe_ids)
        ), cwe_ids
        if isinstance(credits, Iterable):
            for credit in credits:
                github.AdvisoryCredit.AdvisoryCredit._validate_credit(credit)
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
                github.AdvisoryVulnerability.AdvisoryVulnerability._to_github_dict(vulnerability)
                for vulnerability in vulnerabilities
            ]
        if isinstance(cwe_ids, Iterable):
            patch_parameters["cwe_ids"] = list(cwe_ids)
        if isinstance(credits, Iterable):
            patch_parameters["credits"] = [
                github.AdvisoryCredit.AdvisoryCredit._to_github_dict(credit) for credit in credits
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
        Accepts the advisory reported from an external reporter via private vulnerability reporting.

        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`

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
        Publishes the advisory.

        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`

        """
        patch_parameters = {"state": "published"}
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
        )
        self._useAttributes(data)

    def request_cve(self) -> None:
        """
        Requests a CVE for the advisory.

        :calls: `POST /repos/{owner}/{repo}/security-advisories/{ghsa_id}/cve <https://docs.github.com/en/rest/security-advisories/repository-advisories#request-a-cve-for-a-repository-security-advisory>`_

        """
        self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/cve",
        )

    def close(self) -> None:
        """
        Closes the advisory.

        :calls: `PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>`

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
        if "collaborating_teams" in attributes:  # pragma no branch
            self._collaborating_teams = self._makeListOfClassesAttribute(
                github.Team.Team, attributes["collaborating_teams"]
            )
        if "collaborating_users" in attributes:  # pragma no branch
            self._collaborating_users = self._makeListOfClassesAttribute(
                github.NamedUser.NamedUser, attributes["collaborating_users"]
            )
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], str), attributes[
                "created_at"
            ]
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "credits" in attributes:  # pragma no branch
            self._credits = self._makeListOfClassesAttribute(
                github.AdvisoryCredit.AdvisoryCredit,
                attributes["credits"],
            )
        if "credits_detailed" in attributes:  # pragma no branch
            self._credits_detailed = self._makeListOfClassesAttribute(
                github.AdvisoryCreditDetailed.AdvisoryCreditDetailed,
                attributes["credits_detailed"],
            )
        if "cwe_ids" in attributes:  # pragma no branch
            self._cwe_ids = self._makeListOfStringsAttribute(attributes["cwe_ids"])
        if "private_fork" in attributes:  # pragma no branch
            self._private_fork = self._makeClassAttribute(github.Repository.Repository, attributes["private_fork"])
        if "publisher" in attributes:  # pragma no branch
            self._publisher = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["publisher"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "submission" in attributes:  # pragma no branch
            self._submission = self._makeDictAttribute(attributes["submission"])
        if "vulnerabilities" in attributes:
            self._vulnerabilities = self._makeListOfClassesAttribute(
                github.AdvisoryVulnerability.AdvisoryVulnerability,
                attributes["vulnerabilities"],
            )
        super()._useAttributes(attributes)
