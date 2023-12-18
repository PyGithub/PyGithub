############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Justin Kufro <jkufro@andrew.cmu.edu>                          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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


class Path(NonCompletableGithubObject):
    """
    This class represents a popular Path for a GitHub repository.
    The reference can be found here https://docs.github.com/en/rest/reference/repos#traffic
    """

    def _initAttributes(self) -> None:
        self._path: Attribute[str] = NotSet
        self._title: Attribute[str] = NotSet
        self._count: Attribute[int] = NotSet
        self._uniques: Attribute[int] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "path": self._path.value,
                "title": self._title.value,
                "count": self._count.value,
                "uniques": self._uniques.value,
            }
        )

    @property
    def path(self) -> str:
        return self._path.value

    @property
    def title(self) -> str:
        return self._title.value

    @property
    def count(self) -> int:
        return self._count.value

    @property
    def uniques(self) -> int:
        return self._uniques.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
        if "title" in attributes:  # pragma no branch
            self._title = self._makeStringAttribute(attributes["title"])
        if "count" in attributes:  # pragma no branch
            self._count = self._makeIntAttribute(attributes["count"])
        if "uniques" in attributes:  # pragma no branch
            self._uniques = self._makeIntAttribute(attributes["uniques"])
