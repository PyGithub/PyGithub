############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Henkhogan <henkhogan@gmail.com>                               #
# Copyright 2025 Harrison Boyd <8950185+hboyd2003@users.noreply.github.com>    #
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
from enum import StrEnum, auto
from typing import Any, TYPE_CHECKING

import github.NamedUser
import github.Repository
from github.GithubObject import (
    Attribute,
    CompletableGithubObject,
    NotSet, Opt,
)
from github.PackageVersion import PackageVersion
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.NamedUser import NamedUser
    from github.Repository import Repository


class PackageType(StrEnum):
    NPM = auto()
    MAVEN = auto()
    RUBYGEMS = auto()
    DOCKER = auto()
    NUGET = auto()
    CONTAINER = auto()

class PackageVisibility(StrEnum):
    public = auto()
    private = auto()
    internal = auto()

class Package(CompletableGithubObject):
    """
    This class represents Packages.

    The reference can be found here
    https://docs.github.com/en/rest/packages/packages?apiVersion=latest#about-github-packages
    """

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def id(self) -> int:
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def package_type(self) -> PackageType:
        """
        :type: :class:`github.Package.PackageType`
        """
        self._completeIfNotSet(self._package_type)
        return self._package_type.value


    @property
    def url(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def html_url(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def version_count(self) -> int:
        """
        :type: integer
        """
        return self._version_count.value

    @property
    def visibility(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._visibility)
        return self._visibility.value

    @property
    def owner(self) -> NamedUser:
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._owner)
        return self._owner.value


    @property
    def repository(self) -> Repository:
        """
        :type: :class:`github.Repository.Repository`
        """
        return self._repository.value

    @property
    def created_at(self) -> datetime:
        """
        :type: datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self) -> datetime:
        """
        :type: datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    def delete(self):
        self._requester.requestJsonAndCheck("DELETE", f"{self.url}")

    def list_versions(self) -> PaginatedList[PackageVersion]:
        """
        :calls: `GET /packages/{package_type}/{package_name}/versions <https://docs.github.com/en/rest/reference/packages#get-a-package-version>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.PackageVersion.PackageVersion`
        """
        return PaginatedList(
            PackageVersion,
            self._requester,
            self.url + "/versions",
            None,
        )

    def get_version(self, package_version_id: int) -> PackageVersion:
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/versions/{package_version_id}")
        return PackageVersion(self._requester, headers, data, completed=True)

    def delete_version(self, package_version_id: int) -> None:
        self._requester.requestJsonAndCheck("DELETE", f"{self.url}/versions/{package_version_id}")

    def restore_version(self, package_version_id: int) -> None:
        self._requester.requestJsonAndCheck("POST", f"{self.url}/versions/{package_version_id}/restore")

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._package_type: Attribute[PackageType] = NotSet
        self._owner: Attribute[NamedUser] = NotSet
        self._version_count: Attribute[Opt[int]] = NotSet
        self._visibility: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._repository: Attribute[Opt[Repository]] = NotSet
        self._html_url: Attribute[str] = NotSet

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "package_type" in attributes:
            self._package_type = self._makeEnumAttribute(PackageType, attributes["package_type"])
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
        if "html_url" in attributes:
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "version_count" in attributes:
            self._version_count = self._makeIntAttribute(attributes["version_count"])
        if "visibility" in attributes:
            self._visibility = self._makeStringAttribute(attributes["visibility"])
        if "owner" in attributes:  # pragma no branch
            self._owner = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["owner"])
        if "repository" in attributes:
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])

        
