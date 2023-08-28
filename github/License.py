############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
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

from typing import Any

from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class License(CompletableGithubObject):
    """
    This class represents Licenses. The reference can be found here https://docs.github.com/en/rest/reference/licenses
    """

    def _initAttributes(self) -> None:
        self._key: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._spdx_id: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._description: Attribute[str] = NotSet
        self._implementation: Attribute[str] = NotSet
        self._body: Attribute[str] = NotSet
        self._permissions: Attribute[list[str]] = NotSet
        self._conditions: Attribute[list[str]] = NotSet
        self._limitations: Attribute[list[str]] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def key(self) -> str:
        self._completeIfNotSet(self._key)
        return self._key.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def spdx_id(self) -> str:
        self._completeIfNotSet(self._spdx_id)
        return self._spdx_id.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def implementation(self) -> str:
        self._completeIfNotSet(self._implementation)
        return self._implementation.value

    @property
    def body(self) -> str:
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def permissions(self) -> list[str]:
        self._completeIfNotSet(self._permissions)
        return self._permissions.value

    @property
    def conditions(self) -> list[str]:
        self._completeIfNotSet(self._conditions)
        return self._conditions.value

    @property
    def limitations(self) -> list[str]:
        self._completeIfNotSet(self._limitations)
        return self._limitations.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "key" in attributes:  # pragma no branch
            self._key = self._makeStringAttribute(attributes["key"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "spdx_id" in attributes:  # pragma no branch
            self._spdx_id = self._makeStringAttribute(attributes["spdx_id"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "implementation" in attributes:  # pragma no branch
            self._implementation = self._makeStringAttribute(attributes["implementation"])
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeListOfStringsAttribute(attributes["permissions"])
        if "conditions" in attributes:  # pragma no branch
            self._conditions = self._makeListOfStringsAttribute(attributes["conditions"])
        if "limitations" in attributes:  # pragma no branch
            self._limitations = self._makeListOfStringsAttribute(attributes["limitations"])
