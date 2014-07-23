# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class GitObject(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes:
      * :class:`.GitBlob`
      * :class:`.GitCommit`
      * :class:`.GitTag`
      * :class:`.GitTree`

    Methods and attributes returning instances of this class: none.
    """

    def _initAttributes(self, sha=_rcv.Absent, type=_rcv.Absent, **kwds):
        super(GitObject, self)._initAttributes(**kwds)
        self.__sha = _rcv.Attribute("GitObject.sha", _rcv.StringConverter, sha)
        self.__type = _rcv.Attribute("GitObject.type", _rcv.StringConverter, type)

    def _updateAttributes(self, eTag, sha=_rcv.Absent, type=_rcv.Absent, **kwds):
        super(GitObject, self)._updateAttributes(eTag, **kwds)
        self.__sha.update(sha)
        self.__type.update(type)

    @property
    def sha(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__sha.needsLazyCompletion)
        return self.__sha.value

    @property
    def type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__type.needsLazyCompletion)
        return self.__type.value
