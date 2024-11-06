############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Victor Zeng <zacker150@users.noreply.github.com>              #
# Copyright 2022 Eric Nieuwland <eric.nieuwland@gmail.com>                     #
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

import github.Reaction
from github.GithubObject import Attribute, GraphQlObject, NonCompletableGithubObject, NotSet, as_rest_api_attributes

if TYPE_CHECKING:
    from github.Repository import Repository


class RepositoryDiscussionCategory(GraphQlObject, NonCompletableGithubObject):
    """
    This class represents GraphQL DiscussionCategory.

    The reference can be found here
    https://docs.github.com/en/graphql/reference/objects#discussioncategory

    """

    def _initAttributes(self) -> None:
        self._created_at: Attribute[datetime] = NotSet
        self._description: Attribute[str] = NotSet
        self._emoji: Attribute[str] = NotSet
        self._emoji_html: Attribute[str] = NotSet
        self._id: Attribute[str] = NotSet
        self._is_answerable: Attribute[bool] = NotSet
        self._name: Attribute[str] = NotSet
        self._repository: Attribute[Repository] = NotSet
        self._slug: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def emoji(self) -> str:
        return self._emoji.value

    @property
    def emoji_html(self) -> str:
        return self._emoji_html.value

    @property
    def id(self) -> str:
        return self._id.value

    @property
    def node_id(self) -> str:
        return self.id

    @property
    def is_answerable(self) -> bool:
        return self._is_answerable.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def repository(self) -> Repository:
        return self._repository.value

    @property
    def slug(self) -> str:
        return self._slug.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "createdAt" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["createdAt"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "emoji" in attributes:  # pragma no branch
            self._emoji = self._makeStringAttribute(attributes["emoji"])
        if "emojiHTML" in attributes:  # pragma no branch
            self._emoji_html = self._makeStringAttribute(attributes["emojiHTML"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        if "isAnswerable" in attributes:  # pragma no branch
            self._is_answerable = self._makeBoolAttribute(attributes["isAnswerable"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "repository" in attributes:  # pragma no branch
            # repository is a REST API object
            self._repository = self._makeClassAttribute(
                github.Repository.Repository, as_rest_api_attributes(attributes["repository"])
            )
        if "slug" in attributes:  # pragma no branch
            self._slug = self._makeStringAttribute(attributes["slug"])
        if "updatedAt" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updatedAt"])
