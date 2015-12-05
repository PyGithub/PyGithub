# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Brett Weir <brett@lamestation.com>                            #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
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
# ##############################################################################

import github.GithubObject

import github.NamedUser
import github.ReleaseAsset


class Release(github.GithubObject.CompletableGithubObject):
    """
    This class represents Releases as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def assets_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._assets_url)
        return self._assets_url.value

    @property
    def upload_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._upload_url)
        return self._upload_url.value

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

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def tag_name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._tag_name)
        return self._tag_name.value

    @property
    def target_commitish(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._target_commitish)
        return self._target_commitish.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def body(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._body)
        return self._body.value

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
    def author(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._author)
        return self._author.value

    @property
    def assets(self):
        """
        :type: :class:`github.PaginatedList.PaginatedList` of :class:`github.ReleaseAsset.ReleaseAsset`
        """
        self._completeIfNotSet(self._assets)
        return self._assets.value

    def _initAttributes(self):
        self._url = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._assets_url = github.GithubObject.NotSet
        self._upload_url = github.GithubObject.NotSet
        self._tarball_url = github.GithubObject.NotSet
        self._zipball_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._tag_name = github.GithubObject.NotSet
        self._target_commitish = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._body = github.GithubObject.NotSet
        self._draft = github.GithubObject.NotSet
        self._prerelease = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._published_at = github.GithubObject.NotSet
        self._author = github.GithubObject.NotSet
        self._assets = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])  # pragma no cover
        if "html_url" in attributes:  # pragma no branch
            self._html_url = self._makeStringAttribute(attributes["html_url"])  # pragma no cover
        if "assets_url" in attributes:  # pragma no branch
            self._assets_url = self._makeStringAttribute(attributes["assets_url"])  # pragma no cover
        if "upload_url" in attributes:  # pragma no branch
            self._upload_url = self._makeStringAttribute(attributes["upload_url"])
        if "tarball_url" in attributes:  # pragma no branch
            self._tarball_url = self._makeStringAttribute(attributes["tarball_url"])
        if "zipball_url" in attributes:  # pragma no branch
            self._zipball_url = self._makeStringAttribute(attributes["zipball_url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "tag_name" in attributes:  # pragma no branch
            self._tag_name = self._makeStringAttribute(attributes["tag_name"])
        if "target_commitish" in attributes:  # pragma no branch
            self._target_commitish = self._makeStringAttribute(attributes["target_commitish"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "body" in attributes:  # pragma no branch
            self._body = self._makeStringAttribute(attributes["body"])
        if "draft" in attributes:  # pragma no branch
            self._draft = self._makeBoolAttribute(attributes["draft"])
        if "prerelease" in attributes:  # pragma no branch
            self._prerelease = self._makeBoolAttribute(attributes["prerelease"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "published_at" in attributes:  # pragma no branch
            self._published_at = self._makeDatetimeAttribute(attributes["published_at"])
        if "author" in attributes:  # pragma no branch
            self._author = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["author"])
        if "assets" in attributes:  # pragma no branch
            self._assets = self._makeListOfClassesAttribute(github.ReleaseAsset.ReleaseAsset, attributes["assets"])

