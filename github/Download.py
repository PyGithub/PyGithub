# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
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
################################################################################

import github.GithubObject


class Download(github.GithubObject.CompletableGithubObject):
    """
    This class represents Downloads as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def accesskeyid(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._accesskeyid)
        return self._NoneIfNotSet(self._accesskeyid)

    @property
    def acl(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._acl)
        return self._NoneIfNotSet(self._acl)

    @property
    def bucket(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._bucket)
        return self._NoneIfNotSet(self._bucket)

    @property
    def content_type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._content_type)
        return self._NoneIfNotSet(self._content_type)

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._NoneIfNotSet(self._description)

    @property
    def download_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._download_count)
        return self._NoneIfNotSet(self._download_count)

    @property
    def expirationdate(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._expirationdate)
        return self._NoneIfNotSet(self._expirationdate)

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def mime_type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._mime_type)
        return self._NoneIfNotSet(self._mime_type)

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._NoneIfNotSet(self._name)

    @property
    def path(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._path)
        return self._NoneIfNotSet(self._path)

    @property
    def policy(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._policy)
        return self._NoneIfNotSet(self._policy)

    @property
    def prefix(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._prefix)
        return self._NoneIfNotSet(self._prefix)

    @property
    def redirect(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._redirect)
        return self._NoneIfNotSet(self._redirect)

    @property
    def s3_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._s3_url)
        return self._NoneIfNotSet(self._s3_url)

    @property
    def signature(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._signature)
        return self._NoneIfNotSet(self._signature)

    @property
    def size(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._size)
        return self._NoneIfNotSet(self._size)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def delete(self):
        """
        :calls: `DELETE /repos/:owner/:repo/downloads/:id <http://developer.github.com/v3/repos/downloads>`_
        :rtype: None
        """
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url
        )

    def _initAttributes(self):
        self._accesskeyid = github.GithubObject.NotSet
        self._acl = github.GithubObject.NotSet
        self._bucket = github.GithubObject.NotSet
        self._content_type = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._description = github.GithubObject.NotSet
        self._download_count = github.GithubObject.NotSet
        self._expirationdate = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._mime_type = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._path = github.GithubObject.NotSet
        self._policy = github.GithubObject.NotSet
        self._prefix = github.GithubObject.NotSet
        self._redirect = github.GithubObject.NotSet
        self._s3_url = github.GithubObject.NotSet
        self._signature = github.GithubObject.NotSet
        self._size = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "accesskeyid" in attributes:  # pragma no branch
            assert attributes["accesskeyid"] is None or isinstance(attributes["accesskeyid"], (str, unicode)), attributes["accesskeyid"]
            self._accesskeyid = attributes["accesskeyid"]
        if "acl" in attributes:  # pragma no branch
            assert attributes["acl"] is None or isinstance(attributes["acl"], (str, unicode)), attributes["acl"]
            self._acl = attributes["acl"]
        if "bucket" in attributes:  # pragma no branch
            assert attributes["bucket"] is None or isinstance(attributes["bucket"], (str, unicode)), attributes["bucket"]
            self._bucket = attributes["bucket"]
        if "content_type" in attributes:  # pragma no branch
            assert attributes["content_type"] is None or isinstance(attributes["content_type"], (str, unicode)), attributes["content_type"]
            self._content_type = attributes["content_type"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            assert attributes["description"] is None or isinstance(attributes["description"], (str, unicode)), attributes["description"]
            self._description = attributes["description"]
        if "download_count" in attributes:  # pragma no branch
            assert attributes["download_count"] is None or isinstance(attributes["download_count"], (int, long)), attributes["download_count"]
            self._download_count = attributes["download_count"]
        if "expirationdate" in attributes:  # pragma no branch
            assert attributes["expirationdate"] is None or isinstance(attributes["expirationdate"], (str, unicode)), attributes["expirationdate"]
            self._expirationdate = self._parseDatetime(attributes["expirationdate"])
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "mime_type" in attributes:  # pragma no branch
            assert attributes["mime_type"] is None or isinstance(attributes["mime_type"], (str, unicode)), attributes["mime_type"]
            self._mime_type = attributes["mime_type"]
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "path" in attributes:  # pragma no branch
            assert attributes["path"] is None or isinstance(attributes["path"], (str, unicode)), attributes["path"]
            self._path = attributes["path"]
        if "policy" in attributes:  # pragma no branch
            assert attributes["policy"] is None or isinstance(attributes["policy"], (str, unicode)), attributes["policy"]
            self._policy = attributes["policy"]
        if "prefix" in attributes:  # pragma no branch
            assert attributes["prefix"] is None or isinstance(attributes["prefix"], (str, unicode)), attributes["prefix"]
            self._prefix = attributes["prefix"]
        if "redirect" in attributes:  # pragma no branch
            assert attributes["redirect"] is None or isinstance(attributes["redirect"], bool), attributes["redirect"]
            self._redirect = attributes["redirect"]
        if "s3_url" in attributes:  # pragma no branch
            assert attributes["s3_url"] is None or isinstance(attributes["s3_url"], (str, unicode)), attributes["s3_url"]
            self._s3_url = attributes["s3_url"]
        if "signature" in attributes:  # pragma no branch
            assert attributes["signature"] is None or isinstance(attributes["signature"], (str, unicode)), attributes["signature"]
            self._signature = attributes["signature"]
        if "size" in attributes:  # pragma no branch
            assert attributes["size"] is None or isinstance(attributes["size"], (int, long)), attributes["size"]
            self._size = attributes["size"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
