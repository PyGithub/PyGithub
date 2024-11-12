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
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Colby Gallup <colbygallup@gmail.com>                          #
# Copyright 2020 Mahesh Raju <coder@mahesh.net>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

import github.GithubObject
import github.NamedUser
from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class GithubApp(CompletableGithubObject):
    """
    This class represents github apps.

    The reference can be found here
    https://docs.github.com/en/rest/reference/apps

    """

    def _initAttributes(self) -> None:
        self._created_at: Attribute[datetime] = NotSet
        self._description: Attribute[str] = NotSet
        self._events: Attribute[list[str]] = NotSet
        self._external_url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._owner: Attribute[github.NamedUser.NamedUser] = NotSet
        self._permissions: Attribute[dict[str, str]] = NotSet
        self._slug: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "url": self._url.value})

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def events(self) -> list[str]:
        self._completeIfNotSet(self._events)
        return self._events.value

    @property
    def external_url(self) -> str:
        self._completeIfNotSet(self._external_url)
        return self._external_url.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def owner(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._owner)
        return self._owner.value

    @property
    def permissions(self) -> dict[str, str]:
        self._completeIfNotSet(self._permissions)
        return self._permissions.value

    @property
    def slug(self) -> str:
        self._completeIfNotSet(self._slug)
        return self._slug.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "events" in attributes:  # pragma no branch
            self._events = self._makeListOfStringsAttribute(attributes["events"])
        if "external_url" in attributes:  # pragma no branch
            self._external_url = self._makeStringAttribute(attributes["external_url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "owner" in attributes:  # pragma no branch
            self._owner = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["owner"])
        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeDictAttribute(attributes["permissions"])
        if "slug" in attributes:  # pragma no branch
            self._slug = self._makeStringAttribute(attributes["slug"])
            self._url = self._makeStringAttribute(f"/apps/{attributes['slug']}")
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
