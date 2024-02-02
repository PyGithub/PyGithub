from typing import Any, Dict

import github.NamedUser
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class SecretScanningAlert(NonCompletableGithubObject):
    """
    This class represents SecretScanningAlert. The reference can be found here https://docs.github.com/en/rest/secret-scanning#list-secret-scanning-alerts-for-a-repository
    """

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "created_at": self._created_at.value,
                "html_url": self._html_url.value,
                "locations_url": self._locations_url.value,
                "number": self._number.value,
                "push_protection_bypassed": self._push_protection_bypassed.value,
                "push_protection_bypassed_at": self._push_protection_bypassed_at.value,
                "push_protection_bypassed_by": self._push_protection_bypassed_by.value,
                "resolution": self._resolution.value,
                "resolution_comment": self._resolution_comment.value,
                "resolved_at": self._resolved_at.value,
                "resolved_by": self._resolved_by.value,
                "secret": self._secret.value,
                "secret_type": self._secret_type.value,
                "secret_type_display_name": self._secret_type_display_name.value,
                "state": self._state.value,
                "updated_at": self._updated_at,
                "url": self._url.value,
            }
        )

    @property
    def created_at(self) -> str:
        return self._created_at.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def locations_url(self) -> str:
        return self._locations_url.value

    @property
    def number(self) -> int:
        return self._number.value

    @property
    def push_protection_bypassed(self) -> bool:
        return self._push_protection_bypassed.value

    @property
    def push_protection_bypassed_at(self) -> str:
        return self._push_protection_bypassed_at.value

    @property
    def push_protection_bypassed_by(self) -> github.NamedUser.NamedUser:
        return self._push_protection_bypassed_by.value

    @property
    def resolution(self) -> str:
        return self._resolution.value

    @property
    def resolution_comment(self) -> str:
        return self._resolution_comment.value

    @property
    def resolved_at(self) -> str:
        return self._resolved_at.value

    @property
    def resolved_by(self) -> github.NamedUser.NamedUser:
        return self._resolved_by.value

    @property
    def secret(self) -> str:
        return self._secret.value

    @property
    def secret_type(self) -> str:
        return self._secret_type.value

    @property
    def secret_type_display_name(self) -> str:
        return self._secret_type_display_name.value

    @property
    def state(self) -> str:
        return self._state.value

    @property
    def updated_at(self) -> str:
        return self._updated_at.value

    @property
    def url(self) -> str:
        return self._url.value

    def _initAttributes(self) -> None:
        self._created_at: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._locations_url: Attribute[str] = NotSet
        self._number: Attribute[int] = NotSet
        self._push_protection_bypassed: Attribute[bool] = NotSet
        self._push_protection_bypassed_at: Attribute[str] = NotSet
        self._push_protection_bypassed_by: Attribute[github.NamedUser.NamedUser] = NotSet
        self._resolution: Attribute[str] = NotSet
        self._resolution_comment: Attribute[str] = NotSet
        self._resolved_at: Attribute[str] = NotSet
        self._resolved_by: Attribute[github.NamedUser.NamedUser] = NotSet
        self._secret: Attribute[str] = NotSet
        self._secret_type: Attribute[str] = NotSet
        self._secret_type_display_name: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._updated_at: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeStringAttribute(attributes["created_at"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "locations_url" in attributes:  # pragma no branch
            self._locations_url = self._makeStringAttribute(attributes["locations_url"])
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "push_protection_bypassed" in attributes:  # pragma no branch
            self._push_protection_bypassed = self._makeBoolAttribute(attributes["push_protection_bypassed"])
        if "push_protection_bypassed_at" in attributes:  # pragma no branch
            self._push_protection_bypassed_at = self._makeStringAttribute(attributes["push_protection_bypassed_at"])
        if "push_protection_bypassed_by" in attributes:  # pragma no branch
            self._push_protection_bypassed_by = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["push_protection_bypassed_by"]
            )
        if "resolution" in attributes:  # pragma no branch
            self._resolution = self._makeStringAttribute(attributes["resolution"])
        if "resolution_comment" in attributes:  # pragma no branch
            self._resolution_comment = self._makeStringAttribute(attributes["resolution_comment"])
        if "resolved_at" in attributes:  # pragma no branch
            self._resolved_at = self._makeStringAttribute(attributes["resolved_at"])
        if "resolved_by" in attributes:  # pragma no branch
            self._resolved_by = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["resolved_by"])
        if "secret" in attributes:  # pragma no branch
            self._secret = self._makeStringAttribute(attributes["secret"])
        if "secret_type" in attributes:  # pragma no branch
            self._secret_type = self._makeStringAttribute(attributes["secret_type"])
        if "secret_type_display_name" in attributes:  # pragma no branch
            self._secret_type_display_name = self._makeStringAttribute(attributes["secret_type_display_name"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeStringAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
