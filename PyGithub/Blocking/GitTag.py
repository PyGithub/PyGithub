# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv

import PyGithub.Blocking.GitObject


class GitTag(PyGithub.Blocking.GitObject.GitObject):
    """
    Base class: :class:`.GitObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.GitRef.object`
      * :attr:`.GitTag.object`
      * :meth:`.Repository.create_git_tag`
      * :meth:`.Repository.get_git_tag`
    """

    class Tagger(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.GitTag.tagger`
        """

        def _initAttributes(self, date=None, email=None, name=None, **kwds):
            super(GitTag.Tagger, self)._initAttributes(**kwds)
            self.__date = _rcv.Attribute("GitTag.Tagger.date", _rcv.DatetimeConverter, date)
            self.__email = _rcv.Attribute("GitTag.Tagger.email", _rcv.StringConverter, email)
            self.__name = _rcv.Attribute("GitTag.Tagger.name", _rcv.StringConverter, name)

        def _updateAttributes(self, date=None, email=None, name=None, **kwds):
            super(GitTag.Tagger, self)._updateAttributes(**kwds)
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

    def _initAttributes(self, message=_rcv.Absent, object=_rcv.Absent, tag=_rcv.Absent, tagger=_rcv.Absent, **kwds):
        import PyGithub.Blocking.GitBlob
        import PyGithub.Blocking.GitCommit
        import PyGithub.Blocking.GitTree
        super(GitTag, self)._initAttributes(**kwds)
        self.__message = _rcv.Attribute("GitTag.message", _rcv.StringConverter, message)
        self.__object = _rcv.Attribute("GitTag.object", _rcv.KeyedStructureUnionConverter("type", dict(blob=_rcv.ClassConverter(self.Session, PyGithub.Blocking.GitBlob.GitBlob), commit=_rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit), tag=_rcv.ClassConverter(self.Session, GitTag), tree=_rcv.ClassConverter(self.Session, PyGithub.Blocking.GitTree.GitTree))), object)
        self.__tag = _rcv.Attribute("GitTag.tag", _rcv.StringConverter, tag)
        self.__tagger = _rcv.Attribute("GitTag.tagger", _rcv.StructureConverter(self.Session, GitTag.Tagger), tagger)

    def _updateAttributes(self, eTag, message=_rcv.Absent, object=_rcv.Absent, tag=_rcv.Absent, tagger=_rcv.Absent, **kwds):
        super(GitTag, self)._updateAttributes(eTag, **kwds)
        self.__message.update(message)
        self.__object.update(object)
        self.__tag.update(tag)
        self.__tagger.update(tagger)

    @property
    def message(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__message.needsLazyCompletion)
        return self.__message.value

    @property
    def object(self):
        """
        :type: :class:`.GitBlob` or :class:`.GitTree` or :class:`.GitCommit` or :class:`.GitTag`
        """
        self._completeLazily(self.__object.needsLazyCompletion)
        return self.__object.value

    @property
    def tag(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__tag.needsLazyCompletion)
        return self.__tag.value

    @property
    def tagger(self):
        """
        :type: :class:`.Tagger`
        """
        self._completeLazily(self.__tagger.needsLazyCompletion)
        return self.__tagger.value
