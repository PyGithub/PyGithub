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

from datetime import datetime
from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class PagesHttpsCertificate(NonCompletableGithubObject):
    """
    This class represents the HTTPS certificate of a GitHub Pages site.

    The reference can be found here
    https://docs.github.com/en/rest/pages/pages#get-a-github-pages-site

    The OpenAPI schema can be found at

    - /components/schemas/pages-https-certificate

    """

    def _initAttributes(self) -> None:
        self._description: Attribute[str] = NotSet
        self._domains: Attribute[list[str]] = NotSet
        self._expires_at: Attribute[datetime] = NotSet
        self._state: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"state": self._state.value})

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def domains(self) -> list[str]:
        return self._domains.value

    @property
    def expires_at(self) -> datetime:
        return self._expires_at.value

    @property
    def state(self) -> str:
        return self._state.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "domains" in attributes:  # pragma no branch
            self._domains = self._makeListOfStringsAttribute(attributes["domains"])
        if "expires_at" in attributes:  # pragma no branch
            self._expires_at = self._makeDatetimeAttribute(attributes["expires_at"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
