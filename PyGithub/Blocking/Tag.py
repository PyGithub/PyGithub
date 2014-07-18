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


class Tag(bgo.SessionedGithubObject):
    """
    Base class: :class:`.SessionedGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.get_tags`
    """

    def _initAttributes(self, commit=rcv.Absent, name=rcv.Absent, tarball_url=rcv.Absent, zipball_url=rcv.Absent, **kwds):
        import PyGithub.Blocking.Commit
        super(Tag, self)._initAttributes(**kwds)
        self.__commit = rcv.Attribute("Tag.commit", rcv.StructureConverter(self.Session, PyGithub.Blocking.Commit.Commit), commit)
        self.__name = rcv.Attribute("Tag.name", rcv.StringConverter, name)
        self.__tarball_url = rcv.Attribute("Tag.tarball_url", rcv.StringConverter, tarball_url)
        self.__zipball_url = rcv.Attribute("Tag.zipball_url", rcv.StringConverter, zipball_url)

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

    @property
    def tarball_url(self):
        """
        :type: :class:`string`
        """
        return self.__tarball_url.value

    @property
    def zipball_url(self):
        """
        :type: :class:`string`
        """
        return self.__zipball_url.value
