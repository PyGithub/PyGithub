# FILE AUTO GENERATED DO NOT TOUCH
############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Matt Babineau <mbabineau@dataxu.com>                          #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Martijn Koster <mak-github@greenhills.co.uk>                  #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Pavan Kunisetty <nagapavan@users.noreply.github.com>          #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
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

from typing import Any

from . import NamedUser, Organization
from .GithubObject import Attribute, CompletableGithubObject, NotSet


class Membership(CompletableGithubObject):
    """
    This class represents Membership of an organization.

    The reference can be found here
    https://docs.github.com/en/rest/reference/orgs

    The OpenAPI schema can be found at

    - /components/schemas/org-membership
    - /components/schemas/team-membership

    """

    def _initAttributes(self) -> None:
        self._direct_membership: Attribute[bool] = NotSet
        self._enterprise_teams_providing_indirect_membership: Attribute[list[str]] = NotSet
        self._organization: Attribute[Organization.Organization] = NotSet
        self._organization_url: Attribute[str] = NotSet
        self._permissions: Attribute[dict[str, Any]] = NotSet
        self._role: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet
        self._user: Attribute[NamedUser.NamedUser] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"url": self._url.value})

    @property
    async def direct_membership(self) -> bool:
        await self._completeIfNotSet(self._direct_membership)
        return self._direct_membership.value

    @property
    async def enterprise_teams_providing_indirect_membership(self) -> list[str]:
        await self._completeIfNotSet(self._enterprise_teams_providing_indirect_membership)
        return self._enterprise_teams_providing_indirect_membership.value

    @property
    async def organization(self) -> Organization.Organization:
        await self._completeIfNotSet(self._organization)
        return self._organization.value

    @property
    async def organization_url(self) -> str:
        await self._completeIfNotSet(self._organization_url)
        return self._organization_url.value

    @property
    async def permissions(self) -> dict[str, Any]:
        await self._completeIfNotSet(self._permissions)
        return self._permissions.value

    @property
    async def role(self) -> str:
        await self._completeIfNotSet(self._role)
        return self._role.value

    @property
    async def state(self) -> str:
        await self._completeIfNotSet(self._state)
        return self._state.value

    @property
    async def url(self) -> str:
        await self._completeIfNotSet(self._url)
        return self._url.value

    @property
    async def user(self) -> NamedUser.NamedUser:
        await self._completeIfNotSet(self._user)
        return self._user.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "direct_membership" in attributes:  # pragma no branch
            self._direct_membership = self._makeBoolAttribute(attributes["direct_membership"])
        if "enterprise_teams_providing_indirect_membership" in attributes:  # pragma no branch
            self._enterprise_teams_providing_indirect_membership = self._makeListOfStringsAttribute(
                attributes["enterprise_teams_providing_indirect_membership"]
            )
        if "organization" in attributes:  # pragma no branch
            self._organization = self._makeClassAttribute(Organization.Organization, attributes["organization"])
        if "organization_url" in attributes:  # pragma no branch
            self._organization_url = self._makeStringAttribute(attributes["organization_url"])
        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeDictAttribute(attributes["permissions"])
        if "role" in attributes:  # pragma no branch
            self._role = self._makeStringAttribute(attributes["role"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(NamedUser.NamedUser, attributes["user"])
