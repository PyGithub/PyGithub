############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Mark Amery <markamery@btinternet.com>                         #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 YugoHino <henom06@gmail.com>                                  #
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

from datetime import datetime
from typing import TYPE_CHECKING, Any

from typing_extensions import deprecated

import github.EnterpriseConsumedLicenses
import github.Requester
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet, is_defined, is_undefined

if TYPE_CHECKING:
    from github.EnterpriseConsumedLicenses import EnterpriseConsumedLicenses
    from github.Requester import Requester


class Enterprise(NonCompletableGithubObject):
    """
    This class represents Enterprises.

    The reference can be found here
    https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin

    The OpenAPI schema can be found at

    - /components/schemas/enterprise

    """

    def _initAttributes(self) -> None:
        self._avatar_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._description: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._slug: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._website_url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"slug": self._slug.value})

    @property
    def avatar_url(self) -> str:
        return self._avatar_url.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    @deprecated("Use slug instead")
    def enterprise(self) -> str:
        # alias for slug
        return self._slug.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def node_id(self) -> str:
        return self._node_id.value

    @property
    def slug(self) -> str:
        return self._slug.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def url(self) -> str:
        if is_undefined(self._url) and is_defined(self._slug):
            self._url = self._makeStringAttribute(f"/enterprises/{self.slug}")
        return self._url.value

    @property
    def website_url(self) -> str:
        return self._website_url.value

    @staticmethod
    def from_slug(requester: Requester, slug: str) -> Enterprise:
        return github.Enterprise.Enterprise(requester, {}, {"slug": slug})

    def get_consumed_licenses(self) -> EnterpriseConsumedLicenses:
        """
        :calls: `GET /enterprises/{enterprise}/consumed-licenses <https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses>`_
        """
        headers, data = self._requester.requestJsonAndCheck("GET", self.url + "/consumed-licenses")
        if "url" not in data:
            data["url"] = self.url + "/consumed-licenses"

        return github.EnterpriseConsumedLicenses.EnterpriseConsumedLicenses(
            self._requester, headers, data, completed=True
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "avatar_url" in attributes:  # pragma no branch
            self._avatar_url = self._makeStringAttribute(attributes["avatar_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "slug" in attributes:  # pragma no branch
            self._slug = self._makeStringAttribute(attributes["slug"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "website_url" in attributes:  # pragma no branch
            self._website_url = self._makeStringAttribute(attributes["website_url"])
