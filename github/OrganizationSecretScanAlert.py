############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2026 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2026 Matt Davis <35502728+matt-davis27@users.noreply.github.com>   #
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

from typing import TYPE_CHECKING, Any

import github.NamedUser
import github.Organization
import github.Repository
from github.GithubObject import Attribute, NotSet
from github.SecretScanAlert import SecretScanAlert

if TYPE_CHECKING:
    from github.NamedUser import NamedUser
    from github.Organization import Organization
    from github.Repository import Repository


class OrganizationSecretScanAlert(SecretScanAlert):
    """
    This class represents a Secret Scanning Alert on an organization.

    The reference can be found here
    https://docs.github.com/en/rest/secret-scanning/secret-scanning#list-secret-scanning-alerts-for-an-organization

    The OpenAPI schema can be found at

    - /components/schemas/organization-secret-scanning-alert

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._closure_request_comment: Attribute[str] = NotSet
        self._closure_request_reviewer: Attribute[NamedUser | Organization] = NotSet
        self._closure_request_reviewer_comment: Attribute[str] = NotSet
        self._provider: Attribute[str] = NotSet
        self._provider_slug: Attribute[str] = NotSet
        self._repository: Attribute[Repository] = NotSet

    @property
    def closure_request_comment(self) -> str:
        return self._closure_request_comment.value

    @property
    def closure_request_reviewer(self) -> NamedUser | Organization:
        return self._closure_request_reviewer.value

    @property
    def closure_request_reviewer_comment(self) -> str:
        return self._closure_request_reviewer_comment.value

    @property
    def provider(self) -> str:
        return self._provider.value

    @property
    def provider_slug(self) -> str:
        return self._provider_slug.value

    @property
    def repository(self) -> Repository:
        return self._repository.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "closure_request_comment" in attributes:  # pragma no branch
            self._closure_request_comment = self._makeStringAttribute(attributes["closure_request_comment"])
        if "closure_request_reviewer" in attributes:  # pragma no branch
            self._closure_request_reviewer = self._makeUnionClassAttributeFromTypeKey(
                "type",
                "User",
                attributes["closure_request_reviewer"],
                (github.NamedUser.NamedUser, "User"),
                (github.Organization.Organization, "Organization"),
            )
        if "closure_request_reviewer_comment" in attributes:  # pragma no branch
            self._closure_request_reviewer_comment = self._makeStringAttribute(
                attributes["closure_request_reviewer_comment"]
            )
        if "provider" in attributes:  # pragma no branch
            self._provider = self._makeStringAttribute(attributes["provider"])
        if "provider_slug" in attributes:  # pragma no branch
            self._provider_slug = self._makeStringAttribute(attributes["provider_slug"])
        if "repository" in attributes:
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
