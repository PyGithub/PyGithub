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
from __future__ import annotations

from datetime import datetime
from typing import Any

import github.GithubObject
import github.NamedUser
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class PullRequestReview(NonCompletableGithubObject):
    """
    This class represents PullRequestReviews. The reference can be found here https://docs.github.com/en/rest/reference/pulls#reviews
    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._user: Attribute[github.NamedUser.NamedUser] = NotSet
        self._body: Attribute[str] = NotSet
        self._commit_id: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._pull_request_url: Attribute[str] = NotSet
        self._submitted_at: Attribute[datetime] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "user": self._user.value})

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def user(self) -> github.NamedUser.NamedUser:
        return self._user.value

    @property
    def body(self) -> str:
        return self._body.value

    @property
    def commit_id(self) -> str:
        return self._commit_id.value

    @property
    def state(self) -> str:
        return self._state.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def pull_request_url(self) -> str:
        return self._pull_request_url.value

    @property
    def submitted_at(self) -> datetime:
        return self._submitted_at.value

    def dismiss(self, message: str) -> None:
        """
        :calls: `PUT /repos/{owner}/{repo}/pulls/{number}/reviews/{review_id}/dismissals <https://docs.github.com/en/rest/reference/pulls#reviews>`_
        """
        post_parameters = {"message": message}
        headers, data = self._requester.requestJsonAndCheck(
            "PUT",
            f"{self.pull_request_url}/reviews/{self.id}/dismissals",
            input=post_parameters,
        )

    def delete(self) -> None:
        """
        :calls: `DELETE /repos/:owner/:repo/pulls/:number/reviews/:review_id <https://developer.github.com/v3/pulls/reviews/>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.pull_request_url}/reviews/{self.id}")

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["user"])
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "commit_id" in attributes:  # pragma no branch
            self._commit_id = self._makeStringAttribute(attributes["commit_id"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "pull_request_url" in attributes:  # pragma no branch
            self._pull_request_url = self._makeStringAttribute(attributes["pull_request_url"])
        if "submitted_at" in attributes:  # pragma no branch
            self._submitted_at = self._makeDatetimeAttribute(attributes["submitted_at"])
