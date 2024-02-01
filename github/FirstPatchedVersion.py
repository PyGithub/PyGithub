from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class FirstPatchedVersion(NonCompletableGithubObject):
    """
    This class represents FirstPatchedVersion. The reference can be found in the alert here https://docs.github.com/en/rest/dependabot/alerts#get-a-dependabot-alert
    """

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "identifier": self._identifier.value,
            }
        )

    @property
    def identifier(self) -> str:
        """
        :type: string
        """
        return self._identifier.value

    def _initAttributes(self) -> None:
        self._identifier: Attribute[str] = NotSet

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "identifier" in attributes:  # pragma no branch
            self._identifier = self._makeStringAttribute(attributes["identifier"])
