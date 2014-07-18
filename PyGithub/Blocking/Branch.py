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

    def _initAttributes(self, author=rcv.Absent, commit=rcv.Absent, commiter=rcv.Absent, name=rcv.Absent, parents=rcv.Absent, url=rcv.Absent, **kwds):
        import PyGithub.Blocking.Commit
        import PyGithub.Blocking.GitCommit
        import PyGithub.Blocking.User
        super(Branch, self)._initAttributes(**kwds)
        self.__author = rcv.Attribute("Branch.author", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), author)
        self.__commit = rcv.Attribute("Branch.commit", rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit), commit)
        self.__commiter = rcv.Attribute("Branch.commiter", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), commiter)
        self.__name = rcv.Attribute("Branch.name", rcv.StringConverter, name)
        self.__parents = rcv.Attribute("Branch.parents", rcv.ListConverter(rcv.ClassConverter(self.Session, PyGithub.Blocking.Commit.Commit)), parents)
        self.__url = rcv.Attribute("Branch.url", rcv.StringConverter, url)

    @property
    def author(self):
        """
        :type: :class:`.User`
        """
        return self.__author.value

    @property
    def commit(self):
        """
        :type: :class:`.GitCommit`
        """
        return self.__commit.value

    @property
    def commiter(self):
        """
        :type: :class:`.User`
        """
        return self.__commiter.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        return self.__name.value

    @property
    def parents(self):
        """
        :type: :class:`list` of :class:`.Commit`
        """
        return self.__parents.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self.__url.value
