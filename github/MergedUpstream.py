############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Mikhail f. Shiryaev <mr.felixoid@gmail.com>                   #
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


class MergedUpstream(NonCompletableGithubObject):
    """
    This class represents a result of merge-upstream call.

    The OpenAPI schema can be found at
    - /components/schemas/merged-upstream

    """

    def _initAttributes(self) -> None:
        self._merge_type: Attribute[str] = NotSet
        self._base_branch: Attribute[str] = NotSet
        self._message: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"message": self._message.value})

    @property
    def merge_type(self) -> str:
        return self._merge_type.value

    @property
    def base_branch(self) -> str:
        return self._base_branch.value

    @property
    def message(self) -> str:
        return self._message.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "merge_type" in attributes:  # pragma no branch
            self._merge_type = self._makeStringAttribute(attributes["merge_type"])
        if "base_branch" in attributes:  # pragma no branch
            self._base_branch = self._makeStringAttribute(attributes["base_branch"])
        if "message" in attributes:  # pragma no branch
            self._message = self._makeStringAttribute(attributes["message"])
