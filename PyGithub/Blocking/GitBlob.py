# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking._base_github_object as bgo
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv


class GitBlob(bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.GitTree.tree`
      * :meth:`.Repository.create_git_blob`
      * :meth:`.Repository.get_git_blob`
    """

    def _initAttributes(self, content=rcv.Absent, encoding=rcv.Absent, mode=rcv.Absent, path=rcv.Absent, sha=rcv.Absent, size=rcv.Absent, type=rcv.Absent, url=rcv.Absent, **kwds):
        super(GitBlob, self)._initAttributes(**kwds)
        self.__content = rcv.Attribute("GitBlob.content", rcv.StringConverter, content)
        self.__encoding = rcv.Attribute("GitBlob.encoding", rcv.StringConverter, encoding)
        self.__mode = rcv.Attribute("GitBlob.mode", rcv.StringConverter, mode)
        self.__path = rcv.Attribute("GitBlob.path", rcv.StringConverter, path)
        self.__sha = rcv.Attribute("GitBlob.sha", rcv.StringConverter, sha)
        self.__size = rcv.Attribute("GitBlob.size", rcv.IntConverter, size)
        self.__type = rcv.Attribute("GitBlob.type", rcv.StringConverter, type)
        self.__url = rcv.Attribute("GitBlob.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, content=rcv.Absent, encoding=rcv.Absent, mode=rcv.Absent, path=rcv.Absent, sha=rcv.Absent, size=rcv.Absent, type=rcv.Absent, url=rcv.Absent, **kwds):
        super(GitBlob, self)._updateAttributes(eTag, **kwds)
        self.__content.update(content)
        self.__encoding.update(encoding)
        self.__mode.update(mode)
        self.__path.update(path)
        self.__sha.update(sha)
        self.__size.update(size)
        self.__type.update(type)
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
    def mode(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__mode.needsLazyCompletion)
        return self.__mode.value

    @property
    def path(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__path.needsLazyCompletion)
        return self.__path.value

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
    def type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__type.needsLazyCompletion)
        return self.__type.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value
