# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

########################################################################
###### This file is generated. Manual changes will likely be lost. #####
########################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.PaginatedList
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv

import PyGithub.Blocking.User


class Contributor(PyGithub.Blocking.User.User):
    """
    Base class: :class:`.User`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.get_contributors`
    """

    def _initAttributes(self, contributions=rcv.Absent, **kwds):
        super(Contributor, self)._initAttributes(**kwds)
        self.__contributions = rcv.Attribute("Contributor.contributions", rcv.IntConverter, contributions)

    def _updateAttributes(self, eTag, contributions=rcv.Absent, **kwds):
        super(Contributor, self)._updateAttributes(eTag, **kwds)
        self.__contributions.update(contributions)

    @property
    def contributions(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__contributions.needsLazyCompletion)
        return self.__contributions.value
