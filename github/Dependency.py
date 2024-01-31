import github.Commit
import github.GithubObject
import github.Package


class Dependency(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Dependency. The reference can be found in the alert here https://docs.github.com/en/rest/dependabot/alerts#list-dependabot-alerts-for-a-repository
    """

    def __repr__(self):
        return self.get__repr__(
            {
                "package": self._package.value,
                "manifest_path": self._manifest_path.value,
                "scope": self._scope.value,
            }
        )

    @property
    def package(self):
        """
        :type: :class:`github.Package.Package`
        """
        return self._package.value

    @property
    def manifest_path(self):
        """
        :type: string
        """
        return self._manifest_path.value

    @property
    def scope(self):
        """
        :type: string
        """
        return self._scope.value

    def _initAttributes(self):
        self._package = github.GithubObject.NotSet
        self._manifest_path = github.GithubObject.NotSet
        self._scope = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "package" in attributes:  # pragma no branch
            self._package = self._makeClassAttribute(github.Package.Package, attributes["package"])
        if "manifest_path" in attributes:  # pragma no branch
            self._manifest_path = self._makeStringAttribute(attributes["manifest_path"])
        if "scope" in attributes:  # pragma no branch
            self._scope = self._makeStringAttribute(attributes["scope"])
