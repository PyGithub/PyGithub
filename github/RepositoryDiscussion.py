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

from typing import TYPE_CHECKING, Any, List

import github
import github.Label
import github.Reaction
import github.Repository
from github.DiscussionBase import DiscussionBase
from github.GithubObject import Attribute, NotSet, as_rest_api_attributes
from github.PaginatedList import PaginatedList
from github.RepositoryDiscussionComment import RepositoryDiscussionComment

if TYPE_CHECKING:
    from github.Label import Label
    from github.Reaction import Reaction
    from github.Repository import Repository


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
        self._comments_page = None
        self._database_id: Attribute[int] = NotSet
        self._id: Attribute[str] = NotSet
        self._labels_page = None
        self._reactions_page = None
        self._repository: Attribute[Repository] = NotSet

    @property
    def body_text(self) -> str:
        self._completeIfNotSet(self._body_text)
        return self._body_text.value

    @property
    def database_id(self) -> int:
        self._completeIfNotSet(self._database_id)
        return self._database_id.value

    @property
    def id(self) -> str:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def node_id(self) -> str:
        return self.id

    @property
    def repository(self) -> Repository:
        self._completeIfNotSet(self._repository)
        return self._repository.value

    def get_labels(self) -> PaginatedList[Label]:
        if self._labels_page is None:
            raise RuntimeError("Fetching labels not implemented")
        return PaginatedList(
            github.Label.Label,
            self._requester,
            firstData=self._labels_page,
            firstHeaders={}
        )

    def get_comments(self) -> PaginatedList[RepositoryDiscussionComment]:
        if self._comments_page is None:
            raise RuntimeError("Fetching comments not implemented")
        return PaginatedList(
            github.RepositoryDiscussionComment.RepositoryDiscussionComment,
            self._requester,
            firstData=self._comments_page,
            firstHeaders={}
        )

    def get_reactions(self) -> PaginatedList[Reaction]:
        if self._reactions_page is None:
            raise RuntimeError("Fetching reactions not implemented")
        return PaginatedList(
            github.Reaction.Reaction,
            self._requester,
            firstData=self._reactions_page,
            firstHeaders={}
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        # super class is a REST API GithubObject, attributes are coming from GraphQL
        super()._useAttributes(as_rest_api_attributes(attributes))
        if "bodyText" in attributes:  # pragma no branch
            self._body_text = self._makeStringAttribute(attributes["bodyText"])
        if "comments" in attributes:  # pragma no branch
            # comments are GraphQL API objects
            self._comments_page = attributes["comments"]["nodes"]
        if "databaseId" in attributes:  # pragma no branch
            self._database_id = self._makeIntAttribute(attributes["databaseId"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        if "labels" in attributes:  # pragma no branch
            # labels are REST API objects
            self._labels_page = as_rest_api_attributes(attributes["labels"]["nodes"])
        if "reactions" in attributes:  # pragma no branch
            # reactions are REST API objects
            self._reactions_page = as_rest_api_attributes(attributes["reactions"]["nodes"])
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(github.Repository.Repository, as_rest_api_attributes(attributes["repository"]))
