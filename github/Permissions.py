############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 karsten-wagner <39054096+karsten-wagner@users.noreply.github.com>#
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class Permissions(NonCompletableGithubObject):
    """
    This class represents Permissions.

    The OpenAPI schema can be found at
    - /components/schemas/collaborator/properties/permissions
    - /components/schemas/full-repository/properties/permissions
    - /components/schemas/minimal-repository/properties/permissions
    - /components/schemas/nullable-repository/properties/permissions
    - /components/schemas/repo-search-result-item/properties/permissions
    - /components/schemas/repository/properties/permissions
    - /components/schemas/team/properties/permissions

    """

    def _initAttributes(self) -> None:
        self._admin: Attribute[bool] = NotSet
        self._maintain: Attribute[bool] = NotSet
        self._pull: Attribute[bool] = NotSet
        self._push: Attribute[bool] = NotSet
        self._triage: Attribute[bool] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "admin": self._admin.value,
                "maintain": self._maintain.value,
                "pull": self._pull.value,
                "push": self._push.value,
                "triage": self._triage.value,
            }
        )

    @property
    def admin(self) -> bool:
        return self._admin.value

    @property
    def maintain(self) -> bool:
        return self._maintain.value

    @property
    def pull(self) -> bool:
        return self._pull.value

    @property
    def push(self) -> bool:
        return self._push.value

    @property
    def triage(self) -> bool:
        return self._triage.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "admin" in attributes:  # pragma no branch
            self._admin = self._makeBoolAttribute(attributes["admin"])
        if "maintain" in attributes:  # pragma no branch
            self._maintain = self._makeBoolAttribute(attributes["maintain"])
        if "pull" in attributes:  # pragma no branch
            self._pull = self._makeBoolAttribute(attributes["pull"])
        if "push" in attributes:  # pragma no branch
            self._push = self._makeBoolAttribute(attributes["push"])
        if "triage" in attributes:  # pragma no branch
            self._triage = self._makeBoolAttribute(attributes["triage"])
