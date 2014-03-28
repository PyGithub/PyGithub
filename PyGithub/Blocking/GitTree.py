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

import PyGithub.Blocking.GitBlob


class GitTree(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
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

    class GitSubmodule(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.GitTree.tree`
        """

        def _initAttributes(self, mode=None, path=None, sha=None, type=None, **kwds):
            super(GitTree.GitSubmodule, self)._initAttributes(**kwds)
            self.__mode = PyGithub.Blocking.Attributes.Attribute("GitTree.GitSubmodule.mode", PyGithub.Blocking.Attributes.StringConverter, mode)
            self.__path = PyGithub.Blocking.Attributes.Attribute("GitTree.GitSubmodule.path", PyGithub.Blocking.Attributes.StringConverter, path)
            self.__sha = PyGithub.Blocking.Attributes.Attribute("GitTree.GitSubmodule.sha", PyGithub.Blocking.Attributes.StringConverter, sha)
            self.__type = PyGithub.Blocking.Attributes.Attribute("GitTree.GitSubmodule.type", PyGithub.Blocking.Attributes.StringConverter, type)

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

    def _initAttributes(self, mode=PyGithub.Blocking.Attributes.Absent, path=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, tree=PyGithub.Blocking.Attributes.Absent, type=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(GitTree, self)._initAttributes(**kwds)
        self.__mode = PyGithub.Blocking.Attributes.Attribute("GitTree.mode", PyGithub.Blocking.Attributes.StringConverter, mode)
        self.__path = PyGithub.Blocking.Attributes.Attribute("GitTree.path", PyGithub.Blocking.Attributes.StringConverter, path)
        self.__sha = PyGithub.Blocking.Attributes.Attribute("GitTree.sha", PyGithub.Blocking.Attributes.StringConverter, sha)
        self.__tree = PyGithub.Blocking.Attributes.Attribute("GitTree.tree", PyGithub.Blocking.Attributes.ListConverter(PyGithub.Blocking.Attributes.KeyedStructureUnionConverter("type", dict(blob=PyGithub.Blocking.Attributes.ClassConverter(self.Session, PyGithub.Blocking.GitBlob.GitBlob), commit=PyGithub.Blocking.Attributes.StructureConverter(self.Session, GitTree.GitSubmodule), tree=PyGithub.Blocking.Attributes.ClassConverter(self.Session, GitTree)))), tree)
        self.__type = PyGithub.Blocking.Attributes.Attribute("GitTree.type", PyGithub.Blocking.Attributes.StringConverter, type)
        self.__url = PyGithub.Blocking.Attributes.Attribute("GitTree.url", PyGithub.Blocking.Attributes.StringConverter, url)

    def _updateAttributes(self, eTag, mode=PyGithub.Blocking.Attributes.Absent, path=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, tree=PyGithub.Blocking.Attributes.Absent, type=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(GitTree, self)._updateAttributes(eTag, **kwds)
        self.__mode.update(mode)
        self.__path.update(path)
        self.__sha.update(sha)
        self.__tree.update(tree)
        self.__type.update(type)
        self.__url.update(url)

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

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value

    def create_modified_copy(self, tree):
        """
        Calls the `POST /repos/:owner/:repo/git/trees <http://developer.github.com/v3/git/trees#create-a-tree>`__ end point.

        The following methods also call this end point:
          * :meth:`.Repository.create_git_tree`

        :param tree: mandatory :class:`list` of :class:`dict`
        :rtype: :class:`.GitTree`
        """

        tree = PyGithub.Blocking.Parameters.normalizeList(PyGithub.Blocking.Parameters.normalizeDict, tree)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/git/trees", owner=self.owner.login, repo=self.name)
        postArguments = PyGithub.Blocking.Parameters.dictionary(base_tree=self.sha, tree=tree)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return GitTree(self.Session, r.json(), r.headers.get("ETag"))
