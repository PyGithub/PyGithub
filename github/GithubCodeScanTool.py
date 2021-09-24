
import github.GithubObject


class CodeScanTool(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents code scanning tools.
    The reference can be found here https://docs.github.com/en/rest/reference/code-scanning.
    """

    def __repr__(self):
        return self.get__repr__({"name": self.number})

    @property
    def name(self):
        """
        :type: str
        """
        return self._name.value

    @property
    def version(self):
        """
        :type: str
        """
        return self._version.value

    @property
    def guid(self):
        """
        :type: str
        """
        return self._guid.value

    def _initAttributes(self):
        self._name = github.GithubObject.NotSet
        self._version = github.GithubObject.NotSet
        self._guid = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "version" in attributes:  # pragma no branch
            self._version = self._makeStringAttribute(attributes["version"])
        if "guid" in attributes:  # pragma no branch
            self._guid = self._makeStringAttribute(attributes["guid"])
