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


class Commit(bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.Branch.parents`
      * :meth:`.Repository.get_commit`
      * :meth:`.Repository.get_commits`
      * :attr:`.Tag.commit`
    """

    def _initAttributes(self, sha=rcv.Absent, url=rcv.Absent, **kwds):
        super(Commit, self)._initAttributes(**kwds)
        self.__sha = rcv.Attribute("Commit.sha", rcv.StringConverter, sha)
        self.__url = rcv.Attribute("Commit.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, sha=rcv.Absent, url=rcv.Absent, **kwds):
        super(Commit, self)._updateAttributes(eTag, **kwds)
        self.__sha.update(sha)
        self.__url.update(url)

    @property
    def sha(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__sha.needsLazyCompletion)
        return self.__sha.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value
