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
import github.GithubObject
import github.PaginatedList
import github.NamedEnterpriseUser


class EnterpriseConsumedLicenses(github.GithubObject.CompletableGithubObject):
    """
    This class represents Enterprises. The reference can be found here https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses
    """

    def __repr__(self):
        return self.get__repr__({"login": self._login.value})

    @property
    def total_seats_consumed(self):
        """
        :type: int
        """
        return self._total_seats_consumed.value

    @property
    def total_seats_purchased(self):
        """
        :type: int
        """
        return self._total_seats_purchased.value

    @property
    def login(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._login)
        return self._login.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value


    def get_enterprise_users(
        self, filter_=github.GithubObject.NotSet, role=github.GithubObject.NotSet
    ):
        """
        :calls: `GET /enterprise/{enterprise}/consumed-licenses <https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses>`_
        :param filter_: string
        :param role: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.NamedEnterpriseUser.NamedEnterpriseUser`
        """
        assert filter_ is github.GithubObject.NotSet or isinstance(
            filter_, str
        ), filter_
        assert role is github.GithubObject.NotSet or isinstance(role, str), role

        url_parameters = {}
        if filter_ is not github.GithubObject.NotSet:
            url_parameters["filter"] = filter_
        if role is not github.GithubObject.NotSet:
            url_parameters["role"] = role
        return github.PaginatedList.PaginatedList(
            github.NamedEnterpriseUser.NamedEnterpriseUser,
            self._requester,
            self.url,
            url_parameters,
            None,
            "users"
        )

    def _initAttributes(self):
        self._total_seats_consumed = github.GithubObject.NotSet
        self._total_seats_purchased = github.GithubObject.NotSet
        self._login = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "total_seats_consumed" in attributes:  # pragma no branch
            self._total_seats_consumed = self._makeIntAttribute(attributes["total_seats_consumed"])
        if "total_seats_purchased" in attributes:  # pragma no branch
            self._total_seats_purchased = self._makeIntAttribute(attributes["total_seats_purchased"])
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
