
import github.GithubObject
import github.PaginatedList
import github.GithubCodeScanRule
import github.GithubCodeScanTool
import github.GithubCodeScanAlertInstance


class CodeScanAlert(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents alerts from code scanning.
    The reference can be found here https://docs.github.com/en/rest/reference/code-scanning.
    """

    def __repr__(self):
        return self.get__repr__({"number": self.number})

    @property
    def number(self):
        """
        :type: int
        """
        return self._number.value

    @property
    def rule(self):
        """
        :type: :class: `github.GithubCodeScanRule.CodeScanRule`
        """
        return self._rule.value

    @property
    def tool(self):
        """
        :type:  :class: `github.GithubCodeScanTool.CodeScanTool`
        """
        return self._tool.value

    @property
    def created_at(self):
        """
        :type: datetime
        """
        return self._created_at.value

    @property
    def dismissed_at(self):
        """
        :type: datetime
        """
        return self._dismissed_at.value

    @property
    def dismissed_by(self):
        """
        :type: dict
        """
        return self._dismissed_by.value

    @property
    def dismissed_reason(self):
        """
        :type: str
        """
        return self._dismissed_reason.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    @property
    def html_url(self):
        """
        :type: string
        """
        return self._html_url.value

    @property
    def instances_url(self):
        """
        :type: string
        """
        return self._instances_url.value

    @property
    def most_recent_instance(self):
        """
        :type: dict
        """
        return self._most_recent_instance.value

    @property
    def state(self):
        """
        :type: str
        """
        return self._state.value

    def get_instances(self):
        """
        :calls: `GET` on the URL for instances as provided by Github
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.GithubCodeScanAlertInstance.CodeScanAlertInstance`
        """
        return github.PaginatedList.PaginatedList(
            github.GithubCodeScanAlertInstance.CodeScanAlertInstance,
            self._requester,
            self.instances_url,
            None
        )

    def _initAttributes(self):
        self._number = github.GithubObject.NotSet
        self._rule = github.GithubObject.NotSet
        self._tool = github.GithubObject.NotSet

        self._created_at = github.GithubObject.NotSet
        self._dismissed_at = github.GithubObject.NotSet
        self._dismissed_by = github.GithubObject.NotSet
        self._dismissed_reason = github.GithubObject.NotSet

        self._url = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._instances_url = github.GithubObject.NotSet

        self._most_recent_instance = github.GithubObject.NotSet
        self._state = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "rule" in attributes:  # pragma no branch
            self._rule = self._makeClassAttribute(
                github.GithubCodeScanRule.CodeScanRule, attributes["rule"]
            )
        if "tool" in attributes:  # pragma no branch
            self._tool = self._makeClassAttribute(
                github.GithubCodeScanTool.CodeScanTool, attributes["tool"]
            )

        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "dismissed_at" in attributes:  # pragma no branch
            self._dismissed_at = self._makeDatetimeAttribute(attributes["dismissed_at"])
        if "dismissed_by" in attributes:  # pragma no branch
            self._dismissed_by = self._makeDictAttribute(attributes["dismissed_by"])

        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "instances_url" in attributes:  # pragma no branch
            self._instances_url = self._makeStringAttribute(attributes["instances_url"])

        if "most_recent_instance" in attributes:  # pragma no branch
            self._most_recent_instance = self._makeClassAttribute(
                github.GithubCodeScanAlertInstance.CodeScanAlertInstance, attributes["most_recent_instance"]
            )
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
