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

from github.GithubObject import (
    Attribute,
    CompletableGithubObject,
    NotSet,
    Opt,
    _NotSetType,
    is_defined,
    is_optional,
    is_optional_list,
    is_undefined,
)



class PackageVersion(CompletableGithubObject):
    """
    This class represents PackageVersions.

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
    def url(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def package_html_url(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._package_html_url)
        return self._package_html_url.value

    @property
    def license(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._license)
        return self._license.value

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

    @property
    def description(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def html_url(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def metadata(self) -> dict:
        """
        :type: dict
        """
        self._completeIfNotSet(self._metadata)
        return self._metadata.value

    def delete(self) -> None:
        self._requester.requestJsonAndCheck("DELETE", self.url)

    def restore(self) -> None:
        self._requester.requestJsonAndCheck("POST", self.url + "/restore")

    def _initAttributes(self):
        self._id: Opt[int] = NotSet
        self._name: Opt[str] = NotSet
        self._url: Opt[str] = NotSet
        self._package_html_url: Opt[str] = NotSet
        self._license: Opt[str] = NotSet
        self._created_at: Opt[str] = NotSet
        self._updated_at: Opt[str] = NotSet
        self._description: Opt[str] = NotSet
        self._html_url: Opt[str] = NotSet
        self._metadata: Opt[dict] = NotSet

    def _useAttributes(self, attributes: dict):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
        if "package_html_url" in attributes:
            self._package_html_url = self._makeStringAttribute(attributes["package_html_url"])
        if "license" in attributes:
            self._license = self._makeStringAttribute(attributes["license"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "description" in attributes:
            self._description = self._makeStringAttribute(attributes["description"])
        if "html_url" in attributes:
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "metadata" in attributes:
            self._metadata = self._makeDictAttribute(attributes["metadata"])
