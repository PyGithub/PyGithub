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


class GitCommit(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.ContentCommit.commit`
      * :meth:`.File.delete`
      * :meth:`.File.edit`
    """

    class Author(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.GitCommit.author`
          * :attr:`.GitCommit.committer`
        """

        def _initAttributes(self, date=None, email=None, name=None, **kwds):
            super(GitCommit.Author, self)._initAttributes(**kwds)
            self.__date = self._createDatetimeAttribute("GitCommit.Author.date", date)
            self.__email = self._createStringAttribute("GitCommit.Author.email", email)
            self.__name = self._createStringAttribute("GitCommit.Author.name", name)

        def _updateAttributes(self, date=None, email=None, name=None, **kwds):
            super(GitCommit.Author, self)._updateAttributes(**kwds)
            self.__date.update(date)
            self.__email.update(email)
            self.__name.update(name)

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

    def _initAttributes(self, author=PyGithub.Blocking.Attributes.Absent, committer=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, message=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, parents=None, tree=None, **kwds):
        super(GitCommit, self)._initAttributes(**kwds)
        self.__author = self._createStructAttribute("GitCommit.author", GitCommit.Author, author)
        self.__committer = self._createStructAttribute("GitCommit.committer", GitCommit.Author, committer)
        self.__html_url = self._createStringAttribute("GitCommit.html_url", html_url)
        self.__message = self._createStringAttribute("GitCommit.message", message)
        self.__sha = self._createStringAttribute("GitCommit.sha", sha)
        self.__url = self._createStringAttribute("GitCommit.url", url)

    def _updateAttributes(self, eTag, author=PyGithub.Blocking.Attributes.Absent, committer=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, message=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, parents=None, tree=None, **kwds):
        super(GitCommit, self)._updateAttributes(eTag, **kwds)
        self.__author.update(author)
        self.__committer.update(committer)
        self.__html_url.update(html_url)
        self.__message.update(message)
        self.__sha.update(sha)
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
    def sha(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__sha.needsLazyCompletion)
        return self.__sha.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value
