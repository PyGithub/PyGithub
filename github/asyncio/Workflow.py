# FILE AUTO GENERATED DO NOT TOUCH
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
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Mahesh Raju <coder@mahesh.net>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Thomas Burghout <thomas.burghout@nedap.com>                   #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 sd-kialo <138505487+sd-kialo@users.noreply.github.com>        #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Nick McClorey <32378821+nickrmcclorey@users.noreply.github.com>#
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
from typing import Any

import github

from . import Branch, Commit, NamedUser, Tag, WorkflowRun
from .GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_defined, is_undefined
from .PaginatedList import PaginatedList


class Workflow(CompletableGithubObject):
    """
    This class represents Workflows.

    The reference can be found here
    https://docs.github.com/en/rest/reference/actions#workflows

    The OpenAPI schema can be found at

    - /components/schemas/workflow

    """

    def _initAttributes(self) -> None:
        self._badge_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._deleted_at: Attribute[datetime] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._path: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value, "url": self._url.value})

    @property
    async def badge_url(self) -> str:
        await self._completeIfNotSet(self._badge_url)
        return self._badge_url.value

    @property
    async def created_at(self) -> datetime:
        await self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    async def deleted_at(self) -> datetime:
        await self._completeIfNotSet(self._deleted_at)
        return self._deleted_at.value

    @property
    async def html_url(self) -> str:
        await self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    async def id(self) -> int:
        await self._completeIfNotSet(self._id)
        return self._id.value

    @property
    async def name(self) -> str:
        await self._completeIfNotSet(self._name)
        return self._name.value

    @property
    async def node_id(self) -> str:
        await self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    async def path(self) -> str:
        await self._completeIfNotSet(self._path)
        return self._path.value

    @property
    async def state(self) -> str:
        await self._completeIfNotSet(self._state)
        return self._state.value

    @property
    async def updated_at(self) -> datetime:
        await self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    async def url(self) -> str:
        await self._completeIfNotSet(self._url)
        return self._url.value

    # v3: default throw to True
    async def create_dispatch(
        self,
        ref: Branch.Branch | Tag.Tag | Commit.Commit | str,
        inputs: Opt[dict] = NotSet,
        throw: bool = False,
    ) -> bool:
        """
        :calls: `POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches <https://docs.github.com/en/rest/reference/actions#create-a-workflow-dispatch-event>`_
        Note: raises or return False without details on error, depending on the ``throw`` parameter.
        """
        assert (
            isinstance(ref, Branch.Branch)
            or isinstance(ref, Tag.Tag)
            or isinstance(ref, Commit.Commit)
            or isinstance(ref, str)
        ), ref
        assert is_undefined(inputs) or isinstance(inputs, dict), inputs
        if isinstance(ref, Branch.Branch):
            ref = ref.name
        elif isinstance(ref, Commit.Commit):
            ref = await ref.sha
        elif isinstance(ref, Tag.Tag):
            ref = ref.name
        if is_undefined(inputs):
            inputs = {}
        url = f"{await self.url}/dispatches"
        input = {"ref": ref, "inputs": inputs}

        if throw:
            await self._requester.requestJsonAndCheck("POST", url, input=input)
            return True
        else:
            status, _, _ = await self._requester.requestJson("POST", url, input=input)
            return status == 204

    async def get_runs(
        self,
        actor: Opt[NamedUser.NamedUser | str] = NotSet,
        branch: Opt[Branch.Branch | str] = NotSet,
        event: Opt[str] = NotSet,
        status: Opt[str] = NotSet,
        created: Opt[str] = NotSet,
        exclude_pull_requests: Opt[bool] = NotSet,
        check_suite_id: Opt[int] = NotSet,
        head_sha: Opt[str] = NotSet,
    ) -> PaginatedList[WorkflowRun.WorkflowRun]:
        """
        :calls: `GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs <https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2022-11-28#list-workflow-runs-for-a-workflow>`_
        """
        assert (
            is_undefined(actor)
            or isinstance(actor, (NamedUser.NamedUser, github.NamedUser.NamedUser))
            or isinstance(actor, str)
        ), actor
        assert (
            is_undefined(branch) or isinstance(branch, (Branch.Branch, github.Branch.Branch)) or isinstance(branch, str)
        ), branch
        assert is_undefined(event) or isinstance(event, str), event
        assert is_undefined(status) or isinstance(status, str), status
        assert is_undefined(created) or isinstance(created, str), created
        assert is_undefined(exclude_pull_requests) or isinstance(exclude_pull_requests, bool), exclude_pull_requests
        assert is_undefined(check_suite_id) or isinstance(check_suite_id, int), check_suite_id
        assert is_undefined(head_sha) or isinstance(head_sha, str), head_sha
        url_parameters: dict[str, Any] = dict()
        if is_defined(actor):
            url_parameters["actor"] = (await actor._identity) if isinstance(actor, NamedUser.NamedUser) else actor
        if is_defined(branch):
            url_parameters["branch"] = branch.name if isinstance(branch, Branch.Branch) else branch
        if is_defined(event):
            url_parameters["event"] = event
        if is_defined(status):
            url_parameters["status"] = status
        if is_defined(created):
            url_parameters["created"] = created
        if is_defined(exclude_pull_requests):
            url_parameters["exclude_pull_requests"] = exclude_pull_requests
        if is_defined(check_suite_id):
            url_parameters["check_suite_id"] = check_suite_id
        if is_defined(head_sha):
            url_parameters["head_sha"] = head_sha

        return PaginatedList(
            WorkflowRun.WorkflowRun,
            self._requester,
            f"{await self.url}/runs",
            url_parameters,
            headers=None,
            list_item="workflow_runs",
        )

    async def disable(self) -> bool:
        """
        :calls: `PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable <https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28#disable-a-workflow>`_
        :rtype: bool
        """
        status, _, _ = await self._requester.requestJson("PUT", f"{await self.url}/disable")
        return status == 204

    async def enable(self) -> bool:
        """
        :calls: `PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable <https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28#enable-a-workflow>`_
        :rtype: bool
        """
        status, _, _ = await self._requester.requestJson("PUT", f"{await self.url}/enable")
        return status == 204

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "badge_url" in attributes:  # pragma no branch
            self._badge_url = self._makeStringAttribute(attributes["badge_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "deleted_at" in attributes:  # pragma no branch
            self._deleted_at = self._makeDatetimeAttribute(attributes["deleted_at"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        elif "url" in attributes and attributes["url"]:
            id = attributes["url"].split("/")[-1]
            if id.isnumeric():
                self._id = self._makeIntAttribute(int(id))
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
