############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Eric Nieuwland <eric.nieuwland@gmail.com>                     #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 ReenigneArcher <42013603+ReenigneArcher@users.noreply.github.com>#
# Copyright 2025 Matthew Davis <35502728+matt-davis27@users.noreply.github.com>#
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
from typing import TYPE_CHECKING, Any

import github.CodeScanAlertInstance
import github.CodeScanRule
import github.CodeScanTool
import github.NamedUser
import github.Organization
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.CodeScanAlertInstance import CodeScanAlertInstance
    from github.CodeScanRule import CodeScanRule
    from github.CodeScanTool import CodeScanTool
    from github.NamedUser import NamedUser
    from github.Organization import Organization


class CodeScanAlert(NonCompletableGithubObject):
    """
    This class represents alerts from code scanning.

    The reference can be found here
    https://docs.github.com/en/rest/reference/code-scanning.

    The OpenAPI schema can be found at

    - /components/schemas/code-scanning-alert
    - /components/schemas/code-scanning-alert-items

    """

    def _initAttributes(self) -> None:
        self._assignees: Attribute[list[NamedUser]] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._dismissal_approved_by: Attribute[NamedUser | Organization] = NotSet
        self._dismissed_at: Attribute[datetime | None] = NotSet
        self._dismissed_by: Attribute[NamedUser | None] = NotSet
        self._dismissed_comment: Attribute[str | None] = NotSet
        self._dismissed_reason: Attribute[str | None] = NotSet
        self._fixed_at: Attribute[datetime | None] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._instances_url: Attribute[str] = NotSet
        self._most_recent_instance: Attribute[CodeScanAlertInstance] = NotSet
        self._number: Attribute[int] = NotSet
        self._rule: Attribute[CodeScanRule] = NotSet
        self._state: Attribute[str] = NotSet
        self._tool: Attribute[CodeScanTool] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"number": self.number, "id": self.rule.id})

    @property
    def assignees(self) -> list[NamedUser]:
        return self._assignees.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def dismissal_approved_by(self) -> NamedUser | Organization:
        return self._dismissal_approved_by.value

    @property
    def dismissed_at(self) -> datetime | None:
        return self._dismissed_at.value

    @property
    def dismissed_by(self) -> NamedUser | None:
        return self._dismissed_by.value

    @property
    def dismissed_comment(self) -> str | None:
        return self._dismissed_comment.value

    @property
    def dismissed_reason(self) -> str | None:
        return self._dismissed_reason.value

    @property
    def fixed_at(self) -> datetime | None:
        return self._fixed_at.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def instances_url(self) -> str:
        return self._instances_url.value

    @property
    def most_recent_instance(self) -> CodeScanAlertInstance:
        return self._most_recent_instance.value

    @property
    def number(self) -> int:
        return self._number.value

    @property
    def rule(self) -> CodeScanRule:
        return self._rule.value

    @property
    def state(self) -> str:
        return self._state.value

    @property
    def tool(self) -> CodeScanTool:
        return self._tool.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def url(self) -> str:
        return self._url.value

    def get_instances(self) -> PaginatedList[CodeScanAlertInstance]:
        """
        :calls: `GET /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances <https://docs.github.com/en/rest/code-scanning/code-scanning#list-instances-of-a-code-scanning-alert>`_
        """
        return PaginatedList(
            github.CodeScanAlertInstance.CodeScanAlertInstance,
            self._requester,
            self.instances_url,
            None,
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "assignees" in attributes:  # pragma no branch
            self._assignees = self._makeListOfClassesAttribute(github.NamedUser.NamedUser, attributes["assignees"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "dismissal_approved_by" in attributes:  # pragma no branch
            self._dismissal_approved_by = self._makeUnionClassAttributeFromTypeKey(
                "type",
                "User",
                attributes["dismissal_approved_by"],
                (github.NamedUser.NamedUser, "User"),
                (github.Organization.Organization, "Organization"),
            )
        if "dismissed_at" in attributes:  # pragma no branch
            self._dismissed_at = self._makeDatetimeAttribute(attributes["dismissed_at"])
        if "dismissed_by" in attributes:  # pragma no branch
            self._dismissed_by = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["dismissed_by"])
        if "dismissed_comment" in attributes:  # pragma no branch
            self._dismissed_comment = self._makeStringAttribute(attributes["dismissed_comment"])
        if "dismissed_reason" in attributes:  # pragma no branch
            self._dismissed_reason = self._makeStringAttribute(attributes["dismissed_reason"])
        if "fixed_at" in attributes:  # pragma no branch
            self._fixed_at = self._makeDatetimeAttribute(attributes["fixed_at"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "instances_url" in attributes:  # pragma no branch
            self._instances_url = self._makeStringAttribute(attributes["instances_url"])
        if "most_recent_instance" in attributes:  # pragma no branch
            self._most_recent_instance = self._makeClassAttribute(
                github.CodeScanAlertInstance.CodeScanAlertInstance,
                attributes["most_recent_instance"],
            )
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "rule" in attributes:  # pragma no branch
            self._rule = self._makeClassAttribute(github.CodeScanRule.CodeScanRule, attributes["rule"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "tool" in attributes:  # pragma no branch
            self._tool = self._makeClassAttribute(github.CodeScanTool.CodeScanTool, attributes["tool"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
