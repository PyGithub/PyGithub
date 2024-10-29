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

from typing import TYPE_CHECKING, Any

import github
import github.Label
import github.NamedUser
import github.Reaction
import github.Repository
import github.RepositoryDiscussionCategory
import github.RepositoryDiscussionComment
from github.DiscussionBase import DiscussionBase
from github.GithubObject import (
    Attribute,
    GraphQlObject,
    NotSet,
    as_rest_api_attributes,
    as_rest_api_attributes_list,
    is_undefined,
)
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.Label import Label
    from github.NamedUser import NamedUser
    from github.Reaction import Reaction
    from github.Repository import Repository
    from github.RepositoryDiscussionCategory import RepositoryDiscussionCategory
    from github.RepositoryDiscussionComment import RepositoryDiscussionComment


class RepositoryDiscussion(GraphQlObject, DiscussionBase):
    """
    This class represents GraphQL Discussion.

    The reference can be found here
    https://docs.github.com/en/graphql/reference/objects#discussion

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._answer: Attribute[RepositoryDiscussionComment | None] = NotSet
        self._body_text: Attribute[str] = NotSet
        self._category: Attribute[RepositoryDiscussionCategory] = NotSet
        self._comments_page = None
        self._database_id: Attribute[int] = NotSet
        self._editor: Attribute[NamedUser] = NotSet
        self._id: Attribute[str] = NotSet
        self._labels_page = None
        self._reactions_page = None
        self._repository: Attribute[Repository] = NotSet

    @property
    def answer(self) -> RepositoryDiscussionComment | None:
        return self._answer.value

    @property
    def body_text(self) -> str:
        return self._body_text.value

    @property
    def category(self) -> RepositoryDiscussionCategory:
        return self._category.value

    @property
    def database_id(self) -> int:
        return self._database_id.value

    @property
    def editor(self) -> NamedUser:
        return self._editor.value

    @property
    def id(self) -> str:
        return self._id.value

    @property
    def node_id(self) -> str:
        return self.id

    @property
    def repository(self) -> Repository:
        return self._repository.value

    def get_comments(self, comment_graphql_schema: str) -> PaginatedList[RepositoryDiscussionComment]:
        if self._comments_page is not None:
            return PaginatedList(
                github.RepositoryDiscussionComment.RepositoryDiscussionComment,
                self._requester,
                firstData=self._comments_page,
                firstHeaders={},
            )

        if is_undefined(self._id):
            raise RuntimeError("Retrieving discussion comments requires the discussion field 'id'")
        if not comment_graphql_schema.startswith("\n"):
            comment_graphql_schema = f" {comment_graphql_schema} "

        query = (
            """
            query Q($discussionId: ID!, $first: Int, $last: Int, $before: String, $after: String) {
              node(id: $discussionId) {
                ... on Discussion {
                  comments(first: $first, last: $last, before: $before, after: $after) {
                    totalCount
                    pageInfo {
                      startCursor
                      endCursor
                      hasNextPage
                      hasPreviousPage
                    }
                    nodes {"""
            + comment_graphql_schema
            + """}
                  }
                }
              }
            }"""
        )
        variables = {"discussionId": self.node_id}
        return PaginatedList(
            github.RepositoryDiscussionComment.RepositoryDiscussionComment,
            self._requester,
            graphql_query=query,
            graphql_variables=variables,
            list_item=["node", "comments"],
        )

    def get_labels(self) -> PaginatedList[Label]:
        if self._labels_page is None:
            raise RuntimeError("Fetching labels not implemented")
        return PaginatedList(github.Label.Label, self._requester, firstData=self._labels_page, firstHeaders={})

    def get_reactions(self) -> PaginatedList[Reaction]:
        if self._reactions_page is None:
            raise RuntimeError("Fetching reactions not implemented")
        return PaginatedList(github.Reaction.Reaction, self._requester, firstData=self._reactions_page, firstHeaders={})

    def add_comment(
        self, body: str, reply_to: RepositoryDiscussionComment | str | None = None, output_schema: str = "id"
    ) -> RepositoryDiscussionComment:
        reply_to_id = (
            reply_to.id
            if isinstance(reply_to, github.RepositoryDiscussionComment.RepositoryDiscussionComment)
            else reply_to
        )
        if not output_schema.startswith("\n"):
            output_schema = f" {output_schema} "

        variables = {"body": body, "discussionId": self.id, "replyToId": reply_to_id}
        return self._requester.graphql_named_mutation_class(
            "addDiscussionComment",
            NotSet.remove_unset_items(variables),
            f"comment {{{output_schema}}}",
            "comment",
            github.RepositoryDiscussionComment.RepositoryDiscussionComment,
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        # super class is a REST API GithubObject, attributes are coming from GraphQL
        super()._useAttributes(as_rest_api_attributes(attributes))
        if "answer" in attributes:  # pragma no branch
            self._answer = self._makeClassAttribute(
                github.RepositoryDiscussionComment.RepositoryDiscussionComment, attributes["answer"]
            )
        if "bodyText" in attributes:  # pragma no branch
            self._body_text = self._makeStringAttribute(attributes["bodyText"])
        if "category" in attributes:  # pragma no branch
            self._category = self._makeClassAttribute(
                github.RepositoryDiscussionCategory.RepositoryDiscussionCategory, attributes["category"]
            )
        if "comments" in attributes:  # pragma no branch
            # comments are GraphQL API objects
            self._comments_page = attributes["comments"]["nodes"]
        if "databaseId" in attributes:  # pragma no branch
            self._database_id = self._makeIntAttribute(attributes["databaseId"])
        if "editor" in attributes:  # pragma no branch
            self._editor = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["editor"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        if "labels" in attributes:  # pragma no branch
            # labels are REST API objects
            self._labels_page = as_rest_api_attributes_list(attributes["labels"]["nodes"])  # type: ignore
        if "reactions" in attributes:  # pragma no branch
            # reactions are REST API objects
            self._reactions_page = as_rest_api_attributes_list(attributes["reactions"]["nodes"])  # type: ignore
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(
                github.Repository.Repository, as_rest_api_attributes(attributes["repository"])
            )
