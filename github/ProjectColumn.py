############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 bbi-yggy <yossarian@blackbirdinteractive.com>                 #
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
import github.Project
import github.ProjectCard
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt
from github.PaginatedList import PaginatedList

from . import Consts


class ProjectColumn(CompletableGithubObject):
    """
    This class represents Project Columns. The reference can be found here https://docs.github.com/en/rest/reference/projects#columns
    """

    def _initAttributes(self) -> None:
        self._cards_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._project_url: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def cards_url(self) -> str:
        return self._cards_url.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def id(self) -> int:
        return self._id.value

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def node_id(self) -> str:
        return self._node_id.value

    @property
    def project_url(self) -> str:
        return self._project_url.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def url(self) -> str:
        return self._url.value

    def get_cards(self, archived_state: Opt[str] = NotSet) -> PaginatedList[github.ProjectCard.ProjectCard]:
        """
        :calls: `GET /projects/columns/{column_id}/cards <https://docs.github.com/en/rest/reference/projects#list-project-cards>`_
        """
        assert archived_state is NotSet or isinstance(archived_state, str), archived_state

        url_parameters = dict()
        if archived_state is not NotSet:
            url_parameters["archived_state"] = archived_state

        return PaginatedList(
            github.ProjectCard.ProjectCard,
            self._requester,
            f"{self.url}/cards",
            url_parameters,
            {"Accept": Consts.mediaTypeProjectsPreview},
        )

    def create_card(
        self,
        note: Opt[str] = NotSet,
        content_id: Opt[int] = NotSet,
        content_type: Opt[str] = NotSet,
    ) -> github.ProjectCard.ProjectCard:
        """
        :calls: `POST /projects/columns/{column_id}/cards <https://docs.github.com/en/rest/reference/projects#create-a-project-card>`_
        """
        if isinstance(note, str):
            assert content_id is NotSet, content_id
            assert content_type is NotSet, content_type
            post_parameters: dict[str, Any] = {"note": note}
        else:
            assert note is NotSet, note
            assert isinstance(content_id, int), content_id
            assert isinstance(content_type, str), content_type
            post_parameters = {"content_id": content_id, "content_type": content_type}

        import_header = {"Accept": Consts.mediaTypeProjectsPreview}
        headers, data = self._requester.requestJsonAndCheck(
            "POST", f"{self.url}/cards", headers=import_header, input=post_parameters
        )
        return github.ProjectCard.ProjectCard(self._requester, headers, data, completed=True)

    def move(self, position: str) -> bool:
        """
        :calls: `POST POST /projects/columns/{column_id}/moves <https://docs.github.com/en/rest/reference/projects#move-a-project-column>`_
        """
        assert isinstance(position, str), position
        post_parameters = {"position": position}
        status, _, _ = self._requester.requestJson(
            "POST",
            f"{self.url}/moves",
            input=post_parameters,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        return status == 201

    def delete(self) -> bool:
        """
        :calls: `DELETE /projects/columns/{column_id} <https://docs.github.com/en/rest/reference/projects#delete-a-project-column>`_
        """
        status, _, _ = self._requester.requestJson(
            "DELETE",
            self.url,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        return status == 204

    def edit(self, name: str) -> None:
        """
        :calls: `PATCH /projects/columns/{column_id} <https://docs.github.com/en/rest/reference/projects#update-an-existing-project-column>`_
        """
        assert isinstance(name, str), name
        patch_parameters = {"name": name}

        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )

        self._useAttributes(data)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "cards_url" in attributes:  # pragma no branch
            self._cards_url = self._makeStringAttribute(attributes["cards_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "project_url" in attributes:  # pragma no branch
            self._project_url = self._makeStringAttribute(attributes["project_url"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
