from typing import Any, Dict

from github.AdvancedSecurity import AdvancedSecurity
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet
from github.SecretScanning import SecretScanning
from github.SecretScanningPushProtection import SecretScanningPushProtection


class SecurityAndAnalysis(NonCompletableGithubObject):
    """
    This class represents SecurityAndAnalysis.
    """

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "advanced_security": self._advanced_security.value,
                "secret_scanning": self._secret_scanning.value,
                "secret_scanning_push_protection": self._secret_scanning_push_protection.value,
            }
        )

    @property
    def advanced_security(self) -> AdvancedSecurity:
        return self._advanced_security.value

    @property
    def secret_scanning(self) -> SecretScanning:
        return self._secret_scanning.value

    @property
    def secret_scanning_push_protection(self) -> SecretScanningPushProtection:
        return self._secret_scanning_push_protection.value

    def _initAttributes(self) -> None:
        self._advanced_security: Attribute[AdvancedSecurity] = NotSet
        self._secret_scanning: Attribute[SecretScanning] = NotSet
        self._secret_scanning_push_protection: Attribute[SecretScanningPushProtection] = NotSet

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "advanced_security" in attributes:  # pragma no branch
            self._advanced_security = self._makeClassAttribute(AdvancedSecurity, attributes["advanced_security"])
        if "secret_scanning" in attributes:  # pragma no branch
            self._secret_scanning = self._makeClassAttribute(SecretScanning, attributes["secret_scanning"])
        if "secret_scanning_push_protection" in attributes:  # pragma no branch
            self._secret_scanning_push_protection = self._makeClassAttribute(
                SecretScanningPushProtection, attributes["secret_scanning_push_protection"]
            )
