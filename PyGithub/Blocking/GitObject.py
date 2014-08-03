# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class GitObject(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes:
      * :class:`.GitBlob`
      * :class:`.GitCommit`
      * :class:`.GitTag`
      * :class:`.GitTree`

    Methods and attributes returning instances of this class: none.

    Methods accepting instances of this class as parameter: none.
    """

    class Author(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.GitCommit.author`
          * :attr:`.GitCommit.committer`
          * :attr:`.GitTag.tagger`

        Methods accepting instances of this class as parameter: none.
        """

        def _initAttributes(self, date=None, email=None, name=None, **kwds):
            super(GitObject.Author, self)._initAttributes(**kwds)
            self.__date = _rcv.Attribute("GitObject.Author.date", _rcv.DatetimeConverter, date)
            self.__email = _rcv.Attribute("GitObject.Author.email", _rcv.StringConverter, email)
            self.__name = _rcv.Attribute("GitObject.Author.name", _rcv.StringConverter, name)

        def _updateAttributes(self, date=None, email=None, name=None, **kwds):
            super(GitObject.Author, self)._updateAttributes(**kwds)
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

    def _initAttributes(self, sha=_rcv.Absent, type=_rcv.Absent, **kwds):
        super(GitObject, self)._initAttributes(**kwds)
        self.__sha = _rcv.Attribute("GitObject.sha", _rcv.StringConverter, sha)
        self.__type = _rcv.Attribute("GitObject.type", _rcv.StringConverter, type)

    def _updateAttributes(self, eTag, sha=_rcv.Absent, type=_rcv.Absent, **kwds):
        super(GitObject, self)._updateAttributes(eTag, **kwds)
        self.__sha.update(sha)
        self.__type.update(type)

    @property
    def sha(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__sha.needsLazyCompletion)
        return self.__sha.value

    @property
    def type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__type.needsLazyCompletion)
        return self.__type.value
