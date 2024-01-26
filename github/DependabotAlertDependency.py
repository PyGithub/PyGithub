from __future__ import annotations

from typing import Any

from github.AdvisoryVulnerabilityPackage import AdvisoryVulnerabilityPackage
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class DependabotAlertDependency(NonCompletableGithubObject):
    """
    This class represents a DependabotAlertDependency.
    The reference can be found here https://docs.github.com/en/rest/dependabot/alerts
    """

    def _initAttributes(self) -> None:
        self._package: Attribute[AdvisoryVulnerabilityPackage] = NotSet
        self._manifest_path: Attribute[str] = NotSet
        self._scope: Attribute[str] = NotSet

    @property
    def package(self) -> AdvisoryVulnerabilityPackage:
        return self._package.value

    @property
    def manifest_path(self) -> str:
        return self._manifest_path.value

    @property
    def scope(self) -> str:
        return self._scope.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "package" in attributes:
            self._package = self._makeClassAttribute(
                AdvisoryVulnerabilityPackage,
                attributes["package"],
            )
        if "manifest_path" in attributes:
            self._manifest_path = self._makeStringAttribute(attributes["manifest_path"])
        if "scope" in attributes:
            self._scope = self._makeStringAttribute(attributes["scope"])
