############################ Copyrights and license ############################
#                                                                              #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

import github.GithubObject
import github.NamedUser
import github.Repository
from github.GithubObject import Attribute, CompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.NamedUser import NamedUser
    from github.Repository import Repository


class Invitation(CompletableGithubObject):
    """
    This class represents repository invitations. The reference can be found here https://docs.github.com/en/rest/reference/repos#invitations
    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._permissions: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._invitee: Attribute[NamedUser] = NotSet
        self._inviter: Attribute[NamedUser] = NotSet
        self._url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._repository: Attribute[Repository] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def permissions(self) -> str:
        self._completeIfNotSet(self._permissions)
        return self._permissions.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def invitee(self) -> NamedUser:
        self._completeIfNotSet(self._invitee)
        return self._invitee.value

    @property
    def inviter(self) -> NamedUser:
        self._completeIfNotSet(self._inviter)
        return self._inviter.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def repository(self) -> Repository:
        self._completeIfNotSet(self._repository)
        return self._repository.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "invitee" in attributes:  # pragma no branch
            self._invitee = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["invitee"])
        if "inviter" in attributes:  # pragma no branch
            self._inviter = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["inviter"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])

        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeStringAttribute(attributes["permissions"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
