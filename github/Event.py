############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
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

import github.GithubObject
import github.NamedUser
import github.Organization
import github.Repository
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class Event(NonCompletableGithubObject):
    """
    This class represents Events.

    The reference can be found here
    https://docs.github.com/en/rest/reference/activity#events

    The OpenAPI schema can be found at
    - /components/schemas/event

    """

    def _initAttributes(self) -> None:
        self._actor: Attribute[github.NamedUser.NamedUser] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._id: Attribute[str] = NotSet
        self._org: Attribute[github.Organization.Organization] = NotSet
        self._payload: Attribute[dict[str, Any]] = NotSet
        self._public: Attribute[bool] = NotSet
        self._repo: Attribute[github.Repository.Repository] = NotSet
        self._type: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "type": self._type.value})

    @property
    def actor(self) -> github.NamedUser.NamedUser:
        return self._actor.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def id(self) -> str:
        return self._id.value

    @property
    def org(self) -> github.Organization.Organization:
        return self._org.value

    @property
    def payload(self) -> dict[str, Any]:
        return self._payload.value

    @property
    def public(self) -> bool:
        return self._public.value

    @property
    def repo(self) -> github.Repository.Repository:
        return self._repo.value

    @property
    def type(self) -> str:
        return self._type.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "actor" in attributes:  # pragma no branch
            self._actor = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["actor"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        if "org" in attributes:  # pragma no branch
            self._org = self._makeClassAttribute(github.Organization.Organization, attributes["org"])
        if "payload" in attributes:  # pragma no branch
            self._payload = self._makeDictAttribute(attributes["payload"])
        if "public" in attributes:  # pragma no branch
            self._public = self._makeBoolAttribute(attributes["public"])
        if "repo" in attributes:  # pragma no branch
            self._repo = self._makeClassAttribute(github.Repository.Repository, attributes["repo"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
