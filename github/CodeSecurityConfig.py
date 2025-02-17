############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Bill Napier <napier@pobox.com>                                #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import annotations

from datetime import datetime
from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CodeSecurityConfig(NonCompletableGithubObject):
    """
    This class represents Configurations for Code Security.

    The reference can be found here
    https://docs.github.com/en/rest/code-security/configurations.

    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._advanced_security: Attribute[str] = NotSet
        self._code_scanning_default_setup: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._dependabot_alerts: Attribute[str] = NotSet
        self._dependabot_security_updates: Attribute[str] = NotSet
        self._dependency_graph: Attribute[str] = NotSet
        self._dependency_graph_autosubmit_action: Attribute[str] = NotSet
        self._description: Attribute[str] = NotSet
        self._enforcement: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._private_vulnerability_reporting: Attribute[str] = NotSet
        self._secret_scanning: Attribute[str] = NotSet
        self._secret_scanning_delegated_bypass: Attribute[str] = NotSet
        self._secret_scanning_non_provider_patterns: Attribute[str] = NotSet
        self._secret_scanning_push_protection: Attribute[str] = NotSet
        self._secret_scanning_validity_checks: Attribute[str] = NotSet
        self._target_type: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "id": self.id,
                "name": self.name,
                "description": self.description,
            }
        )

    @property
    def advanced_security(self) -> str:
        return self._advanced_security.value

    @property
    def code_scanning_default_setup(self) -> str:
        return self._code_scanning_default_setup.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def dependabot_alerts(self) -> str:
        return self._dependabot_alerts.value

    @property
    def dependabot_security_updates(self) -> str:
        return self._dependabot_security_updates.value

    @property
    def dependency_graph(self) -> str:
        return self._dependency_graph.value

    @property
    def dependency_graph_autosubmit_action(self) -> str:
        return self._dependency_graph_autosubmit_action.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def enforcement(self) -> str:
        return self._enforcement.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def private_vulnerability_reporting(self) -> str:
        return self._private_vulnerability_reporting.value

    @property
    def secret_scanning(self) -> str:
        return self._secret_scanning.value

    @property
    def secret_scanning_delegated_bypass(self) -> str:
        return self._secret_scanning_delegated_bypass.value

    @property
    def secret_scanning_non_provider_patterns(self) -> str:
        return self._secret_scanning_non_provider_patterns.value

    @property
    def secret_scanning_push_protection(self) -> str:
        return self._secret_scanning_push_protection.value

    @property
    def secret_scanning_validity_checks(self) -> str:
        return self._secret_scanning_validity_checks.value

    @property
    def target_type(self) -> str:
        return self._target_type.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def url(self) -> str:
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "advanced_security" in attributes:  # pragma no branch
            self._advanced_security = self._makeStringAttribute(attributes["advanced_security"])
        if "code_scanning_default_setup" in attributes:  # pragma no branch
            self._code_scanning_default_setup = self._makeStringAttribute(attributes["code_scanning_default_setup"])
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], str), attributes[
                "created_at"
            ]
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "dependabot_alerts" in attributes:  # pragma no branch
            self._dependabot_alerts = self._makeStringAttribute(attributes["dependabot_alerts"])
        if "dependabot_security_updates" in attributes:  # pragma no branch
            self._dependabot_security_updates = self._makeStringAttribute(attributes["dependabot_security_updates"])
        if "dependency_graph" in attributes:  # pragma no branch
            self._dependency_graph = self._makeStringAttribute(attributes["dependency_graph"])
        if "dependency_graph_autosubmit_action" in attributes:  # pragma no branch
            self._dependency_graph_autosubmit_action = self._makeStringAttribute(
                attributes["dependency_graph_autosubmit_action"]
            )
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "enforcement" in attributes:  # pragma no branch
            self._enforcement = self._makeStringAttribute(attributes["enforcement"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "private_vulnerability_reporting" in attributes:  # pragma no branch
            self._private_vulnerability_reporting = self._makeStringAttribute(
                attributes["private_vulnerability_reporting"]
            )
        if "secret_scanning" in attributes:  # pragma no branch
            self._secret_scanning = self._makeStringAttribute(attributes["secret_scanning"])
        if "secret_scanning_delegated_bypass" in attributes:  # pragma no branch
            self._secret_scanning_delegated_bypass = self._makeStringAttribute(
                attributes["secret_scanning_delegated_bypass"]
            )
        if "secret_scanning_non_provider_patterns" in attributes:  # pragma no branch
            self._secret_scanning_non_provider_patterns = self._makeStringAttribute(
                attributes["secret_scanning_non_provider_patterns"]
            )
        if "secret_scanning_push_protection" in attributes:  # pragma no branch
            self._secret_scanning_push_protection = self._makeStringAttribute(
                attributes["secret_scanning_push_protection"]
            )
        if "secret_scanning_validity_checks" in attributes:  # pragma no branch
            self._secret_scanning_validity_checks = self._makeStringAttribute(
                attributes["secret_scanning_validity_checks"]
            )
        if "target_type" in attributes:  # pragma no branch
            self._target_type = self._makeStringAttribute(attributes["target_type"])
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], str), attributes[
                "updated_at"
            ]
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
