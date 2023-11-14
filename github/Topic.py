############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
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

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class Topic(NonCompletableGithubObject):
    """
    This class represents topics as used by https://github.com/topics. The object reference can be found here https://docs.github.com/en/rest/reference/search#search-topics
    """

    def _initAttributes(self) -> None:
        self._name: Attribute[str] = NotSet
        self._display_name: Attribute[str] = NotSet
        self._short_description: Attribute[str] = NotSet
        self._description: Attribute[str] = NotSet
        self._created_by: Attribute[str] = NotSet
        self._released: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._featured: Attribute[bool] = NotSet
        self._curated: Attribute[bool] = NotSet
        self._score: Attribute[float] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def display_name(self) -> str:
        return self._display_name.value

    @property
    def short_description(self) -> str:
        return self._short_description.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def created_by(self) -> str:
        return self._created_by.value

    @property
    def released(self) -> str:
        return self._released.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def featured(self) -> bool:
        return self._featured.value

    @property
    def curated(self) -> bool:
        return self._curated.value

    @property
    def score(self) -> float:
        return self._score.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "display_name" in attributes:  # pragma no branch
            self._display_name = self._makeStringAttribute(attributes["display_name"])
        if "short_description" in attributes:  # pragma no branch
            self._short_description = self._makeStringAttribute(attributes["short_description"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "created_by" in attributes:  # pragma no branch
            self._created_by = self._makeStringAttribute(attributes["created_by"])
        if "released" in attributes:  # pragma no branch
            self._released = self._makeStringAttribute(attributes["released"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "featured" in attributes:  # pragma no branch
            self._featured = self._makeBoolAttribute(attributes["featured"])
        if "curated" in attributes:  # pragma no branch
            self._curated = self._makeBoolAttribute(attributes["curated"])
        if "score" in attributes:  # pragma no branch
            self._score = self._makeFloatAttribute(attributes["score"])
