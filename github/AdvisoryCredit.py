############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Leitschuh <jonathan.leitschuh@gmail.com>             #
# Copyright 2023 Joseph Henrich <crimsonknave@gmail.com>                       #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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

from typing import Any, Union

from typing_extensions import TypedDict

import github.NamedUser
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class SimpleCredit(TypedDict):
    """
    A simple credit for a security advisory.
    """

    login: str | github.NamedUser.NamedUser
    type: str


Credit = Union[SimpleCredit, "AdvisoryCredit"]


class AdvisoryCredit(NonCompletableGithubObject):
    """
    This class represents a credit that is assigned to a SecurityAdvisory.

    The reference can be found here
    https://docs.github.com/en/rest/security-advisories/repository-advisories

    """

    @property
    def login(self) -> str:
        """
        :type: string
        """
        return self._login.value

    @property
    def type(self) -> str:
        """
        :type: string
        """
        return self._type.value

    def _initAttributes(self) -> None:
        self._login: Attribute[str] = NotSet
        self._type: Attribute[str] = NotSet

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])

    @staticmethod
    def _validate_credit(credit: Credit) -> None:
        assert isinstance(credit, (dict, AdvisoryCredit)), credit
        if isinstance(credit, dict):
            assert "login" in credit, credit
            assert "type" in credit, credit
            assert isinstance(credit["login"], (str, github.NamedUser.NamedUser)), credit["login"]
            assert isinstance(credit["type"], str), credit["type"]
        else:
            assert isinstance(credit.login, str), credit.login
            assert isinstance(credit.type, str), credit.type

    @staticmethod
    def _to_github_dict(credit: Credit) -> SimpleCredit:
        assert isinstance(credit, (dict, AdvisoryCredit)), credit
        if isinstance(credit, dict):
            assert "login" in credit, credit
            assert "type" in credit, credit
            assert isinstance(credit["login"], (str, github.NamedUser.NamedUser)), credit["login"]
            login = credit["login"]
            if isinstance(login, github.NamedUser.NamedUser):
                login = login.login
            return {
                "login": login,
                "type": credit["type"],
            }
        else:
            return {
                "login": credit.login,
                "type": credit.type,
            }
