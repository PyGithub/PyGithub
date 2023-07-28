############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 crimsonknave <crimsonknave@github.com>                        #
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

from decimal import Decimal

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CVSS(NonCompletableGithubObject):
    """
    This class represents a CVSS.
    The reference can be found here <https://docs.github.com/en/rest/security-advisories/global-advisories>
    """

    def _initAttributes(self) -> None:
        self._vector_string: Attribute[str] = NotSet
        self._score: Attribute[str] = NotSet

    @property
    def score(self) -> Decimal:
        return Decimal(self._score)

    @property
    def cvss_version(self) -> Decimal:
        return Decimal(self._vector_string.split(":")[0])

    @property
    def vector_string(self) -> str:
        return self._vector_string
