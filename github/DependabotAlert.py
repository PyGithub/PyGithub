import github.Commit
import github.Dependency
import github.GithubObject
import github.NamedUser
import github.SecurityVulnerability


class DependabotAlert(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents DependabotAlert. The reference can be found here https://docs.github.com/en/rest/dependabot/alerts#list-dependabot-alerts-for-a-repository
    """

    def __repr__(self):
        return self.get__repr__(
            {
                "created_at": self._created_at.value,
                "dependency": self._dependency.value,
                "dismissed_at": self._dismissed_at.value,
                "dismissed_comment": self._dismissed_comment.value,
                "dismissed_reason": self._dismissed_reason.value,
                "fixed_at": self._fixed_at.value,
                "html_url": self._html_url.value,
                "number": self._number.value,
                "security_vulnerability": self._security_vulnerability.value,
                "state": self._state.value,
                "update_at": self._update_at.value,
                "url": self._url.value,
            }
        )

    @property
    def created_at(self):
        """
        :type: string
        """
        return self._created_at.value

    @property
    def dependency(self):
        """
        :type: :class:`github.Dependency.Dependency`
        """
        return self._dependency.value

    @property
    def dismissed_at(self):
        """
        :type: string
        """
        return self._dismissed_at.value

    @property
    def dismissed_by(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        return self._dismissed_by.value

    @property
    def dismissed_comment(self):
        """
        :type: string
        """
        return self._dismissed_comment.value

    @property
    def dismissed_reason(self):
        """
        :type: string
        """
        return self._dismissed_reason.value

    @property
    def fixed_at(self):
        """
        :type: string
        """
        return self._fixed_at.value

    @property
    def html_url(self):
        """
        :type: string
        """
        return self._html_url.value

    @property
    def number(self):
        """
        :type: integer
        """
        return self._number.value

    @property
    def security_vulnerability(self):
        """
        :type: :class:`github.SecurityVulnerability.SecurityVulnerability`
        """
        return self._security_vulnerability.value

    @property
    def state(self):
        """
        :type: string
        """
        return self._state.value

    @property
    def update_at(self):
        """
        :type: string
        """
        return self._update_at.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    def _initAttributes(self):
        self._created_at = github.GithubObject.NotSet
        self._dependency = github.GithubObject.NotSet
        self._dismissed_at = github.GithubObject.NotSet
        self._dismissed_comment = github.GithubObject.NotSet
        self._dismissed_reason = github.GithubObject.NotSet
        self._fixed_at = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._number = github.GithubObject.NotSet
        self._security_vulnerability = github.GithubObject.NotSet
        self._state = github.GithubObject.NotSet
        self._update_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeStringAttribute(attributes["created_at"])
        if "dependency" in attributes:  # pragma no branch
            self._dependency = self._makeClassAttribute(
                github.Dependency.Dependency, attributes["dependency"]
            )
        if "dismissed_at" in attributes:  # pragma no branch
            self._dismissed_at = self._makeStringAttribute(attributes["dismissed_at"])
        if "dismissed_by" in attributes:  # pragma no branch
            self._dismissed_by = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["dismissed_by"]
            )
        if "dismissed_comment" in attributes:  # pragma no branch
            self._dismissed_comment = self._makeStringAttribute(
                attributes["dismissed_comment"]
            )
        if "dismissed_reason" in attributes:  # pragma no branch
            self._dismissed_reason = self._makeStringAttribute(
                attributes["dismissed_reason"]
            )
        if "fixed_at" in attributes:  # pragma no branch
            self._fixed_at = self._makeStringAttribute(attributes["fixed_at"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "number" in attributes:  # pragma no branch
            self._commit = self._makeIntAttribute(attributes["number"])
        if "security_vulnerability" in attributes:  # pragma no branch
            self._security_vulnerability = self._makeClassAttribute(
                github.SecurityVulnerability.SecurityVulnerability,
                attributes["security_vulnerability"],
            )
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "update_at" in attributes:  # pragma no branch
            self._update_at = self._makeStringAttribute(attributes["update_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
