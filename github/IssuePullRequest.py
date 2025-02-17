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


from __future__ import annotations

from datetime import datetime
from typing import Any

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class IssuePullRequest(NonCompletableGithubObject):
    """
    This class represents IssuePullRequests.

    The OpenAPI schema can be found at
    - /components/schemas/issue-search-result-item/properties/pull_request
    - /components/schemas/issue/properties/pull_request
    - /components/schemas/nullable-issue/properties/pull_request

    """

    def _initAttributes(self) -> None:
        self._diff_url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._merged_at: Attribute[datetime] = NotSet
        self._patch_url: Attribute[str] = NotSet
        self._url: Attribute[str] = NotSet

    @property
    def diff_url(self) -> str:
        return self._diff_url.value

    @property
    def html_url(self) -> str:
        return self._html_url.value

    @property
    def merged_at(self) -> datetime:
        return self._merged_at.value

    @property
    def patch_url(self) -> str:
        return self._patch_url.value

    @property
    def url(self) -> str:
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "diff_url" in attributes:  # pragma no branch
            self._diff_url = self._makeStringAttribute(attributes["diff_url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "merged_at" in attributes:  # pragma no branch
            self._merged_at = self._makeDatetimeAttribute(attributes["merged_at"])
        if "patch_url" in attributes:  # pragma no branch
            self._patch_url = self._makeStringAttribute(attributes["patch_url"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
