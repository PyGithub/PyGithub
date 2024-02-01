from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject, NotSet


class Package(NonCompletableGithubObject):
    """
    This class represents Package. The reference can be found here in the alert https://docs.github.com/en/rest/dependabot/alerts?#list-dependabot-alerts-for-a-repository
    """

    def __repr__(self) -> str:
        return self.get__repr__({"ecosystem": self._ecosystem.value, "name": self._name.value})

    @property
    def ecosystem(self) -> str:
        """
        :type: string
        """
        return self._ecosystem.value

    @property
    def name(self) -> str:
        """
        :type: string
        """
        return self._name.value

    def _initAttributes(self) -> str:
        self._ecosystem = NotSet
        self._name = NotSet

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "ecosystem" in attributes:  # pragma no branch
            self._ecosystem = self._makeStringAttribute(attributes["ecosystem"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
