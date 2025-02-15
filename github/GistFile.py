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
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class GistFile(NonCompletableGithubObject):
    """
    This class represents GistFiles.

    The OpenAPI schema can be found at
    - /components/schemas/base-gist/properties/files
    - /components/schemas/gist-simple/properties/files
    - /components/schemas/gist-simple/properties/fork_of/properties/files

    """

    def _initAttributes(self) -> None:
        self._content: Attribute[str] = NotSet
        self._filename: Attribute[str] = NotSet
        self._language: Attribute[str] = NotSet
        self._raw_url: Attribute[str] = NotSet
        self._size: Attribute[int] = NotSet
        self._type: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"filename": self._filename.value})

    @property
    def content(self) -> str:
        return self._content.value

    @property
    def filename(self) -> str:
        return self._filename.value

    @property
    def language(self) -> str:
        return self._language.value

    @property
    def raw_url(self) -> str:
        return self._raw_url.value

    @property
    def size(self) -> int:
        return self._size.value

    @property
    def type(self) -> str:
        return self._type.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "content" in attributes:  # pragma no branch
            self._content = self._makeStringAttribute(attributes["content"])
        if "filename" in attributes:  # pragma no branch
            self._filename = self._makeStringAttribute(attributes["filename"])
        if "language" in attributes:  # pragma no branch
            self._language = self._makeStringAttribute(attributes["language"])
        if "raw_url" in attributes:  # pragma no branch
            self._raw_url = self._makeStringAttribute(attributes["raw_url"])
        if "size" in attributes:  # pragma no branch
            self._size = self._makeIntAttribute(attributes["size"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
