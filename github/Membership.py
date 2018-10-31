import github.GithubObject


class Membership(github.GithubObject.CompletableGithubObject):
    """
    This class represents Organizations. The reference can be found here http://developer.github.com/v3/orgs/
    """

    def __repr__(self):
        return self.get__repr__({"url": self._url.value})

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def state(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def role(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._role)
        return self._role.value

    @property
    def organization_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._organization_url)
        return self._organization_url.value

    @property
    def organization(self):
        """
        :type: :class:`github.Organization.Organization`
        """
        self._completeIfNotSet(self._organization)
        return self._organization.value

    @property
    def user(self):
        """
        :type: :class:`github.AuthenticatedUser.AuthenticatedUser`
        """
        self._completeIfNotSet(self._user)
        return self._user.value

    def _initAttributes(self):
        self._url = github.GithubObject.NotSet
        self._state = github.GithubObject.NotSet
        self._role = github.GithubObject.NotSet
        self._organization_url = github.GithubObject.NotSet
        self._organization = github.GithubObject.NotSet
        self._user = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "role" in attributes:  # pragma no branch
            self._role = self._makeStringAttribute(attributes["role"])
        if "organization_url" in attributes:  # pragma no branch
            self._organization_url = self._makeStringAttribute(attributes["organization_url"])
        if "organization" in attributes:  # pragma no branch
            self._organization = self._makeClassAttribute(github.Organization.Organization, attributes["organization"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(github.AuthenticatedUser.AuthenticatedUser, attributes["user"])
