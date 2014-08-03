# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class GitTag(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.GitRef.object`
      * :attr:`.GitTag.object`
      * :meth:`.Repository.create_git_tag`
      * :meth:`.Repository.get_git_tag`

    Methods accepting instances of this class as parameter: none.
    """

    def _initAttributes(self, message=_rcv.Absent, object=_rcv.Absent, sha=_rcv.Absent, tag=_rcv.Absent, tagger=_rcv.Absent, type=_rcv.Absent, **kwds):
        import PyGithub.Blocking.GitBlob
        import PyGithub.Blocking.GitCommit
        import PyGithub.Blocking.GitTree
        super(GitTag, self)._initAttributes(**kwds)
        self.__message = _rcv.Attribute("GitTag.message", _rcv.StringConverter, message)
        self.__object = _rcv.Attribute("GitTag.object", _rcv.KeyedStructureUnionConverter("type", dict(blob=_rcv.ClassConverter(self.Session, PyGithub.Blocking.GitBlob.GitBlob), commit=_rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit), tag=_rcv.ClassConverter(self.Session, GitTag), tree=_rcv.ClassConverter(self.Session, PyGithub.Blocking.GitTree.GitTree))), object)
        self.__sha = _rcv.Attribute("GitTag.sha", _rcv.StringConverter, sha)
        self.__tag = _rcv.Attribute("GitTag.tag", _rcv.StringConverter, tag)
        self.__tagger = _rcv.Attribute("GitTag.tagger", _rcv.StructureConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit.Author), tagger)
        self.__type = _rcv.Attribute("GitTag.type", _rcv.StringConverter, type)

    def _updateAttributes(self, eTag, message=_rcv.Absent, object=_rcv.Absent, sha=_rcv.Absent, tag=_rcv.Absent, tagger=_rcv.Absent, type=_rcv.Absent, **kwds):
        super(GitTag, self)._updateAttributes(eTag, **kwds)
        self.__message.update(message)
        self.__object.update(object)
        self.__sha.update(sha)
        self.__tag.update(tag)
        self.__tagger.update(tagger)
        self.__type.update(type)

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
    def sha(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__sha.needsLazyCompletion)
        return self.__sha.value

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
        :type: :class:`.GitCommit.Author`
        """
        self._completeLazily(self.__tagger.needsLazyCompletion)
        return self.__tagger.value

    @property
    def type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__type.needsLazyCompletion)
        return self.__type.value
