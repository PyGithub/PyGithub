# FILE AUTO GENERATED DO NOT TOUCH
############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jeppe Fihl-Pearson <tenzer@tenzer.dk>                         #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Xavi Vega <xabi1309@gmail.com>                                #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Yossi Rozantsev <54272821+Apakottur@users.noreply.github.com> #
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

from . import WorkflowStep
from .GithubObject import Attribute, CompletableGithubObject, NotSet


class WorkflowJob(CompletableGithubObject):
    """
    This class represents Workflow Jobs.

    The reference can be found here
    https://docs.github.com/en/rest/reference/actions#workflow-jobs

    """

    def _initAttributes(self) -> None:
        self._check_run_url: Attribute[str] = NotSet
        self._completed_at: Attribute[datetime] = NotSet
        self._conclusion: Attribute[str | None] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._head_branch: Attribute[str] = NotSet
        self._head_sha: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._labels: Attribute[list[str]] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._run_attempt: Attribute[int] = NotSet
        self._run_id: Attribute[int] = NotSet
        self._run_url: Attribute[str] = NotSet
        self._runner_group_id: Attribute[int] = NotSet
        self._runner_group_name: Attribute[str] = NotSet
        self._runner_id: Attribute[int] = NotSet
        self._runner_name: Attribute[str] = NotSet
        self._started_at: Attribute[datetime] = NotSet
        self._status: Attribute[str] = NotSet
        self._steps: Attribute[list[WorkflowStep.WorkflowStep]] = NotSet
        self._url: Attribute[str] = NotSet
        self._workflow_name: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "url": self._url.value})

    @property
    async def check_run_url(self) -> str:
        await self._completeIfNotSet(self._check_run_url)
        return self._check_run_url.value

    @property
    async def completed_at(self) -> datetime:
        await self._completeIfNotSet(self._completed_at)
        return self._completed_at.value

    @property
    async def conclusion(self) -> str | None:
        await self._completeIfNotSet(self._conclusion)
        return self._conclusion.value

    @property
    async def created_at(self) -> datetime:
        await self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    async def head_branch(self) -> str:
        await self._completeIfNotSet(self._head_branch)
        return self._head_branch.value

    @property
    async def head_sha(self) -> str:
        await self._completeIfNotSet(self._head_sha)
        return self._head_sha.value

    @property
    async def html_url(self) -> str:
        await self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    async def id(self) -> int:
        await self._completeIfNotSet(self._id)
        return self._id.value

    @property
    async def labels(self) -> list[str]:
        await self._completeIfNotSet(self._labels)
        return self._labels.value

    @property
    async def name(self) -> str:
        await self._completeIfNotSet(self._name)
        return self._name.value

    @property
    async def node_id(self) -> str:
        await self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    async def run_attempt(self) -> int:
        await self._completeIfNotSet(self._run_attempt)
        return self._run_attempt.value

    @property
    async def run_id(self) -> int:
        await self._completeIfNotSet(self._run_id)
        return self._run_id.value

    @property
    async def run_url(self) -> str:
        await self._completeIfNotSet(self._run_url)
        return self._run_url.value

    @property
    async def runner_group_id(self) -> int:
        await self._completeIfNotSet(self._runner_group_id)
        return self._runner_group_id.value

    @property
    async def runner_group_name(self) -> str:
        await self._completeIfNotSet(self._runner_group_name)
        return self._runner_group_name.value

    @property
    async def runner_id(self) -> int:
        await self._completeIfNotSet(self._runner_id)
        return self._runner_id.value

    @property
    async def runner_name(self) -> str:
        await self._completeIfNotSet(self._runner_name)
        return self._runner_name.value

    @property
    async def started_at(self) -> datetime:
        await self._completeIfNotSet(self._started_at)
        return self._started_at.value

    @property
    async def status(self) -> str:
        await self._completeIfNotSet(self._status)
        return self._status.value

    @property
    async def steps(self) -> list[WorkflowStep.WorkflowStep]:
        await self._completeIfNotSet(self._steps)
        return self._steps.value

    @property
    async def url(self) -> str:
        await self._completeIfNotSet(self._url)
        return self._url.value

    @property
    async def workflow_name(self) -> str:
        await self._completeIfNotSet(self._workflow_name)
        return self._workflow_name.value

    async def logs_url(self) -> str:
        headers, _ = await self._requester.requestBlobAndCheck("GET", f"{await self.url}/logs")
        return headers["location"]

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "check_run_url" in attributes:  # pragma no branch
            self._check_run_url = self._makeStringAttribute(attributes["check_run_url"])
        if "completed_at" in attributes:  # pragma no branch
            self._completed_at = self._makeDatetimeAttribute(attributes["completed_at"])
        if "conclusion" in attributes:  # pragma no branch
            self._conclusion = self._makeStringAttribute(attributes["conclusion"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "head_branch" in attributes:  # pragma no branch
            self._head_branch = self._makeStringAttribute(attributes["head_branch"])
        if "head_sha" in attributes:  # pragma no branch
            self._head_sha = self._makeStringAttribute(attributes["head_sha"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "labels" in attributes:  # pragma no branch
            self._labels = self._makeListOfStringsAttribute(attributes["labels"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "run_attempt" in attributes:  # pragma no branch
            self._run_attempt = self._makeIntAttribute(attributes["run_attempt"])
        if "run_id" in attributes:  # pragma no branch
            self._run_id = self._makeIntAttribute(attributes["run_id"])
        if "run_url" in attributes:  # pragma no branch
            self._run_url = self._makeStringAttribute(attributes["run_url"])
        if "runner_group_id" in attributes:  # pragma no branch
            self._runner_group_id = self._makeIntAttribute(attributes["runner_group_id"])
        if "runner_group_name" in attributes:  # pragma no branch
            self._runner_group_name = self._makeStringAttribute(attributes["runner_group_name"])
        if "runner_id" in attributes:  # pragma no branch
            self._runner_id = self._makeIntAttribute(attributes["runner_id"])
        if "runner_name" in attributes:  # pragma no branch
            self._runner_name = self._makeStringAttribute(attributes["runner_name"])
        if "started_at" in attributes:  # pragma no branch
            self._started_at = self._makeDatetimeAttribute(attributes["started_at"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
        if "steps" in attributes:  # pragma no branch
            self._steps = self._makeListOfClassesAttribute(WorkflowStep.WorkflowStep, attributes["steps"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "workflow_name" in attributes:  # pragma no branch
            self._workflow_name = self._makeStringAttribute(attributes["workflow_name"])
