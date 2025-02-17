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

import github.Authorization
import github.Event
import github.Gist
import github.GithubObject
import github.Issue
import github.NamedUser
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
    from github.NamedUser import NamedUser
    from github.Organization import Organization

INTEGRATION_PREVIEW_HEADERS = {"Accept": Consts.mediaTypeIntegrationPreview}


class Installation(NonCompletableGithubObject):
    """
    This class represents Installations.

    The reference can be found here
    https://docs.github.com/en/rest/reference/apps#installations

    The OpenAPI schema can be found at
    - /components/schemas/installation

    """

    def _initAttributes(self) -> None:
        self._access_tokens_url: Attribute[str] = NotSet
        self._account: Attribute[NamedUser | Organization] = NotSet
        self._app_id: Attribute[int] = NotSet
        self._app_slug: Attribute[str] = NotSet
        self._contact_email: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._events: Attribute[list[str]] = NotSet
        self._has_multiple_single_files: Attribute[bool] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._permissions: Attribute[dict[str, Any]] = NotSet
        self._repositories_url: Attribute[str] = NotSet
        self._repository_selection: Attribute[str] = NotSet
        self._single_file_name: Attribute[str] = NotSet
        self._single_file_paths: Attribute[list[str]] = NotSet
        self._suspended_at: Attribute[datetime] = NotSet
        self._suspended_by: Attribute[NamedUser] = NotSet
        self._target_id: Attribute[int] = NotSet
        self._target_type: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet

    def __init__(
        self,
        requester: Requester,
        headers: dict[str, str | int],
        attributes: Any,
    ) -> None:
        super().__init__(requester, headers, attributes)

        auth = self._requester.auth if self._requester is not None else None
        # Usually, an Installation is created from a Requester with App authentication
        if isinstance(auth, AppAuth):
            # But the installation has to authenticate as an installation (e.g. for get_repos())
            auth = auth.get_installation_auth(self.id, requester=self._requester)
            self._requester = self._requester.withAuth(auth)

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def access_tokens_url(self) -> str:
        return self._access_tokens_url.value

    @property
    def account(self) -> NamedUser | Organization:
        return self._account.value

    @property
    def app_id(self) -> int:
        return self._app_id.value

    @property
    def app_slug(self) -> str:
        return self._app_slug.value

    @property
    def contact_email(self) -> str:
        return self._contact_email.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def events(self) -> list[str]:
        return self._events.value

    @property
    def has_multiple_single_files(self) -> bool:
        return self._has_multiple_single_files.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def permissions(self) -> dict[str, Any]:
        return self._permissions.value

    @property
    def repositories_url(self) -> str:
        return self._repositories_url.value

    @property
    def repository_selection(self) -> str:
        return self._repository_selection.value

    @property
    def requester(self) -> Requester:
        """
        Return my Requester object.

        For example, to make requests to API endpoints not yet supported by PyGitHub.

        """
        return self._requester

    @property
    def single_file_name(self) -> str:
        return self._single_file_name.value

    @property
    def single_file_paths(self) -> list[str]:
        return self._single_file_paths.value

    @property
    def suspended_at(self) -> datetime:
        return self._suspended_at.value

    @property
    def suspended_by(self) -> NamedUser:
        return self._suspended_by.value

    @property
    def target_id(self) -> int:
        return self._target_id.value

    @property
    def target_type(self) -> str:
        return self._target_type.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    def get_github_for_installation(self) -> Github:
        return github.Github(**self._requester.kwargs)

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
        if "access_tokens_url" in attributes:  # pragma no branch
            self._access_tokens_url = self._makeStringAttribute(attributes["access_tokens_url"])
        if "account" in attributes and "target_type" in attributes:  # pragma no branch
            target_type = attributes["target_type"]
            if target_type == "User":
                self._account = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["account"])
            if target_type == "Organization":
                self._account = self._makeClassAttribute(github.Organization.Organization, attributes["account"])
        if "app_id" in attributes:  # pragma no branch
            self._app_id = self._makeIntAttribute(attributes["app_id"])
        if "app_slug" in attributes:  # pragma no branch
            self._app_slug = self._makeStringAttribute(attributes["app_slug"])
        if "contact_email" in attributes:  # pragma no branch
            self._contact_email = self._makeStringAttribute(attributes["contact_email"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "events" in attributes:  # pragma no branch
            self._events = self._makeListOfStringsAttribute(attributes["events"])
        if "has_multiple_single_files" in attributes:  # pragma no branch
            self._has_multiple_single_files = self._makeBoolAttribute(attributes["has_multiple_single_files"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "permissions" in attributes:  # pragma no branch
            self._permissions = self._makeDictAttribute(attributes["permissions"])
        if "repositories_url" in attributes:  # pragma no branch
            self._repositories_url = self._makeStringAttribute(attributes["repositories_url"])
        if "repository_selection" in attributes:  # pragma no branch
            self._repository_selection = self._makeStringAttribute(attributes["repository_selection"])
        if "single_file_name" in attributes:  # pragma no branch
            self._single_file_name = self._makeStringAttribute(attributes["single_file_name"])
        if "single_file_paths" in attributes:  # pragma no branch
            self._single_file_paths = self._makeListOfStringsAttribute(attributes["single_file_paths"])
        if "suspended_at" in attributes:  # pragma no branch
            self._suspended_at = self._makeDatetimeAttribute(attributes["suspended_at"])
        if "suspended_by" in attributes:  # pragma no branch
            self._suspended_by = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["suspended_by"])
        if "target_id" in attributes:  # pragma no branch
            self._target_id = self._makeIntAttribute(attributes["target_id"])
        if "target_type" in attributes:  # pragma no branch
            self._target_type = self._makeStringAttribute(attributes["target_type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
