############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Matt Babineau <mbabineau@dataxu.com>                          #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Martijn Koster <mak-github@greenhills.co.uk>                  #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Colby Gallup <colbygallup@gmail.com>                          #
# Copyright 2020 Pascal Hofmann <mail@pascalhofmann.de>                        #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Nevins <nevins-b@users.noreply.github.com>                    #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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

import github.Consts
import github.DeploymentStatus
import github.GithubApp
import github.NamedUser
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.GithubApp import GithubApp
    from github.NamedUser import NamedUser


class Deployment(CompletableGithubObject):
    """
    This class represents Deployments.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#deployments

    The OpenAPI schema can be found at
    - /components/schemas/deployment
    - /components/schemas/deployment-simple

    """

    def _initAttributes(self) -> None:
        self._created_at: Attribute[datetime] = NotSet
        self._creator: Attribute[NamedUser] = NotSet
        self._description: Attribute[str] = NotSet
        self._environment: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._original_environment: Attribute[str] = NotSet
        self._payload: Attribute[dict[str, Any]] = NotSet
        self._performed_via_github_app: Attribute[GithubApp] = NotSet
        self._production_environment: Attribute[bool] = NotSet
        self._ref: Attribute[str] = NotSet
        self._repository_url: Attribute[str] = NotSet
        self._sha: Attribute[str] = NotSet
        self._statuses_url: Attribute[str] = NotSet
        self._task: Attribute[str] = NotSet
        self._transient_environment: Attribute[bool] = NotSet
        self._updated_at: Attribute[datetime | None] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "url": self._url.value})

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def creator(self) -> NamedUser:
        self._completeIfNotSet(self._creator)
        return self._creator.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def environment(self) -> str:
        self._completeIfNotSet(self._environment)
        return self._environment.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def original_environment(self) -> str:
        self._completeIfNotSet(self._original_environment)
        return self._original_environment.value

    @property
    def payload(self) -> dict[str, Any]:
        self._completeIfNotSet(self._payload)
        return self._payload.value

    @property
    def performed_via_github_app(self) -> GithubApp:
        self._completeIfNotSet(self._performed_via_github_app)
        return self._performed_via_github_app.value

    @property
    def production_environment(self) -> bool:
        self._completeIfNotSet(self._production_environment)
        return self._production_environment.value

    @property
    def ref(self) -> str:
        self._completeIfNotSet(self._ref)
        return self._ref.value

    @property
    def repository_url(self) -> str:
        self._completeIfNotSet(self._repository_url)
        return self._repository_url.value

    @property
    def sha(self) -> str:
        self._completeIfNotSet(self._sha)
        return self._sha.value

    @property
    def statuses_url(self) -> str:
        self._completeIfNotSet(self._statuses_url)
        return self._statuses_url.value

    @property
    def task(self) -> str:
        self._completeIfNotSet(self._task)
        return self._task.value

    @property
    def transient_environment(self) -> bool:
        self._completeIfNotSet(self._transient_environment)
        return self._transient_environment.value

    @property
    def updated_at(self) -> datetime | None:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def get_statuses(self) -> PaginatedList[github.DeploymentStatus.DeploymentStatus]:
        """
        :calls: `GET /repos/{owner}/deployments/{deployment_id}/statuses <https://docs.github.com/en/rest/reference/repos#list-deployments>`_
        """
        return PaginatedList(
            github.DeploymentStatus.DeploymentStatus,
            self._requester,
            f"{self.url}/statuses",
            None,
            headers={"Accept": self._get_accept_header()},
        )

    def get_status(self, id_: int) -> github.DeploymentStatus.DeploymentStatus:
        """
        :calls: `GET /repos/{owner}/deployments/{deployment_id}/statuses/{status_id}  <https://docs.github.com/en/rest/reference/repos#get-a-deployment>`_
        """
        assert isinstance(id_, int), id_
        headers, data = self._requester.requestJsonAndCheck(
            "GET",
            f"{self.url}/statuses/{id_}",
            headers={"Accept": self._get_accept_header()},
        )
        return github.DeploymentStatus.DeploymentStatus(self._requester, headers, data, completed=True)

    def create_status(
        self,
        state: str,
        target_url: Opt[str] = NotSet,
        description: Opt[str] = NotSet,
        environment: Opt[str] = NotSet,
        environment_url: Opt[str] = NotSet,
        auto_inactive: Opt[bool] = NotSet,
    ) -> github.DeploymentStatus.DeploymentStatus:
        """
        :calls: `POST /repos/{owner}/{repo}/deployments/{deployment_id}/statuses <https://docs.github.com/en/rest/reference/repos#create-a-deployment-status>`_
        """
        assert isinstance(state, str), state
        assert target_url is NotSet or isinstance(target_url, str), target_url
        assert description is NotSet or isinstance(description, str), description
        assert environment is NotSet or isinstance(environment, str), environment
        assert environment_url is NotSet or isinstance(environment_url, str), environment_url
        assert auto_inactive is NotSet or isinstance(auto_inactive, bool), auto_inactive

        post_parameters = NotSet.remove_unset_items(
            {
                "state": state,
                "target_url": target_url,
                "description": description,
                "environment": environment,
                "environment_url": environment_url,
                "auto_inactive": auto_inactive,
            }
        )

        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"{self.url}/statuses",
            input=post_parameters,
            headers={"Accept": self._get_accept_header()},
        )
        return github.DeploymentStatus.DeploymentStatus(self._requester, headers, data, completed=True)

    @staticmethod
    def _get_accept_header() -> str:
        return ", ".join(
            [
                github.Consts.deploymentEnhancementsPreview,
                github.Consts.deploymentStatusEnhancementsPreview,
            ]
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "creator" in attributes:  # pragma no branch
            self._creator = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["creator"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "environment" in attributes:  # pragma no branch
            self._environment = self._makeStringAttribute(attributes["environment"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "original_environment" in attributes:  # pragma no branch
            self._original_environment = self._makeStringAttribute(attributes["original_environment"])
        if "payload" in attributes:  # pragma no branch
            self._payload = self._makeDictAttribute(attributes["payload"])
        if "performed_via_github_app" in attributes:  # pragma no branch
            self._performed_via_github_app = self._makeClassAttribute(
                github.GithubApp.GithubApp, attributes["performed_via_github_app"]
            )
        if "production_environment" in attributes:  # pragma no branch
            self._production_environment = self._makeBoolAttribute(attributes["production_environment"])
        if "ref" in attributes:  # pragma no branch
            self._ref = self._makeStringAttribute(attributes["ref"])
        if "repository_url" in attributes:  # pragma no branch
            self._repository_url = self._makeStringAttribute(attributes["repository_url"])
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "statuses_url" in attributes:  # pragma no branch
            self._statuses_url = self._makeStringAttribute(attributes["statuses_url"])
        if "task" in attributes:  # pragma no branch
            self._task = self._makeStringAttribute(attributes["task"])
        if "transient_environment" in attributes:  # pragma no branch
            self._transient_environment = self._makeBoolAttribute(attributes["transient_environment"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
