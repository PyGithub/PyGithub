############################ Copyrights and license ############################
#                                                                              #
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


class PagesSource(NonCompletableGithubObject):
    """
    This class represents the branch and directory a GitHub Pages site is published from.

    The reference can be found here
    https://docs.github.com/en/rest/pages/pages#get-a-github-pages-site

    The OpenAPI schema can be found at

    - /components/schemas/pages-source-hash

    """

    def _initAttributes(self) -> None:
        self._branch: Attribute[str] = NotSet
        self._path: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"branch": self._branch.value, "path": self._path.value})

    @property
    def branch(self) -> str:
        return self._branch.value

    @property
    def path(self) -> str:
        return self._path.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "branch" in attributes:  # pragma no branch
            self._branch = self._makeStringAttribute(attributes["branch"])
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
