import github
import github.GithubObject
import github.Repository
import github.GithubObject


class Secret(github.GithubObject.CompletableGithubObject):
    """
    This class represents a GitHub secret
    """

    def __repr__(self):
        return self.get__repr__({"name": self.name})

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def visibility(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._visibility)
        return self._visibility.value

    @property
    def selected_repositories(self):
        """
        :type: List of type Repository
        """
        self._completeIfNotSet(self._selected_repositories)
        return self._selected_repositories.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    def _initAttributes(self):
        self._name = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._visibility = github.GithubObject.NotSet
        self._selected_repositories = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "visibility" in attributes:
            self._visibility = self._makeStringAttribute(attributes["visibility"])
        if "selected_repositories_url" in attributes:
            headers, data = self._requester.requestJsonAndCheck(
                "GET", attributes["selected_repositories_url"]
            )
            self._selected_repositories = self._makeListOfClassesAttribute(
                github.Repository.Repository, data["repositories"]
            )
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])

    def add_repo(self, repo):
        if self.visibility != "selected":
            return False
        self._requester.requestJsonAndCheck(
            "PUT", f"{self.url}/repositories/{repo.id}"
        )
        self._selected_repositories.value.append(repo)

    def remove_repo(self, repo):
        if self.visibility != "selected":
            return False
        self._requester.requestJsonAndCheck(
            "DELETE", f"{self.url}/repositories/{repo.id}"
        )
        self._selected_repositories.value.remove(repo)
