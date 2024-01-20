from typing import Any, Dict

from github.AdvisoryBase import AdvisoryBase
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class Package(NonCompletableGithubObject):
    """
    This class represents a Package.
    The reference can be found here https://docs.github.com/en/rest/dependabot/alerts
    """

    def _initAttributes(self) -> None:
        self._ecosystem: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self.name})

    @property
    def ecosystem(self) -> str:
        return self._ecosystem.value

    @property
    def name(self) -> str:
        return self._name.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "ecosystem" in attributes:
            self._ecosystem = self._makeStringAttribute(attributes["ecosystem"])
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])


class Dependency(NonCompletableGithubObject):
    """
    This class represents a Dependency.
    The reference can be found here https://docs.github.com/en/rest/dependabot/alerts
    """

    def _initAttributes(self) -> None:
        self._package: Attribute[Package] = NotSet
        self._manifest_path: Attribute[str] = NotSet
        self._scope: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"package": self.package})

    @property
    def package(self) -> Package:
        return self._package.value

    @property
    def manifest_path(self) -> str:
        return self._manifest_path.value

    @property
    def scope(self) -> str:
        return self._scope.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "package" in attributes:
            self._package = self._makeClassAttribute(Package, attributes["package"])
        if "manifest_path" in attributes:
            self._manifest_path = self._makeStringAttribute(attributes["manifest_path"])
        if "scope" in attributes:
            self._scope = self._makeStringAttribute(attributes["scope"])


class DependabotAlert(NonCompletableGithubObject):
    """
    This class represents a DependabotAlert.
    The reference can be found here https://docs.github.com/en/rest/dependabot/alerts
    """

    def _initAttributes(self) -> None:
        self._number: Attribute[int] = NotSet
        self._state: Attribute[str] = NotSet
        self._dependency: Attribute[Dependency] = NotSet
        self._security_advisory: Attribute[AdvisoryBase] = NotSet
        self._security_vulnerability: Attribute[dict] = NotSet
        self._url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._created_at: Attribute[str] = NotSet
        self._updated_at: Attribute[str] = NotSet
        self._dismissed_at: Attribute[str] = NotSet
        self._dismissed_by: Attribute[dict] = NotSet
        self._dismissed_reason: Attribute[str] = NotSet
        self._dismissed_comment: Attribute[str] = NotSet
        self._fixed_at: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self.number})

    @property
    def number(self) -> int:
        return self._number.value

    @property
    def state(self) -> str:
        return self._state.value

    @property
    def dependency(self) -> Dependency:
        return self._dependency.value

    @property
    def security_advisory(self) -> AdvisoryBase:
        return self._security_advisory.value

    @property
    def security_vulnerability(self) -> dict:
        return self._security_vulnerability.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def created_at(self) -> str:
        return self._created_at.value

    @property
    def updated_at(self) -> str:
        return self._updated_at.value

    @property
    def dismissed_at(self) -> str:
        return self._dismissed_at.value

    @property
    def dismissed_by(self) -> dict:
        return self._dismissed_by.value

    @property
    def dismissed_reason(self) -> str:
        return self._dismissed_reason.value

    @property
    def dismissed_comment(self) -> str:
        return self._dismissed_comment.value

    @property
    def fixed_at(self) -> str:
        return self._fixed_at.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "number" in attributes:
            self._number = self._makeIntAttribute(attributes["number"])
        if "state" in attributes:
            self._state = self._makeStringAttribute(attributes["state"])
        if "dependency" in attributes:
            self._dependency = self._makeClassAttribute(Dependency, attributes["dependency"])
