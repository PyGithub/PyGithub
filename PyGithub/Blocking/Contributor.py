# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv

import PyGithub.Blocking.User


class Contributor(PyGithub.Blocking.User.User):
    """
    Base class: :class:`.User`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.get_contributors`
    """

    def _initAttributes(self, contributions=_rcv.Absent, **kwds):
        super(Contributor, self)._initAttributes(**kwds)
        self.__contributions = _rcv.Attribute("Contributor.contributions", _rcv.IntConverter, contributions)

    def _updateAttributes(self, eTag, contributions=_rcv.Absent, **kwds):
        super(Contributor, self)._updateAttributes(eTag, **kwds)
        self.__contributions.update(contributions)

    @property
    def contributions(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__contributions.needsLazyCompletion)
        return self.__contributions.value
