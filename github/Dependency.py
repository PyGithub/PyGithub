from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet
from github.Package import Package


class Dependency(NonCompletableGithubObject):
    """
    This class represents Dependency. The reference can be found in the alert here https://docs.github.com/en/rest/dependabot/alerts#list-dependabot-alerts-for-a-repository
    """

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "package": self._package.value,
                "manifest_path": self._manifest_path.value,
                "scope": self._scope.value,
            }
        )

    @property
    def package(self) -> Package:
        return self._package.value

    @property
    def manifest_path(self) -> str:
        return self._manifest_path.value

    @property
    def scope(self) -> str:
        """
        :type: string
        """
        return self._scope.value

    def _initAttributes(self) -> None:
        self._package: Attribute[Package] = NotSet
        self._manifest_path: Attribute[str] = NotSet
        self._scope: Attribute[str] = NotSet

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "package" in attributes:  # pragma no branch
            self._package = self._makeClassAttribute(Package, attributes["package"])
        if "manifest_path" in attributes:  # pragma no branch
            self._manifest_path = self._makeStringAttribute(attributes["manifest_path"])
        if "scope" in attributes:  # pragma no branch
            self._scope = self._makeStringAttribute(attributes["scope"])
