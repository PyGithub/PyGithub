import github.Commit
import github.GithubObject


class Tool(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Tool.
    """

    def __repr__(self):
        return self.get__repr__(
            {
                "name": self._name.value,
                "guid": self._guid.value,
                "version": self._version.value,
            }
        )

    @property
    def name(self):
        """
        :type: string
        """
        return self._name.value

    @property
    def guid(self):
        """
        :type: string
        """
        return self._guid.value

    @property
    def version(self):
        """
        :type: string
        """
        return self._version.value

    def _initAttributes(self):
        self._name = github.GithubObject.NotSet
        self._guid = github.GithubObject.NotSet
        self._version = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "guid" in attributes:  # pragma no branch
            self._guid = self._makeStringAttribute(attributes["guid"])
        if "version" in attributes:  # pragma no branch
            self._version = self._makeStringAttribute(attributes["version"])
