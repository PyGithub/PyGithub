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

from datetime import datetime
from typing import Any

import github.CommitStats
import github.Gist
import github.GithubObject
import github.NamedUser
from github.GistFile import GistFile
from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class GistHistoryState(CompletableGithubObject):
    """
    This class represents GistHistoryStates.
    """

    def _initAttributes(self) -> None:
        self._change_status: Attribute[github.CommitStats.CommitStats] = NotSet
        self._comments: Attribute[int] = NotSet
        self._comments_url: Attribute[str] = NotSet
        self._commits_url: Attribute[str] = NotSet
        self._committed_at: Attribute[datetime] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._description: Attribute[str] = NotSet
        self._files: Attribute[dict[str, GistFile]] = NotSet
        self._forks: Attribute[list[github.Gist.Gist]] = NotSet
        self._forks_url: Attribute[str] = NotSet
        self._git_pull_url: Attribute[str] = NotSet
        self._git_push_url: Attribute[str] = NotSet
        self._history: Attribute[list[GistHistoryState]] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[str] = NotSet
        self._owner: Attribute[github.NamedUser.NamedUser] = NotSet
        self._public: Attribute[bool] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._user: Attribute[github.NamedUser.NamedUser] = NotSet
        self._version: Attribute[str] = NotSet

    @property
    def change_status(self) -> github.CommitStats.CommitStats:
        self._completeIfNotSet(self._change_status)
        return self._change_status.value

    @property
    def comments(self) -> int:
        self._completeIfNotSet(self._comments)
        return self._comments.value

    @property
    def comments_url(self) -> str:
        self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    def commits_url(self) -> str:
        self._completeIfNotSet(self._commits_url)
        return self._commits_url.value

    @property
    def committed_at(self) -> datetime:
        self._completeIfNotSet(self._committed_at)
        return self._committed_at.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def files(self) -> dict[str, GistFile]:
        self._completeIfNotSet(self._files)
        return self._files.value

    @property
    def forks(self) -> list[github.Gist.Gist]:
        self._completeIfNotSet(self._forks)
        return self._forks.value

    @property
    def forks_url(self) -> str:
        self._completeIfNotSet(self._forks_url)
        return self._forks_url.value

    @property
    def git_pull_url(self) -> str:
        self._completeIfNotSet(self._git_pull_url)
        return self._git_pull_url.value

    @property
    def git_push_url(self) -> str:
        self._completeIfNotSet(self._git_push_url)
        return self._git_push_url.value

    @property
    def history(self) -> list[GistHistoryState]:
        self._completeIfNotSet(self._history)
        return self._history.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> str:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def owner(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._owner)
        return self._owner.value

    @property
    def public(self) -> bool:
        self._completeIfNotSet(self._public)
        return self._public.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def user(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._user)
        return self._user.value

    @property
    def version(self) -> str:
        self._completeIfNotSet(self._version)
        return self._version.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "change_status" in attributes:  # pragma no branch
            self._change_status = self._makeClassAttribute(github.CommitStats.CommitStats, attributes["change_status"])
        if "comments" in attributes:  # pragma no branch
            self._comments = self._makeIntAttribute(attributes["comments"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "commits_url" in attributes:  # pragma no branch
            self._commits_url = self._makeStringAttribute(attributes["commits_url"])
        if "committed_at" in attributes:  # pragma no branch
            self._committed_at = self._makeDatetimeAttribute(attributes["committed_at"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "files" in attributes:  # pragma no branch
            self._files = self._makeDictOfStringsToClassesAttribute(github.GistFile.GistFile, attributes["files"])
        if "forks" in attributes:  # pragma no branch
            self._forks = self._makeListOfClassesAttribute(github.Gist.Gist, attributes["forks"])
        if "forks_url" in attributes:  # pragma no branch
            self._forks_url = self._makeStringAttribute(attributes["forks_url"])
        if "git_pull_url" in attributes:  # pragma no branch
            self._git_pull_url = self._makeStringAttribute(attributes["git_pull_url"])
        if "git_push_url" in attributes:  # pragma no branch
            self._git_push_url = self._makeStringAttribute(attributes["git_push_url"])
        if "history" in attributes:  # pragma no branch
            self._history = self._makeListOfClassesAttribute(GistHistoryState, attributes["history"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        if "owner" in attributes:  # pragma no branch
            self._owner = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["owner"])
        if "public" in attributes:  # pragma no branch
            self._public = self._makeBoolAttribute(attributes["public"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["user"])
        if "version" in attributes:  # pragma no branch
            self._version = self._makeStringAttribute(attributes["version"])
