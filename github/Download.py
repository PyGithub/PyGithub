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
        return self._accesskeyid.value

    @property
    def acl(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._acl)
        return self._acl.value

    @property
    def bucket(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._bucket)
        return self._bucket.value

    @property
    def content_type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._content_type)
        return self._content_type.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._description.value

    @property
    def download_count(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._download_count)
        return self._download_count.value

    @property
    def expirationdate(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._expirationdate)
        return self._expirationdate.value

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._html_url.value

    @property
    def id(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def mime_type(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._mime_type)
        return self._mime_type.value

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def path(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._path)
        return self._path.value

    @property
    def policy(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._policy)
        return self._policy.value

    @property
    def prefix(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._prefix)
        return self._prefix.value

    @property
    def redirect(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._redirect)
        return self._redirect.value

    @property
    def s3_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._s3_url)
        return self._s3_url.value

    @property
    def signature(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._signature)
        return self._signature.value

    @property
    def size(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._size)
        return self._size.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

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
            self._accesskeyid = github.GithubObject.ValuedAttribute(attributes["accesskeyid"])
        if "acl" in attributes:  # pragma no branch
            assert attributes["acl"] is None or isinstance(attributes["acl"], (str, unicode)), attributes["acl"]
            self._acl = github.GithubObject.ValuedAttribute(attributes["acl"])
        if "bucket" in attributes:  # pragma no branch
            assert attributes["bucket"] is None or isinstance(attributes["bucket"], (str, unicode)), attributes["bucket"]
            self._bucket = github.GithubObject.ValuedAttribute(attributes["bucket"])
        if "content_type" in attributes:  # pragma no branch
            assert attributes["content_type"] is None or isinstance(attributes["content_type"], (str, unicode)), attributes["content_type"]
            self._content_type = github.GithubObject.ValuedAttribute(attributes["content_type"])
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = github.GithubObject.ValuedAttribute(self._parseDatetime(attributes["created_at"]))
        if "description" in attributes:  # pragma no branch
            assert attributes["description"] is None or isinstance(attributes["description"], (str, unicode)), attributes["description"]
            self._description = github.GithubObject.ValuedAttribute(attributes["description"])
        if "download_count" in attributes:  # pragma no branch
            assert attributes["download_count"] is None or isinstance(attributes["download_count"], (int, long)), attributes["download_count"]
            self._download_count = github.GithubObject.ValuedAttribute(attributes["download_count"])
        if "expirationdate" in attributes:  # pragma no branch
            assert attributes["expirationdate"] is None or isinstance(attributes["expirationdate"], (str, unicode)), attributes["expirationdate"]
            self._expirationdate = github.GithubObject.ValuedAttribute(self._parseDatetime(attributes["expirationdate"]))
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = github.GithubObject.ValuedAttribute(attributes["html_url"])
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = github.GithubObject.ValuedAttribute(attributes["id"])
        if "mime_type" in attributes:  # pragma no branch
            assert attributes["mime_type"] is None or isinstance(attributes["mime_type"], (str, unicode)), attributes["mime_type"]
            self._mime_type = github.GithubObject.ValuedAttribute(attributes["mime_type"])
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = github.GithubObject.ValuedAttribute(attributes["name"])
        if "path" in attributes:  # pragma no branch
            assert attributes["path"] is None or isinstance(attributes["path"], (str, unicode)), attributes["path"]
            self._path = github.GithubObject.ValuedAttribute(attributes["path"])
        if "policy" in attributes:  # pragma no branch
            assert attributes["policy"] is None or isinstance(attributes["policy"], (str, unicode)), attributes["policy"]
            self._policy = github.GithubObject.ValuedAttribute(attributes["policy"])
        if "prefix" in attributes:  # pragma no branch
            assert attributes["prefix"] is None or isinstance(attributes["prefix"], (str, unicode)), attributes["prefix"]
            self._prefix = github.GithubObject.ValuedAttribute(attributes["prefix"])
        if "redirect" in attributes:  # pragma no branch
            assert attributes["redirect"] is None or isinstance(attributes["redirect"], bool), attributes["redirect"]
            self._redirect = github.GithubObject.ValuedAttribute(attributes["redirect"])
        if "s3_url" in attributes:  # pragma no branch
            assert attributes["s3_url"] is None or isinstance(attributes["s3_url"], (str, unicode)), attributes["s3_url"]
            self._s3_url = github.GithubObject.ValuedAttribute(attributes["s3_url"])
        if "signature" in attributes:  # pragma no branch
            assert attributes["signature"] is None or isinstance(attributes["signature"], (str, unicode)), attributes["signature"]
            self._signature = github.GithubObject.ValuedAttribute(attributes["signature"])
        if "size" in attributes:  # pragma no branch
            assert attributes["size"] is None or isinstance(attributes["size"], (int, long)), attributes["size"]
            self._size = github.GithubObject.ValuedAttribute(attributes["size"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = github.GithubObject.ValuedAttribute(attributes["url"])
