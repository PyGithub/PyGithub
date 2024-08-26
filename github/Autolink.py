############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Nick Campbell <nicholas.j.campbell@gmail.com>                 #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Marco Köpcke <hello@parakoopa.de>                             #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Oskar Jansson <56458534+janssonoskar@users.noreply.github.com>#
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

from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class Autolink(NonCompletableGithubObject):
    """
    This class represents Repository autolinks.

    The reference can be found here
    https://docs.github.com/en/rest/repos/autolinks?apiVersion=2022-11-28

    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._key_prefix: Attribute[str] = NotSet
        self._url_template: Attribute[str] = NotSet
        self._is_alphanumeric: Attribute[bool] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def key_prefix(self) -> str:
        return self._key_prefix.value

    @property
    def url_template(self) -> str:
        return self._url_template.value

    @property
    def is_alphanumeric(self) -> bool:
        return self._is_alphanumeric.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "key_prefix" in attributes:  # pragma no branch
            self._key_prefix = self._makeStringAttribute(attributes["key_prefix"])
        if "url_template" in attributes:  # pragma no branch
            self._url_template = self._makeStringAttribute(attributes["url_template"])
        if "is_alphanumeric" in attributes:  # pragma no branch
            self._is_alphanumeric = self._makeBoolAttribute(attributes["is_alphanumeric"])
