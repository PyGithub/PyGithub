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

from datetime import datetime
from typing import TYPE_CHECKING, Any

import github.GistComment
import github.GistFile
import github.GistHistoryState
import github.GithubObject
import github.NamedUser
import github.PaginatedList
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, _NotSetType, is_defined, is_optional
from github.PaginatedList import PaginatedList

if TYPE_CHECKING:
    from github.GistComment import GistComment
    from github.GistHistoryState import GistHistoryState
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
        self._comments_url: Attribute[str] = NotSet
        self._commits_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._description: Attribute[str] = NotSet
        self._files: Attribute[dict[str, github.GistFile.GistFile]] = NotSet
        self._fork_of: Attribute[Gist] = NotSet
        self._forks: Attribute[list[Gist]] = NotSet
        self._forks_url: Attribute[str] = NotSet
        self._git_pull_url: Attribute[str] = NotSet
        self._git_push_url: Attribute[str] = NotSet
        self._history: Attribute[list[GistHistoryState]] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._owner: Attribute[github.NamedUser.NamedUser] = NotSet
        self._public: Attribute[bool] = NotSet
        self._truncated: Attribute[bool] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._user: Attribute[github.NamedUser.NamedUser] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

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
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def files(self) -> dict[str, github.GistFile.GistFile]:
        self._completeIfNeeded()
        return self._files.value

    @property
    def fork_of(self) -> github.Gist.Gist:
        self._completeIfNotSet(self._fork_of)
        return self._fork_of.value

    @property
    def forks(self) -> list[Gist]:
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
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def owner(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._owner)
        return self._owner.value

    @property
    def public(self) -> bool:
        self._completeIfNotSet(self._public)
        return self._public.value

    @property
    def truncated(self) -> bool:
        self._completeIfNotSet(self._truncated)
        return self._truncated.value

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

    def create_comment(self, body: str) -> GistComment:
        """
        :calls: `POST /gists/{gist_id}/comments <https://docs.github.com/en/rest/reference/gists#comments>`_
        """
        assert isinstance(body, str), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/comments", input=post_parameters)
        return github.GistComment.GistComment(self._requester, headers, data, completed=True)

    def create_fork(self) -> Gist:
        """
        :calls: `POST /gists/{id}/forks <https://docs.github.com/en/rest/reference/gists>`_
        """
        headers, data = self._requester.requestJsonAndCheck("POST", f"{self.url}/forks")
        return Gist(self._requester, headers, data, completed=True)

    def delete(self) -> None:
        """
        :calls: `DELETE /gists/{id} <https://docs.github.com/en/rest/reference/gists>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def edit(self, description: Opt[str] = NotSet, files: Opt[dict[str, InputFileContent | None]] = NotSet) -> None:
        """
        :calls: `PATCH /gists/{id} <https://docs.github.com/en/rest/reference/gists>`_
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
        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        self._useAttributes(data)

    def get_comment(self, id: int) -> GistComment:
        """
        :calls: `GET /gists/{gist_id}/comments/{id} <https://docs.github.com/en/rest/reference/gists#comments>`_
        """
        assert isinstance(id, int), id
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/comments/{id}")
        return github.GistComment.GistComment(self._requester, headers, data, completed=True)

    def get_comments(self) -> PaginatedList[GistComment]:
        """
        :calls: `GET /gists/{gist_id}/comments <https://docs.github.com/en/rest/reference/gists#comments>`_
        """
        return PaginatedList(
            github.GistComment.GistComment,
            self._requester,
            f"{self.url}/comments",
            None,
        )

    def is_starred(self) -> bool:
        """
        :calls: `GET /gists/{id}/star <https://docs.github.com/en/rest/reference/gists>`_
        """
        status, headers, data = self._requester.requestJson("GET", f"{self.url}/star")
        return status == 204

    def reset_starred(self) -> None:
        """
        :calls: `DELETE /gists/{id}/star <https://docs.github.com/en/rest/reference/gists>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", f"{self.url}/star")

    def set_starred(self) -> None:
        """
        :calls: `PUT /gists/{id}/star <https://docs.github.com/en/rest/reference/gists>`_
        """
        headers, data = self._requester.requestJsonAndCheck("PUT", f"{self.url}/star")

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "comments" in attributes:  # pragma no branch
            self._comments = self._makeIntAttribute(attributes["comments"])
        if "comments_url" in attributes:  # pragma no branch
            self._comments_url = self._makeStringAttribute(attributes["comments_url"])
        if "commits_url" in attributes:  # pragma no branch
            self._commits_url = self._makeStringAttribute(attributes["commits_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "files" in attributes:  # pragma no branch
            self._files = self._makeDictOfStringsToClassesAttribute(github.GistFile.GistFile, attributes["files"])
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
            self._history = self._makeListOfClassesAttribute(
                github.GistHistoryState.GistHistoryState, attributes["history"]
            )
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeStringAttribute(attributes["id"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "owner" in attributes:  # pragma no branch
            self._owner = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["owner"])
        if "public" in attributes:  # pragma no branch
            self._public = self._makeBoolAttribute(attributes["public"])
        if "truncated" in attributes:  # pragma no branch
            self._truncated = self._makeBoolAttribute(attributes["truncated"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["user"])
