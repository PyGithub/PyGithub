############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Mateusz Loskot <mateusz@loskot.net>                           #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from datetime import datetime

from typing import Any
import urllib.parse
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_optional


class IssueType(CompletableGithubObject):
    """
    This class represents IssueTypes.
    
    The OpenAPI schema can be found at
    - /components/schemas/issue-type
    """
    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._description: Attribute[str] = NotSet
        self._color: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._is_enabled: Attribute[bool] = NotSet
        
    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})
    
    @property
    def _identity(self) -> str:
        return urllib.parse.quote(self.name)
    
    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value
    
    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value
    
    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value
    
    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value
        
    @property
    def color(self) -> str:
        self._completeIfNotSet(self._color)
        return self._color.value
    
    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value
    
    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value
    
    @property
    def is_enabled(self) -> bool:
        self._completeIfNotSet(self._is_enabled)
        return self._is_enabled.value
    
    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:
            self._id = self._makeIntAttribute(attributes["id"])
        if "node_id" in attributes:
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "description" in attributes:
            self._description = self._makeStringAttribute(attributes["description"])
        if "color" in attributes:
            self._color = self._makeStringAttribute(attributes["color"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "is_enabled" in attributes:
            self._is_enabled = self._makeBoolAttribute(attributes["is_enabled"])
            