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

from github.DiscussionCommentBase import DiscussionCommentBase
from github.GithubObject import Attribute, NotSet


class RepositoryDiscussionComment(DiscussionCommentBase):
    """
    This class represents RepositoryDiscussionComments.

    The reference can be found here
    https://docs.github.com/en/graphql/reference/objects#discussioncomment

    """

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

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "body_text" in attributes:  # pragma no branch
            self._body_text = self._makeStringAttribute(attributes["body_text"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
