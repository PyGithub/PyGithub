############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Denis Blanchette <dblanchette@coveo.com>                      #
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
from typing import TYPE_CHECKING, Any

import github.NamedUser
import github.PaginatedList
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.NamedUser import NamedUser


class InstallationAuthorization(NonCompletableGithubObject):
    """
    This class represents InstallationAuthorizations.
    """

    def _initAttributes(self) -> None:
        self._token: Attribute[str] = NotSet
        self._expires_at: Attribute[datetime] = NotSet
        self._on_behalf_of: Attribute[NamedUser] = NotSet
        self._permissions: Attribute[dict] = NotSet
        self._repository_selection: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"expires_at": self._expires_at.value})

    @property
    def token(self) -> str:
        return self._token.value

    @property
    def expires_at(self) -> datetime:
        return self._expires_at.value

    @property
    def on_behalf_of(self) -> NamedUser:
        return self._on_behalf_of.value

    @property
    def permissions(self) -> dict:
        return self._permissions.value

    @property
    def repository_selection(self) -> str:
        return self._repository_selection.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "token" in attributes:  # pragma no branch
            self._token = self._makeStringAttribute(attributes["token"])
        if "expires_at" in attributes:  # pragma no branch
            self._expires_at = self._makeDatetimeAttribute(attributes["expires_at"])
        if "on_behalf_of" in attributes:  # pragma no branch
            self._on_behalf_of = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["on_behalf_of"])
        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeDictAttribute(attributes["permissions"])
        if "repository_selection" in attributes:  # pragma no branch
            self._repository_selection = self._makeStringAttribute(attributes["repository_selection"])
