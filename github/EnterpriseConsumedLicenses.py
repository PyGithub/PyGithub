############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Yugo Hino <henom06@gmail.com>                                 #
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
from github.NamedEnterpriseUser import NamedEnterpriseUser
from github.PaginatedList import PaginatedList


class EnterpriseConsumedLicenses(CompletableGithubObject):
    """
    This class represents license consumed by enterprises. The reference can be found here https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses
    """

    def _initAttributes(self) -> None:
        self._total_seats_consumed: Attribute[int] = NotSet
        self._total_seats_purchased: Attribute[int] = NotSet
        self._enterprise: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"enterprise": self._enterprise.value})

    @property
    def total_seats_consumed(self) -> int:
        return self._total_seats_consumed.value

    @property
    def total_seats_purchased(self) -> int:
        return self._total_seats_purchased.value

    @property
    def enterprise(self) -> str:
        self._completeIfNotSet(self._enterprise)
        return self._enterprise.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def get_users(self) -> PaginatedList[NamedEnterpriseUser]:
        """
        :calls: `GET /enterprises/{enterprise}/consumed-licenses <https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses>`_
        """

        url_parameters: Dict[str, Any] = {}
        return PaginatedList(
            NamedEnterpriseUser,
            self._requester,
            self.url,
            url_parameters,
            None,
            "users",
            self.raw_data,
            self.raw_headers,
        )

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "total_seats_consumed" in attributes:  # pragma no branch
            self._total_seats_consumed = self._makeIntAttribute(attributes["total_seats_consumed"])
        if "total_seats_purchased" in attributes:  # pragma no branch
            self._total_seats_purchased = self._makeIntAttribute(attributes["total_seats_purchased"])
        if "enterprise" in attributes:  # pragma no branch
            self._enterprise = self._makeStringAttribute(attributes["enterprise"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
