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
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Colby Gallup <colbygallup@gmail.com>                          #
# Copyright 2020 Mahesh Raju <coder@mahesh.net>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Aleksei Fedotov <lexa@cfotr.com>                              #
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

import github.WorkflowRun
from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.WorkflowRun import WorkflowRun


class Artifact(NonCompletableGithubObject):
    """
    This class represents an Artifact of Github Run.

    The OpenAPI schema can be found at
    - /components/schemas/artifact

    """

    def _initAttributes(self) -> None:
        self._archive_download_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._expired: Attribute[bool] = NotSet
        self._expires_at: Attribute[datetime] = NotSet
        self._head_sha: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._size_in_bytes: Attribute[int] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._url: Attribute[str] = NotSet
        self._workflow_run: Attribute[WorkflowRun] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"name": self._name.value, "id": self._id.value})

    @property
    def archive_download_url(self) -> str:
        return self._archive_download_url.value

    @property
    def created_at(self) -> datetime:
        return self._created_at.value

    @property
    def expired(self) -> bool:
        return self._expired.value

    @property
    def expires_at(self) -> datetime:
        return self._expires_at.value

    @property
    def head_sha(self) -> str:
        return self._head_sha.value

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
    def size_in_bytes(self) -> int:
        return self._size_in_bytes.value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at.value

    @property
    def url(self) -> str:
        return self._url.value

    @property
    def workflow_run(self) -> WorkflowRun:
        return self._workflow_run.value

    def delete(self) -> bool:
        """
        :calls: `DELETE /repos/{owner}/{repo}/actions/artifacts/{artifact_id} <https://docs.github.com/en/rest/actions/artifacts#delete-an-artifact>`_
        """
        status, headers, data = self._requester.requestBlob("DELETE", self.url)
        return status == 204

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "archive_download_url" in attributes:  # pragma no branch
            self._archive_download_url = self._makeStringAttribute(attributes["archive_download_url"])
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str,)), attributes[
                "created_at"
            ]
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "expired" in attributes:  # pragma no branch
            self._expired = self._makeBoolAttribute(attributes["expired"])
        if "expires_at" in attributes:  # pragma no branch
            assert attributes["expires_at"] is None or isinstance(attributes["expires_at"], (str,)), attributes[
                "expires_at"
            ]
            self._expires_at = self._makeDatetimeAttribute(attributes["expires_at"])
        if "head_sha" in attributes:  # pragma no branch
            self._head_sha = self._makeStringAttribute(attributes["head_sha"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "size_in_bytes" in attributes:  # pragma no branch
            self._size_in_bytes = self._makeIntAttribute(attributes["size_in_bytes"])
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str,)), attributes[
                "updated_at"
            ]
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "workflow_run" in attributes:  # pragma no branch
            self._workflow_run = self._makeClassAttribute(github.WorkflowRun.WorkflowRun, attributes["workflow_run"])
