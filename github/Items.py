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

from typing import TYPE_CHECKING, Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.GithubObject import NonCompletableGithubObject


class Items(NonCompletableGithubObject):
    """
    This class represents Items.

    The reference can be found here
    https://docs.github.com/en/rest

    The OpenAPI schema can be found at
    - /components/schemas/search-result-text-matches/items

    """

    def _initAttributes(self) -> None:
        # TODO: remove if parent does not implement this
        super()._initAttributes()
        self._fragment: Attribute[str] = NotSet
        self._matches: Attribute[list[dict[str, Any]]] = NotSet
        self._object_type: Attribute[str] = NotSet
        self._object_url: Attribute[str] = NotSet
        self._property: Attribute[str] = NotSet

    def __repr__(self) -> str:
        # TODO: replace "some_attribute" with uniquely identifying attributes in the dict, then run:
        return self.get__repr__({"some_attribute": self._some_attribute.value})

    @property
    def fragment(self) -> str:
        return self._fragment.value

    @property
    def matches(self) -> list[dict[str, Any]]:
        return self._matches.value

    @property
    def object_type(self) -> str:
        return self._object_type.value

    @property
    def object_url(self) -> str:
        return self._object_url.value

    @property
    def property(self) -> str:
        return self._property.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        # TODO: remove if parent does not implement this
        super()._useAttributes(attributes)
        if "fragment" in attributes:  # pragma no branch
            self._fragment = self._makeStringAttribute(attributes["fragment"])
        if "matches" in attributes:  # pragma no branch
            self._matches = self._makeListOfDictsAttribute(attributes["matches"])
        if "object_type" in attributes:  # pragma no branch
            self._object_type = self._makeStringAttribute(attributes["object_type"])
        if "object_url" in attributes:  # pragma no branch
            self._object_url = self._makeStringAttribute(attributes["object_url"])
        if "property" in attributes:  # pragma no branch
            self._property = self._makeStringAttribute(attributes["property"])
