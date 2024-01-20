from __future__ import annotations

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

import github.AdvisoryBase
import github.DependabotAlertVulnerability
from github.GithubObject import Attribute, NotSet

if TYPE_CHECKING:
    from github.DependabotAlertVulnerability import DependabotAlertVulnerability


class SimpleAdvisoryReference(TypedDict):
    """
    A simple reference in a security advisory.
    """

    url: str


class DependabotAlertAdvisory(github.AdvisoryBase.AdvisoryBase):
    """
    This class represents a package flagged by a Dependabot alert that is vulnerable to a parent SecurityAdvisory.
    The reference can be found here https://docs.github.com/en/rest/dependabot/alerts
    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._references: Attribute[SimpleAdvisoryReference] = NotSet
        self._vulnerabilities: Attribute[list[DependabotAlertVulnerability]] = NotSet

    @property
    def references(self) -> SimpleAdvisoryReference:
        """
        :type: :class:`github.AdvisoryVulnerability.AdvisoryVulnerability`
        """
        return self._references.value

    @property
    def vulnerabilities(self) -> list[DependabotAlertVulnerability]:
        return self._vulnerabilities.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "references" in attributes:
            self._references = self._makeClassAttribute(
                SimpleAdvisoryReference,
                attributes["references"],
            )
        if "vulnerabilities" in attributes:
            self._vulnerabilities = self._makeListOfClassesAttribute(
                github.DependabotAlertVulnerability.DependabotAlertVulnerability,
                attributes["vulnerabilities"],
            )
