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

from typing import Any, Dict

import github
import github.GithubObject
import github.Repository
from github.GithubObject import CompletableGithubObject


class Variable(CompletableGithubObject):
    """
    This class represents a GitHub variable. The reference can be found here https://docs.github.com/en/rest/actions/variables
    """

    def __repr__(self):
        return self.get__repr__({"name": self.name})

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def value(self):
        """
        :type: string
        """
        self._completeIfNotSet(self.value)
        return self._value.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    def edit(self, variable_name: str, value: str) -> bool:
        """
        :calls: `PATCH /repos/{owner}/{repo}/actions/variables/{variable_name} <https://docs.github.com/en/rest/reference/actions/variables#update-a-repository-variable>`_
        :param variable_name: string
        :param value: string
        :rtype: bool
        """
        assert isinstance(variable_name, str), variable_name
        assert isinstance(value, str), value
        patch_parameters = {
            "name": variable_name,
            "value": value,
        }
        status, headers, data = self._requester.requestJson(
            "PATCH",
            f"{self.url}/actions/variables/{variable_name}",
            input=patch_parameters,
        )
        return github.Variable.Variable(self._requester, headers, data, completed=True)

    def delete(self) -> None:
        """
        :calls: `DELETE {variable_url} <https://docs.github.com/en/rest/actions/variables>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def _initAttributes(self) -> None:
        self._name = github.GithubObject.NotSet
        self._value = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
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
