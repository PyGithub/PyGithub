############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Ed Holland <eholland@alertlogic.com>                          #
# Copyright 2016 Benjamin Whitney <benjamin.whitney@ironnetcybersecurity.com>  #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Daniel Kesler <kesler.daniel@gmail.com>                       #
# Copyright 2018 Ggicci <ggicci.t@gmail.com>                                   #
# Copyright 2018 Kuba <jakub.glapa@adspired.com>                               #
# Copyright 2018 Maarten Fonville <mfonville@users.noreply.github.com>         #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 edquist <edquist@users.noreply.github.com>                    #
# Copyright 2018 nurupo <nurupo.contributions@gmail.com>                       #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Alice GIRARD <bouhahah@gmail.com>                             #
# Copyright 2020 Jesse Li <jesse.li2002@gmail.com>                             #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Mark Walker <mark.walker@realbuzz.com>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Mikhail f. Shiryaev <mr.felixoid@gmail.com>                   #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2023 Wojciech Barczyński <104033489+WojciechBarczynski@users.noreply.github.com>#
# Copyright 2024 Benjamin K <53038537+treee111@users.noreply.github.com>       #
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
from os.path import basename
from typing import Any, BinaryIO

import github.GitReleaseAsset
import github.NamedUser
from github.GithubObject import Attribute, CompletableGithubObject, NotSet, Opt, is_optional
from github.PaginatedList import PaginatedList

from . import Consts


