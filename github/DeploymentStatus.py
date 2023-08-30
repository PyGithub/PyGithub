############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Colby Gallup <colbygallup@gmail.com>                          #
# Copyright 2020 Pascal Hofmann <mail@pascalhofmann.de>                        #
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

import github.NamedUser
from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class DeploymentStatus(CompletableGithubObject):
    """
    This class represents Deployment Statuses. The reference can be found here https://docs.github.com/en/rest/reference/repos#deployments
    """

    def _initAttributes(self) -> None:
        self._created_at: Attribute[datetime] = NotSet
        self._creator: Attribute[github.NamedUser.NamedUser] = NotSet
        self._deployment_url: Attribute[str] = NotSet
        self._description: Attribute[str] = NotSet
        self._environment: Attribute[str] = NotSet
        self._environment_url: Attribute[str] = NotSet
        self._repository_url: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._target_url: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._node_id: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "url": self._url.value})

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def creator(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._creator)
        return self._creator.value

    @property
    def deployment_url(self) -> str:
        self._completeIfNotSet(self._deployment_url)
        return self._deployment_url.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def environment(self) -> str:
        self._completeIfNotSet(self._environment)
        return self._environment.value

    @property
    def environment_url(self) -> str:
        self._completeIfNotSet(self._environment_url)
        return self._environment_url.value

    @property
    def repository_url(self) -> str:
        self._completeIfNotSet(self._repository_url)
        return self._repository_url.value

    @property
    def state(self) -> str:
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def target_url(self) -> str:
        self._completeIfNotSet(self._target_url)
        return self._target_url.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "environment_url" in attributes:  # pragma no branch
            self._environment_url = self._makeStringAttribute(attributes["environment_url"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "creator" in attributes:  # pragma no branch
            self._creator = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["creator"])
        if "deployment_url" in attributes:  # pragma no branch
            self._deployment_url = self._makeStringAttribute(attributes["deployment_url"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "environment" in attributes:  # pragma no branch
            self._environment = self._makeStringAttribute(attributes["environment"])
        if "repository_url" in attributes:  # pragma no branch
            self._repository_url = self._makeStringAttribute(attributes["repository_url"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "target_url" in attributes:  # pragma no branch
            self._target_url = self._makeStringAttribute(attributes["target_url"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
