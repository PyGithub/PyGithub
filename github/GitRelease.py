# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2015 Ed Holland <eholland@alertlogic.com>                          #
# Copyright 2016 Benjamin Whitney <benjamin.whitney@ironnetcybersecurity.com>  #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 edquist <edquist@users.noreply.github.com>                    #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

from os.path import basename
import github.GithubObject
import github.GitAuthor
import github.GitReleaseAsset


class GitRelease(github.GithubObject.CompletableGithubObject):
    """
    This class represents GitReleases. The reference can be found here https://developer.github.com/v3/repos/releases
    """

    def __repr__(self):
        return self.get__repr__({"title": self._title.value})

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def body(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._body)
        return self._body.value

    @property
    def title(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._title)
        return self._title.value

    @property
    def tag_name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._tag_name)
        return self._tag_name.value

    @property
    def draft(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._draft)
        return self._draft.value

    @property
    def prerelease(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._prerelease)
        return self._prerelease.value

    @property
    def author(self):
        """
        :type: :class:`github.GitAuthor.GitAuthor`
        """
        self._completeIfNotSet(self._author)
        return self._author.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def published_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._published_at)
        return self._published_at.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def upload_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._upload_url)
        return self._upload_url.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def tarball_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._tarball_url)
        return self._tarball_url.value

    @property
    def zipball_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._zipball_url)
        return self._zipball_url.value

    def delete_release(self):
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url
        )
        return True

    def update_release(self, name, message, draft=False, prerelease=False):
        assert isinstance(name, (str, unicode)), name
        assert isinstance(message, (str, unicode)), message
        assert isinstance(draft, bool), draft
        assert isinstance(prerelease, bool), prerelease
        post_parameters = {
            "tag_name": self.tag_name,
            "name": name,
            "body": message,
            "draft": draft,
            "prerelease": prerelease,
        }
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            input=post_parameters
        )
        return github.GitRelease.GitRelease(self._requester, headers, data, completed=True)

    def upload_asset(self, path, label="", content_type=""):
        assert isinstance(path, (str, unicode)), path
        assert isinstance(label, (str, unicode)), label

        post_parameters = {
            "name": basename(path),
            "label": label
        }
        headers = {}
        if len(content_type) > 0:
            headers["Content-Type"] = content_type
        resp_headers, data = self._requester.requestBlobAndCheck(
            "POST",
            self.upload_url.split("{?")[0],
            parameters=post_parameters,
            headers=headers,
            input=path
        )
        return github.GitReleaseAsset.GitReleaseAsset(self._requester, resp_headers, data, completed=True)

    def get_assets(self):
        return github.PaginatedList.PaginatedList(
            github.GitReleaseAsset.GitReleaseAsset,
            self._requester,
            self.url + "/assets",
            None
        )

    def _initAttributes(self):
        self._id = github.GithubObject.NotSet
        self._body = github.GithubObject.NotSet
        self._title = github.GithubObject.NotSet
        self._tag_name = github.GithubObject.NotSet
        self._draft = github.GithubObject.NotSet
        self._prerelease = github.GithubObject.NotSet
        self._author = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._upload_url = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._published_at = github.GithubObject.NotSet
        self._tarball_url = github.GithubObject.NotSet
        self._zipball_url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "id" in attributes:
            self._id = self._makeIntAttribute(attributes["id"])
        if "body" in attributes:
            self._body = self._makeStringAttribute(attributes["body"])
        if "name" in attributes:
            self._title = self._makeStringAttribute(attributes["name"])
        if "tag_name" in attributes:
            self._tag_name = self._makeStringAttribute(attributes["tag_name"])
        if "draft" in attributes:
            self._draft = self._makeBoolAttribute(attributes["draft"])
        if "prerelease" in attributes:
            self._prerelease = self._makeBoolAttribute(attributes["prerelease"])
        if "author" in attributes:
            self._author = self._makeClassAttribute(github.GitAuthor.GitAuthor, attributes["author"])
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
