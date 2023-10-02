############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Justin Kufro <jkufro@andrew.cmu.edu>                          #
# Copyright 2018 Ivan Minno <iminno@andrew.cmu.edu>                            #
# Copyright 2018 Zilei Gu <zileig@andrew.cmu.edu>                              #
# Copyright 2018 Yves Zumbach <yzumbach@andrew.cmu.edu>                        #
# Copyright 2018 Leying Chen <leyingc@andrew.cmu.edu>                          #
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


class Referrer(NonCompletableGithubObject):
    """
    This class represents a popylar Referrer for a GitHub repository.
    The reference can be found here https://docs.github.com/en/rest/reference/repos#traffic
    """

    def _initAttributes(self) -> None:
        self._referrer: Attribute[str] = NotSet
        self._count: Attribute[int] = NotSet
        self._uniques: Attribute[int] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "referrer": self._referrer.value,
                "count": self._count.value,
                "uniques": self._uniques.value,
            }
        )

    @property
    def referrer(self) -> str:
        return self._referrer.value

    @property
    def count(self) -> int:
        return self._count.value

    @property
    def uniques(self) -> int:
        return self._uniques.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "referrer" in attributes:  # pragma no branch
            self._referrer = self._makeStringAttribute(attributes["referrer"])
        if "count" in attributes:  # pragma no branch
            self._count = self._makeIntAttribute(attributes["count"])
        if "uniques" in attributes:  # pragma no branch
            self._uniques = self._makeIntAttribute(attributes["uniques"])
