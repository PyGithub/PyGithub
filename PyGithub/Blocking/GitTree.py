# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class GitTree(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.GitCommit.tree`
      * :meth:`.GitTree.create_modified_copy`
      * :attr:`.GitTree.tree`
      * :meth:`.Repository.create_git_tree`
      * :meth:`.Repository.get_git_tree`
    """

    class GitSubmodule(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.GitTree.tree`
        """

        def _initAttributes(self, mode=None, path=None, sha=None, type=None, **kwds):
            super(GitTree.GitSubmodule, self)._initAttributes(**kwds)
            self.__mode = _rcv.Attribute("GitTree.GitSubmodule.mode", _rcv.StringConverter, mode)
            self.__path = _rcv.Attribute("GitTree.GitSubmodule.path", _rcv.StringConverter, path)
            self.__sha = _rcv.Attribute("GitTree.GitSubmodule.sha", _rcv.StringConverter, sha)
            self.__type = _rcv.Attribute("GitTree.GitSubmodule.type", _rcv.StringConverter, type)

        def _updateAttributes(self, mode=None, path=None, sha=None, type=None, **kwds):
            super(GitTree.GitSubmodule, self)._updateAttributes(**kwds)
            self.__mode.update(mode)
            self.__path.update(path)
            self.__sha.update(sha)
            self.__type.update(type)

        @property
        def mode(self):
            """
            :type: :class:`string`
            """
            return self.__mode.value

        @property
        def path(self):
            """
            :type: :class:`string`
            """
            return self.__path.value

        @property
        def sha(self):
            """
            :type: :class:`string`
            """
            return self.__sha.value

        @property
        def type(self):
            """
            :type: :class:`string`
            """
            return self.__type.value

    def _initAttributes(self, mode=_rcv.Absent, path=_rcv.Absent, sha=_rcv.Absent, tree=_rcv.Absent, type=_rcv.Absent, **kwds):
        import PyGithub.Blocking.GitBlob
        super(GitTree, self)._initAttributes(**kwds)
        self.__mode = _rcv.Attribute("GitTree.mode", _rcv.StringConverter, mode)
        self.__path = _rcv.Attribute("GitTree.path", _rcv.StringConverter, path)
        self.__sha = _rcv.Attribute("GitTree.sha", _rcv.StringConverter, sha)
        self.__tree = _rcv.Attribute("GitTree.tree", _rcv.ListConverter(_rcv.KeyedStructureUnionConverter("type", dict(blob=_rcv.ClassConverter(self.Session, PyGithub.Blocking.GitBlob.GitBlob), commit=_rcv.StructureConverter(self.Session, GitTree.GitSubmodule), tree=_rcv.ClassConverter(self.Session, GitTree)))), tree)
        self.__type = _rcv.Attribute("GitTree.type", _rcv.StringConverter, type)

    def _updateAttributes(self, eTag, mode=_rcv.Absent, path=_rcv.Absent, sha=_rcv.Absent, tree=_rcv.Absent, type=_rcv.Absent, **kwds):
        super(GitTree, self)._updateAttributes(eTag, **kwds)
        self.__mode.update(mode)
        self.__path.update(path)
        self.__sha.update(sha)
        self.__tree.update(tree)
        self.__type.update(type)

    @property
    def mode(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__mode.needsLazyCompletion)
        return self.__mode.value

    @property
    def path(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__path.needsLazyCompletion)
        return self.__path.value

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
        :type: :class:`list` of :class:`.GitTree` or :class:`.GitBlob` or :class:`.GitSubmodule`
        """
        self._completeLazily(self.__tree.needsLazyCompletion)
        return self.__tree.value

    @property
    def type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__type.needsLazyCompletion)
        return self.__type.value

    def create_modified_copy(self, tree):
        """
        Calls the `POST /repos/:owner/:repo/git/trees <http://developer.github.com/v3/git/trees#create-a-tree>`__ end point.

        The following methods also call this end point:
          * :meth:`.Repository.create_git_tree`

        :param tree: mandatory :class:`list` of :class:`dict`
        :rtype: :class:`.GitTree`
        """

        tree = _snd.normalizeList(_snd.normalizeDict, tree)

        url = self.url[:self.url.rfind(self.sha) - 1]
        postArguments = _snd.dictionary(base_tree=self.sha, tree=tree)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, GitTree)(None, r.json(), r.headers.get("ETag"))
