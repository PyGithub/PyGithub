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

from datetime import datetime
from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class GitAuthor(NonCompletableGithubObject):
    """
    This class represents GitAuthors.

    The OpenAPI schema can be found at
    - /components/schemas/commit-search-result-item/properties/commit/properties/author
    - /components/schemas/file-commit/properties/commit/properties/author
    - /components/schemas/file-commit/properties/commit/properties/committer
    - /components/schemas/git-commit/properties/author
    - /components/schemas/git-commit/properties/committer
    - /components/schemas/git-tag/properties/tagger
    - /components/schemas/nullable-git-user
    - /components/schemas/nullable-simple-commit/properties/author
    - /components/schemas/nullable-simple-commit/properties/committer
    - /components/schemas/simple-commit/properties/author
    - /components/schemas/simple-commit/properties/committer

    """

    def _initAttributes(self) -> None:
        self._date: Attribute[datetime] = NotSet
        self._email: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def date(self) -> datetime:
        return self._date.value

    @property
    def email(self) -> str:
        return self._email.value

    @property
    def name(self) -> str:
        return self._name.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "date" in attributes:  # pragma no branch
            self._date = self._makeDatetimeAttribute(attributes["date"])
        if "email" in attributes:  # pragma no branch
            self._email = self._makeStringAttribute(attributes["email"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
