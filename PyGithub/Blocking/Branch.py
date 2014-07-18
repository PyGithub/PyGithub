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


class Branch(bgo.SessionedGithubObject):
    """
    Base class: :class:`.SessionedGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.get_branch`
      * :meth:`.Repository.get_branches`
    """

    def _initAttributes(self, commit=rcv.Absent, name=rcv.Absent, _links=None, **kwds):
        import PyGithub.Blocking.Commit
        super(Branch, self)._initAttributes(**kwds)
        self.__commit = rcv.Attribute("Branch.commit", rcv.StructureConverter(self.Session, PyGithub.Blocking.Commit.Commit), commit)
        self.__name = rcv.Attribute("Branch.name", rcv.StringConverter, name)

    @property
    def commit(self):
        """
        :type: :class:`.Commit`
        """
        return self.__commit.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        return self.__name.value
