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
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Eric Nieuwland <eric.nieuwland@gmail.com>                     #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Joseph Henrich <crimsonknave@gmail.com>                       #
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

from decimal import Decimal
from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CVSS(NonCompletableGithubObject):
    """
    This class represents a CVSS.

    The reference can be found here
    <https://docs.github.com/en/rest/security-advisories/global-advisories>

    """

    def _initAttributes(self) -> None:
        self._score: Attribute[Decimal] = NotSet
        self._vector_string: Attribute[str] = NotSet
        self._version: Attribute[Decimal] = NotSet

    @property
    def score(self) -> Decimal:
        return self._score.value

    @property
    def vector_string(self) -> str:
        return self._vector_string.value

    @property
    def version(self) -> Decimal:
        return self._version.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "score" in attributes and attributes["score"] is not None:  # pragma no branch
            # ensure string so we don't have all the float extra nonsense
            self._score = self._makeDecimalAttribute(Decimal(str(attributes["score"])))
        if "vector_string" in attributes and attributes["vector_string"] is not None:  # pragma no branch
            self._vector_string = self._makeStringAttribute(attributes["vector_string"])
            self._version = self._makeDecimalAttribute(Decimal(self.vector_string.split(":")[1].split("/")[0]))
