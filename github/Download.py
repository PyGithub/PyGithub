############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class Download(CompletableGithubObject):
    """
    This class represents Downloads.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos

    """

    def _initAttributes(self) -> None:
        self._accesskeyid: Attribute[str] = NotSet
        self._acl: Attribute[str] = NotSet
        self._bucket: Attribute[str] = NotSet
        self._content_type: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._description: Attribute[str] = NotSet
        self._download_count: Attribute[int] = NotSet
        self._expirationdate: Attribute[datetime] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._mime_type: Attribute[str] = NotSet
        self._name: Attribute[str] = NotSet
        self._path: Attribute[str] = NotSet
        self._policy: Attribute[str] = NotSet
        self._prefix: Attribute[str] = NotSet
        self._redirect: Attribute[bool] = NotSet
        self._s3_url: Attribute[str] = NotSet
        self._signature: Attribute[str] = NotSet
        self._size: Attribute[int] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"id": self._id.value})

    @property
    def accesskeyid(self) -> str:
        self._completeIfNotSet(self._accesskeyid)
        return self._accesskeyid.value

    @property
    def acl(self) -> str:
        self._completeIfNotSet(self._acl)
        return self._acl.value

    @property
    def bucket(self) -> str:
        self._completeIfNotSet(self._bucket)
        return self._bucket.value

    @property
    def content_type(self) -> str:
        self._completeIfNotSet(self._content_type)
        return self._content_type.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def description(self) -> str:
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def download_count(self) -> int:
        self._completeIfNotSet(self._download_count)
        return self._download_count.value

    @property
    def expirationdate(self) -> datetime:
        self._completeIfNotSet(self._expirationdate)
        return self._expirationdate.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def mime_type(self) -> str:
        self._completeIfNotSet(self._mime_type)
        return self._mime_type.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def path(self) -> str:
        self._completeIfNotSet(self._path)
        return self._path.value

    @property
    def policy(self) -> str:
        self._completeIfNotSet(self._policy)
        return self._policy.value

    @property
    def prefix(self) -> str:
        self._completeIfNotSet(self._prefix)
        return self._prefix.value

    @property
    def redirect(self) -> bool:
        self._completeIfNotSet(self._redirect)
        return self._redirect.value

    @property
    def s3_url(self) -> str:
        self._completeIfNotSet(self._s3_url)
        return self._s3_url.value

    @property
    def signature(self) -> str:
        self._completeIfNotSet(self._signature)
        return self._signature.value

    @property
    def size(self) -> int:
        self._completeIfNotSet(self._size)
        return self._size.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    def delete(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/downloads/{id} <https://docs.github.com/en/rest/reference/repos>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "accesskeyid" in attributes:  # pragma no branch
            self._accesskeyid = self._makeStringAttribute(
                attributes["accesskeyid"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "acl" in attributes:  # pragma no branch
            self._acl = self._makeStringAttribute(
                attributes["acl"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "bucket" in attributes:  # pragma no branch
            self._bucket = self._makeStringAttribute(
                attributes["bucket"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "content_type" in attributes:  # pragma no branch
            self._content_type = self._makeStringAttribute(attributes["content_type"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            self._description = self._makeStringAttribute(attributes["description"])
        if "download_count" in attributes:  # pragma no branch
            self._download_count = self._makeIntAttribute(attributes["download_count"])
        if "expirationdate" in attributes:  # pragma no branch
            self._expirationdate = self._makeDatetimeAttribute(
                attributes["expirationdate"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "mime_type" in attributes:  # pragma no branch
            self._mime_type = self._makeStringAttribute(
                attributes["mime_type"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(
                attributes["path"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "policy" in attributes:  # pragma no branch
            self._policy = self._makeStringAttribute(
                attributes["policy"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "prefix" in attributes:  # pragma no branch
            self._prefix = self._makeStringAttribute(
                attributes["prefix"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "redirect" in attributes:  # pragma no branch
            self._redirect = self._makeBoolAttribute(
                attributes["redirect"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "s3_url" in attributes:  # pragma no branch
            self._s3_url = self._makeStringAttribute(
                attributes["s3_url"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "signature" in attributes:  # pragma no branch
            self._signature = self._makeStringAttribute(
                attributes["signature"]
            )  # pragma no cover (was covered only by create_download, which has been removed)
        if "size" in attributes:  # pragma no branch
            self._size = self._makeIntAttribute(attributes["size"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
