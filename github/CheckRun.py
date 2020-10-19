# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
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

import github.GithubApp
import github.GithubObject
import github.PullRequest


class CheckRun(github.GithubObject.CompletableGithubObject):
    """
    This class represents check runs.
    The reference can be found here https://docs.github.com/en/rest/reference/checks#check-runs
    """

    def __repr__(self):
        return self.get__repr__(
            {"id": self._id.value, "conclusion": self._conclusion.value}
        )

    @property
    def app(self):
        """
        :rtype: :class:`github.GithubApp.GithubApp`
        """
        self._completeIfNotSet(self._app)
        return self._app.value

    @property
    def check_suite(self):
        """
        :type: dict
        """
        self._completeIfNotSet(self._check_suite)
        return self._check_suite.value

    @property
    def completed_at(self):
        """
        :rtype: datetime.datetime
        """
        self._completeIfNotSet(self._completed_at)
        return self._completed_at.value

    @property
    def conclusion(self):
        """
        :rtype: string
        """
        self._completeIfNotSet(self._conclusion)
        return self._conclusion.value

    @property
    def details_url(self):
        """
        :rtype: string
        """
        self._completeIfNotSet(self._details_url)
        return self._details_url.value

    @property
    def external_id(self):
        """
        :rtype: string
        """
        self._completeIfNotSet(self._external_id)
        return self._external_id.value

    @property
    def head_sha(self):
        """
        :rtype: string
        """
        self._completeIfNotSet(self._head_sha)
        return self._head_sha.value

    @property
    def html_url(self):
        """
        :rtype: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self):
        """
        :rtype: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self):
        """
        :rtype: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def node_id(self):
        """
        :rtype: string
        """
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def output(self):
        """
        :rtype: dict
        """
        self._completeIfNotSet(self._output)
        return self._output.value

    @property
    def pull_requests(self):
        """
        :rtype: list of :class:`github.PullRequest.PullRequest`
        """
        self._completeIfNotSet(self._pull_requests)
        return self._pull_requests.value

    @property
    def started_at(self):
        """
        :rtype: datetime.datetime
        """
        self._completeIfNotSet(self._started_at)
        return self._started_at.value

    @property
    def status(self):
        """
        :rtype: string
        """
        self._completeIfNotSet(self._status)
        return self._status.value

    @property
    def url(self):
        """
        :rtype: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    def _initAttributes(self):
        self._app = github.GithubObject.NotSet
        self._check_suite = github.GithubObject.NotSet
        self._completed_at = github.GithubObject.NotSet
        self._conclusion = github.GithubObject.NotSet
        self._details_url = github.GithubObject.NotSet
        self._external_id = github.GithubObject.NotSet
        self._head_sha = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._node_id = github.GithubObject.NotSet
        self._output = github.GithubObject.NotSet
        self._output = github.GithubObject.NotSet
        self._pull_requests = github.GithubObject.NotSet
        self._started_at = github.GithubObject.NotSet
        self._status = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "app" in attributes:  # pragma no branch
            self._app = self._makeClassAttribute(
                github.GithubApp.GithubApp, attributes["app"]
            )
        # This only gives us a dictionary with `id` attribute of `check_suite`
        if "check_suite" in attributes:  # pragma no branch
            self._check_suite = self._makeDictAttribute(attributes["check_suite"])
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
            self._output = self._makeDictAttribute(attributes["output"])
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
