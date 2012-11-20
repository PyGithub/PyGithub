# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import GithubObject


class Download(GithubObject.GithubObject):
    @property
    def accesskeyid(self):
        self._completeIfNotSet(self._accesskeyid)
        return self._NoneIfNotSet(self._accesskeyid)

    @property
    def acl(self):
        self._completeIfNotSet(self._acl)
        return self._NoneIfNotSet(self._acl)

    @property
    def bucket(self):
        self._completeIfNotSet(self._bucket)
        return self._NoneIfNotSet(self._bucket)

    @property
    def content_type(self):
        self._completeIfNotSet(self._content_type)
        return self._NoneIfNotSet(self._content_type)

    @property
    def created_at(self):
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def description(self):
        self._completeIfNotSet(self._description)
        return self._NoneIfNotSet(self._description)

    @property
    def download_count(self):
        self._completeIfNotSet(self._download_count)
        return self._NoneIfNotSet(self._download_count)

    @property
    def expirationdate(self):
        self._completeIfNotSet(self._expirationdate)
        return self._NoneIfNotSet(self._expirationdate)

    @property
    def html_url(self):
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def id(self):
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def mime_type(self):
        self._completeIfNotSet(self._mime_type)
        return self._NoneIfNotSet(self._mime_type)

    @property
    def name(self):
        self._completeIfNotSet(self._name)
        return self._NoneIfNotSet(self._name)

    @property
    def path(self):
        self._completeIfNotSet(self._path)
        return self._NoneIfNotSet(self._path)

    @property
    def policy(self):
        self._completeIfNotSet(self._policy)
        return self._NoneIfNotSet(self._policy)

    @property
    def prefix(self):
        self._completeIfNotSet(self._prefix)
        return self._NoneIfNotSet(self._prefix)

    @property
    def redirect(self):
        self._completeIfNotSet(self._redirect)
        return self._NoneIfNotSet(self._redirect)

    @property
    def s3_url(self):
        self._completeIfNotSet(self._s3_url)
        return self._NoneIfNotSet(self._s3_url)

    @property
    def signature(self):
        self._completeIfNotSet(self._signature)
        return self._NoneIfNotSet(self._signature)

    @property
    def size(self):
        self._completeIfNotSet(self._size)
        return self._NoneIfNotSet(self._size)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def delete(self):
        headers, data = self._requester.requestAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def _initAttributes(self):
        self._accesskeyid = GithubObject.NotSet
        self._acl = GithubObject.NotSet
        self._bucket = GithubObject.NotSet
        self._content_type = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._description = GithubObject.NotSet
        self._download_count = GithubObject.NotSet
        self._expirationdate = GithubObject.NotSet
        self._html_url = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._mime_type = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._path = GithubObject.NotSet
        self._policy = GithubObject.NotSet
        self._prefix = GithubObject.NotSet
        self._redirect = GithubObject.NotSet
        self._s3_url = GithubObject.NotSet
        self._signature = GithubObject.NotSet
        self._size = GithubObject.NotSet
        self._url = GithubObject.NotSet

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
