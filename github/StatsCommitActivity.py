############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
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

import github.GithubObject
from github.GithubObject import Attribute


class StatsCommitActivity(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents StatsCommitActivities.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#get-the-last-year-of-commit-activity

    The OpenAPI schema can be found at
    - /components/schemas/commit-activity

    """

    def _initAttributes(self) -> None:
        self._days: Attribute[int] = github.GithubObject.NotSet
        self._total: Attribute[int] = github.GithubObject.NotSet
        self._week: Attribute[datetime] = github.GithubObject.NotSet

    @property
    def days(self) -> int:
        return self._days.value

    @property
    def total(self) -> int:
        return self._total.value

    @property
    def week(self) -> datetime:
        return self._week.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "days" in attributes:  # pragma no branch
            self._days = self._makeListOfIntsAttribute(attributes["days"])
        if "total" in attributes:  # pragma no branch
            self._total = self._makeIntAttribute(attributes["total"])
        if "week" in attributes:  # pragma no branch
            self._week = self._makeTimestampAttribute(attributes["week"])
