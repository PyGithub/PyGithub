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
from github.GithubObject import CompletableGithubObject, NotSet
from github.EnterpriseConsumedLicenses import EnterpriseConsumedLicenses


class Enterprise(CompletableGithubObject):
    """
    This class represents Enterprises. The reference can be found here https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses
    """

    def __repr__(self) -> str:
        return self.get__repr__({"login": self._login.value})

    @property
    def login(self) -> str:
        self._completeIfNotSet(self._login)
        return self._login.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def get_enterprise_consumed_licenses(self) -> EnterpriseConsumedLicenses:
        """
        :calls: `GET /enterprise/{enterprise}/consumed-licenses <https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses>`_
        """
        assert isinstance(self.login, str), self.login
        firstURL = f"/enterprises/{self.login}/consumed-licenses"
        headers, data = self._requester.requestJsonAndCheck("GET", firstURL)
        # The response doesn't have the key of login and url, manually add it to data.
        data["login"] = self.login
        data["url"] = self.url + "/consumed-licenses"
        return EnterpriseConsumedLicenses(
            self._requester, headers, data, completed=True
        )

    def _initAttributes(self) -> None:
        self._login = NotSet
        self._url = NotSet

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
