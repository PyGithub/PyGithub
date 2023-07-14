############################ Copyrights and license ############################
#                                                                              #
# Copyright 2015 Dan Vanderkam <danvdk@gmail.com>                              #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
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

import github.NamedUser
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.NamedUser import NamedUser


class Stargazer(NonCompletableGithubObject):
    """
    This class represents Stargazers. The reference can be found here https://docs.github.com/en/rest/reference/activity#starring
    """

    def _initAttributes(self) -> None:
        self._starred_at: Attribute[datetime] = NotSet
        self._user: Attribute[NamedUser] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        # this is not a type error, just we didn't type `NamedUser` yet.
        # enable type checker here after we typed attribute of `NamedUser`
        return self.get__repr__({"user": self._user.value._login.value})  # type: ignore

    @property
    def starred_at(self) -> datetime:
        return self._starred_at.value

    @property
    def user(self) -> NamedUser:
        return self._user.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "starred_at" in attributes:
            self._starred_at = self._makeDatetimeAttribute(attributes["starred_at"])
        if "user" in attributes:
            self._user = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["user"])
