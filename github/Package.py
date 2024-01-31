import github.Commit
import github.GithubObject


class Package(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Package. The reference can be found here in the alert https://docs.github.com/en/rest/dependabot/alerts?#list-dependabot-alerts-for-a-repository
    """

    def __repr__(self):
        return self.get__repr__({"ecosystem": self._ecosystem.value, "name": self._name.value})

    @property
    def ecosystem(self):
        """
        :type: string
        """
        return self._ecosystem.value

    @property
    def name(self):
        """
        :type: string
        """
        return self._name.value

    def _initAttributes(self):
        self._ecosystem = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "ecosystem" in attributes:  # pragma no branch
            self._ecosystem = self._makeStringAttribute(attributes["ecosystem"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
