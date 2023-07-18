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

import github.GitAuthor
import github.GithubObject
import github.GitObject
import github.GitTreeElement
from github.GithubObject import Attribute, CompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.GitAuthor import GitAuthor
    from github.GitObject import GitObject


class GitTag(CompletableGithubObject):
    """
    This class represents GitTags. The reference can be found here https://docs.github.com/en/rest/reference/git#tags
    """

    def _initAttributes(self) -> None:
        self._message: Attribute[str] = NotSet
        self._object: Attribute[GitObject] = NotSet
        self._sha: Attribute[str] = NotSet
        self._tag: Attribute[str] = NotSet
        self._tagger: Attribute[GitAuthor] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"sha": self._sha.value, "tag": self._tag.value})

    @property
    def message(self) -> str:
        self._completeIfNotSet(self._message)
        return self._message.value

    @property
    def object(self) -> GitObject:
        self._completeIfNotSet(self._object)
        return self._object.value

    @property
    def sha(self) -> str:
        self._completeIfNotSet(self._sha)
        return self._sha.value

    @property
    def tag(self) -> str:
        self._completeIfNotSet(self._tag)
        return self._tag.value

    @property
    def tagger(self) -> GitAuthor:
        self._completeIfNotSet(self._tagger)
        return self._tagger.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "message" in attributes:  # pragma no branch
            self._message = self._makeStringAttribute(attributes["message"])
        if "object" in attributes:  # pragma no branch
            self._object = self._makeClassAttribute(github.GitObject.GitObject, attributes["object"])
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "tag" in attributes:  # pragma no branch
            self._tag = self._makeStringAttribute(attributes["tag"])
        if "tagger" in attributes:  # pragma no branch
            self._tagger = self._makeClassAttribute(github.GitAuthor.GitAuthor, attributes["tagger"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
