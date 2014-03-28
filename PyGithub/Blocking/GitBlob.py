# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

########################################################################
###### This file is generated. Manual changes will likely be lost. #####
########################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.Parameters
import PyGithub.Blocking.Attributes


class GitBlob(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.create_git_blob`
      * :meth:`.Repository.get_git_blob`
    """

    def _initAttributes(self, content=PyGithub.Blocking.Attributes.Absent, encoding=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, size=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(GitBlob, self)._initAttributes(**kwds)
        self.__content = PyGithub.Blocking.Attributes.Attribute("GitBlob.content", PyGithub.Blocking.Attributes.StringConverter, content)
        self.__encoding = PyGithub.Blocking.Attributes.Attribute("GitBlob.encoding", PyGithub.Blocking.Attributes.StringConverter, encoding)
        self.__sha = PyGithub.Blocking.Attributes.Attribute("GitBlob.sha", PyGithub.Blocking.Attributes.StringConverter, sha)
        self.__size = PyGithub.Blocking.Attributes.Attribute("GitBlob.size", PyGithub.Blocking.Attributes.IntConverter, size)
        self.__url = PyGithub.Blocking.Attributes.Attribute("GitBlob.url", PyGithub.Blocking.Attributes.StringConverter, url)

    def _updateAttributes(self, eTag, content=PyGithub.Blocking.Attributes.Absent, encoding=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, size=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(GitBlob, self)._updateAttributes(eTag, **kwds)
        self.__content.update(content)
        self.__encoding.update(encoding)
        self.__sha.update(sha)
        self.__size.update(size)
        self.__url.update(url)

    @property
    def content(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__content.needsLazyCompletion)
        return self.__content.value

    @property
    def encoding(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__encoding.needsLazyCompletion)
        return self.__encoding.value

    @property
    def sha(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__sha.needsLazyCompletion)
        return self.__sha.value

    @property
    def size(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__size.needsLazyCompletion)
        return self.__size.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value