class GitRelease(CompletableGithubObject):
    """
    This class represents GitReleases.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#releases

    """

    def _initAttributes(self) -> None:
        self._id: Attribute[int] = NotSet
        self._body: Attribute[str] = NotSet
        self._title: Attribute[str] = NotSet
        self._tag_name: Attribute[str] = NotSet
        self._target_commitish: Attribute[str] = NotSet
        self._draft: Attribute[bool] = NotSet
        self._prerelease: Attribute[bool] = NotSet
        self._generate_release_notes: Attribute[bool] = NotSet
        self._author: Attribute[github.NamedUser.NamedUser] = NotSet
        self._url: Attribute[str] = NotSet
        self._upload_url: Attribute[str] = NotSet
        self._html_url: Attribute[str] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._published_at: Attribute[datetime] = NotSet
        self._tarball_url: Attribute[str] = NotSet
        self._zipball_url: Attribute[str] = NotSet
        self._assets: Attribute[list[github.GitReleaseAsset.GitReleaseAsset]] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"title": self._title.value})

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def body(self) -> str:
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def title(self) -> str:
        self._completeIfNotSet(self._title)
        return self._title.value

    @property
    def tag_name(self) -> str:
        self._completeIfNotSet(self._tag_name)
        return self._tag_name.value

    @property
    def target_commitish(self) -> str:
        self._completeIfNotSet(self._target_commitish)
        return self._target_commitish.value

    @property
    def draft(self) -> bool:
        self._completeIfNotSet(self._draft)
        return self._draft.value

    @property
    def prerelease(self) -> bool:
        self._completeIfNotSet(self._prerelease)
        return self._prerelease.value

    @property
    def author(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._author)
        return self._author.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def published_at(self) -> datetime:
        self._completeIfNotSet(self._published_at)
        return self._published_at.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def upload_url(self) -> str:
        self._completeIfNotSet(self._upload_url)
        return self._upload_url.value

    @property
    def html_url(self) -> str:
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def tarball_url(self) -> str:
        self._completeIfNotSet(self._tarball_url)
        return self._tarball_url.value

    @property
    def zipball_url(self) -> str:
        self._completeIfNotSet(self._zipball_url)
        return self._zipball_url.value

    @property
    def assets(self) -> list[github.GitReleaseAsset.GitReleaseAsset]:
        self._completeIfNotSet(self._assets)
        return self._assets.value

    def delete_release(self) -> None:
        """
        :calls: `DELETE /repos/{owner}/{repo}/releases/{release_id} <https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#delete-a-release>`_
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)

    def update_release(
        self,
        name: str,
        message: str,
        draft: bool = False,
        prerelease: bool = False,
        tag_name: Opt[str] = NotSet,
        target_commitish: Opt[str] = NotSet,
        make_latest: Opt[str] = NotSet,
        discussion_category_name: Opt[str] = NotSet,
    ) -> GitRelease:
        """
        :calls: `PATCH /repos/{owner}/{repo}/releases/{release_id} <https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#update-a-release>`_
        """
        assert isinstance(name, str), name
        assert isinstance(message, str), message
        assert isinstance(draft, bool), draft
        assert isinstance(prerelease, bool), prerelease
        assert is_optional(tag_name, str), "tag_name must be a str/unicode object"
        assert is_optional(target_commitish, str), "target_commitish must be a str/unicode object"
        assert make_latest in ["true", "false", "legacy", NotSet], make_latest
        assert is_optional(discussion_category_name, str), discussion_category_name
        # default tag_name with instance attribute if not given to the method
        if tag_name is NotSet:
            tag_name = self.tag_name
        post_parameters = {
            "tag_name": tag_name,
            "name": name,
            "body": message,
            "draft": draft,
            "prerelease": prerelease,
        }
        # Do not set target_commitish to self.target_commitish when omitted, just don't send it
        # altogether in that case, in order to match the Github API behaviour. Only send it when set.
        if target_commitish is not NotSet:
            post_parameters["target_commitish"] = target_commitish
        if make_latest is not NotSet:
            post_parameters["make_latest"] = make_latest
        if discussion_category_name is not NotSet:
            post_parameters["discussion_category_name"] = discussion_category_name
        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        return github.GitRelease.GitRelease(self._requester, headers, data, completed=True)

    def upload_asset(
        self, path: str, label: str = "", content_type: Opt[str] = NotSet, name: Opt[str] = NotSet
    ) -> github.GitReleaseAsset.GitReleaseAsset:
        """
        :calls: `POST https://<upload_url>/repos/{owner}/{repo}/releases/{release_id}/assets <https://docs.github.com/en/rest/releases/assets?apiVersion=2022-11-28#upload-a-release-assett>`_
        """
        assert isinstance(path, str), path
        assert isinstance(label, str), label
        assert name is NotSet or isinstance(name, str), name

        post_parameters: dict[str, Any] = {"label": label}
        if name is NotSet:
            post_parameters["name"] = basename(path)
        else:
            post_parameters["name"] = name
        headers: dict[str, Any] = {}
        if content_type is not NotSet:
            headers["Content-Type"] = content_type
        resp_headers, data = self._requester.requestBlobAndCheck(
            "POST",
            self.upload_url.split("{?")[0],
            parameters=post_parameters,
            headers=headers,
            input=path,
        )
        return github.GitReleaseAsset.GitReleaseAsset(self._requester, resp_headers, data, completed=True)

    def upload_asset_from_memory(
        self,
        file_like: BinaryIO,
        file_size: int,
        name: str,
        content_type: Opt[str] = NotSet,
        label: str = "",
    ) -> github.GitReleaseAsset.GitReleaseAsset:
        """
        Uploads an asset.

        Unlike ``upload_asset()`` this method allows you to pass in a file-like object to upload.
        Note that this method is more strict and requires you to specify the ``name``, since there's no file name to infer these from.
        :calls: `POST https://<upload_url>/repos/{owner}/{repo}/releases/{release_id}/assets <https://docs.github.com/en/rest/reference/repos#upload-a-release-asset>`_
        :param file_like: binary file-like object, such as those returned by ``open("file_name", "rb")``. At the very minimum, this object must implement ``read()``.
        :param file_size: int, size in bytes of ``file_like``

        """
        assert isinstance(name, str), name
        assert isinstance(file_size, int), file_size
        assert isinstance(label, str), label

        post_parameters = {"label": label, "name": name}
        content_type = content_type if content_type is not NotSet else Consts.defaultMediaType
        headers = {"Content-Type": content_type, "Content-Length": str(file_size)}

        resp_headers, data = self._requester.requestMemoryBlobAndCheck(
            "POST",
            self.upload_url.split("{?")[0],
            parameters=post_parameters,
            headers=headers,
            file_like=file_like,
        )
        return github.GitReleaseAsset.GitReleaseAsset(self._requester, resp_headers, data, completed=True)

    def get_assets(self) -> PaginatedList[github.GitReleaseAsset.GitReleaseAsset]:
        """
        :calls: `GET /repos/{owner}/{repo}/releases/{release_id}/assets <https://docs.github.com/en/rest/releases/assets?apiVersion=2022-11-28#get-a-release-asset>`_
        """
        return github.PaginatedList.PaginatedList(
            github.GitReleaseAsset.GitReleaseAsset,
            self._requester,
            f"{self.url}/assets",
            None,
        )

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "id" in attributes:
            self._id = self._makeIntAttribute(attributes["id"])
        if "body" in attributes:
            self._body = self._makeStringAttribute(attributes["body"])
        if "name" in attributes:
            self._title = self._makeStringAttribute(attributes["name"])
        if "tag_name" in attributes:
            self._tag_name = self._makeStringAttribute(attributes["tag_name"])
        if "target_commitish" in attributes:
            self._target_commitish = self._makeStringAttribute(attributes["target_commitish"])
        if "draft" in attributes:
            self._draft = self._makeBoolAttribute(attributes["draft"])
        if "prerelease" in attributes:
            self._prerelease = self._makeBoolAttribute(attributes["prerelease"])
        if "generate_release_notes" in attributes:
            self._generate_release_notes = self._makeBoolAttribute(attributes["generate_release_notes"])
        if "author" in attributes:
            self._author = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["author"])
        if "url" in attributes:
            self._url = self._makeStringAttribute(attributes["url"])
        if "upload_url" in attributes:
            self._upload_url = self._makeStringAttribute(attributes["upload_url"])
        if "html_url" in attributes:
            self._html_url = self._makeStringAttribute(attributes["html_url"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "published_at" in attributes:
            self._published_at = self._makeDatetimeAttribute(attributes["published_at"])
        if "tarball_url" in attributes:
            self._tarball_url = self._makeStringAttribute(attributes["tarball_url"])
        if "zipball_url" in attributes:
            self._zipball_url = self._makeStringAttribute(attributes["zipball_url"])
        if "assets" in attributes:
            self._assets = self._makeListOfClassesAttribute(
                github.GitReleaseAsset.GitReleaseAsset, attributes["assets"]
            )
