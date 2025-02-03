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

import github.Commit
import github.File
from github.GithubObject import Attribute, CompletableGithubObject, NotSet
from github.PaginatedList import PaginatedList


class Comparison(CompletableGithubObject):
    """
    This class represents Comparisons.
    """

    def _initAttributes(self) -> None:
        self._ahead_by: Attribute[int] = NotSet
        self._base_commit: Attribute[github.Commit.Commit] = NotSet
        self._behind_by: Attribute[int] = NotSet
        self._diff_url: Attribute[str] = NotSet
        self._files: Attribute[list[github.File.File]] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._merge_base_commit: Attribute[github.Commit.Commit] = NotSet
        self._patch_url: Attribute[str] = NotSet
        self._permalink_url: Attribute[str] = NotSet
        self._status: Attribute[str] = NotSet
        self._total_commits: Attribute[int] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"url": self._url.value})

    @property
    def ahead_by(self) -> int:
        self._completeIfNotSet(self._ahead_by)
        return self._ahead_by.value

    @property
    def base_commit(self) -> github.Commit.Commit:
        self._completeIfNotSet(self._base_commit)
        return self._base_commit.value

    @property
    def behind_by(self) -> int:
        self._completeIfNotSet(self._behind_by)
        return self._behind_by.value

    # This should be a method, but this used to be a property and cannot be changed without breaking user code
    # TODO: remove @property on version 3
    @property
    def commits(self) -> PaginatedList[github.Commit.Commit]:
        return PaginatedList(
            github.Commit.Commit,
            self._requester,
            self.url,
            {},
            headers=None,
            list_item="commits",
            total_count_item="total_commits",
            firstData=self.raw_data,
            firstHeaders=self.raw_headers,
        )

    @property
    def diff_url(self) -> str:
        self._completeIfNotSet(self._diff_url)
        return self._diff_url.value

    @property
    def files(self) -> list[github.File.File]:
        self._completeIfNotSet(self._files)
        return self._files.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def merge_base_commit(self) -> github.Commit.Commit:
        self._completeIfNotSet(self._merge_base_commit)
        return self._merge_base_commit.value

    @property
    def patch_url(self) -> str:
        self._completeIfNotSet(self._patch_url)
        return self._patch_url.value

    @property
    def permalink_url(self) -> str:
        self._completeIfNotSet(self._permalink_url)
        return self._permalink_url.value

    @property
    def status(self) -> str:
        self._completeIfNotSet(self._status)
        return self._status.value

    @property
    def total_commits(self) -> int:
        self._completeIfNotSet(self._total_commits)
        return self._total_commits.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "ahead_by" in attributes:  # pragma no branch
            self._ahead_by = self._makeIntAttribute(attributes["ahead_by"])
        if "base_commit" in attributes:  # pragma no branch
            self._base_commit = self._makeClassAttribute(github.Commit.Commit, attributes["base_commit"])
        if "behind_by" in attributes:  # pragma no branch
            self._behind_by = self._makeIntAttribute(attributes["behind_by"])
        if "diff_url" in attributes:  # pragma no branch
            self._diff_url = self._makeStringAttribute(attributes["diff_url"])
        if "files" in attributes:  # pragma no branch
            self._files = self._makeListOfClassesAttribute(github.File.File, attributes["files"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "merge_base_commit" in attributes:  # pragma no branch
            self._merge_base_commit = self._makeClassAttribute(github.Commit.Commit, attributes["merge_base_commit"])
        if "patch_url" in attributes:  # pragma no branch
            self._patch_url = self._makeStringAttribute(attributes["patch_url"])
        if "permalink_url" in attributes:  # pragma no branch
            self._permalink_url = self._makeStringAttribute(attributes["permalink_url"])
        if "status" in attributes:  # pragma no branch
            self._status = self._makeStringAttribute(attributes["status"])
        if "total_commits" in attributes:  # pragma no branch
            self._total_commits = self._makeIntAttribute(attributes["total_commits"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
