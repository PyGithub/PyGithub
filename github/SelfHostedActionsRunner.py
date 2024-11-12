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
# Copyright 2020 Victor Zeng <zacker150@users.noreply.github.com>              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class SelfHostedActionsRunner(NonCompletableGithubObject):
    """
    This class represents Self-hosted GitHub Actions Runners.

    The reference can be found at
    https://docs.github.com/en/free-pro-team@latest/rest/reference/actions#self-hosted-runners

    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._os: Attribute[str] = NotSet
        self._status: Attribute[str] = NotSet
        self._busy: Attribute[bool] = NotSet
        self._labels: Attribute[list[dict[str, int | str]]] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def os(self) -> str:
        return self._os.value

    @property
    def status(self) -> str:
        return self._status.value

    @property
    def busy(self) -> bool:
        return self._busy.value

    def labels(self) -> list[dict[str, int | str]]:
        return self._labels.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "os" in attributes:  # pragma no branch
            self._os = self._makeStringAttribute(attributes["os"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
        if "busy" in attributes:
            self._busy = self._makeBoolAttribute(attributes["busy"])
        if "labels" in attributes:
            self._labels = self._makeListOfDictsAttribute(attributes["labels"])
