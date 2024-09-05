############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

from typing import Any

import github
from github.DiscussionBase import DiscussionBase
from github.GithubObject import Attribute, NotSet, as_rest_api_attributes
from github.PaginatedList import PaginatedList
from github.RepositoryDiscussionComment import RepositoryDiscussionComment


class RepositoryDiscussion(DiscussionBase):
    """
    This class represents RepositoryDiscussions.

    The reference can be found here
    https://docs.github.com/en/graphql/reference/objects#discussion

    """

    minimal_graphql_schema = "{ id url number }"

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._body_text: Attribute[str] = NotSet
        self._id: Attribute[str] = NotSet

    @property
    def body_text(self) -> str:
        self._completeIfNotSet(self._body_text)
        return self._body_text.value

    @property
    def id(self) -> str:
        self._completeIfNotSet(self._id)
        return self._id.value

    def get_comments(self) -> PaginatedList[RepositoryDiscussionComment]:
        return PaginatedList(
            github.RepositoryDiscussionComment.RepositoryDiscussionComment,
            self._requester,
            f"{self.url}/pulls",
            {},
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        # super class is a REST API GithubObject, attributes are coming from GraphQL
        super()._useAttributes(as_rest_api_attributes(attributes))
        if "bodyText" in attributes:  # pragma no branch
            self._body_text = self._makeStringAttribute(attributes["bodyText"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
