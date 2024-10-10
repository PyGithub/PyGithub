############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Mauricio Alejandro Martínez Pacheco <mauricio.martinez@premise.com>#
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Thomas Crowley <15927917+thomascrowley@users.noreply.github.com>#
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

from datetime import datetime
from typing import Any, Dict

from github.GithubObject import Attribute, NotSet
from github.PaginatedList import PaginatedList
from github.Repository import Repository
from github.Secret import Secret


class OrganizationSecret(Secret):
    """
    This class represents a org level GitHub secret.

    The reference can be found here
    https://docs.github.com/en/rest/actions/secrets

    """

    def _initAttributes(self) -> None:
        self._name: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._visibility: Attribute[str] = NotSet
        self._selected_repositories: Attribute[PaginatedList[Repository]] = NotSet
        self._selected_repositories_url: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet

    @property
    def visibility(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._visibility)
        return self._visibility.value

    @property
    def selected_repositories(self) -> PaginatedList[Repository]:
        return PaginatedList(
            Repository,
            self._requester,
            self._selected_repositories_url.value,
            None,
            list_item="repositories",
        )

    def edit(
        self,
        value: str,
        visibility: str = "all",
        secret_type: str = "actions",
    ) -> bool:
        """
        :calls: `PATCH /orgs/{org}/{secret_type}/secrets/{variable_name} <https://docs.github.com/en/rest/reference/actions/secrets#update-an-organization-variable>`_
        :param variable_name: string
        :param value: string
        :param visibility: string
        :param secret_type: string options actions or dependabot
        :rtype: bool
        """
        assert isinstance(value, str), value
        assert isinstance(visibility, str), visibility
        assert secret_type in ["actions", "dependabot"], "secret_type should be actions or dependabot"

        patch_parameters: Dict[str, Any] = {
            "name": self.name,
            "value": value,
            "visibility": visibility,
        }

        status, _, _ = self._requester.requestJson(
            "PATCH",
            f"{self.url}/{secret_type}/secrets/{self.name}",
            input=patch_parameters,
        )
        return status == 204

    def add_repo(self, repo: Repository) -> bool:
        """
        :calls: 'PUT {org_url}/actions/secrets/{secret_name} <https://docs.github.com/en/rest/actions/secrets#add-selected-repository-to-an-organization-secret>`_
        :param repo: github.Repository.Repository
        :rtype: bool
        """
        if self.visibility != "selected":
            return False
        self._requester.requestJsonAndCheck("PUT", f"{self._selected_repositories_url.value}/{repo.id}")
        return True

    def remove_repo(self, repo: Repository) -> bool:
        """
        :calls: 'DELETE {org_url}/actions/secrets/{secret_name} <https://docs.github.com/en/rest/actions/secrets#add-selected-repository-to-an-organization-secret>`_
        :param repo: github.Repository.Repository
        :rtype: bool
        """
        if self.visibility != "selected":
            return False
        self._requester.requestJsonAndCheck("DELETE", f"{self._selected_repositories_url.value}/{repo.id}")
        return True

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "visibility" in attributes:
            self._visibility = self._makeStringAttribute(attributes["visibility"])
        if "selected_repositories_url" in attributes:
            self._selected_repositories_url = self._makeStringAttribute(attributes["selected_repositories_url"])
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
