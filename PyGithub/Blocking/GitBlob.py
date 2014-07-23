# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv

import PyGithub.Blocking.GitObject


class GitBlob(PyGithub.Blocking.GitObject.GitObject):
    """
    Base class: :class:`.GitObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.GitRef.object`
      * :attr:`.GitTag.object`
      * :attr:`.GitTree.tree`
      * :meth:`.Repository.create_git_blob`
      * :meth:`.Repository.get_git_blob`
    """

    def _initAttributes(self, content=_rcv.Absent, encoding=_rcv.Absent, mode=_rcv.Absent, path=_rcv.Absent, size=_rcv.Absent, **kwds):
        super(GitBlob, self)._initAttributes(**kwds)
        self.__content = _rcv.Attribute("GitBlob.content", _rcv.StringConverter, content)
        self.__encoding = _rcv.Attribute("GitBlob.encoding", _rcv.StringConverter, encoding)
        self.__mode = _rcv.Attribute("GitBlob.mode", _rcv.StringConverter, mode)
        self.__path = _rcv.Attribute("GitBlob.path", _rcv.StringConverter, path)
        self.__size = _rcv.Attribute("GitBlob.size", _rcv.IntConverter, size)

    def _updateAttributes(self, eTag, content=_rcv.Absent, encoding=_rcv.Absent, mode=_rcv.Absent, path=_rcv.Absent, size=_rcv.Absent, **kwds):
        super(GitBlob, self)._updateAttributes(eTag, **kwds)
        self.__content.update(content)
        self.__encoding.update(encoding)
        self.__mode.update(mode)
        self.__path.update(path)
        self.__size.update(size)

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
    def size(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__size.needsLazyCompletion)
        return self.__size.value
