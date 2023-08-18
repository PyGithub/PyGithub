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

from github.EnterpriseConsumedLicenses import EnterpriseConsumedLicenses
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet
from github.Requester import Requester


class Enterprise(NonCompletableGithubObject):
    """
    This class represents Enterprises. Such objects do not exist in the Github API, so this class merely collects all endpoints the start with /enterprises/{enterprise}/. See methods below for specific endpoints and docs.
    https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin?apiVersion=2022-11-28
    """

    def __init__(
        self,
        requester: Requester,
        enterprise: str,
    ):
        super().__init__(requester, {}, {"enterprise": enterprise, "url": f"/enterprises/{enterprise}"}, True)

    def _initAttributes(self) -> None:
        self._enterprise: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"enterprise": self._enterprise.value})

    @property
    def enterprise(self) -> str:
        return self._enterprise.value

    @property
    def url(self) -> str:
        return self._url.value

    def get_consumed_licenses(self) -> EnterpriseConsumedLicenses:
        """
        :calls: `GET /enterprises/{enterprise}/consumed-licenses <https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/license#list-enterprise-consumed-licenses>`_
        """
        headers, data = self._requester.requestJsonAndCheck("GET", self.url + "/consumed-licenses")
        if "url" not in data:
            data["url"] = self.url + "/consumed-licenses"

        return EnterpriseConsumedLicenses(self._requester, headers, data, completed=True)

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "enterprise" in attributes:  # pragma no branch
            self._enterprise = self._makeStringAttribute(attributes["enterprise"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
