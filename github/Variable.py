############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Mauricio Martinez <mauricio.martinez@premise.com>             #
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

from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class Variable(CompletableGithubObject):
    """
    This class represents a GitHub variable. The reference can be found here https://docs.github.com/en/rest/actions/variables
    """

    def _initAttributes(self) -> None:
        self._name: Attribute[str] = NotSet
        self._value: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self.name})

    @property
    def name(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def value(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._value)
        return self._value.value

    @property
    def created_at(self) -> datetime:
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self) -> datetime:
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        """
        :type: string
        """
        return self._url.value

    def edit(self, value: str) -> bool:
        """
        :calls: `PATCH /repos/{owner}/{repo}/actions/variables/{variable_name} <https://docs.github.com/en/rest/reference/actions/variables#update-a-repository-variable>`_
        :param variable_name: string
        :param value: string
        :rtype: bool
        """
        assert isinstance(value, str), value
        patch_parameters = {
            "name": self.name,
            "value": value,
        }
        status, _, _ = self._requester.requestJson(
            "PATCH",
            f"{self.url}/actions/variables/{self.name}",
            input=patch_parameters,
        )
        return status == 204

    def delete(self) -> None:
        """
        :calls: `DELETE {variable_url} <https://docs.github.com/en/rest/actions/variables>`_
        :rtype: None
        """
        self._requester.requestJsonAndCheck("DELETE", f"{self.url}/actions/variables/{self.name}")

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "value" in attributes:
            self._value = self._makeStringAttribute(attributes["value"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
