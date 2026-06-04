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

from typing import Any

import github.CommitStatus
import github.Repository
from github.GithubObject import Attribute, CompletableGithubObjectWithPaginatedProperty, NotSet
from github.PaginatedList import PaginatedList


class CommitCombinedStatus(CompletableGithubObjectWithPaginatedProperty):
    """
    This class represents CommitCombinedStatuses.

    The reference can be found here
    https://docs.github.com/en/rest/commits/statuses#get-the-combined-status-for-a-specific-reference

    This class has a `paginated property <https://pygithub.readthedocs.io/en/stable/utilities.html#classes-with-paginated-properties>`_.
    For details, see :meth:`CommitCombinedStatus.statuses` or :meth:`CommitCombinedStatus.get_statuses`.

    The OpenAPI schema can be found at

    - /components/schemas/combined-commit-status

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._commit_url: Attribute[str] = NotSet
        self._repository: Attribute[github.Repository.Repository] = NotSet
        self._sha: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._statuses: Attribute[list[github.CommitStatus.CommitStatus]] = NotSet
        self._total_count: Attribute[int] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"sha": self._sha.value, "state": self._state.value})

    @property
    def commit_url(self) -> str:
        self._completeIfNotSet(self._commit_url)
        return self._commit_url.value

    @property
    def repository(self) -> github.Repository.Repository:
        self._completeIfNotSet(self._repository)
        return self._repository.value

    @property
    def sha(self) -> str:
        self._completeIfNotSet(self._sha)
        return self._sha.value

    @property
    def state(self) -> str:
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def statuses(self) -> PaginatedList[github.CommitStatus.CommitStatus]:
        """
        This is a `paginated property <https://pygithub.readthedocs.io/en/stable/utilities.html#classes-with-paginated-properties>`_.

        Iterating over this paginated list may fetch multiple pages. The size of these pages can be controlled via
        the ``…_per_page`` parameter of :meth:`github.Commit.Commit.get_combined_status`,
        :meth:`github.CommitCombinedStatus.CommitCombinedStatus.get_statuses`, or :meth:`github.Github`.

        If no ``per_page`` is given, the default page size is 30. The maximum is 100.
        """
        return PaginatedList(
            github.CommitStatus.CommitStatus,
            self._requester,
            self.url,
            self._pagination_parameters,
            headers=None,
            list_item="statuses",
            total_count_item="total_count",
            firstData=self.raw_data if self.completed else None,
            firstHeaders=self.raw_headers if self.completed else None,
        )

    @property
    def total_count(self) -> int:
        self._completeIfNotSet(self._total_count)
        return self._total_count.value

    def get_statuses(self, *, combined_status_statuses_per_page: int | None = None) -> PaginatedList[github.CommitStatus.CommitStatus]:
        """
        :calls: `GET /repos/{owner}/{repo}/commits/{ref}/status <https://docs.github.com/en/rest/commits/statuses#get-the-combined-status-for-a-specific-reference>`_

        Identical to calling :meth:`github.CommitCombinedStatus.CommitCombinedStatus.statuses`, except that this uses the given ``per_page`` value.

        For more details, see :meth:`github.CommitCombinedStatus.CommitCombinedStatus.statuses`.

        :param combined_status_statuses_per_page: int Number of statuses retrieved per page.
               Iterating over the statuses will fetch pages of this size. The default page size is 30, the maximum is 100.
        """
        return PaginatedList(
            github.CommitStatus.CommitStatus,
            self._requester,
            self.url,
            self._pagination_parameters_with(page=1, per_page=combined_status_statuses_per_page),
            headers=None,
            list_item="statuses",
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "commit_url" in attributes:  # pragma no branch
            self._commit_url = self._makeStringAttribute(attributes["commit_url"])
        if "repository" in attributes:  # pragma no branch
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "statuses" in attributes:  # pragma no branch
            self._statuses = self._makeListOfClassesAttribute(github.CommitStatus.CommitStatus, attributes["statuses"])
        if "total_count" in attributes:  # pragma no branch
            self._total_count = self._makeIntAttribute(attributes["total_count"])
