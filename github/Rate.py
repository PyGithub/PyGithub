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
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Nikolay Yurin <yurinnick93@gmail.com>                         #
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

from datetime import datetime
from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class Rate(NonCompletableGithubObject):
    """
    This class represents Rates.

    The reference can be found here
    https://docs.github.com/en/rest/reference/rate-limit

    The OpenAPI schema can be found at
    - /components/schemas/rate-limit

    """

    def _initAttributes(self) -> None:
        self._limit: Attribute[int] = NotSet
        self._remaining: Attribute[int] = NotSet
        self._reset: Attribute[datetime] = NotSet
        self._used: Attribute[int] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__(
            {
                "limit": self._limit.value,
                "remaining": self._remaining.value,
                "reset": self._reset.value,
            }
        )

    @property
    def limit(self) -> int:
        return self._limit.value

    @property
    def remaining(self) -> int:
        return self._remaining.value

    @property
    def reset(self) -> datetime:
        return self._reset.value

    @property
    def used(self) -> int:
        return self._used.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "limit" in attributes:  # pragma no branch
            self._limit = self._makeIntAttribute(attributes["limit"])
        if "remaining" in attributes:  # pragma no branch
            self._remaining = self._makeIntAttribute(attributes["remaining"])
        if "reset" in attributes:  # pragma no branch
            self._reset = self._makeTimestampAttribute(attributes["reset"])
        if "used" in attributes:  # pragma no branch
            self._used = self._makeIntAttribute(attributes["used"])
