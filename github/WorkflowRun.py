############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Yannick Jadoul <yannick.jadoul@belgacom.net>                  #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Aleksei Fedotov <lexa@cfotr.com>                              #
# Copyright 2022 Gabriele Oliaro <ict@gabrieleoliaro.it>                       #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jeppe Fihl-Pearson <tenzer@tenzer.dk>                         #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Sasha Chung <50770626+nuang-ee@users.noreply.github.com>      #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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
from typing import TYPE_CHECKING, Any, NamedTuple

import github.GitCommit
import github.PullRequest
import github.WorkflowJob
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_optional
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.Artifact import Artifact
    from github.GitCommit import GitCommit
    from github.PullRequest import PullRequest
    from github.Repository import Repository
    from github.WorkflowJob import WorkflowJob


class TimingData(NamedTuple):
    billable: dict[str, dict[str, int]]
    run_duration_ms: int


class WorkflowRun(CompletableGithubObject):
    """
    This class represents Workflow Runs.

    The reference can be found here
    https://docs.github.com/en/rest/reference/actions#workflow-runs

    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._url: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._path: Attribute[str] = NotSet
        self._head_branch: Attribute[str] = NotSet
        self._head_sha: Attribute[str] = NotSet
        self._run_attempt: Attribute[int] = NotSet
        self._run_number: Attribute[int] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._pull_requests: Attribute[list[PullRequest]] = NotSet
        self._status: Attribute[str] = NotSet
        self._conclusion: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._jobs_url: Attribute[str] = NotSet
        self._logs_url: Attribute[str] = NotSet
        self._display_title: Attribute[str] = NotSet
        self._event: Attribute[str] = NotSet
        self._run_started_at: Attribute[datetime] = NotSet
        self._check_suite_url: Attribute[str] = NotSet
        self._cancel_url: Attribute[str] = NotSet
        self._rerun_url: Attribute[str] = NotSet
        self._artifacts_url: Attribute[str] = NotSet
        self._workflow_url: Attribute[str] = NotSet
        self._head_commit: Attribute[GitCommit] = NotSet
        self._repository: Attribute[Repository] = NotSet
        self._head_repository: Attribute[Repository] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "url": self._url.value})

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def head_branch(self) -> str:
        self._completeIfNotSet(self._head_branch)
        return self._head_branch.value

    @property
    def head_sha(self) -> str:
        self._completeIfNotSet(self._head_sha)
        return self._head_sha.value

    @property
    def display_title(self) -> str:
        self._completeIfNotSet(self._display_title)
        return self._display_title.value

    @property
    def path(self) -> str:
        self._completeIfNotSet(self._path)
        return self._path.value

    @property
    def run_attempt(self) -> int:
        self._completeIfNotSet(self._run_attempt)
        return self._run_attempt.value

    @property
    def run_number(self) -> int:
        self._completeIfNotSet(self._run_number)
        return self._run_number.value

    @property
    def event(self) -> str:
        self._completeIfNotSet(self._event)
        return self._event.value

    @property
    def run_started_at(self) -> datetime:
        self._completeIfNotSet(self._run_started_at)
        return self._run_started_at.value

    @property
    def status(self) -> str:
        self._completeIfNotSet(self._status)
        return self._status.value

    @property
    def conclusion(self) -> str:
        self._completeIfNotSet(self._conclusion)
        return self._conclusion.value

    @property
    def workflow_id(self) -> int:
        self._completeIfNotSet(self._workflow_id)
        return self._workflow_id.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def pull_requests(self) -> list[PullRequest]:
        self._completeIfNotSet(self._pull_requests)
        return self._pull_requests.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def jobs_url(self) -> str:
        self._completeIfNotSet(self._jobs_url)
        return self._jobs_url.value

    @property
    def logs_url(self) -> str:
        self._completeIfNotSet(self._logs_url)
        return self._logs_url.value

    @property
    def check_suite_url(self) -> str:
        self._completeIfNotSet(self._check_suite_url)
        return self._check_suite_url.value

    @property
    def artifacts_url(self) -> str:
        self._completeIfNotSet(self._artifacts_url)
        return self._artifacts_url.value

    def get_artifacts(self) -> PaginatedList[Artifact]:
        return PaginatedList(
            github.Artifact.Artifact,
            self._requester,
            self._artifacts_url.value,
            None,
            list_item="artifacts",
        )

    @property
    def cancel_url(self) -> str:
        self._completeIfNotSet(self._cancel_url)
        return self._cancel_url.value

    @property
    def rerun_url(self) -> str:
        self._completeIfNotSet(self._rerun_url)
        return self._rerun_url.value

    @property
    def workflow_url(self) -> str:
        self._completeIfNotSet(self._workflow_url)
        return self._workflow_url.value

    @property
    def head_commit(self) -> GitCommit:
        self._completeIfNotSet(self._head_commit)
        return self._head_commit.value

    @property
    def repository(self) -> Repository:
        self._completeIfNotSet(self._repository)
        return self._repository.value

    @property
    def head_repository(self) -> Repository:
        self._completeIfNotSet(self._head_repository)
        return self._head_repository.value

    def cancel(self) -> bool:
        """
        :calls: `POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel <https://docs.github.com/en/rest/reference/actions#workflow-runs>`_
        """
        status, _, _ = self._requester.requestJson("POST", self.cancel_url)
        return status == 202

    def rerun(self) -> bool:
        """
        :calls: `POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun <https://docs.github.com/en/rest/reference/actions#workflow-runs>`_
        """
        status, _, _ = self._requester.requestJson("POST", self.rerun_url)
        return status == 201

    def timing(self) -> TimingData:
        """
        :calls: `GET /repos/{owner}/{repo}/actions/runs/{run_id}/timing <https://docs.github.com/en/rest/reference/actions#workflow-runs>`_
        """
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/timing")
        return TimingData(billable=data["billable"], run_duration_ms=data["run_duration_ms"])  # type: ignore

    def delete(self) -> bool:
        """
        :calls: `DELETE /repos/{owner}/{repo}/actions/runs/{run_id} <https://docs.github.com/en/rest/reference/actions#workflow-runs>`_
        """
        status, _, _ = self._requester.requestJson("DELETE", self.url)
        return status == 204

    def jobs(self, _filter: Opt[str] = NotSet) -> PaginatedList[WorkflowJob]:
        """
        :calls "`GET /repos/{owner}/{repo}/actions/runs/{run_id}/jobs <https://docs.github.com/en/rest/reference/actions#list-jobs-for-a-workflow-run>`_
        :param _filter: string `latest`, or `all`
        """
        assert is_optional(_filter, str), _filter

        url_parameters = NotSet.remove_unset_items({"filter": _filter})

        return PaginatedList(
            github.WorkflowJob.WorkflowJob,
            self._requester,
            self.jobs_url,
            url_parameters,
            list_item="jobs",
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "head_branch" in attributes:  # pragma no branch
            self._head_branch = self._makeStringAttribute(attributes["head_branch"])
        if "head_sha" in attributes:  # pragma no branch
            self._head_sha = self._makeStringAttribute(attributes["head_sha"])
        if "display_title" in attributes:  # pragma no branch
            self._display_title = self._makeStringAttribute(attributes["display_title"])
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
        if "run_attempt" in attributes:  # pragma no branch
            self._run_attempt = self._makeIntAttribute(attributes["run_attempt"])
        if "run_number" in attributes:  # pragma no branch
            self._run_number = self._makeIntAttribute(attributes["run_number"])
        if "event" in attributes:  # pragma no branch
            self._event = self._makeStringAttribute(attributes["event"])
        if "run_started_at" in attributes:  # pragma no branch
            assert attributes["run_started_at"] is None or isinstance(attributes["run_started_at"], str), attributes[
                "run_started_at"
            ]
            self._run_started_at = self._makeDatetimeAttribute(attributes["run_started_at"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
        if "conclusion" in attributes:  # pragma no branch
            self._conclusion = self._makeStringAttribute(attributes["conclusion"])
        if "workflow_id" in attributes:  # pragma no branch
            self._workflow_id = self._makeIntAttribute(attributes["workflow_id"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "pull_requests" in attributes:  # pragma no branch
            self._pull_requests = self._makeListOfClassesAttribute(
                github.PullRequest.PullRequest, attributes["pull_requests"]
            )
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "jobs_url" in attributes:  # pragma no branch
            self._jobs_url = self._makeStringAttribute(attributes["jobs_url"])
        if "logs_url" in attributes:  # pragma no branch
            self._logs_url = self._makeStringAttribute(attributes["logs_url"])
        if "check_suite_url" in attributes:  # pragma no branch
            self._check_suite_url = self._makeStringAttribute(attributes["check_suite_url"])
        if "artifacts_url" in attributes:  # pragma no branch
            self._artifacts_url = self._makeStringAttribute(attributes["artifacts_url"])
        if "cancel_url" in attributes:  # pragma no branch
            self._cancel_url = self._makeStringAttribute(attributes["cancel_url"])
        if "rerun_url" in attributes:  # pragma no branch
            self._rerun_url = self._makeStringAttribute(attributes["rerun_url"])
        if "workflow_url" in attributes:  # pragma no branch
            self._workflow_url = self._makeStringAttribute(attributes["workflow_url"])
        if "head_commit" in attributes:  # pragma no branch
            self._head_commit = self._makeClassAttribute(github.GitCommit.GitCommit, attributes["head_commit"])
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
        if "head_repository" in attributes:  # pragma no branch
            self._head_repository = self._makeClassAttribute(
                github.Repository.Repository, attributes["head_repository"]
            )
