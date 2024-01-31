import github.AdvancedSecurity
import github.CodeScanTool
import github.GithubObject
import github.SecretScanning
import github.SecretScanningPushProtection


class CodeScanningAnalysis(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents CodeScanningAnalysis. The reference can be found here https://docs.github.com/en/rest/code-scanning?#list-code-scanning-analyses-for-a-repository
    """

    def __repr__(self):
        return self.get__repr__(
            {
                "ref": self._ref.value,
                "commit_sha": self._commit_sha.value,
                "analysis_key": self._analysis_key.value,
                "environment": self._environment.value,
                "error": self._error.value,
                "category": self._category.value,
                "created_at": self._created_at.value,
                "results_count": self._results_count.value,
                "rules_count": self._rules_count.value,
                "id": self._id.value,
                "url": self._url.value,
                "sarif_id": self._sarif_id.value,
                "tool": self._tool.value,
                "deletable": self._deletable.value,
                "warning": self._warning.value,
            }
        )

    @property
    def ref(self):
        """
        :type: string
        """
        return self._ref.value

    @property
    def commit_sha(self):
        """
        :type: string
        """
        return self._commit_sha.value

    @property
    def analysis_key(self):
        """
        :type: string
        """
        return self._analysis_key.value

    @property
    def environment(self):
        """
        :type: string
        """
        return self._environment.value

    @property
    def error(self):
        """
        :type: string
        """
        return self._error.value

    @property
    def category(self):
        """
        :type: string
        """
        return self._category.value

    @property
    def created_at(self):
        """
        :type: string
        """
        return self._created_at.value

    @property
    def results_count(self):
        """
        :type: integer
        """
        return self._results_count.value

    @property
    def rules_count(self):
        """
        :type: integer
        """
        return self._rules_count.value

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    @property
    def sarif_id(self):
        """
        :type: string
        """
        return self._sarif_id.value

    @property
    def tool(self):
        """
        :type: :class:`github.Tool.Tool`
        """
        return self._tool.value

    @property
    def deletable(self):
        """
        :type: bool
        """
        return self._deletable.value

    @property
    def warning(self):
        """
        :type: string
        """
        return self._warning.value

    def _initAttributes(self):
        self._ref = github.GithubObject.NotSet
        self._commit_sha = github.GithubObject.NotSet
        self._analysis_key = github.GithubObject.NotSet
        self._environment = github.GithubObject.NotSet
        self._error = github.GithubObject.NotSet
        self._category = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._results_count = github.GithubObject.NotSet
        self._rules_count = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._sarif_id = github.GithubObject.NotSet
        self._tool = github.GithubObject.NotSet
        self._deletable = github.GithubObject.NotSet
        self._warning = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "ref" in attributes:  # pragma no branch
            self._ref = self._makeStringAttribute(attributes["ref"])
        if "commit_sha" in attributes:  # pragma no branch
            self._commit_sha = self._makeStringAttribute(attributes["commit_sha"])
        if "analysis_key" in attributes:  # pragma no branch
            self._analysis_key = self._makeStringAttribute(attributes["analysis_key"])
        if "environment" in attributes:  # pragma no branch
            self._environment = self._makeStringAttribute(attributes["environment"])
        if "error" in attributes:  # pragma no branch
            self._error = self._makeStringAttribute(attributes["error"])
        if "category" in attributes:  # pragma no branch
            self._category = self._makeStringAttribute(attributes["category"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeStringAttribute(attributes["created_at"])
        if "results_count" in attributes:  # pragma no branch
            self._results_count = self._makeIntAttribute(attributes["results_count"])
        if "rules_count" in attributes:  # pragma no branch
            self._rules_count = self._makeIntAttribute(attributes["rules_count"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "sarif_id" in attributes:  # pragma no branch
            self._sarif_id = self._makeStringAttribute(attributes["sarif_id"])
        if "tool" in attributes:  # pragma no branch
            self._tool = self._makeClassAttribute(github.CodeScanTool.CodeScanTool, attributes["tool"])
        if "deletable" in attributes:  # pragma no branch
            self._deletable = self._makeBoolAttribute(attributes["deletable"])
        if "warning" in attributes:  # pragma no branch
            self._warning = self._makeStringAttribute(attributes["warning"])
