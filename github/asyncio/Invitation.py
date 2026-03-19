# FILE AUTO GENERATED DO NOT TOUCH
############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from . import NamedUser, Organization, Repository
from .GithubObject import Attribute, CompletableGithubObject, NotSet


class Invitation(CompletableGithubObject):
    """
    This class represents repository invitations.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#invitations

    The OpenAPI schema can be found at

    - /components/schemas/repository-invitation

    """

    def _initAttributes(self) -> None:
        self._created_at: Attribute[datetime] = NotSet
        self._expired: Attribute[bool] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._invitee: Attribute[NamedUser.NamedUser | Organization.Organization] = NotSet
        self._inviter: Attribute[NamedUser.NamedUser | Organization.Organization] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._permissions: Attribute[str] = NotSet
        self._repository: Attribute[Repository.Repository] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    async def created_at(self) -> datetime:
        await self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    async def expired(self) -> bool:
        await self._completeIfNotSet(self._expired)
        return self._expired.value

    @property
    async def html_url(self) -> str:
        await self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    async def id(self) -> int:
        await self._completeIfNotSet(self._id)
        return self._id.value

    @property
    async def invitee(self) -> NamedUser.NamedUser | Organization.Organization:
        await self._completeIfNotSet(self._invitee)
        return self._invitee.value

    @property
    async def inviter(self) -> NamedUser.NamedUser | Organization.Organization:
        await self._completeIfNotSet(self._inviter)
        return self._inviter.value

    @property
    async def node_id(self) -> str:
        await self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    async def permissions(self) -> str:
        await self._completeIfNotSet(self._permissions)
        return self._permissions.value

    @property
    async def repository(self) -> Repository.Repository:
        await self._completeIfNotSet(self._repository)
        return self._repository.value

    @property
    async def url(self) -> str:
        await self._completeIfNotSet(self._url)
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "expired" in attributes:  # pragma no branch
            self._expired = self._makeBoolAttribute(attributes["expired"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "invitee" in attributes:  # pragma no branch
            self._invitee = self._makeUnionClassAttributeFromTypeKey(
                "type",
                "User",
                attributes["invitee"],
                (NamedUser.NamedUser, "User"),
                (Organization.Organization, "Organization"),
            )
        if "inviter" in attributes:  # pragma no branch
            self._inviter = self._makeUnionClassAttributeFromTypeKey(
                "type",
                "User",
                attributes["inviter"],
                (NamedUser.NamedUser, "User"),
                (Organization.Organization, "Organization"),
            )
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])

        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeStringAttribute(attributes["permissions"])
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(Repository.Repository, attributes["repository"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
