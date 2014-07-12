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


class SymLink(bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Dir.get_contents`
      * :meth:`.Repository.get_contents`
    """

    def _initAttributes(self, git_url=rcv.Absent, html_url=rcv.Absent, name=rcv.Absent, path=rcv.Absent, sha=rcv.Absent, size=rcv.Absent, target=rcv.Absent, type=rcv.Absent, url=rcv.Absent, _links=None, **kwds):
        super(SymLink, self)._initAttributes(**kwds)
        self.__git_url = rcv.Attribute("SymLink.git_url", rcv.StringConverter, git_url)
        self.__html_url = rcv.Attribute("SymLink.html_url", rcv.StringConverter, html_url)
        self.__name = rcv.Attribute("SymLink.name", rcv.StringConverter, name)
        self.__path = rcv.Attribute("SymLink.path", rcv.StringConverter, path)
        self.__sha = rcv.Attribute("SymLink.sha", rcv.StringConverter, sha)
        self.__size = rcv.Attribute("SymLink.size", rcv.IntConverter, size)
        self.__target = rcv.Attribute("SymLink.target", rcv.StringConverter, target)
        self.__type = rcv.Attribute("SymLink.type", rcv.StringConverter, type)
        self.__url = rcv.Attribute("SymLink.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, git_url=rcv.Absent, html_url=rcv.Absent, name=rcv.Absent, path=rcv.Absent, sha=rcv.Absent, size=rcv.Absent, target=rcv.Absent, type=rcv.Absent, url=rcv.Absent, _links=None, **kwds):
        super(SymLink, self)._updateAttributes(eTag, **kwds)
        self.__git_url.update(git_url)
        self.__html_url.update(html_url)
        self.__name.update(name)
        self.__path.update(path)
        self.__sha.update(sha)
        self.__size.update(size)
        self.__target.update(target)
        self.__type.update(type)
        self.__url.update(url)

    @property
    def git_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_url.needsLazyCompletion)
        return self.__git_url.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__html_url.needsLazyCompletion)
        return self.__html_url.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

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
    def target(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__target.needsLazyCompletion)
        return self.__target.value

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
