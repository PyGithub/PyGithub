import github.Commit
import github.GithubObject
import github.NamedUser


class FirstPatchedVersion(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents FirstPatchedVersion. The reference can be found in the alert here https://docs.github.com/en/rest/dependabot/alerts#get-a-dependabot-alert
    """

    def __repr__(self):
        return self.get__repr__(
            {
                "identifier": self._identifier.value,
            }
        )

    @property
    def identifier(self):
        """
        :type: string
        """
        return self._identifier.value

    def _initAttributes(self):
        self._identifier = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "identifier" in attributes:  # pragma no branch
            self._identifier = self._makeStringAttribute(attributes["identifier"])
