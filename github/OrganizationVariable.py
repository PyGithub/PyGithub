############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Mauricio Alejandro Martínez Pacheco <mauricio.martinez@premise.com>#
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

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import github.Repository
from github.GithubObject import Attribute, NotSet
from github.PaginatedList import PaginatedList
from github.Variable import Variable

if TYPE_CHECKING:
    from github.Repository import Repository


class OrganizationVariable(Variable):
    """
    This class represents a org level GitHub variable.

    The reference can be found here
    https://docs.github.com/en/rest/actions/variables

    The OpenAPI schema can be found at

    - /components/schemas/organization-actions-variable

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._selected_repositories_url: Attribute[str] = NotSet
        self._visibility: Attribute[str] = NotSet

    @property
    def selected_repositories(self) -> PaginatedList[Repository]:
        return PaginatedList(
            github.Repository.Repository,
            self._requester,
            self.selected_repositories_url,
            None,
            list_item="repositories",
        )

    @property
    def selected_repositories_url(self) -> str:
        self._completeIfNotSet(self._selected_repositories_url)
        return self._selected_repositories_url.value

    @property
    def visibility(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._visibility)
        return self._visibility.value

    def edit(
        self,
        value: str,
        visibility: str = "all",
    ) -> bool:
        """
        :calls: `PATCH /orgs/{org}/actions/variables/{name} <https://docs.github.com/en/rest/reference/actions/variables#update-an-organization-variable>`_
        :param variable_name: string
        :param value: string
        :param visibility: string
        :rtype: bool
        """
        assert isinstance(value, str), value
        assert isinstance(visibility, str), visibility

        patch_parameters: dict[str, Any] = {
            "name": self.name,
            "value": value,
            "visibility": visibility,
        }

        status, _, _ = self._requester.requestJson(
            "PATCH",
            self.url,
            input=patch_parameters,
        )
        return status == 204

    def add_repo(self, repo: Repository) -> bool:
        """
        :calls: `PUT /orgs/{org}/actions/variables/{name}/repositories/{repository_id} <https://docs.github.com/en/rest/actions/variables#add-selected-repository-to-an-organization-secret>`_
        :param repo: github.Repository.Repository
        :rtype: bool
        """
        if self.visibility != "selected":
            return False
        self._requester.requestJsonAndCheck("PUT", f"{self._selected_repositories_url.value}/{repo.id}")
        return True

    def remove_repo(self, repo: Repository) -> bool:
        """
        :calls: `DELETE /orgs/{org}/actions/variables/{name}/repositories/{repository_id} <https://docs.github.com/en/rest/actions/variables#add-selected-repository-to-an-organization-secret>`_
        :param repo: github.Repository.Repository
        :rtype: bool
        """
        if self.visibility != "selected":
            return False
        self._requester.requestJsonAndCheck("DELETE", f"{self._selected_repositories_url.value}/{repo.id}")
        return True

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "selected_repositories_url" in attributes:
            self._selected_repositories_url = self._makeStringAttribute(attributes["selected_repositories_url"])
        if "visibility" in attributes:
            self._visibility = self._makeStringAttribute(attributes["visibility"])
