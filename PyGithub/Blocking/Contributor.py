# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

########################################################################
###### This file is generated. Manual changes will likely be lost. #####
########################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.Parameters
import PyGithub.Blocking.Attributes

import PyGithub.Blocking.User


class Contributor(PyGithub.Blocking.User.User):
    """
    Base class: :class:`.User`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.get_contributors`
    """

    def _initAttributes(self, contributions=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(Contributor, self)._initAttributes(**kwds)
        self.__contributions = self._createIntAttribute("Contributor.contributions", contributions)

    def _updateAttributes(self, eTag, contributions=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(Contributor, self)._updateAttributes(eTag, **kwds)
        self.__contributions.update(contributions)

    @property
    def contributions(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__contributions.needsLazyCompletion)
        return self.__contributions.value
