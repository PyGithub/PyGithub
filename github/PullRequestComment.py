############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Michael Stead <michael.stead@gmail.com>                       #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Nicolas Agustín Torres <nicolastrres@gmail.com>               #
# Copyright 2018 Jess Morgan <979404+JessMorgan@users.noreply.github.com>      #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 per1234 <accounts@perglass.com>                               #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Huan-Cheng Chang <changhc84@gmail.com>                        #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Den Stroebel <stroebs@users.noreply.github.com>               #
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

import github.GithubObject
import github.NamedUser
import github.Reaction
from github import Consts
from github.GithubObject import Attribute, CompletableGithubObject, NotSet
from github.PaginatedList import PaginatedList


class PullRequestComment(CompletableGithubObject):
    """
    This class represents PullRequestComments.

    The reference can be found here
    https://docs.github.com/en/rest/reference/pulls#review-comments

    The OpenAPI schema can be found at
    - /components/schemas/pull-request-review-comment

    """

    def _initAttributes(self) -> None:
        self.__links: Attribute[dict[str, Any]] = NotSet
        self._author_association: Attribute[str] = NotSet
        self._body: Attribute[str] = NotSet
        self._body_html: Attribute[str] = NotSet
        self._body_text: Attribute[str] = NotSet
        self._commit_id: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._diff_hunk: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._in_reply_to_id: Attribute[int] = NotSet
        self._line: Attribute[int] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._original_commit_id: Attribute[str] = NotSet
        self._original_line: Attribute[int] = NotSet
        self._original_position: Attribute[int] = NotSet
        self._original_start_line: Attribute[int] = NotSet
        self._path: Attribute[str] = NotSet
        self._position: Attribute[int] = NotSet
        self._pull_request_review_id: Attribute[int] = NotSet
        self._pull_request_url: Attribute[str] = NotSet
        self._reactions: Attribute[dict[str, Any]] = NotSet
        self._side: Attribute[str] = NotSet
        self._start_line: Attribute[int] = NotSet
        self._start_side: Attribute[str] = NotSet
        self._subject_type: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._user: Attribute[github.NamedUser.NamedUser] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "user": self._user.value})

    @property
    def _links(self) -> dict[str, Any]:
        self._completeIfNotSet(self.__links)
        return self.__links.value

    @property
    def author_association(self) -> str:
        self._completeIfNotSet(self._author_association)
        return self._author_association.value

    @property
    def body(self) -> str:
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def body_html(self) -> str:
        self._completeIfNotSet(self._body_html)
        return self._body_html.value

    @property
    def body_text(self) -> str:
        self._completeIfNotSet(self._body_text)
        return self._body_text.value

    @property
    def commit_id(self) -> str:
        self._completeIfNotSet(self._commit_id)
        return self._commit_id.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def diff_hunk(self) -> str:
        self._completeIfNotSet(self._diff_hunk)
        return self._diff_hunk.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def in_reply_to_id(self) -> int:
        self._completeIfNotSet(self._in_reply_to_id)
        return self._in_reply_to_id.value

    @property
    def line(self) -> int:
        self._completeIfNotSet(self._line)
        return self._line.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def original_commit_id(self) -> str:
        self._completeIfNotSet(self._original_commit_id)
        return self._original_commit_id.value

    @property
    def original_line(self) -> int:
        self._completeIfNotSet(self._original_line)
        return self._original_line.value

    @property
    def original_position(self) -> int:
        self._completeIfNotSet(self._original_position)
        return self._original_position.value

    @property
    def original_start_line(self) -> int:
        self._completeIfNotSet(self._original_start_line)
        return self._original_start_line.value

    @property
    def path(self) -> str:
        self._completeIfNotSet(self._path)
        return self._path.value

    @property
    def position(self) -> int:
        self._completeIfNotSet(self._position)
        return self._position.value

    @property
    def pull_request_review_id(self) -> int:
        self._completeIfNotSet(self._pull_request_review_id)
        return self._pull_request_review_id.value

    @property
    def pull_request_url(self) -> str:
        self._completeIfNotSet(self._pull_request_url)
        return self._pull_request_url.value

    @property
    def reactions(self) -> dict[str, Any]:
        self._completeIfNotSet(self._reactions)
        return self._reactions.value

    @property
    def side(self) -> str:
        self._completeIfNotSet(self._side)
        return self._side.value

    @property
    def start_line(self) -> int:
        self._completeIfNotSet(self._start_line)
        return self._start_line.value

    @property
    def start_side(self) -> str:
        self._completeIfNotSet(self._start_side)
        return self._start_side.value

    @property
    def subject_type(self) -> str:
        self._completeIfNotSet(self._subject_type)
        return self._subject_type.value

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

    def delete(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/pulls/comments/{number} <https://docs.github.com/en/rest/reference/pulls#review-comments>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def edit(self, body: str) -> None:
        """
        :calls: `PATCH /repos/{owner}/{repo}/pulls/comments/{number} <https://docs.github.com/en/rest/reference/pulls#review-comments>`_
        :param body: string
        :rtype: None
        """
        assert isinstance(body, str), body
        post_parameters = {
            "body": body,
        }
        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        self._useAttributes(data)

    def get_reactions(self) -> PaginatedList[github.Reaction.Reaction]:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/comments/{number}/reactions
                <https://docs.github.com/en/rest/reference/reactions#list-reactions-for-a-pull-request-review-comment>`_
        :return: :class: :class:`github.PaginatedList.PaginatedList` of :class:`github.Reaction.Reaction`
        """
        return PaginatedList(
            github.Reaction.Reaction,
            self._requester,
            f"{self.url}/reactions",
            None,
            headers={"Accept": Consts.mediaTypeReactionsPreview},
        )

    def create_reaction(self, reaction_type: str) -> github.Reaction.Reaction:
        """
        :calls: `POST /repos/{owner}/{repo}/pulls/comments/{number}/reactions
                <https://docs.github.com/en/rest/reference/reactions#create-reaction-for-a-pull-request-review-comment>`_
        :param reaction_type: string
        :rtype: :class:`github.Reaction.Reaction`
        """
        assert isinstance(reaction_type, str), reaction_type
        post_parameters = {
            "content": reaction_type,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            f"{self.url}/reactions",
            input=post_parameters,
            headers={"Accept": Consts.mediaTypeReactionsPreview},
        )
        return github.Reaction.Reaction(self._requester, headers, data, completed=True)

    def delete_reaction(self, reaction_id: int) -> bool:
        """
        :calls: `DELETE /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}
                <https://docs.github.com/en/rest/reference/reactions#delete-a-pull-request-comment-reaction>`_
        :param reaction_id: integer
        :rtype: bool
        """
        assert isinstance(reaction_id, int), reaction_id
        status, _, _ = self._requester.requestJson(
            "DELETE",
            f"{self.url}/reactions/{reaction_id}",
            headers={"Accept": Consts.mediaTypeReactionsPreview},
        )
        return status == 204

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "_links" in attributes:  # pragma no branch
            self.__links = self._makeDictAttribute(attributes["_links"])
        if "author_association" in attributes:  # pragma no branch
            self._author_association = self._makeStringAttribute(attributes["author_association"])
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "body_html" in attributes:  # pragma no branch
            self._body_html = self._makeStringAttribute(attributes["body_html"])
        if "body_text" in attributes:  # pragma no branch
            self._body_text = self._makeStringAttribute(attributes["body_text"])
        if "commit_id" in attributes:  # pragma no branch
            self._commit_id = self._makeStringAttribute(attributes["commit_id"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "diff_hunk" in attributes:  # pragma no branch
            self._diff_hunk = self._makeStringAttribute(attributes["diff_hunk"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "in_reply_to_id" in attributes:  # pragma no branch
            self._in_reply_to_id = self._makeIntAttribute(attributes["in_reply_to_id"])
        if "line" in attributes:  # pragma no branch
            self._line = self._makeIntAttribute(attributes["line"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "original_commit_id" in attributes:  # pragma no branch
            self._original_commit_id = self._makeStringAttribute(attributes["original_commit_id"])
        if "original_line" in attributes:  # pragma no branch
            self._original_line = self._makeIntAttribute(attributes["original_line"])
        if "original_position" in attributes:  # pragma no branch
            self._original_position = self._makeIntAttribute(attributes["original_position"])
        if "original_start_line" in attributes:  # pragma no branch
            self._original_start_line = self._makeIntAttribute(attributes["original_start_line"])
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
        if "position" in attributes:  # pragma no branch
            self._position = self._makeIntAttribute(attributes["position"])
        if "pull_request_review_id" in attributes:  # pragma no branch
            self._pull_request_review_id = self._makeIntAttribute(attributes["pull_request_review_id"])
        if "pull_request_url" in attributes:  # pragma no branch
            self._pull_request_url = self._makeStringAttribute(attributes["pull_request_url"])
        if "reactions" in attributes:  # pragma no branch
            self._reactions = self._makeDictAttribute(attributes["reactions"])
        if "side" in attributes:  # pragma no branch
            self._side = self._makeStringAttribute(attributes["side"])
        if "start_line" in attributes:  # pragma no branch
            self._start_line = self._makeIntAttribute(attributes["start_line"])
        if "start_side" in attributes:  # pragma no branch
            self._start_side = self._makeStringAttribute(attributes["start_side"])
        if "subject_type" in attributes:  # pragma no branch
            self._subject_type = self._makeStringAttribute(attributes["subject_type"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["user"])
