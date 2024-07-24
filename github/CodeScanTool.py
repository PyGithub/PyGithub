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
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Eric Nieuwland <eric.nieuwland@gmail.com>                     #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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


class CodeScanTool(NonCompletableGithubObject):
    """
    This class represents code scanning tools.

    The reference can be found here
    https://docs.github.com/en/rest/reference/code-scanning.

    """

    def _initAttributes(self) -> None:
        self._name: Attribute[str] = NotSet
        self._version: Attribute[str] = NotSet
        self._guid: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "guid": self.guid,
                "name": self.name,
                "version": self.version,
            }
        )

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def version(self) -> str:
        return self._version.value

    @property
    def guid(self) -> str:
        return self._guid.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "version" in attributes:  # pragma no branch
            self._version = self._makeStringAttribute(attributes["version"])
        if "guid" in attributes:  # pragma no branch
            self._guid = self._makeStringAttribute(attributes["guid"])
