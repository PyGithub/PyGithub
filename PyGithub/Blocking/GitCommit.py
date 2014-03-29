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

import PyGithub.Blocking.GitTree


class GitCommit(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.ContentCommit.commit`
      * :meth:`.File.delete`
      * :meth:`.File.edit`
      * :attr:`.GitCommit.parents`
      * :meth:`.Repository.get_git_commit`
    """

    class Author(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.GitCommit.author`
          * :attr:`.GitCommit.committer`
        """

        def _initAttributes(self, date=None, email=None, name=None, **kwds):
            super(GitCommit.Author, self)._initAttributes(**kwds)
            self.__date = rcv.Attribute("GitCommit.Author.date", rcv.DatetimeConverter, date)
            self.__email = rcv.Attribute("GitCommit.Author.email", rcv.StringConverter, email)
            self.__name = rcv.Attribute("GitCommit.Author.name", rcv.StringConverter, name)

        @property
        def date(self):
            """
            :type: :class:`datetime`
            """
            return self.__date.value

        @property
        def email(self):
            """
            :type: :class:`string`
            """
            return self.__email.value

        @property
        def name(self):
            """
            :type: :class:`string`
            """
            return self.__name.value

    def _initAttributes(self, author=rcv.Absent, committer=rcv.Absent, html_url=rcv.Absent, message=rcv.Absent, parents=rcv.Absent, sha=rcv.Absent, tree=rcv.Absent, url=rcv.Absent, **kwds):
        super(GitCommit, self)._initAttributes(**kwds)
        self.__author = rcv.Attribute("GitCommit.author", rcv.StructureConverter(self.Session, GitCommit.Author), author)
        self.__committer = rcv.Attribute("GitCommit.committer", rcv.StructureConverter(self.Session, GitCommit.Author), committer)
        self.__html_url = rcv.Attribute("GitCommit.html_url", rcv.StringConverter, html_url)
        self.__message = rcv.Attribute("GitCommit.message", rcv.StringConverter, message)
        self.__parents = rcv.Attribute("GitCommit.parents", rcv.ListConverter(rcv.ClassConverter(self.Session, GitCommit)), parents)
        self.__sha = rcv.Attribute("GitCommit.sha", rcv.StringConverter, sha)
        self.__tree = rcv.Attribute("GitCommit.tree", rcv.ClassConverter(self.Session, PyGithub.Blocking.GitTree.GitTree), tree)
        self.__url = rcv.Attribute("GitCommit.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, author=rcv.Absent, committer=rcv.Absent, html_url=rcv.Absent, message=rcv.Absent, parents=rcv.Absent, sha=rcv.Absent, tree=rcv.Absent, url=rcv.Absent, **kwds):
        super(GitCommit, self)._updateAttributes(eTag, **kwds)
        self.__author.update(author)
        self.__committer.update(committer)
        self.__html_url.update(html_url)
        self.__message.update(message)
        self.__parents.update(parents)
        self.__sha.update(sha)
        self.__tree.update(tree)
        self.__url.update(url)

    @property
    def author(self):
        """
        :type: :class:`.Author`
        """
        self._completeLazily(self.__author.needsLazyCompletion)
        return self.__author.value

    @property
    def committer(self):
        """
        :type: :class:`.Author`
        """
        self._completeLazily(self.__committer.needsLazyCompletion)
        return self.__committer.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__html_url.needsLazyCompletion)
        return self.__html_url.value

    @property
    def message(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__message.needsLazyCompletion)
        return self.__message.value

    @property
    def parents(self):
        """
        :type: :class:`list` of :class:`.GitCommit`
        """
        self._completeLazily(self.__parents.needsLazyCompletion)
        return self.__parents.value

    @property
    def sha(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__sha.needsLazyCompletion)
        return self.__sha.value

    @property
    def tree(self):
        """
        :type: :class:`.GitTree`
        """
        self._completeLazily(self.__tree.needsLazyCompletion)
        return self.__tree.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value
