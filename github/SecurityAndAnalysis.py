import github.AdvancedSecurity
import github.GithubObject
import github.SecretScanning
import github.SecretScanningPushProtection


class SecurityAndAnalysis(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents SecurityAndAnalysis.
    """

    def __repr__(self):
        return self.get__repr__(
            {
                "advanced_security": self._advanced_security.value,
                "secret_scanning": self._secret_scanning.value,
                "secret_scanning_push_protection": self._secret_scanning_push_protection.value,
            }
        )

    @property
    def advanced_security(self):
        """
        :type: :class:`github.AdvancedSecurity.AdvancedSecurity`
        """
        return self._advanced_security.value

    @property
    def secret_scanning(self):
        """
        :type: :class:`github.SecretScanning.SecretScanning`
        """
        return self._secret_scanning.value

    @property
    def secret_scanning_push_protection(self):
        """
        :type: :class:`github.SecretScanningPushProtection.SecretScanningPushProtection`
        """
        return self._secret_scanning_push_protection.value

    def _initAttributes(self):
        self._advanced_security = github.GithubObject.NotSet
        self._secret_scanning = github.GithubObject.NotSet
        self._secret_scanning_push_protection = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "advanced_security" in attributes:  # pragma no branch
            self._advanced_security = self._makeClassAttribute(
                github.AdvancedSecurity.AdvancedSecurity,
                attributes["advanced_security"],
            )
        if "secret_scanning" in attributes:  # pragma no branch
            self._secret_scanning = self._makeClassAttribute(
                github.SecretScanning.SecretScanning, attributes["secret_scanning"]
            )
        if "secret_scanning_push_protection" in attributes:  # pragma no branch
            self._secret_scanning_push_protection = self._makeClassAttribute(
                github.SecretScanningPushProtection.SecretScanningPushProtection,
                attributes["secret_scanning_push_protection"],
            )
