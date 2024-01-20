from __future__ import annotations

from typing import TYPE_CHECKING, Any

import github.AdvisoryBase
import github.DependabotAlertVulnerability
from github.GithubObject import Attribute, NotSet

if TYPE_CHECKING:
    from github.DependabotAlertVulnerability import DependabotAlertVulnerability


class DependabotAlertAdvisory(github.AdvisoryBase.AdvisoryBase):
    """
    This class represents a package flagged by a Dependabot alert that is vulnerable to a parent SecurityAdvisory.
    The reference can be found here https://docs.github.com/en/rest/dependabot/alerts
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._references: Attribute[list[dict]] = NotSet
        self._vulnerabilities: Attribute[list[DependabotAlertVulnerability]] = NotSet

    @property
    def references(self) -> list[dict]:
        return self._references.value

    @property
    def vulnerabilities(self) -> list[DependabotAlertVulnerability]:
        return self._vulnerabilities.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "references" in attributes:
            self._references = self._makeListOfDictsAttribute(
                attributes["references"],
            )
        if "vulnerabilities" in attributes:
            self._vulnerabilities = self._makeListOfClassesAttribute(
                github.DependabotAlertVulnerability.DependabotAlertVulnerability,
                attributes["vulnerabilities"],
            )
        super()._useAttributes(attributes)
