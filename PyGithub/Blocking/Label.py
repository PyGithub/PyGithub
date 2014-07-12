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


class Label(bgo.SessionedGithubObject):
    """
    Base class: :class:`.SessionedGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.Issue.labels`
      * :meth:`.Repository.get_label`
    """

    def _initAttributes(self, color=rcv.Absent, name=rcv.Absent, url=rcv.Absent, **kwds):
        super(Label, self)._initAttributes(**kwds)
        self.__color = rcv.Attribute("Label.color", rcv.StringConverter, color)
        self.__name = rcv.Attribute("Label.name", rcv.StringConverter, name)
        self.__url = rcv.Attribute("Label.url", rcv.StringConverter, url)

    @property
    def color(self):
        """
        :type: :class:`string`
        """
        return self.__color.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        return self.__name.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self.__url.value
