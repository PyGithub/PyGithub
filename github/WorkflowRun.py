############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
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

from collections import namedtuple

import github.GithubObject
import github.PullRequest


class WorkflowRun(github.GithubObject.CompletableGithubObject):
    """
    This class represents Workflow Runs. The reference can be found here https://docs.github.com/en/rest/reference/actions#workflow-runs
    """

    def __repr__(self):
        return self.get__repr__({"id": self._id.value, "url": self._url.value})

    @property
    def id(self):
        """
        :type: int
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def head_branch(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._head_branch)
        return self._head_branch.value

    @property
    def head_sha(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._head_sha)
        return self._head_sha.value

    @property
    def run_number(self):
        """
        :type: int
        """
        self._completeIfNotSet(self._run_number)
        return self._run_number.value

    @property
    def event(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._event)
        return self._event.value

    @property
    def status(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._status)
        return self._status.value

    @property
    def conclusion(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._conclusion)
        return self._conclusion.value

    @property
    def workflow_id(self):
        """
        :type: int
        """
        self._completeIfNotSet(self._workflow_id)
        return self._workflow_id.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def pull_requests(self):
        """
        :type: list of :class:`github.PullRequest.PullRequest`
        """
        self._completeIfNotSet(self._pull_requests)
        return self._pull_requests.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def jobs_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._jobs_url)
        return self._jobs_url.value

    @property
    def logs_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._logs_url)
        return self._logs_url.value

    @property
    def check_suite_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._check_suite_url)
        return self._check_suite_url.value

    @property
    def artifacts_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._artifacts_url)
        return self._artifacts_url.value

    @property
    def cancel_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._cancel_url)
        return self._cancel_url.value

    @property
    def rerun_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._rerun_url)
        return self._rerun_url.value

    @property
    def workflow_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._workflow_url)
        return self._workflow_url.value

    @property
    def head_commit(self):
        """
        :type: :class:`github.GitCommit.GitCommit`
        """
        self._completeIfNotSet(self._head_commit)
        return self._head_commit.value

    @property
    def repository(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        self._completeIfNotSet(self._repository)
        return self._repository.value

    @property
    def head_repository(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        self._completeIfNotSet(self._head_repository)
        return self._head_repository.value

    def cancel(self):
        """
        :calls: `POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel <https://docs.github.com/en/rest/reference/actions#workflow-runs>`_
        :rtype: bool
        """
        status, _, _ = self._requester.requestJson("POST", self.cancel_url)
        return status == 202

    def rerun(self):
        """
        :calls: `POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun <https://docs.github.com/en/rest/reference/actions#workflow-runs>`_
        :rtype: bool
        """
        status, _, _ = self._requester.requestJson("POST", self.rerun_url)
        return status == 201

    def timing(self):
        """
        :calls: `GET /repos/{owner}/{repo}/actions/runs/{run_id}/timing <https://docs.github.com/en/rest/reference/actions#workflow-runs>`_
        :rtype: namedtuple with billable and run_duration_ms members
        """
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/timing")
        timingdata = namedtuple("TimingData", data.keys())
        return timingdata._make(data.values())

    def delete(self):
        """
        :calls: `DELETE /repos/{owner}/{repo}/actions/runs/{run_id} <https://docs.github.com/en/rest/reference/actions#workflow-runs>`_
        :rtype: bool
        """
        status, _, _ = self._requester.requestJson("DELETE", self.url)
        return status == 204

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._head_branch = github.GithubObject.NotSet
        self._head_sha = github.GithubObject.NotSet
        self._run_number = github.GithubObject.NotSet
        self._event = github.GithubObject.NotSet
        self._status = github.GithubObject.NotSet
        self._conclusion = github.GithubObject.NotSet
        self._workflow_id = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._pull_requests = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._jobs_url = github.GithubObject.NotSet
        self._logs_url = github.GithubObject.NotSet
        self._check_suite_url = github.GithubObject.NotSet
        self._artifacts_url = github.GithubObject.NotSet
        self._cancel_url = github.GithubObject.NotSet
        self._rerun_url = github.GithubObject.NotSet
        self._workflow_url = github.GithubObject.NotSet
        self._head_commit = github.GithubObject.NotSet
        self._repository = github.GithubObject.NotSet
        self._head_repository = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "head_branch" in attributes:  # pragma no branch
            self._head_branch = self._makeStringAttribute(attributes["head_branch"])
        if "head_sha" in attributes:  # pragma no branch
            self._head_sha = self._makeStringAttribute(attributes["head_sha"])
        if "run_number" in attributes:  # pragma no branch
            self._run_number = self._makeIntAttribute(attributes["run_number"])
        if "event" in attributes:  # pragma no branch
            self._event = self._makeStringAttribute(attributes["event"])
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
