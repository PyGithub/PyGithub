############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
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

from typing import TYPE_CHECKING, Any

import github.Rate
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.Rate import Rate


class RateLimit(NonCompletableGithubObject):
    """
    This class represents RateLimits.

    The reference can be found here
    https://docs.github.com/en/rest/reference/rate-limit

    """

    def _initAttributes(self) -> None:
        self._core: Attribute[Rate] = NotSet
        self._search: Attribute[Rate] = NotSet
        self._graphql: Attribute[Rate] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"core": self._core.value})

    @property
    def core(self) -> Rate:
        """
        Rate limit for the non-search-related API.
        """
        return self._core.value

    @property
    def search(self) -> Rate:
        """
        Rate limit for the Search API.
        """
        return self._search.value

    @property
    def graphql(self) -> Rate:
        """
        (Experimental) Rate limit for GraphQL API, use with caution.
        """
        return self._graphql.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "core" in attributes:  # pragma no branch
            self._core = self._makeClassAttribute(github.Rate.Rate, attributes["core"])
        if "search" in attributes:  # pragma no branch
            self._search = self._makeClassAttribute(github.Rate.Rate, attributes["search"])
        if "graphql" in attributes:  # pragma no branch
            self._graphql = self._makeClassAttribute(github.Rate.Rate, attributes["graphql"])
