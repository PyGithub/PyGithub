# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2017 Aaron Levine <allevin@sandia.gov>                             #
# Copyright 2017 Mike Miller <github@mikeage.net>                              #
# Copyright 2018 Darragh Bailey <daragh.bailey@gmail.com>                      #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

import github.GithubObject
import github.NamedUser


class PullRequestReview(github.GithubObject.CompletableGithubObject):
    """
    This class represents PullRequestReviews. The reference can be found here https://developer.github.com/v3/pulls/reviews/
    """

    def __repr__(self):
        return self.get__repr__({"id": self._id.value, "user": self._user.value})

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def user(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._user)
        return self._user.value

    @property
    def body(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def commit_id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._commit_id)
        return self._commit_id.value

    @property
    def state(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._state)
        return self._state.value

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
    def pull_request_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._pull_request_url)
        return self._pull_request_url.value

    @property
    def submitted_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._submitted_at)
        return self._submitted_at.value

    def dismiss(self, message):
        """
        :calls: `PUT /repos/:owner/:repo/pulls/:number/reviews/:review_id/dismissals <https://developer.github.com/v3/pulls/reviews/>`_
        :rtype: None
        """
        assert isinstance(message, str), message
        post_parameters = {"message": message}
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            self.pull_request_url + "/reviews/%s/dismissals" % self.id,
            input=post_parameters,
        )

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._user = github.GithubObject.NotSet
        self._body = github.GithubObject.NotSet
        self._commit_id = github.GithubObject.NotSet
        self._state = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._pull_request_url = github.GithubObject.NotSet
        self._submitted_at = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(
                github.NamedUser.NamedUser, attributes["user"]
            )
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "commit_id" in attributes:  # pragma no branch
            self._commit_id = self._makeStringAttribute(attributes["commit_id"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "pull_request_url" in attributes:  # pragma no branch
            self._pull_request_url = self._makeStringAttribute(
                attributes["pull_request_url"]
            )
        if "submitted_at" in attributes:  # pragma no branch
            self._submitted_at = self._makeDatetimeAttribute(attributes["submitted_at"])
