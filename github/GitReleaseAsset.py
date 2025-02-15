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
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Neel Malik <41765022+neel-m@users.noreply.github.com>         #
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
from typing import Any, Iterator

import github.NamedUser
from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class GitReleaseAsset(CompletableGithubObject):
    """
    This class represents GitReleaseAssets.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#releases

    The OpenAPI schema can be found at
    - /components/schemas/release-asset

    """

    def _initAttributes(self) -> None:
        self._browser_download_url: Attribute[str] = NotSet
        self._content_type: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._download_count: Attribute[int] = NotSet
        self._id: Attribute[int] = NotSet
        self._label: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._node_id: Attribute[str] = NotSet
        self._size: Attribute[int] = NotSet
        self._state: Attribute[str] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._uploader: Attribute[github.NamedUser.NamedUser] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"url": self.url})

    @property
    def browser_download_url(self) -> str:
        self._completeIfNotSet(self._browser_download_url)
        return self._browser_download_url.value

    @property
    def content_type(self) -> str:
        self._completeIfNotSet(self._content_type)
        return self._content_type.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def download_count(self) -> int:
        self._completeIfNotSet(self._download_count)
        return self._download_count.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def label(self) -> str:
        self._completeIfNotSet(self._label)
        return self._label.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def node_id(self) -> str:
        self._completeIfNotSet(self._node_id)
        return self._node_id.value

    @property
    def size(self) -> int:
        self._completeIfNotSet(self._size)
        return self._size.value

    @property
    def state(self) -> str:
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def uploader(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._uploader)
        return self._uploader.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def delete_asset(self) -> bool:
        """
        Delete asset from the release.
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)
        return True

    def download_asset(
        self, path: None | str = None, chunk_size: int | None = 1
    ) -> tuple[int, dict[str, Any], Iterator] | None:
        """
        Download asset to the path or return an iterator for the stream.
        """
        if path is None:
            return self._requester.getStream(self.url, chunk_size=chunk_size)
        self._requester.getFile(self.url, path=path, chunk_size=chunk_size)
        return None

    def update_asset(self, name: str, label: str = "") -> GitReleaseAsset:
        """
        Update asset metadata.
        """
        assert isinstance(name, str), name
        assert isinstance(label, str), label
        post_parameters = {"name": name, "label": label}
        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        return GitReleaseAsset(self._requester, headers, data, completed=True)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "browser_download_url" in attributes:  # pragma no branch
            self._browser_download_url = self._makeStringAttribute(attributes["browser_download_url"])
        if "content_type" in attributes:  # pragma no branch
            self._content_type = self._makeStringAttribute(attributes["content_type"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "download_count" in attributes:  # pragma no branch
            self._download_count = self._makeIntAttribute(attributes["download_count"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "label" in attributes:  # pragma no branch
            self._label = self._makeStringAttribute(attributes["label"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "node_id" in attributes:  # pragma no branch
            self._node_id = self._makeStringAttribute(attributes["node_id"])
        if "size" in attributes:  # pragma no branch
            self._size = self._makeIntAttribute(attributes["size"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "uploader" in attributes:  # pragma no branch
            self._uploader = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["uploader"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
