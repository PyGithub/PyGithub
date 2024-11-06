############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Min RK <benjaminrk@gmail.com>                                 #
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

from typing import TYPE_CHECKING, Any

import github.Authorization
import github.Event
import github.Gist
import github.GithubObject
import github.Issue
import github.Notification
import github.Organization
import github.PaginatedList
import github.Plan
import github.Repository
import github.UserKey
from github import Consts
from github.Auth import AppAuth
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet
from github.PaginatedList import PaginatedList
from github.Requester import Requester

if TYPE_CHECKING:
    from github.MainClass import Github

INTEGRATION_PREVIEW_HEADERS = {"Accept": Consts.mediaTypeIntegrationPreview}


class Installation(NonCompletableGithubObject):
    """
    This class represents Installations.

    The reference can be found here
    https://docs.github.com/en/rest/reference/apps#installations

    """

    def __init__(
        self,
        requester: Requester,
        headers: dict[str, str | int],
        attributes: Any,
        completed: bool,
    ) -> None:
        super().__init__(requester, headers, attributes, completed)

        auth = self._requester.auth if self._requester is not None else None
        # Usually, an Installation is created from a Requester with App authentication
        if isinstance(auth, AppAuth):
            # But the installation has to authenticate as an installation (e.g. for get_repos())
            auth = auth.get_installation_auth(self.id, requester=self._requester)
            self._requester = self._requester.withAuth(auth)

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._app_id: Attribute[int] = NotSet
        self._target_id: Attribute[int] = NotSet
        self._target_type: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    def get_github_for_installation(self) -> Github:
        return github.Github(**self._requester.kwargs)

    @property
    def requester(self) -> Requester:
        """
        Return my Requester object.

        For example, to make requests to API endpoints not yet supported by PyGitHub.

        """
        return self._requester

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def app_id(self) -> int:
        return self._app_id.value

    @property
    def target_id(self) -> int:
        return self._target_id.value

    @property
    def target_type(self) -> str:
        return self._target_type.value

    def get_repos(self) -> PaginatedList[github.Repository.Repository]:
        """
        :calls: `GET /installation/repositories <https://docs.github.com/en/rest/reference/integrations/installations#list-repositories>`_
        """
        url_parameters: dict[str, Any] = {}

        return PaginatedList(
            contentClass=github.Repository.Repository,
            requester=self._requester,
            firstUrl="/installation/repositories",
            firstParams=url_parameters,
            headers=INTEGRATION_PREVIEW_HEADERS,
            list_item="repositories",
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "app_id" in attributes:  # pragma no branch
            self._app_id = self._makeIntAttribute(attributes["app_id"])
        if "target_id" in attributes:  # pragma no branch
            self._target_id = self._makeIntAttribute(attributes["target_id"])
        if "target_type" in attributes:  # pragma no branch
            self._target_type = self._makeStringAttribute(attributes["target_type"])
