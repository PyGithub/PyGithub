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
from __future__ import annotations

from datetime import datetime
from typing import Any

import github.Branch
import github.Commit
import github.GithubObject
import github.NamedUser
import github.Tag
import github.WorkflowRun
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt
from github.PaginatedList import PaginatedList


class Workflow(CompletableGithubObject):
    """
    This class represents Workflows. The reference can be found here https://docs.github.com/en/rest/reference/actions#workflows
    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._path: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._badge_url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value, "url": self._url.value})

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def path(self) -> str:
        self._completeIfNotSet(self._path)
        return self._path.value

    @property
    def state(self) -> str:
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def badge_url(self) -> str:
        self._completeIfNotSet(self._badge_url)
        return self._badge_url.value

    def create_dispatch(
        self, ref: github.Branch.Branch | github.Tag.Tag | github.Commit.Commit | str, inputs: Opt[dict] = NotSet
    ) -> bool:
        """
        :calls: `POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches <https://docs.github.com/en/rest/reference/actions#create-a-workflow-dispatch-event>`_
        """
        assert (
            isinstance(ref, github.Branch.Branch)
            or isinstance(ref, github.Tag.Tag)
            or isinstance(ref, github.Commit.Commit)
            or isinstance(ref, str)
        ), ref
        assert inputs is NotSet or isinstance(inputs, dict), inputs
        if isinstance(ref, github.Branch.Branch):
            ref = ref.name
        elif isinstance(ref, github.Commit.Commit):
            ref = ref.sha
        elif isinstance(ref, github.Tag.Tag):
            ref = ref.name
        if inputs is NotSet:
            inputs = {}
        status, _, _ = self._requester.requestJson(
            "POST", f"{self.url}/dispatches", input={"ref": ref, "inputs": inputs}
        )
        return status == 204

    def get_runs(
        self,
        actor: Opt[github.NamedUser.NamedUser] = NotSet,
        branch: Opt[github.Branch.Branch] = NotSet,
        event: Opt[str] = NotSet,
        status: Opt[str] = NotSet,
        created: Opt[str] = NotSet,
        exclude_pull_requests: Opt[bool] = NotSet,
        check_suite_id: Opt[int] = NotSet,
        head_sha: Opt[str] = NotSet,
    ) -> PaginatedList[github.WorkflowRun.WorkflowRun]:
        """
        :calls: `GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs <https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2022-11-28#list-workflow-runs-for-a-workflow>`_
        """
        assert actor is NotSet or isinstance(actor, github.NamedUser.NamedUser) or isinstance(actor, str), actor
        assert branch is NotSet or isinstance(branch, github.Branch.Branch) or isinstance(branch, str), branch
        assert event is NotSet or isinstance(event, str), event
        assert status is NotSet or isinstance(status, str), status
        assert created is NotSet or isinstance(created, str), created
        assert exclude_pull_requests is NotSet or isinstance(exclude_pull_requests, bool), exclude_pull_requests
        assert check_suite_id is NotSet or isinstance(check_suite_id, int), check_suite_id
        assert head_sha is NotSet or isinstance(head_sha, str), head_sha
        url_parameters = dict()
        if actor is not NotSet:
            url_parameters["actor"] = actor._identity if isinstance(actor, github.NamedUser.NamedUser) else actor
        if branch is not NotSet:
            url_parameters["branch"] = branch.name if isinstance(branch, github.Branch.Branch) else branch
        if event is not NotSet:
            url_parameters["event"] = event
        if status is not NotSet:
            url_parameters["status"] = status
        if created is not NotSet:
            url_parameters["created"] = created
        if exclude_pull_requests is not NotSet:
            url_parameters["exclude_pull_requests"] = exclude_pull_requests
        if check_suite_id is not NotSet:
            url_parameters["check_suite_id"] = check_suite_id
        if head_sha is not NotSet:
            url_parameters["head_sha"] = head_sha

        return PaginatedList(
            github.WorkflowRun.WorkflowRun,
            self._requester,
            f"{self.url}/runs",
            url_parameters,
            None,
            list_item="workflow_runs",
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "badge_url" in attributes:  # pragma no branch
            self._badge_url = self._makeStringAttribute(attributes["badge_url"])
