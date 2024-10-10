############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Matt Babineau <mbabineau@dataxu.com>                          #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Martijn Koster <mak-github@greenhills.co.uk>                  #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 Yossarian King <yggy@blackbirdinteractive.com>                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Jody McIntyre <scjody@modernduck.com>                         #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 chloe jungah kim <43295963+chloeeekim@users.noreply.github.com>#
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

from datetime import datetime
from typing import Any

import github.Issue
import github.NamedUser
import github.ProjectColumn
import github.PullRequest
from github import Consts
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt

# NOTE: There is currently no way to get cards "in triage" for a project.
# https://platform.github.community/t/moving-github-project-cards-that-are-in-triage/3784
#
# See also https://developer.github.com/v4/object/projectcard for the next generation GitHub API,
# which may point the way to where the API is likely headed and what might come back to v3. E.g. ProjectCard.content member.


class ProjectCard(CompletableGithubObject):
    """
    This class represents Project Cards.

    The reference can be found here
    https://docs.github.com/en/rest/reference/projects#cards

    """

    def _initAttributes(self) -> None:
        self._archived: Attribute[bool] = NotSet
        self._column_url: Attribute[str] = NotSet
        self._content_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._creator: Attribute[github.NamedUser.NamedUser] = NotSet
        self._id: Attribute[int] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._note: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def archived(self) -> bool:
        return self._archived.value

    @property
    def column_url(self) -> str:
        return self._column_url.value

    @property
    def content_url(self) -> str:
        return self._content_url.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def creator(self) -> github.NamedUser.NamedUser:
        return self._creator.value

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def node_id(self) -> str:
        return self._node_id.value

    @property
    def note(self) -> str:
        return self._note.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def url(self) -> str:
        return self._url.value

    # Note that the content_url for any card will be an "issue" URL, from
    # which you can retrieve either an Issue or a PullRequest. Unfortunately
    # the API doesn't make it clear which you are dealing with.
    def get_content(
        self, content_type: Opt[str] = NotSet
    ) -> github.PullRequest.PullRequest | github.Issue.Issue | None:
        """
        :calls: `GET /repos/{owner}/{repo}/pulls/{number} <https://docs.github.com/en/rest/reference/pulls#get-a-pull-request>`_
        """
        assert content_type is NotSet or isinstance(content_type, str), content_type
        if self.content_url is None:
            return None

        retclass: type[github.PullRequest.PullRequest] | type[github.Issue.Issue]
        if content_type == "PullRequest":
            url = self.content_url.replace("issues", "pulls")
            retclass = github.PullRequest.PullRequest
        elif content_type is NotSet or content_type == "Issue":
            url = self.content_url
            retclass = github.Issue.Issue
        else:
            raise ValueError(f"Unknown content type: {content_type}")
        headers, data = self._requester.requestJsonAndCheck("GET", url)
        return retclass(self._requester, headers, data, completed=True)

    def move(self, position: str, column: github.ProjectColumn.ProjectColumn | int) -> bool:
        """
        :calls: `POST /projects/columns/cards/{card_id}/moves <https://docs.github.com/en/rest/reference/projects#cards>`_
        """
        assert isinstance(position, str), position
        assert isinstance(column, github.ProjectColumn.ProjectColumn) or isinstance(column, int), column
        post_parameters = {
            "position": position,
            "column_id": column.id if isinstance(column, github.ProjectColumn.ProjectColumn) else column,
        }
        status, _, _ = self._requester.requestJson(
            "POST",
            f"{self.url}/moves",
            input=post_parameters,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        return status == 201

    def delete(self) -> bool:
        """
        :calls: `DELETE /projects/columns/cards/{card_id} <https://docs.github.com/en/rest/reference/projects#cards>`_
        """
        status, _, _ = self._requester.requestJson(
            "DELETE",
            self.url,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        return status == 204

    def edit(self, note: Opt[str] = NotSet, archived: Opt[bool] = NotSet) -> None:
        """
        :calls: `PATCH /projects/columns/cards/{card_id} <https://docs.github.com/en/rest/reference/projects#cards>`_
        """
        assert note is NotSet or isinstance(note, str), note
        assert archived is NotSet or isinstance(archived, bool), archived
        patch_parameters: dict[str, Any] = NotSet.remove_unset_items({"note": note, "archived": archived})
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        self._useAttributes(data)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "archived" in attributes:  # pragma no branch
            self._archived = self._makeBoolAttribute(attributes["archived"])
        if "column_url" in attributes:  # pragma no branch
            self._column_url = self._makeStringAttribute(attributes["column_url"])
        if "content_url" in attributes:  # pragma no branch
            self._content_url = self._makeStringAttribute(attributes["content_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "creator" in attributes:  # pragma no branch
            self._creator = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["creator"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "note" in attributes:  # pragma no branch
            self._note = self._makeStringAttribute(attributes["note"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
