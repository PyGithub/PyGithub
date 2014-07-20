# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Label(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.Issue.labels`
      * :meth:`.Repository.get_label`
    """

    def _initAttributes(self, color=_rcv.Absent, name=_rcv.Absent, url=_rcv.Absent, **kwds):
        super(Label, self)._initAttributes(**kwds)
        self.__color = _rcv.Attribute("Label.color", _rcv.StringConverter, color)
        self.__name = _rcv.Attribute("Label.name", _rcv.StringConverter, name)
        self.__url = _rcv.Attribute("Label.url", _rcv.StringConverter, url)

    def _updateAttributes(self, eTag, color=_rcv.Absent, name=_rcv.Absent, url=_rcv.Absent, **kwds):
        super(Label, self)._updateAttributes(eTag, **kwds)
        self.__color.update(color)
        self.__name.update(name)
        self.__url.update(url)

    @property
    def color(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__color.needsLazyCompletion)
        return self.__color.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value
