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
from typing import Any, Dict, Union

from github.GithubObject import CompletableGithubObject, NotSet, _NotSetType
from github.NamedEnterpriseUser import NamedEnterpriseUser
from github.PaginatedList import PaginatedList


class EnterpriseConsumedLicenses(CompletableGithubObject):
    """
    This class represents Enterprises. The reference can be found here https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses
    """

    def __repr__(self) -> str:
        return self.get__repr__({"login": self._login.value})

    @property
    def total_seats_consumed(self) -> int:
        return self._total_seats_consumed.value

    @property
    def total_seats_purchased(self) -> int:
        return self._total_seats_purchased.value

    @property
    def login(self) -> str:
        self._completeIfNotSet(self._login)
        return self._login.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def get_enterprise_users(
        self, filter_: Union[str, _NotSetType] = NotSet, role: Union[str, _NotSetType] = NotSet
    ) -> PaginatedList[NamedEnterpriseUser]:
        """
        :calls: `GET /enterprise/{enterprise}/consumed-licenses <https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses>`_
        """
        assert filter_ is NotSet or isinstance(filter_, str), filter_
        assert role is NotSet or isinstance(role, str), role

        url_parameters = {}
        if filter_ is not NotSet:
            url_parameters["filter"] = filter_
        if role is not NotSet:
            url_parameters["role"] = role
        return PaginatedList(NamedEnterpriseUser, self._requester, self.url, url_parameters, None, "users")

    def _initAttributes(self) -> None:
        self._total_seats_consumed = NotSet
        self._total_seats_purchased = NotSet
        self._login = NotSet
        self._url = NotSet

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "total_seats_consumed" in attributes:  # pragma no branch
            self._total_seats_consumed = self._makeIntAttribute(attributes["total_seats_consumed"])
        if "total_seats_purchased" in attributes:  # pragma no branch
            self._total_seats_purchased = self._makeIntAttribute(attributes["total_seats_purchased"])
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
