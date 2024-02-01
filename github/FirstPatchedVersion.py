from github.GithubObject import NonCompletableGithubObject, NotSet


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
        self._identifier = NotSet

    def _useAttributes(self, attributes) -> None:
        if "identifier" in attributes:  # pragma no branch
            self._identifier = self._makeStringAttribute(attributes["identifier"])
