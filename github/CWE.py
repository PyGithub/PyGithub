############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Jonathan Leitschuh <Jonathan.Leitschuh@gmail.com>             #
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

from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class CWE(CompletableGithubObject):
    """
    This class represents a CWE.
    The reference can be found here https://docs.github.com/en/rest/security-advisories/repository-advisories
    """

    def _initAttributes(self) -> None:
        self._cwe_id: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet

    @property
    def cwe_id(self) -> str:
        return self._cwe_id.value

    @property
    def name(self) -> str:
        return self._name.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "cwe_id" in attributes:  # pragma no branch
            self._cwe_id = self._makeStringAttribute(attributes["cwe_id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
