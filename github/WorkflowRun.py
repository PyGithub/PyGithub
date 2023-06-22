############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Aleksei Fedotov <aleksei@fedotov.email>                       #
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

from datetime import datetime
from typing import Dict, NamedTuple

import github.Artifact
import github.GitCommit
import github.PullRequest
import github.Repository
import github.WorkflowJob
from github.GithubObject import (
    Attribute,
    CompletableGithubObject,
    NotSet,
    Opt,
    _NotSetType,
)
from github.PaginatedList import PaginatedList


class TimingData(NamedTuple):
    billable: Dict[str, Dict[str, int]]
    run_duration_ms: int


class WorkflowRun(CompletableGithubObject):
    """
    This class represents Workflow Runs. The reference can be found here https://docs.github.com/en/rest/reference/actions#workflow-runs
    """

    def __repr__(self):
        return self.get__repr__({"id": self._id.value, "url": self._url.value})

    _id: Attribute[int]

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    _name: Attribute[str]

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    _head_branch: Attribute[str]

    @property
    def head_branch(self) -> str:
        self._completeIfNotSet(self._head_branch)
        return self._head_branch.value

    _head_sha: Attribute[str]

    @property
    def head_sha(self) -> str:
        self._completeIfNotSet(self._head_sha)
        return self._head_sha.value

    _display_title: Attribute[str]

    @property
    def display_title(self) -> str:
        self._completeIfNotSet(self._display_title)
        return self._display_title.value

    _path: Attribute[str]

    @property
    def path(self) -> str:
        self._completeIfNotSet(self._path)
        return self._path.value

    _run_attempt: Attribute[int]

    @property
    def run_attempt(self) -> int:
        self._completeIfNotSet(self._run_attempt)
        return self._run_attempt.value

    _run_number: Attribute[int]

    @property
    def run_number(self) -> int:
        self._completeIfNotSet(self._run_number)
        return self._run_number.value

    _event: Attribute[str]

    @property
    def event(self) -> str:
        self._completeIfNotSet(self._event)
        return self._event.value

    _run_started_at: Attribute[datetime]

    @property
    def run_started_at(self) -> datetime:
        self._completeIfNotSet(self._run_started_at)
        return self._run_started_at.value

    _status: Attribute[str]

    @property
    def status(self) -> str:
        self._completeIfNotSet(self._status)
        return self._status.value

    _conclusion: Attribute[str]

    @property
    def conclusion(self) -> str:
        self._completeIfNotSet(self._conclusion)
        return self._conclusion.value

    @property
    def workflow_id(self):
        """
        :type: int
        """
        self._completeIfNotSet(self._workflow_id)
        return self._workflow_id.value

    _url: Attribute[str]

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    _html_url: Attribute[str]

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    _pull_requests: Attribute[github.PullRequest.PullRequest]

    @property
    def pull_requests(self) -> github.PullRequest.PullRequest:
        self._completeIfNotSet(self._pull_requests)
        return self._pull_requests.value

    _created_at: Attribute[datetime]

    @property
    def created_at(self):
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    _updated_at: Attribute[datetime]

    @property
    def updated_at(self):
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    _jobs_url: Attribute[str]

    @property
    def jobs_url(self) -> str:
        self._completeIfNotSet(self._jobs_url)
        return self._jobs_url.value

    _logs_url: Attribute[str]

    @property
    def logs_url(self) -> str:
        self._completeIfNotSet(self._logs_url)
        return self._logs_url.value

    _check_suite_url: Attribute[str]

    @property
    def check_suite_url(self) -> str:
        self._completeIfNotSet(self._check_suite_url)
        return self._check_suite_url.value

    _artifacts_url: Attribute[str]

    @property
    def artifacts_url(self) -> str:
        self._completeIfNotSet(self._artifacts_url)
        return self._artifacts_url.value

    def get_artifacts(self) -> "PaginatedList[github.Artifact.Artifact]":
        return PaginatedList(
            github.Artifact.Artifact,
            self._requester,
            self._artifacts_url.value,
            None,
            list_item="artifacts",
        )

    _cancel_url: Attribute[str]

    @property
    def cancel_url(self) -> str:
        self._completeIfNotSet(self._cancel_url)
        return self._cancel_url.value

    _rerun_url: Attribute[str]

    @property
    def rerun_url(self) -> str:
        self._completeIfNotSet(self._rerun_url)
        return self._rerun_url.value

    _workflow_url: Attribute[str]

    @property
    def workflow_url(self) -> str:
        """
        :type: string
        """
        self._completeIfNotSet(self._workflow_url)
        return self._workflow_url.value

    _head_commit: Attribute[github.GitCommit.GitCommit]

    @property
    def head_commit(self) -> github.GitCommit.GitCommit:
        self._completeIfNotSet(self._head_commit)
        return self._head_commit.value

    _repository: "Attribute[github.Repository.Repository]"

    @property
    def repository(self) -> "github.Repository.Repository":
        self._completeIfNotSet(self._repository)
        return self._repository.value

    _head_repository: "Attribute[github.Repository.Repository]"

    @property
    def head_repository(self) -> "github.Repository.Repository":
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
        return TimingData(
            billable=data["billable"], run_duration_ms=data["run_duration_ms"]  # type: ignore
        )

    def delete(self) -> bool:
        """
        :calls: `DELETE /repos/{owner}/{repo}/actions/runs/{run_id} <https://docs.github.com/en/rest/reference/actions#workflow-runs>`_
        """
        status, _, _ = self._requester.requestJson("DELETE", self.url)
        return status == 204

    def jobs(
        self, _filter: Opt[str] = NotSet
    ) -> "PaginatedList[github.WorkflowJob.WorkflowJob]":
        """
        :calls "`GET /repos/{owner}/{repo}/actions/runs/{run_id}/jobs <https://docs.github.com/en/rest/reference/actions#list-jobs-for-a-workflow-run>`_
        :param _filter: string `latest`, or `all`
        """
        assert isinstance(_filter, (_NotSetType, str)), _filter

        url_parameters = NotSet.remove_unset_items({"filter": _filter})

        return PaginatedList(
            github.WorkflowJob.WorkflowJob,
            self._requester,
            self.jobs_url,
            url_parameters,
            list_item="jobs",
        )

    def _initAttributes(self):
        self._id = NotSet
        self._name = NotSet
        self._head_branch = NotSet
        self._head_sha = NotSet
        self._display_title = NotSet
        self._path = NotSet
        self._run_attempt = NotSet
        self._run_number = NotSet
        self._event = NotSet
        self._run_started_at = NotSet
        self._status = NotSet
        self._conclusion = NotSet
        self._workflow_id = NotSet
        self._url = NotSet
        self._html_url = NotSet
        self._pull_requests = NotSet
        self._created_at = NotSet
        self._updated_at = NotSet
        self._jobs_url = NotSet
        self._logs_url = NotSet
        self._check_suite_url = NotSet
        self._artifacts_url = NotSet
        self._cancel_url = NotSet
        self._rerun_url = NotSet
        self._workflow_url = NotSet
        self._head_commit = NotSet
        self._repository = NotSet
        self._head_repository = NotSet

    def _useAttributes(self, attributes):
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
            assert attributes["run_started_at"] is None or isinstance(
                attributes["run_started_at"], str
            ), attributes["run_started_at"]
            self._run_started_at = self._makeDatetimeAttribute(
                attributes["run_started_at"]
            )
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
            self._check_suite_url = self._makeStringAttribute(
                attributes["check_suite_url"]
            )
        if "artifacts_url" in attributes:  # pragma no branch
            self._artifacts_url = self._makeStringAttribute(attributes["artifacts_url"])
        if "cancel_url" in attributes:  # pragma no branch
            self._cancel_url = self._makeStringAttribute(attributes["cancel_url"])
        if "rerun_url" in attributes:  # pragma no branch
            self._rerun_url = self._makeStringAttribute(attributes["rerun_url"])
        if "workflow_url" in attributes:  # pragma no branch
            self._workflow_url = self._makeStringAttribute(attributes["workflow_url"])
        if "head_commit" in attributes:  # pragma no branch
            self._head_commit = self._makeClassAttribute(
                github.GitCommit.GitCommit, attributes["head_commit"]
            )
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(
                github.Repository.Repository, attributes["repository"]
            )
        if "head_repository" in attributes:  # pragma no branch
            self._head_repository = self._makeClassAttribute(
                github.Repository.Repository, attributes["head_repository"]
            )
