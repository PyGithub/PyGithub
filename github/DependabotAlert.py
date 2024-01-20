from typing import Any, Dict

from github.AdvisoryBase import AdvisoryBase
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class DependabotAlert(NonCompletableGithubObject):
    """
    This class represents a DependabotAlert.
    The reference can be found here https://docs.github.com/en/rest/dependabot/alerts
    """

    def _initAttributes(self) -> None:
        self._number: Attribute[int] = NotSet
        self._state: Attribute[str] = NotSet
        self._dependency: Attribute[dict] = NotSet
        self._security_advisory: Attribute[AdvisoryBase] = NotSet
        self._security_vulnerability: Attribute[dict] = NotSet
        self._url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._created_at: Attribute[str] = NotSet
        self._updated_at: Attribute[str] = NotSet
        self._dismissed_at: Attribute[str] = NotSet
        self._dismissed_by: Attribute[dict] = NotSet
        self._dismissed_reason: Attribute[str] = NotSet
        self._dismissed_comment: Attribute[str] = NotSet
        self._fixed_at: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self.number})

    @property
    def number(self) -> int:
        return self._number.value

    @property
    def state(self) -> str:
        return self._state.value

    @property
    def dependency(self) -> dict:
        return self._dependency.value

    @property
    def security_advisory(self) -> AdvisoryBase:
        return self._security_advisory.value

    @property
    def security_vulnerability(self) -> dict:
        return self._security_vulnerability.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def created_at(self) -> str:
        return self._created_at.value

    @property
    def updated_at(self) -> str:
        return self._updated_at.value

    @property
    def dismissed_at(self) -> str:
        return self._dismissed_at.value

    @property
    def dismissed_by(self) -> dict:
        return self._dismissed_by.value

    @property
    def dismissed_reason(self) -> str:
        return self._dismissed_reason.value

    @property
    def dismissed_comment(self) -> str:
        return self._dismissed_comment.value

    @property
    def fixed_at(self) -> str:
        return self._fixed_at.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        self._number.value = attributes["number"]
        self._state.value = attributes["state"]
        self._dependency.value = attributes["dependency"]
        self._security_advisory.value = attributes["security_advisory"]
        self._security_vulnerability.value = attributes["security_vulnerability"]
        self._url.value = attributes["url"]
        self._html_url.value = attributes["html_url"]
        self._created_at.value = attributes["created_at"]
        self._updated_at.value = attributes["updated_at"]
        self._dismissed_at.value = attributes["dismissed_at"]
        self._dismissed_by.value = attributes["dismissed_by"]
        self._dismissed_reason.value = attributes["dismissed_reason"]
        self._dismissed_comment.value = attributes["dismissed_comment"]
        self._fixed_at.value = attributes["fixed_at"]
