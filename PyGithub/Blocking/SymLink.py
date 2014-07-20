# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class SymLink(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Dir.get_contents`
      * :meth:`.Repository.get_contents`
    """

    def _initAttributes(self, git_url=_rcv.Absent, html_url=_rcv.Absent, name=_rcv.Absent, path=_rcv.Absent, sha=_rcv.Absent, size=_rcv.Absent, target=_rcv.Absent, type=_rcv.Absent, url=_rcv.Absent, _links=None, **kwds):
        super(SymLink, self)._initAttributes(**kwds)
        self.__git_url = _rcv.Attribute("SymLink.git_url", _rcv.StringConverter, git_url)
        self.__html_url = _rcv.Attribute("SymLink.html_url", _rcv.StringConverter, html_url)
        self.__name = _rcv.Attribute("SymLink.name", _rcv.StringConverter, name)
        self.__path = _rcv.Attribute("SymLink.path", _rcv.StringConverter, path)
        self.__sha = _rcv.Attribute("SymLink.sha", _rcv.StringConverter, sha)
        self.__size = _rcv.Attribute("SymLink.size", _rcv.IntConverter, size)
        self.__target = _rcv.Attribute("SymLink.target", _rcv.StringConverter, target)
        self.__type = _rcv.Attribute("SymLink.type", _rcv.StringConverter, type)
        self.__url = _rcv.Attribute("SymLink.url", _rcv.StringConverter, url)

    def _updateAttributes(self, eTag, git_url=_rcv.Absent, html_url=_rcv.Absent, name=_rcv.Absent, path=_rcv.Absent, sha=_rcv.Absent, size=_rcv.Absent, target=_rcv.Absent, type=_rcv.Absent, url=_rcv.Absent, _links=None, **kwds):
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
