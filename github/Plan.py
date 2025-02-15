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
# Copyright 2020 Geoff Low <glow@mdsol.com>                                    #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
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

from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class Plan(NonCompletableGithubObject):
    """
    This class represents Plans.

    The OpenAPI schema can be found at
    - /components/schemas/organization-full/properties/plan
    - /components/schemas/public-user/properties/plan
    - /components/schemas/team-organization/properties/plan

    """

    def _initAttributes(self) -> None:
        self._collaborators: Attribute[int] = NotSet
        self._filled_seats: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._private_repos: Attribute[int] = NotSet
        self._seats: Attribute[int] = NotSet
        self._space: Attribute[int] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def collaborators(self) -> int:
        return self._collaborators.value

    @property
    def filled_seats(self) -> int:
        return self._filled_seats.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def private_repos(self) -> int:
        return self._private_repos.value

    @property
    def seats(self) -> int:
        return self._seats.value

    @property
    def space(self) -> int:
        return self._space.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "collaborators" in attributes:  # pragma no branch
            self._collaborators = self._makeIntAttribute(attributes["collaborators"])
        if "filled_seats" in attributes:  # pragma no branch
            self._filled_seats = self._makeIntAttribute(attributes["filled_seats"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "private_repos" in attributes:  # pragma no branch
            self._private_repos = self._makeIntAttribute(attributes["private_repos"])
        if "seats" in attributes:  # pragma no branch
            self._seats = self._makeIntAttribute(attributes["seats"])
        if "space" in attributes:  # pragma no branch
            self._space = self._makeIntAttribute(attributes["space"])
