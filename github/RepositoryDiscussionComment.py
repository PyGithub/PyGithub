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

import github.NamedUser
import github.Reaction
from github.DiscussionCommentBase import DiscussionCommentBase
from github.GithubObject import (
    Attribute,
    GraphQlObject,
    NotSet,
    as_rest_api_attributes,
    as_rest_api_attributes_list,
    is_defined,
)
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.NamedUser import NamedUser
    from github.Reaction import Reaction
    from github.RepositoryDiscussion import RepositoryDiscussion


class RepositoryDiscussionComment(GraphQlObject, DiscussionCommentBase):
    """
    This class represents GraphQL DiscussionComment.

    The reference can be found here
    https://docs.github.com/en/graphql/reference/objects#discussioncomment

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._body_text: Attribute[str] = NotSet
        self._database_id: Attribute[int] = NotSet
        self._discussion: Attribute[RepositoryDiscussion]
        self._editor: Attribute[NamedUser] = NotSet
        self._id: Attribute[str] = NotSet
        self._reactions_page = None
        self._replies_page = None

    @property
    def body_text(self) -> str:
        return self._body_text.value

    @property
    def database_id(self) -> int:
        return self._database_id.value

    @property
    def discussion(self) -> RepositoryDiscussion:
        return self._discussion.value

    @property
    def editor(self) -> NamedUser:
        return self._editor.value

    @property
    def id(self) -> str:
        return self._id.value

    @property
    def node_id(self) -> str:
        if is_defined(self._node_id):
            return super().node_id
        return self.id

    def get_reactions(self) -> PaginatedList[Reaction]:
        if self._reactions_page is None:
            raise RuntimeError("Fetching reactions not implemented")
        return PaginatedList(github.Reaction.Reaction, self._requester, firstData=self._reactions_page, firstHeaders={})

    def get_replies(self) -> PaginatedList[RepositoryDiscussionComment]:
        if self._replies_page is None:
            raise RuntimeError("Fetching replies not implemented")
        return PaginatedList(
            RepositoryDiscussionComment, self._requester, firstData=self._replies_page, firstHeaders={}
        )

    def edit(self, body: str, output_schema: str = "id") -> RepositoryDiscussionComment:
        if not output_schema.startswith("\n"):
            output_schema = f" {output_schema} "
        return self._requester.graphql_named_mutation_class(
            "updateDiscussionComment",
            {"commentId": self.node_id, "body": body},
            f"comment {{{output_schema}}}",
            "comment",
            github.RepositoryDiscussionComment.RepositoryDiscussionComment,
        )

    def delete(self, output_schema: str = "id") -> RepositoryDiscussionComment:
        if not output_schema.startswith("\n"):
            output_schema = f" {output_schema} "
        return self._requester.graphql_named_mutation_class(
            "deleteDiscussionComment",
            {"id": self.id},
            f"comment {{{output_schema}}}",
            "comment",
            github.RepositoryDiscussionComment.RepositoryDiscussionComment,
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        # super class is a REST API GithubObject, attributes are coming from GraphQL
        super()._useAttributes(as_rest_api_attributes(attributes))
        if "bodyText" in attributes:  # pragma no branch
            self._body_text = self._makeStringAttribute(attributes["bodyText"])
        if "databaseId" in attributes:  # pragma no branch
            self._database_id = self._makeIntAttribute(attributes["databaseId"])
        if "discussion" in attributes:  # pragma no branch
            # RepositoryDiscussion is a GraphQL API object
            self._discussion = self._makeClassAttribute(
                github.RepositoryDiscussion.RepositoryDiscussion, attributes["discussion"]
            )
        if "editor" in attributes:  # pragma no branch
            # NamedUser is a REST API object
            self._editor = self._makeClassAttribute(
                github.NamedUser.NamedUser, as_rest_api_attributes(attributes["editor"])
            )
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        if "reactions" in attributes:  # pragma no branch
            # reactions are REST API objects
            self._reactions_page = as_rest_api_attributes_list(attributes["reactions"]["nodes"])  # type: ignore
        if "replies" in attributes:  # pragma no branch
            # replies are GraphQL API objects
            self._replies_page = attributes["replies"]["nodes"]
