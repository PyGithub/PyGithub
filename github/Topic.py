############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

    The OpenAPI schema can be found at
    - /components/schemas/topic-search-result-item

    """

    def _initAttributes(self) -> None:
        self._aliases: Attribute[list[dict[str, Any]]] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._created_by: Attribute[str] = NotSet
        self._curated: Attribute[bool] = NotSet
        self._description: Attribute[str] = NotSet
        self._display_name: Attribute[str] = NotSet
        self._featured: Attribute[bool] = NotSet
        self._logo_url: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._related: Attribute[list[dict[str, Any]]] = NotSet
        self._released: Attribute[str] = NotSet
        self._repository_count: Attribute[int] = NotSet
        self._score: Attribute[float] = NotSet
        self._short_description: Attribute[str] = NotSet
        self._text_matches: Attribute[dict[str, Any]] = NotSet
        self._updated_at: Attribute[datetime] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def aliases(self) -> list[dict[str, Any]]:
        return self._aliases.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def created_by(self) -> str:
        return self._created_by.value

    @property
    def curated(self) -> bool:
        return self._curated.value

    @property
    def description(self) -> str:
        return self._description.value

    @property
    def display_name(self) -> str:
        return self._display_name.value

    @property
    def featured(self) -> bool:
        return self._featured.value

    @property
    def logo_url(self) -> str:
        return self._logo_url.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def related(self) -> list[dict[str, Any]]:
        return self._related.value

    @property
    def released(self) -> str:
        return self._released.value

    @property
    def repository_count(self) -> int:
        return self._repository_count.value

    @property
    def score(self) -> float:
        return self._score.value

    @property
    def short_description(self) -> str:
        return self._short_description.value

    @property
    def text_matches(self) -> dict[str, Any]:
        return self._text_matches.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "aliases" in attributes:  # pragma no branch
            self._aliases = self._makeListOfDictsAttribute(attributes["aliases"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "created_by" in attributes:  # pragma no branch
            self._created_by = self._makeStringAttribute(attributes["created_by"])
        if "curated" in attributes:  # pragma no branch
            self._curated = self._makeBoolAttribute(attributes["curated"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "display_name" in attributes:  # pragma no branch
            self._display_name = self._makeStringAttribute(attributes["display_name"])
        if "featured" in attributes:  # pragma no branch
            self._featured = self._makeBoolAttribute(attributes["featured"])
        if "logo_url" in attributes:  # pragma no branch
            self._logo_url = self._makeStringAttribute(attributes["logo_url"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "related" in attributes:  # pragma no branch
            self._related = self._makeListOfDictsAttribute(attributes["related"])
        if "released" in attributes:  # pragma no branch
            self._released = self._makeStringAttribute(attributes["released"])
        if "repository_count" in attributes:  # pragma no branch
            self._repository_count = self._makeIntAttribute(attributes["repository_count"])
        if "score" in attributes:  # pragma no branch
            self._score = self._makeFloatAttribute(attributes["score"])
        if "short_description" in attributes:  # pragma no branch
            self._short_description = self._makeStringAttribute(attributes["short_description"])
        if "text_matches" in attributes:  # pragma no branch
            self._text_matches = self._makeDictAttribute(attributes["text_matches"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
