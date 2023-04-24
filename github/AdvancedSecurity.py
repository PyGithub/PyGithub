import github.Commit
import github.GithubObject


class AdvancedSecurity(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents AdvancedSecurity.
    """

    def __repr__(self):
        return self.get__repr__({"status": self._status.value})

    @property
    def status(self):
        """
        :type: string
        """
        return self._status.value

    def _initAttributes(self):
        self._status = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
