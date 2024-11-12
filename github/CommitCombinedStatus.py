############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 John Eskew <jeskew@edx.org>                                   #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
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

from typing import Any

import github.CommitStatus
import github.Repository
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class CommitCombinedStatus(NonCompletableGithubObject):
    """
    This class represents CommitCombinedStatuses.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#statuses

    """

    def _initAttributes(self) -> None:
        self._state: Attribute[str] = NotSet
        self._sha: Attribute[str] = NotSet
        self._total_count: Attribute[int] = NotSet
        self._commit_url: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet
        self._repository: Attribute[github.Repository.Repository] = NotSet
        self._statuses: Attribute[list[github.CommitStatus.CommitStatus]] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"sha": self._sha.value, "state": self._state.value})

    @property
    def state(self) -> str:
        return self._state.value

    @property
    def sha(self) -> str:
        return self._sha.value

    @property
    def total_count(self) -> int:
        return self._total_count.value

    @property
    def commit_url(self) -> str:
        return self._commit_url.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def repository(self) -> github.Repository.Repository:
        return self._repository.value

    @property
    def statuses(self) -> list[github.CommitStatus.CommitStatus]:
        return self._statuses.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "total_count" in attributes:  # pragma no branch
            self._total_count = self._makeIntAttribute(attributes["total_count"])
        if "commit_url" in attributes:  # pragma no branch
            self._commit_url = self._makeStringAttribute(attributes["commit_url"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
        if "statuses" in attributes:  # pragma no branch
            self._statuses = self._makeListOfClassesAttribute(github.CommitStatus.CommitStatus, attributes["statuses"])
