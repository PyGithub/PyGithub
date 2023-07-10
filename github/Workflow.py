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

import json
from io import BytesIO
from zipfile import ZipFile

import requests

import github.GithubObject
import github.WorkflowRun


class Workflow(github.GithubObject.CompletableGithubObject):
    """
    This class represents Workflows. The reference can be found here https://docs.github.com/en/rest/reference/actions#workflows
    """

    def __repr__(self):
        return self.get__repr__({"name": self._name.value, "url": self._url.value})

    @property
    def id(self):
        """
        :type: int
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def path(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._path)
        return self._path.value

    @property
    def state(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._state)
        return self._state.value

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
    def badge_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._badge_url)
        return self._badge_url.value

    def create_dispatch(self, ref, inputs=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches <https://docs.github.com/en/rest/reference/actions#create-a-workflow-dispatch-event>`_
        :param ref: :class:`github.Branch.Branch` or :class:`github.Tag.Tag` or :class:`github.Commit.Commit` or string
        :param inputs: dict
        :rtype: bool
        """
        assert (
            isinstance(ref, github.Branch.Branch)
            or isinstance(ref, github.Tag.Tag)
            or isinstance(ref, github.Commit.Commit)
            or isinstance(ref, str)
        ), ref
        assert inputs is github.GithubObject.NotSet or isinstance(inputs, dict), inputs
        if isinstance(ref, github.Branch.Branch):
            ref = ref.name
        elif isinstance(ref, github.Commit.Commit):
            ref = ref.sha
        elif isinstance(ref, github.Tag.Tag):
            ref = ref.name
        if inputs is github.GithubObject.NotSet:
            inputs = {}
        status, _, _ = self._requester.requestJson(
            "POST", f"{self.url}/dispatches", input={"ref": ref, "inputs": inputs}
        )
        return status == 204

    def get_runs(
        self,
        actor=github.GithubObject.NotSet,
        branch=github.GithubObject.NotSet,
        event=github.GithubObject.NotSet,
        status=github.GithubObject.NotSet,
        created=github.GithubObject.NotSet,
        exclude_pull_requests=github.GithubObject.NotSet,
        check_suite_id=github.GithubObject.NotSet,
        head_sha=github.GithubObject.NotSet,
    ):
        """
        :calls: `GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs <https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2022-11-28#list-workflow-runs-for-a-workflow>`_
        :param actor: :class:`github.NamedUser.NamedUser` or string
        :param branch: :class:`github.Branch.Branch` or string
        :param event: string
        :param status: string
        :param created: string
        :param exclude_pull_requests: bool
        :param check_suite_id: int
        :param head_sha: string
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.WorkflowRun.WorkflowRun`
        """
        assert (
            actor is github.GithubObject.NotSet
            or isinstance(actor, github.NamedUser.NamedUser)
            or isinstance(actor, str)
        ), actor
        assert (
            branch is github.GithubObject.NotSet
            or isinstance(branch, github.Branch.Branch)
            or isinstance(branch, str)
        ), branch
        assert event is github.GithubObject.NotSet or isinstance(event, str), event
        assert status is github.GithubObject.NotSet or isinstance(status, str), status
        assert created is github.GithubObject.NotSet or isinstance(
            created, str
        ), created
        assert exclude_pull_requests is github.GithubObject.NotSet or isinstance(
            exclude_pull_requests, bool
        ), exclude_pull_requests
        assert check_suite_id is github.GithubObject.NotSet or isinstance(
            check_suite_id, int
        ), check_suite_id
        assert head_sha is github.GithubObject.NotSet or isinstance(
            head_sha, str
        ), head_sha
        url_parameters = dict()
        if actor is not github.GithubObject.NotSet:
            url_parameters["actor"] = (
                actor._identity
                if isinstance(actor, github.NamedUser.NamedUser)
                else actor
            )
        if branch is not github.GithubObject.NotSet:
            url_parameters["branch"] = (
                branch.name if isinstance(branch, github.Branch.Branch) else branch
            )
        if event is not github.GithubObject.NotSet:
            url_parameters["event"] = event
        if status is not github.GithubObject.NotSet:
            url_parameters["status"] = status
        if created is not github.GithubObject.NotSet:
            url_parameters["created"] = created
        if exclude_pull_requests is not github.GithubObject.NotSet:
            url_parameters["exclude_pull_requests"] = exclude_pull_requests
        if check_suite_id is not github.GithubObject.NotSet:
            url_parameters["check_suite_id"] = check_suite_id
        if head_sha is not github.GithubObject.NotSet:
            url_parameters["head_sha"] = head_sha

        return github.PaginatedList.PaginatedList(
            github.WorkflowRun.WorkflowRun,
            self._requester,
            f"{self.url}/runs",
            url_parameters,
            None,
            list_item="workflow_runs",
        )

    def get_artifacts(self, run):
        """
        Get download url for one single download run of a artifact.
        :calls: `GET {run.artifacts_url} <https://docs.github.com/en/rest/reference/actions#workflow-runs>`_
        :param run: :class:`github.WorkflowRun.WorkflowRun`
        :rtype: dict or list[dict] e.g. {'name': 'sandbox-package1, 'url': 'https://pipelines.actions.githubusercontent.com/ddYkl%3D'}
        """

        # get artifact content
        status, artifactHeader, artifact = run._requester.requestJson(
            "GET", run.artifacts_url
        )
        artifact_content = json.loads(artifact)

        # get archive url
        ret = []
        for i in range(artifact_content["total_count"]):
            name = artifact_content["artifacts"][i]["name"]
            url = artifact_content["artifacts"][i]["archive_download_url"]

            # generates a download for one time
            # out = run._requester.requestMultipart(verb = "GET", url = url)
            _, responseHeaders, output = run._requester.requestMultipart(
                verb="GET",
                url=url,
                parameters=None,
                headers=None,
                input=None,
                cnx=run._requester._Requester__customConnection(url),
            )
            # manage return value
            info_dict = {"name": name, "url": responseHeaders["location"]}
            ret.append(info_dict)

        # manage return
        if len(ret) < 1:
            return None
        elif len(ret) == 1:
            return ret[0]
        else:
            return ret

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._path = github.GithubObject.NotSet
        self._state = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._badge_url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
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
