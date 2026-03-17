# FILE AUTO GENERATED DO NOT TOUCH
############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Steve English <steve.english@navetas.com>                     #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Dale Jung <dale@dalejung.com>                                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2018 羽 <Just4test@users.noreply.github.com>                        #
# Copyright 2019 Jon Dufresne <jon.dufresne@gmail.com>                         #
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

import urllib.parse
from datetime import datetime
from typing import TYPE_CHECKING, Any

import github

from . import GistComment, GistFile, GistHistoryState, NamedUser
from .GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, _NotSetType, is_defined, is_optional
from .PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.InputFileContent import InputFileContent


class Gist(CompletableGithubObject):
    """
    This class represents Gists.

    The reference can be found here
    https://docs.github.com/en/rest/reference/gists

    The OpenAPI schema can be found at

    - /components/schemas/base-gist
    - /components/schemas/gist-simple
    - /components/schemas/gist-simple/properties/fork_of
    - /components/schemas/gist-simple/properties/forks/items

    """

    def _initAttributes(self) -> None:
        self._comments: Attribute[int] = NotSet
        self._comments_enabled: Attribute[bool] = NotSet
        self._comments_url: Attribute[str] = NotSet
        self._commits_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._description: Attribute[str] = NotSet
        self._files: Attribute[dict[str, GistFile.GistFile]] = NotSet
        self._fork_of: Attribute[Gist] = NotSet
        self._forks: Attribute[list[Gist]] = NotSet
        self._forks_url: Attribute[str] = NotSet
        self._git_pull_url: Attribute[str] = NotSet
        self._git_push_url: Attribute[str] = NotSet
        self._history: Attribute[list[GistHistoryState]] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._owner: Attribute[NamedUser.NamedUser] = NotSet
        self._public: Attribute[bool] = NotSet
        self._truncated: Attribute[bool] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._user: Attribute[NamedUser.NamedUser] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    async def comments(self) -> int:
        await self._completeIfNotSet(self._comments)
        return self._comments.value

    @property
    async def comments_enabled(self) -> bool:
        await self._completeIfNotSet(self._comments_enabled)
        return self._comments_enabled.value

    @property
    async def comments_url(self) -> str:
        await self._completeIfNotSet(self._comments_url)
        return self._comments_url.value

    @property
    async def commits_url(self) -> str:
        await self._completeIfNotSet(self._commits_url)
        return self._commits_url.value

    @property
    async def created_at(self) -> datetime:
        await self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    async def description(self) -> str:
        await self._completeIfNotSet(self._description)
        return self._description.value

    @property
    async def files(self) -> dict[str, GistFile.GistFile]:
        await self._completeIfNeeded()
        return self._files.value

    @property
    async def fork_of(self) -> Gist:
        await self._completeIfNotSet(self._fork_of)
        return self._fork_of.value

    @property
    async def forks(self) -> list[Gist]:
        await self._completeIfNotSet(self._forks)
        return self._forks.value

    @property
    async def forks_url(self) -> str:
        await self._completeIfNotSet(self._forks_url)
        return self._forks_url.value

    @property
    async def git_pull_url(self) -> str:
        await self._completeIfNotSet(self._git_pull_url)
        return self._git_pull_url.value

    @property
    async def git_push_url(self) -> str:
        await self._completeIfNotSet(self._git_push_url)
        return self._git_push_url.value

    @property
    async def history(self) -> list[GistHistoryState]:
        await self._completeIfNotSet(self._history)
        return self._history.value

    @property
    async def html_url(self) -> str:
        await self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    async def id(self) -> str:
        await self._completeIfNotSet(self._id)
        return self._id.value

    @property
    async def node_id(self) -> str:
        await self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    async def owner(self) -> NamedUser.NamedUser:
        await self._completeIfNotSet(self._owner)
        return self._owner.value

    @property
    async def public(self) -> bool:
        await self._completeIfNotSet(self._public)
        return self._public.value

    @property
    async def truncated(self) -> bool:
        await self._completeIfNotSet(self._truncated)
        return self._truncated.value

    @property
    async def updated_at(self) -> datetime:
        await self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    async def url(self) -> str:
        await self._completeIfNotSet(self._url)
        return self._url.value

    @property
    async def user(self) -> NamedUser.NamedUser:
        await self._completeIfNotSet(self._user)
        return self._user.value

    async def create_comment(self, body: str) -> GistComment:
        """
        :calls: `POST /gists/{gist_id}/comments <https://docs.github.com/en/rest/reference/gists#comments>`_
        """
        assert isinstance(body, str), body
        post_parameters = {
            "body": body,
        }
        headers, data = await self._requester.requestJsonAndCheck(
            "POST", f"{await self.url}/comments", input=post_parameters
        )
        return GistComment.GistComment(self._requester, headers, data, completed=True)

    async def create_fork(self) -> Gist:
        """
        :calls: `POST /gists/{gist_id}/forks <https://docs.github.com/en/rest/reference/gists>`_
        """
        headers, data = await self._requester.requestJsonAndCheck("POST", f"{await self.url}/forks")
        return Gist(self._requester, headers, data, completed=True)

    async def delete(self) -> None:
        """
        :calls: `DELETE /gists/{gist_id} <https://docs.github.com/en/rest/reference/gists>`_
        """
        headers, data = await self._requester.requestJsonAndCheck("DELETE", await self.url)

    async def edit(
        self, description: Opt[str] = NotSet, files: Opt[dict[str, InputFileContent | None]] = NotSet
    ) -> None:
        """
        :calls: `PATCH /gists/{gist_id} <https://docs.github.com/en/rest/reference/gists>`_
        """
        assert is_optional(description, str), description
        # limitation of `TypeGuard`
        assert isinstance(files, _NotSetType) or all(
            element is None or isinstance(element, github.InputFileContent) for element in files.values()
        ), files
        post_parameters: dict[str, Any] = {}
        if is_defined(description):
            post_parameters["description"] = description
        if is_defined(files):
            post_parameters["files"] = {key: None if value is None else value._identity for key, value in files.items()}
        headers, data = await self._requester.requestJsonAndCheck("PATCH", await self.url, input=post_parameters)

        self._useAttributes(data)
        self._set_complete()

    async def get_comment(self, id: int) -> GistComment:
        """
        :calls: `GET /gists/{gist_id}/comments/{comment_id} <https://docs.github.com/en/rest/reference/gists#comments>`_
        """
        assert isinstance(id, int), id
        url = f"{await self.url}/comments/{id}"
        return GistComment.GistComment(self._requester, url=url)

    async def get_comments(self) -> PaginatedList[GistComment]:
        """
        :calls: `GET /gists/{gist_id}/comments <https://docs.github.com/en/rest/reference/gists#comments>`_
        """
        return PaginatedList(
            GistComment.GistComment,
            self._requester,
            f"{await self.url}/comments",
            None,
        )

    async def is_starred(self) -> bool:
        """
        :calls: `GET /gists/{gist_id}/star <https://docs.github.com/en/rest/reference/gists>`_
        """
        status, headers, data = await self._requester.requestJson("GET", f"{await self.url}/star")
        return status == 204

    async def reset_starred(self) -> None:
        """
        :calls: `DELETE /gists/{gist_id}/star <https://docs.github.com/en/rest/reference/gists>`_
        """
        headers, data = await self._requester.requestJsonAndCheck("DELETE", f"{await self.url}/star")

    async def set_starred(self) -> None:
        """
        :calls: `PUT /gists/{gist_id}/star <https://docs.github.com/en/rest/reference/gists>`_
        """
        headers, data = await self._requester.requestJsonAndCheck("PUT", f"{await self.url}/star")

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "comments" in attributes:  # pragma no branch
            self._comments = self._makeIntAttribute(attributes["comments"])
        if "comments_enabled" in attributes:  # pragma no branch
            self._comments_enabled = self._makeBoolAttribute(attributes["comments_enabled"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "commits_url" in attributes:  # pragma no branch
            self._commits_url = self._makeStringAttribute(attributes["commits_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "files" in attributes:  # pragma no branch
            self._files = self._makeDictOfStringsToClassesAttribute(GistFile.GistFile, attributes["files"])
        if "fork_of" in attributes:  # pragma no branch
            self._fork_of = self._makeClassAttribute(Gist, attributes["fork_of"])
        if "forks" in attributes:  # pragma no branch
            self._forks = self._makeListOfClassesAttribute(Gist, attributes["forks"])
        if "forks_url" in attributes:  # pragma no branch
            self._forks_url = self._makeStringAttribute(attributes["forks_url"])
        if "git_pull_url" in attributes:  # pragma no branch
            self._git_pull_url = self._makeStringAttribute(attributes["git_pull_url"])
        if "git_push_url" in attributes:  # pragma no branch
            self._git_push_url = self._makeStringAttribute(attributes["git_push_url"])
        if "history" in attributes:  # pragma no branch
            self._history = self._makeListOfClassesAttribute(GistHistoryState.GistHistoryState, attributes["history"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        elif "url" in attributes and attributes["url"]:
            quoted_id = attributes["url"].split("/")[-1]
            id = urllib.parse.unquote(quoted_id)
            self._id = self._makeStringAttribute(id)
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "owner" in attributes:  # pragma no branch
            self._owner = self._makeClassAttribute(NamedUser.NamedUser, attributes["owner"])
        if "public" in attributes:  # pragma no branch
            self._public = self._makeBoolAttribute(attributes["public"])
        if "truncated" in attributes:  # pragma no branch
            self._truncated = self._makeBoolAttribute(attributes["truncated"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(NamedUser.NamedUser, attributes["user"])
