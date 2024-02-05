from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class SecretScanning(NonCompletableGithubObject):
    """
    This class represents SecretScanning.
    """

    def __repr__(self) -> str:
        return self.get__repr__({"status": self._status.value})

    @property
    def status(self) -> str:
        return self._status.value

    def _initAttributes(self) -> None:
        self._status: Attribute[str] = NotSet

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
