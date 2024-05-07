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

from datetime import datetime

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class StatsCodeFrequency(NonCompletableGithubObject):
    """
    This class represents statistics of StatsCodeFrequencies.

    The reference can be found here
    https://docs.github.com/en/rest/metrics/statistics?apiVersion=2022-11-28#get-the-weekly-commit-activity

    """

    def _initAttributes(self) -> None:
        self._week: Attribute[datetime] = NotSet
        self._additions: Attribute[int] = NotSet
        self._deletions: Attribute[int] = NotSet

    @property
    def week(self) -> datetime:
        return self._week.value

    @property
    def additions(self) -> int:
        return self._additions.value

    @property
    def deletions(self) -> int:
        return self._deletions.value

    def _useAttributes(self, attributes: tuple[int, int, int]) -> None:
        self._week = self._makeTimestampAttribute(attributes[0])
        self._additions = self._makeIntAttribute(attributes[1])
        self._deletions = self._makeIntAttribute(attributes[2])
