############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Benoit Latinier <benoit@latinier.fr>                          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 Yossarian King <yggy@blackbirdinteractive.com>                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Anuj Bansal <bansalanuj1996@gmail.com>                        #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Lars Kellogg-Stedman <lars@oddbit.com>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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
import github.ProjectColumn
from github import Consts
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt
from github.PaginatedList import PaginatedList


class Project(CompletableGithubObject):
    """
    This class represents Projects.

    The reference can be found here
    https://docs.github.com/en/rest/reference/projects

    """

    def _initAttributes(self) -> None:
        self._body: Attribute[str] = NotSet
        self._columns_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._creator: Attribute[github.NamedUser.NamedUser] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._number: Attribute[int] = NotSet
        self._owner_url: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value})

    @property
    def body(self) -> str:
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def columns_url(self) -> str:
        self._completeIfNotSet(self._columns_url)
        return self._columns_url.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def creator(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._creator)
        return self._creator.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def number(self) -> int:
        self._completeIfNotSet(self._number)
        return self._number.value

    @property
    def owner_url(self) -> str:
        self._completeIfNotSet(self._owner_url)
        return self._owner_url.value

    @property
    def state(self) -> str:
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def delete(self) -> None:
        """
        :calls: `DELETE /projects/{project_id} <https://docs.github.com/en/rest/reference/projects#delete-a-project>`_
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE", self.url, headers={"Accept": Consts.mediaTypeProjectsPreview}
        )

    def edit(
        self,
        name: Opt[str] = NotSet,
        body: Opt[str] = NotSet,
        state: Opt[str] = NotSet,
        organization_permission: Opt[str] = NotSet,
        private: Opt[bool] = NotSet,
    ) -> None:
        """
        :calls: `PATCH /projects/{project_id} <https://docs.github.com/en/rest/reference/projects#update-a-project>`_
        """
        assert name is NotSet or isinstance(name, str), name
        assert body is NotSet or isinstance(body, str), body
        assert state is NotSet or isinstance(state, str), state
        assert organization_permission is NotSet or isinstance(organization_permission, str), organization_permission
        assert private is NotSet or isinstance(private, bool), private
        patch_parameters = NotSet.remove_unset_items(
            {
                "name": name,
                "body": body,
                "state": state,
                "organization_permission": organization_permission,
                "private": private,
            }
        )

        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=patch_parameters,
            headers={"Accept": Consts.mediaTypeProjectsPreview},
        )
        self._useAttributes(data)

    def get_columns(self) -> PaginatedList[github.ProjectColumn.ProjectColumn]:
        """
        :calls: `GET /projects/{project_id}/columns <https://docs.github.com/en/rest/reference/projects#list-project-columns>`_
        """

        return PaginatedList(
            github.ProjectColumn.ProjectColumn,
            self._requester,
            self.columns_url,
            None,
            {"Accept": Consts.mediaTypeProjectsPreview},
        )

    def create_column(self, name: str) -> github.ProjectColumn.ProjectColumn:
        """
        calls: `POST /projects/{project_id}/columns <https://docs.github.com/en/rest/reference/projects#create-a-project-column>`_
        """
        assert isinstance(name, str), name
        post_parameters = {"name": name}
        import_header = {"Accept": Consts.mediaTypeProjectsPreview}
        headers, data = self._requester.requestJsonAndCheck(
            "POST", f"{self.url}/columns", headers=import_header, input=post_parameters
        )
        return github.ProjectColumn.ProjectColumn(self._requester, headers, data, completed=True)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "columns_url" in attributes:  # pragma no branch
            self._columns_url = self._makeStringAttribute(attributes["columns_url"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "creator" in attributes:  # pragma no branch
            self._creator = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["creator"])
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "number" in attributes:  # pragma no branch
            self._number = self._makeIntAttribute(attributes["number"])
        if "owner_url" in attributes:  # pragma no branch
            self._owner_url = self._makeStringAttribute(attributes["owner_url"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
