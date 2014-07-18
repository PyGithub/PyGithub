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


class Commit(bgo.SessionedGithubObject):
    """
    Base class: :class:`.SessionedGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.Branch.commit`
      * :attr:`.Commit.parents`
      * :meth:`.Repository.get_commit`
      * :meth:`.Repository.get_commits`
      * :attr:`.Tag.commit`
    """

    class CommitFile(bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Commit.files`
        """

        def _initAttributes(self, additions=None, blob_url=None, changes=None, contents_url=None, deletions=None, filename=None, patch=None, raw_url=None, sha=None, status=None, **kwds):
            super(Commit.CommitFile, self)._initAttributes(**kwds)
            self.__additions = rcv.Attribute("Commit.CommitFile.additions", rcv.IntConverter, additions)
            self.__blob_url = rcv.Attribute("Commit.CommitFile.blob_url", rcv.StringConverter, blob_url)
            self.__changes = rcv.Attribute("Commit.CommitFile.changes", rcv.IntConverter, changes)
            self.__contents_url = rcv.Attribute("Commit.CommitFile.contents_url", rcv.StringConverter, contents_url)
            self.__deletions = rcv.Attribute("Commit.CommitFile.deletions", rcv.IntConverter, deletions)
            self.__filename = rcv.Attribute("Commit.CommitFile.filename", rcv.StringConverter, filename)
            self.__patch = rcv.Attribute("Commit.CommitFile.patch", rcv.StringConverter, patch)
            self.__raw_url = rcv.Attribute("Commit.CommitFile.raw_url", rcv.StringConverter, raw_url)
            self.__sha = rcv.Attribute("Commit.CommitFile.sha", rcv.StringConverter, sha)
            self.__status = rcv.Attribute("Commit.CommitFile.status", rcv.StringConverter, status)

        @property
        def additions(self):
            """
            :type: :class:`int`
            """
            return self.__additions.value

        @property
        def blob_url(self):
            """
            :type: :class:`string`
            """
            return self.__blob_url.value

        @property
        def changes(self):
            """
            :type: :class:`int`
            """
            return self.__changes.value

        @property
        def contents_url(self):
            """
            :type: :class:`string`
            """
            return self.__contents_url.value

        @property
        def deletions(self):
            """
            :type: :class:`int`
            """
            return self.__deletions.value

        @property
        def filename(self):
            """
            :type: :class:`string`
            """
            return self.__filename.value

        @property
        def patch(self):
            """
            :type: :class:`string`
            """
            return self.__patch.value

        @property
        def raw_url(self):
            """
            :type: :class:`string`
            """
            return self.__raw_url.value

        @property
        def sha(self):
            """
            :type: :class:`string`
            """
            return self.__sha.value

        @property
        def status(self):
            """
            :type: :class:`string`
            """
            return self.__status.value

    class Stats(bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Commit.stats`
        """

        def _initAttributes(self, additions=None, deletions=None, total=None, **kwds):
            super(Commit.Stats, self)._initAttributes(**kwds)
            self.__additions = rcv.Attribute("Commit.Stats.additions", rcv.IntConverter, additions)
            self.__deletions = rcv.Attribute("Commit.Stats.deletions", rcv.IntConverter, deletions)
            self.__total = rcv.Attribute("Commit.Stats.total", rcv.IntConverter, total)

        @property
        def additions(self):
            """
            :type: :class:`int`
            """
            return self.__additions.value

        @property
        def deletions(self):
            """
            :type: :class:`int`
            """
            return self.__deletions.value

        @property
        def total(self):
            """
            :type: :class:`int`
            """
            return self.__total.value

    def _initAttributes(self, author=rcv.Absent, comments_url=rcv.Absent, commit=rcv.Absent, committer=rcv.Absent, files=rcv.Absent, html_url=rcv.Absent, parents=rcv.Absent, sha=rcv.Absent, stats=rcv.Absent, url=rcv.Absent, **kwds):
        import PyGithub.Blocking.GitCommit
        import PyGithub.Blocking.User
        super(Commit, self)._initAttributes(**kwds)
        self.__author = rcv.Attribute("Commit.author", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), author)
        self.__comments_url = rcv.Attribute("Commit.comments_url", rcv.StringConverter, comments_url)
        self.__commit = rcv.Attribute("Commit.commit", rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit), commit)
        self.__committer = rcv.Attribute("Commit.committer", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), committer)
        self.__files = rcv.Attribute("Commit.files", rcv.ListConverter(rcv.StructureConverter(self.Session, Commit.CommitFile)), files)
        self.__html_url = rcv.Attribute("Commit.html_url", rcv.StringConverter, html_url)
        self.__parents = rcv.Attribute("Commit.parents", rcv.ListConverter(rcv.StructureConverter(self.Session, Commit)), parents)
        self.__sha = rcv.Attribute("Commit.sha", rcv.StringConverter, sha)
        self.__stats = rcv.Attribute("Commit.stats", rcv.StructureConverter(self.Session, Commit.Stats), stats)
        self.__url = rcv.Attribute("Commit.url", rcv.StringConverter, url)

    @property
    def author(self):
        """
        :type: :class:`.User`
        """
        return self.__author.value

    @property
    def comments_url(self):
        """
        :type: :class:`string`
        """
        return self.__comments_url.value

    @property
    def commit(self):
        """
        :type: :class:`.GitCommit`
        """
        return self.__commit.value

    @property
    def committer(self):
        """
        :type: :class:`.User`
        """
        return self.__committer.value

    @property
    def files(self):
        """
        :type: :class:`list` of :class:`.CommitFile`
        """
        return self.__files.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        return self.__html_url.value

    @property
    def parents(self):
        """
        :type: :class:`list` of :class:`.Commit`
        """
        return self.__parents.value

    @property
    def sha(self):
        """
        :type: :class:`string`
        """
        return self.__sha.value

    @property
    def stats(self):
        """
        :type: :class:`.Stats`
        """
        return self.__stats.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self.__url.value
