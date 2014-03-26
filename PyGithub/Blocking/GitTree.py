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


class GitTree(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.GitTree.create_modified_copy`
      * :meth:`.Repository.create_git_tree`
      * :meth:`.Repository.get_git_tree`
    """

    def _initAttributes(self, sha=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, tree=None, **kwds):
        super(GitTree, self)._initAttributes(**kwds)
        self.__sha = PyGithub.Blocking.Attributes.StringAttribute("GitTree.sha", sha)
        self.__url = PyGithub.Blocking.Attributes.StringAttribute("GitTree.url", url)

    def _updateAttributes(self, eTag, sha=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, tree=None, **kwds):
        super(GitTree, self)._updateAttributes(eTag, **kwds)
        self.__sha.update(sha)
        self.__url.update(url)

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
