from github.GithubObject import NonCompletableGithubObject, NotSet


class AdvancedSecurity(NonCompletableGithubObject):
    """
    This class represents AdvancedSecurity.
    """

    def __repr__(self) -> str:
        return self.get__repr__({"status": self._status.value})

    @property
    def status(self) -> str:
        return self._status.value

    def _initAttributes(self) -> None:
        self._status = NotSet

    def _useAttributes(self, attributes) -> None:
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
