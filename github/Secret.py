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

from datetime import datetime
from typing import Any

import github
import github.GithubObject
import github.Repository
from github.GithubObject import CompletableGithubObject


class Secret(CompletableGithubObject):
    """
    This class represents a GitHub secret. The reference can be found here https://docs.github.com/en/rest/actions/secrets
    """

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

    def delete(self) -> None:
        """
        :calls: `DELETE {secret_url} <https://docs.github.com/en/rest/actions/secrets>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def _initAttributes(self) -> None:
        self._name = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
