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
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

from typing import Any

from github.GithubObject import Attribute, CompletableGithubObjectWithPaginatedProperty, NotSet
from github.NamedEnterpriseUser import NamedEnterpriseUser
from github.PaginatedList import PaginatedList


class EnterpriseConsumedLicenses(CompletableGithubObjectWithPaginatedProperty):
    """
    This class represents license consumed by enterprises.

    The reference can be found here
    https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._enterprise: Attribute[str] = NotSet
        self._total_seats_consumed: Attribute[int] = NotSet
        self._total_seats_purchased: Attribute[int] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"enterprise": self._enterprise.value})

    @property
    def enterprise(self) -> str:
        self._completeIfNotSet(self._enterprise)
        return self._enterprise.value

    @property
    def total_seats_consumed(self) -> int:
        return self._total_seats_consumed.value

    @property
    def total_seats_purchased(self) -> int:
        return self._total_seats_purchased.value

    @property
    def users(self) -> PaginatedList[NamedEnterpriseUser]:
        """
        Identical to calling :meth:`github.Commit.Commit.get_files` except that this uses the pagination given when
        getting this EnterpriseConsumedLicenses object (see
        :meth:`github.Enterprise.Enterprise.get_consumed_licenses`).

        A first page of users is retrieved when calling :meth:`github.Enterprise.Enterprise.get_consumed_licenses`.
        Subsequent pages of the same size are retrieved while iterating over this :class:`github.PaginatedList.PaginatedList`.
        In contrast, :meth:`github.EnterpriseConsumedLicenses.EnterpriseConsumedLicenses.get_users` ignores that exiting first page of users.

        """
        return PaginatedList(
            NamedEnterpriseUser,
            self._requester,
            self.url,
            self._pagination_parameters,
            headers=None,
            list_item="users",
            firstData=self.raw_data,
            firstHeaders=self.raw_headers,
        )

    def get_users(self, licence_users_per_page: int | None = None) -> PaginatedList[NamedEnterpriseUser]:
        """
        :calls: `GET /enterprises/{enterprise}/consumed-licenses <https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses>`_

        Identical to calling :meth:`github.EnterpriseConsumedLicenses.EnterpriseConsumedLicenses.users` except that this uses the given pagination.
        Any existing users retrieved together with this EnterpriseConsumedLicenses object are ignored.

        See :meth:`github.EnterpriseConsumedLicenses.EnterpriseConsumedLicenses.users` for more details.

        :param licence_users_per_page: int Number of users retrieved per page.
               Iterating over the users will fetch pages of this size. The default page size is 30, the maximum is 100.
        """
        return PaginatedList(
            NamedEnterpriseUser,
            self._requester,
            self.url,
            self._pagination_parameters_with(page=1, per_page=licence_users_per_page),
            headers=None,
            list_item="users",
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "enterprise" in attributes:  # pragma no branch
            self._enterprise = self._makeStringAttribute(attributes["enterprise"])
        if "total_seats_consumed" in attributes:  # pragma no branch
            self._total_seats_consumed = self._makeIntAttribute(attributes["total_seats_consumed"])
        if "total_seats_purchased" in attributes:  # pragma no branch
            self._total_seats_purchased = self._makeIntAttribute(attributes["total_seats_purchased"])
