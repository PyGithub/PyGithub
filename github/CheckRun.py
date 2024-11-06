############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 majorvin <majorvin.tan@outlook.com>                           #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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
from typing import TYPE_CHECKING, Any

import github.CheckRunAnnotation
import github.CheckRunOutput
import github.GithubApp
import github.GithubObject
import github.PullRequest
from github.GithubObject import (
    Attribute,
    CompletableGithubObject,
    NotSet,
    Opt,
    is_defined,
    is_optional,
    is_optional_list,
)
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.CheckRunAnnotation import CheckRunAnnotation
    from github.CheckRunOutput import CheckRunOutput
    from github.GithubApp import GithubApp
    from github.PullRequest import PullRequest


class CheckRun(CompletableGithubObject):
    """
    This class represents check runs.

    The reference can be found here
    https://docs.github.com/en/rest/reference/checks#check-runs

    """

    def _initAttributes(self) -> None:
        self._app: Attribute[GithubApp] = NotSet
        self._check_suite_id: Attribute[int] = NotSet
        self._completed_at: Attribute[datetime | None] = NotSet
        self._conclusion: Attribute[str] = NotSet
        self._details_url: Attribute[str] = NotSet
        self._external_id: Attribute[str] = NotSet
        self._head_sha: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._output: Attribute[github.CheckRunOutput.CheckRunOutput] = NotSet
        self._pull_requests: Attribute[list[PullRequest]] = NotSet
        self._started_at: Attribute[datetime] = NotSet
        self._status: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "conclusion": self._conclusion.value})

    @property
    def app(self) -> GithubApp:
        self._completeIfNotSet(self._app)
        return self._app.value

    @property
    def check_suite_id(self) -> int:
        self._completeIfNotSet(self._check_suite_id)
        return self._check_suite_id.value

    @property
    def completed_at(self) -> datetime | None:
        self._completeIfNotSet(self._completed_at)
        return self._completed_at.value

    @property
    def conclusion(self) -> str:
        self._completeIfNotSet(self._conclusion)
        return self._conclusion.value

    @property
    def details_url(self) -> str:
        self._completeIfNotSet(self._details_url)
        return self._details_url.value

    @property
    def external_id(self) -> str:
        self._completeIfNotSet(self._external_id)
        return self._external_id.value

    @property
    def head_sha(self) -> str:
        self._completeIfNotSet(self._head_sha)
        return self._head_sha.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def output(self) -> CheckRunOutput:
        self._completeIfNotSet(self._output)
        return self._output.value

    @property
    def pull_requests(self) -> list[PullRequest]:
        self._completeIfNotSet(self._pull_requests)
        return self._pull_requests.value

    @property
    def started_at(self) -> datetime:
        self._completeIfNotSet(self._started_at)
        return self._started_at.value

    @property
    def status(self) -> str:
        self._completeIfNotSet(self._status)
        return self._status.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def get_annotations(self) -> PaginatedList[CheckRunAnnotation]:
        """
        :calls: `GET /repos/{owner}/{repo}/check-runs/{check_run_id}/annotations <https://docs.github.com/en/rest/reference/checks#list-check-run-annotations>`_
        """
        return PaginatedList(
            github.CheckRunAnnotation.CheckRunAnnotation,
            self._requester,
            f"{self.url}/annotations",
            None,
            headers={"Accept": "application/vnd.github.v3+json"},
        )

    def edit(
        self,
        name: Opt[str] = NotSet,
        head_sha: Opt[str] = NotSet,
        details_url: Opt[str] = NotSet,
        external_id: Opt[str] = NotSet,
        status: Opt[str] = NotSet,
        started_at: Opt[datetime] = NotSet,
        conclusion: Opt[str] = NotSet,
        completed_at: Opt[datetime] = NotSet,
        output: Opt[dict] = NotSet,
        actions: Opt[list[dict]] = NotSet,
    ) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/check-runs/{check_run_id} <https://docs.github.com/en/rest/reference/checks#update-a-check-run>`_
        """
        assert is_optional(name, str), name
        assert is_optional(head_sha, str), head_sha
        assert is_optional(details_url, str), details_url
        assert is_optional(external_id, str), external_id
        assert is_optional(status, str), status
        assert is_optional(started_at, datetime), started_at
        assert is_optional(conclusion, str), conclusion
        assert is_optional(completed_at, datetime), completed_at
        assert is_optional(output, dict), output
        assert is_optional_list(actions, dict), actions

        post_parameters: dict[str, Any] = {}
        if is_defined(name):
            post_parameters["name"] = name
        if is_defined(head_sha):
            post_parameters["head_sha"] = head_sha
        if is_defined(details_url):
            post_parameters["details_url"] = details_url
        if is_defined(external_id):
            post_parameters["external_id"] = external_id
        if is_defined(status):
            post_parameters["status"] = status
        if is_defined(started_at):
            post_parameters["started_at"] = started_at.strftime("%Y-%m-%dT%H:%M:%SZ")
        if is_defined(completed_at):
            post_parameters["completed_at"] = completed_at.strftime("%Y-%m-%dT%H:%M:%SZ")
        if is_defined(conclusion):
            post_parameters["conclusion"] = conclusion
        if is_defined(output):
            post_parameters["output"] = output
        if is_defined(actions):
            post_parameters["actions"] = actions

        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        self._useAttributes(data)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "app" in attributes:  # pragma no branch
            self._app = self._makeClassAttribute(github.GithubApp.GithubApp, attributes["app"])
        # This only gives us a dictionary with `id` attribute of `check_suite`
        if "check_suite" in attributes and "id" in attributes["check_suite"]:  # pragma no branch
            self._check_suite_id = self._makeIntAttribute(attributes["check_suite"]["id"])
        if "completed_at" in attributes:  # pragma no branch
            self._completed_at = self._makeDatetimeAttribute(attributes["completed_at"])
        if "conclusion" in attributes:  # pragma no branch
            self._conclusion = self._makeStringAttribute(attributes["conclusion"])
        if "details_url" in attributes:  # pragma no branch
            self._details_url = self._makeStringAttribute(attributes["details_url"])
        if "external_id" in attributes:  # pragma no branch
            self._external_id = self._makeStringAttribute(attributes["external_id"])
        if "head_sha" in attributes:  # pragma no branch
            self._head_sha = self._makeStringAttribute(attributes["head_sha"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "output" in attributes:  # pragma no branch
            self._output = self._makeClassAttribute(github.CheckRunOutput.CheckRunOutput, attributes["output"])
        if "pull_requests" in attributes:  # pragma no branch
            self._pull_requests = self._makeListOfClassesAttribute(
                github.PullRequest.PullRequest, attributes["pull_requests"]
            )
        if "started_at" in attributes:  # pragma no branch
            self._started_at = self._makeDatetimeAttribute(attributes["started_at"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
