############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Nick Campbell <nicholas.j.campbell@gmail.com>                 #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Marco Köpcke <hello@parakoopa.de>                             #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 alson <git@alm.nufan.net>                                     #
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

from typing import TYPE_CHECKING, Any

import github.EnvironmentProtectionRuleReviewer
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.EnvironmentProtectionRuleReviewer import EnvironmentProtectionRuleReviewer


class EnvironmentProtectionRule(NonCompletableGithubObject):
    """
    This class represents a protection rule for an environment.

    The reference can be found here
    https://docs.github.com/en/rest/reference/deployments#environments

    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._type: Attribute[str] = NotSet
        self._reviewers: Attribute[list[EnvironmentProtectionRuleReviewer]] = NotSet
        self._wait_timer: Attribute[int] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def node_id(self) -> str:
        return self._node_id.value

    @property
    def type(self) -> str:
        return self._type.value

    @property
    def reviewers(
        self,
    ) -> list[EnvironmentProtectionRuleReviewer]:
        return self._reviewers.value

    @property
    def wait_timer(self) -> int:
        return self._wait_timer.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
        if "reviewers" in attributes:  # pragma no branch
            self._reviewers = self._makeListOfClassesAttribute(
                github.EnvironmentProtectionRuleReviewer.EnvironmentProtectionRuleReviewer,
                attributes["reviewers"],
            )
        if "wait_timer" in attributes:  # pragma no branch
            self._wait_timer = self._makeIntAttribute(attributes["wait_timer"])
