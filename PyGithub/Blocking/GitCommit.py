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


class GitCommit(PyGithub.Blocking.GitObject.GitObject):
    """
    Base class: :class:`.GitObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.Commit.commit`
      * :meth:`.File.delete`
      * :meth:`.File.edit`
      * :attr:`.GitCommit.parents`
      * :attr:`.GitRef.object`
      * :attr:`.GitTag.object`
      * :attr:`.Repository.ContentCommit.commit`
      * :meth:`.Repository.create_git_commit`
      * :meth:`.Repository.get_git_commit`

    Methods accepting instances of this class as parameter:
      * :meth:`.Repository.create_git_commit`
    """

    def _initAttributes(self, author=_rcv.Absent, comment_count=_rcv.Absent, committer=_rcv.Absent, html_url=_rcv.Absent, message=_rcv.Absent, parents=_rcv.Absent, tree=_rcv.Absent, **kwds):
        import PyGithub.Blocking.GitTree
        super(GitCommit, self)._initAttributes(**kwds)
        self.__author = _rcv.Attribute("GitCommit.author", _rcv.StructureConverter(self.Session, PyGithub.Blocking.GitObject.GitObject.Author), author)
        self.__comment_count = _rcv.Attribute("GitCommit.comment_count", _rcv.IntConverter, comment_count)
        self.__committer = _rcv.Attribute("GitCommit.committer", _rcv.StructureConverter(self.Session, PyGithub.Blocking.GitObject.GitObject.Author), committer)
        self.__html_url = _rcv.Attribute("GitCommit.html_url", _rcv.StringConverter, html_url)
        self.__message = _rcv.Attribute("GitCommit.message", _rcv.StringConverter, message)
        self.__parents = _rcv.Attribute("GitCommit.parents", _rcv.ListConverter(_rcv.ClassConverter(self.Session, GitCommit)), parents)
        self.__tree = _rcv.Attribute("GitCommit.tree", _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitTree.GitTree), tree)

    def _updateAttributes(self, eTag, author=_rcv.Absent, comment_count=_rcv.Absent, committer=_rcv.Absent, html_url=_rcv.Absent, message=_rcv.Absent, parents=_rcv.Absent, tree=_rcv.Absent, **kwds):
        super(GitCommit, self)._updateAttributes(eTag, **kwds)
        self.__author.update(author)
        self.__comment_count.update(comment_count)
        self.__committer.update(committer)
        self.__html_url.update(html_url)
        self.__message.update(message)
        self.__parents.update(parents)
        self.__tree.update(tree)

    @property
    def author(self):
        """
        :type: :class:`.GitObject.Author`
        """
        self._completeLazily(self.__author.needsLazyCompletion)
        return self.__author.value

    @property
    def comment_count(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__comment_count.needsLazyCompletion)
        return self.__comment_count.value

    @property
    def committer(self):
        """
        :type: :class:`.GitObject.Author`
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
    def tree(self):
        """
        :type: :class:`.GitTree`
        """
        self._completeLazily(self.__tree.needsLazyCompletion)
        return self.__tree.value
