# FILE AUTO GENERATED DO NOT TOUCH
############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Yannick Jadoul <yannick.jadoul@belgacom.net>                  #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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
from typing import Any

from . import CheckRun, GitCommit, GithubApp, PullRequest, Repository
from .GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_defined, is_optional
from .PaginatedList import PaginatedList


class CheckSuite(CompletableGithubObject):
    """
    This class represents check suites.

    The reference can be found here
    https://docs.github.com/en/rest/reference/checks#check-suites

    The OpenAPI schema can be found at

    - /components/schemas/check-run/properties/check_suite
    - /components/schemas/check-suite

    """

    def _initAttributes(self) -> None:
        self._after: Attribute[str] = NotSet
        self._app: Attribute[GithubApp] = NotSet
        self._before: Attribute[str] = NotSet
        self._check_runs_url: Attribute[str] = NotSet
        self._conclusion: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._head_branch: Attribute[str] = NotSet
        self._head_commit: Attribute[GitCommit] = NotSet
        self._head_sha: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._latest_check_runs_count: Attribute[int] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._pull_requests: Attribute[list[PullRequest]] = NotSet
        self._repository: Attribute[Repository] = NotSet
        self._rerequestable: Attribute[bool] = NotSet
        self._runs_rerequestable: Attribute[bool] = NotSet
        self._status: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "url": self._url.value})

    @property
    async def after(self) -> str:
        """
        :type: string
        """
        await self._completeIfNotSet(self._after)
        return self._after.value

    @property
    async def app(self) -> GithubApp:
        """
        :type: :class:`GithubApp.GithubApp`
        """
        await self._completeIfNotSet(self._app)
        return self._app.value

    @property
    async def before(self) -> str:
        """
        :type: string
        """
        await self._completeIfNotSet(self._before)
        return self._before.value

    @property
    async def check_runs_url(self) -> str:
        """
        :type: string
        """
        await self._completeIfNotSet(self._check_runs_url)
        return self._check_runs_url.value

    @property
    async def conclusion(self) -> str:
        """
        :type: string
        """
        await self._completeIfNotSet(self._conclusion)
        return self._conclusion.value

    @property
    async def created_at(self) -> datetime:
        """
        :type: datetime.datetime
        """
        await self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    async def head_branch(self) -> str:
        """
        :type: string
        """
        await self._completeIfNotSet(self._head_branch)
        return self._head_branch.value

    @property
    async def head_commit(self) -> GitCommit:
        """
        :type: :class:`GitCommit.GitCommit`
        """
        await self._completeIfNotSet(self._head_commit)
        return self._head_commit.value

    @property
    async def head_sha(self) -> str:
        """
        :type: string
        """
        await self._completeIfNotSet(self._head_sha)
        return self._head_sha.value

    @property
    async def id(self) -> int:
        """
        :type: int
        """
        await self._completeIfNotSet(self._id)
        return self._id.value

    @property
    async def latest_check_runs_count(self) -> int:
        """
        :type: int
        """
        await self._completeIfNotSet(self._latest_check_runs_count)
        return self._latest_check_runs_count.value

    @property
    async def node_id(self) -> str:
        await self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    async def pull_requests(self) -> list[PullRequest]:
        """
        :type: list of :class:`PullRequest.PullRequest`
        """
        await self._completeIfNotSet(self._pull_requests)
        return self._pull_requests.value

    @property
    async def repository(self) -> Repository:
        """
        :type: :class:`Repository.Repository`
        """
        await self._completeIfNotSet(self._repository)
        return self._repository.value

    @property
    async def rerequestable(self) -> bool:
        await self._completeIfNotSet(self._rerequestable)
        return self._rerequestable.value

    @property
    async def runs_rerequestable(self) -> bool:
        await self._completeIfNotSet(self._runs_rerequestable)
        return self._runs_rerequestable.value

    @property
    async def status(self) -> str:
        """
        :type: string
        """
        await self._completeIfNotSet(self._status)
        return self._status.value

    @property
    async def updated_at(self) -> datetime:
        """
        :type: datetime.datetime
        """
        await self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        """
        :type: string
        """
        return self._url.value

    async def rerequest(self) -> bool:
        """
        :calls: `POST /repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest <https://docs.github.com/en/rest/reference/checks#rerequest-a-check-suite>`_
        :rtype: bool
        """
        request_headers = {"Accept": "application/vnd.github.v3+json"}
        status, _, _ = await self._requester.requestJson("POST", f"{self.url}/rerequest", headers=request_headers)
        return status == 201

    def get_check_runs(
        self,
        check_name: Opt[str] = NotSet,
        status: Opt[str] = NotSet,
        filter: Opt[str] = NotSet,
    ) -> PaginatedList[CheckRun]:
        """
        :calls: `GET /repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs <https://docs.github.com/en/rest/reference/checks#list-check-runs-in-a-check-suite>`_
        """
        assert is_optional(check_name, str), check_name
        assert is_optional(status, str), status
        assert is_optional(filter, str), filter
        url_parameters: dict[str, Any] = {}
        if is_defined(check_name):
            url_parameters["check_name"] = check_name
        if is_defined(status):
            url_parameters["status"] = status
        if is_defined(filter):
            url_parameters["filter"] = filter
        return PaginatedList(
            CheckRun.CheckRun,
            self._requester,
            f"{self.url}/check-runs",
            url_parameters,
            headers={"Accept": "application/vnd.github.v3+json"},
            list_item="check_runs",
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "after" in attributes:  # pragma no branch
            self._after = self._makeStringAttribute(attributes["after"])
        if "app" in attributes:  # pragma no branch
            self._app = self._makeClassAttribute(GithubApp.GithubApp, attributes["app"])
        if "before" in attributes:  # pragma no branch
            self._before = self._makeStringAttribute(attributes["before"])
        if "check_runs_url" in attributes:  # pragma no branch
            self._check_runs_url = self._makeStringAttribute(attributes["check_runs_url"])
        if "conclusion" in attributes:  # pragma no branch
            self._conclusion = self._makeStringAttribute(attributes["conclusion"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "head_branch" in attributes:  # pragma no branch
            self._head_branch = self._makeStringAttribute(attributes["head_branch"])
        if "head_commit" in attributes:  # pragma no branch
            # This JSON swaps the 'sha' attribute for an 'id' attribute.
            # The GitCommit object only looks for 'sha'
            if "id" in attributes["head_commit"]:
                attributes["head_commit"]["sha"] = attributes["head_commit"]["id"]
            self._head_commit = self._makeClassAttribute(GitCommit.GitCommit, attributes["head_commit"])
        if "head_sha" in attributes:  # pragma no branch
            self._head_sha = self._makeStringAttribute(attributes["head_sha"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        elif "url" in attributes and attributes["url"]:
            id = attributes["url"].split("/")[-1]
            if id.isnumeric():
                self._id = self._makeIntAttribute(int(id))
        if "latest_check_runs_count" in attributes:  # pragma no branch
            self._latest_check_runs_count = self._makeIntAttribute(attributes["latest_check_runs_count"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "pull_requests" in attributes:  # pragma no branch
            self._pull_requests = self._makeListOfClassesAttribute(PullRequest.PullRequest, attributes["pull_requests"])
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(Repository.Repository, attributes["repository"])
        if "rerequestable" in attributes:  # pragma no branch
            self._rerequestable = self._makeBoolAttribute(attributes["rerequestable"])
        if "runs_rerequestable" in attributes:  # pragma no branch
            self._runs_rerequestable = self._makeBoolAttribute(attributes["runs_rerequestable"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
