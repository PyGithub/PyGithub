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

    """

    def _initAttributes(self) -> None:
        self._body: Attribute[str] = NotSet
        self._commit_id: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._diff_hunk: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._in_reply_to_id: Attribute[int] = NotSet
        self._original_commit_id: Attribute[str] = NotSet
        self._original_position: Attribute[int] = NotSet
        self._path: Attribute[str] = NotSet
        self._position: Attribute[int] = NotSet
        self._pull_request_url: Attribute[str] = NotSet
        self._pull_request_review_id: Attribute[int] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._user: Attribute[github.NamedUser.NamedUser] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value, "user": self._user.value})

    @property
    def body(self) -> str:
        self._completeIfNotSet(self._body)
        return self._body.value

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
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def in_reply_to_id(self) -> int:
        self._completeIfNotSet(self._in_reply_to_id)
        return self._in_reply_to_id.value

    @property
    def original_commit_id(self) -> str:
        self._completeIfNotSet(self._original_commit_id)
        return self._original_commit_id.value

    @property
    def original_position(self) -> int:
        self._completeIfNotSet(self._original_position)
        return self._original_position.value

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
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

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
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "commit_id" in attributes:  # pragma no branch
            self._commit_id = self._makeStringAttribute(attributes["commit_id"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "diff_hunk" in attributes:  # pragma no branch
            self._diff_hunk = self._makeStringAttribute(attributes["diff_hunk"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "in_reply_to_id" in attributes:  # pragma no branch
            self._in_reply_to_id = self._makeIntAttribute(attributes["in_reply_to_id"])
        if "original_commit_id" in attributes:  # pragma no branch
            self._original_commit_id = self._makeStringAttribute(attributes["original_commit_id"])
        if "original_position" in attributes:  # pragma no branch
            self._original_position = self._makeIntAttribute(attributes["original_position"])
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
        if "position" in attributes:  # pragma no branch
            self._position = self._makeIntAttribute(attributes["position"])
        if "pull_request_review_id" in attributes:  # pragma no branch
            self._pull_request_review_id = self._makeIntAttribute(attributes["pull_request_review_id"])
        if "pull_request_url" in attributes:  # pragma no branch
            self._pull_request_url = self._makeStringAttribute(attributes["pull_request_url"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "user" in attributes:  # pragma no branch
            self._user = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["user"])
