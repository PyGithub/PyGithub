import github
import github.GithubObject


class Secret(github.GithubObject.CompletableGithubObject):
    """
    This class represents a GitHub secret
    """

    def __repr__(self):
        return self.get__repr__({"secret_name": self.secret_name})

    @property
    def secret_name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._secret_name)
        return self._secret_name.value

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
        if self.selected_repositories_url == github.GithubObject.NotSet:
            self._completeIfNotSet(self._selected_repositories)
        return self._selected_repositories.value

    @property
    def selected_repositories_url(self):
        """
        :type: string
        """
        return self._selected_repositories_url.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    def _initAttributes(self):
        self._secret_name = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._visibility = github.GithubObject.NotSet
        self._selected_repositories_url = github.GithubObject.NotSet
        self._selected_repositories = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "secret_name" in attributes:
            self._secret_name = self._makeStringAttribute(attributes["secret_name"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "visibility" in attributes:
            self._visibility = self._makeStringAttribute(attributes["visibility"])
        if "selected_repositories_url" in attributes:
            self._selected_repositories_url = self._makeStringAttribute(attributes["selected_repositories_url"])
            headers, data = self._requester.requestJsonAndCheck(
                "GET", self._selected_repositories_url.value
            )
            self._selected_repositories = self._makeListOfClassesAttribute(
                github.Repository.Repository, data["repositories"]
            )
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])

    def delete(self):
        """
        DELETES THE SECRET (self) do not use after this
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", f"{self.url}"
        )
        return True

    def add_repo(self, repo_name):
        if self.visibility != "selected":
            return False
        self._requester.requestJsonAndCheck(
            "PUT", f"{self.url}/repositories/{repo_name}"
        )
        self.selected_repositories = github.GithubObject.NotSet
        return True

    def remove_repo(self, repo_name):
        if self.visibility != "selected":
            return False
        self._requester.requestJsonAndCheck(
            "DELETE", f"{self.url}/repositories/{repo_name}"
        )

    def update_visibility(self, visibility):
        if self._visibility == "selected":
            self.selected_repositories_url = github.GithubObject.NotSet
            self.selected_repositories = github.GithubObject.NotSet
        self._requester.requestJsonAndCheck(
            "PUT", f"{self.url}", input={"visibility": visibility}
        )
