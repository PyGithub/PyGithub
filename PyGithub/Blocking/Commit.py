# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Commit(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.Branch.commit`
      * :attr:`.Commit.parents`
      * :meth:`.Repository.get_commit`
      * :meth:`.Repository.get_commits`
      * :attr:`.Tag.commit`
    """

    class CommitFile(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Commit.files`
        """

        def _initAttributes(self, additions=None, blob_url=None, changes=None, contents_url=None, deletions=None, filename=None, patch=None, raw_url=None, sha=None, status=None, **kwds):
            super(Commit.CommitFile, self)._initAttributes(**kwds)
            self.__additions = _rcv.Attribute("Commit.CommitFile.additions", _rcv.IntConverter, additions)
            self.__blob_url = _rcv.Attribute("Commit.CommitFile.blob_url", _rcv.StringConverter, blob_url)
            self.__changes = _rcv.Attribute("Commit.CommitFile.changes", _rcv.IntConverter, changes)
            self.__contents_url = _rcv.Attribute("Commit.CommitFile.contents_url", _rcv.StringConverter, contents_url)
            self.__deletions = _rcv.Attribute("Commit.CommitFile.deletions", _rcv.IntConverter, deletions)
            self.__filename = _rcv.Attribute("Commit.CommitFile.filename", _rcv.StringConverter, filename)
            self.__patch = _rcv.Attribute("Commit.CommitFile.patch", _rcv.StringConverter, patch)
            self.__raw_url = _rcv.Attribute("Commit.CommitFile.raw_url", _rcv.StringConverter, raw_url)
            self.__sha = _rcv.Attribute("Commit.CommitFile.sha", _rcv.StringConverter, sha)
            self.__status = _rcv.Attribute("Commit.CommitFile.status", _rcv.StringConverter, status)

        def _updateAttributes(self, additions=None, blob_url=None, changes=None, contents_url=None, deletions=None, filename=None, patch=None, raw_url=None, sha=None, status=None, **kwds):
            super(Commit.CommitFile, self)._updateAttributes(**kwds)
            self.__additions.update(additions)
            self.__blob_url.update(blob_url)
            self.__changes.update(changes)
            self.__contents_url.update(contents_url)
            self.__deletions.update(deletions)
            self.__filename.update(filename)
            self.__patch.update(patch)
            self.__raw_url.update(raw_url)
            self.__sha.update(sha)
            self.__status.update(status)

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

    class Stats(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Commit.stats`
        """

        def _initAttributes(self, additions=None, deletions=None, total=None, **kwds):
            super(Commit.Stats, self)._initAttributes(**kwds)
            self.__additions = _rcv.Attribute("Commit.Stats.additions", _rcv.IntConverter, additions)
            self.__deletions = _rcv.Attribute("Commit.Stats.deletions", _rcv.IntConverter, deletions)
            self.__total = _rcv.Attribute("Commit.Stats.total", _rcv.IntConverter, total)

        def _updateAttributes(self, additions=None, deletions=None, total=None, **kwds):
            super(Commit.Stats, self)._updateAttributes(**kwds)
            self.__additions.update(additions)
            self.__deletions.update(deletions)
            self.__total.update(total)

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

    def _initAttributes(self, author=_rcv.Absent, comments_url=_rcv.Absent, commit=_rcv.Absent, committer=_rcv.Absent, files=_rcv.Absent, html_url=_rcv.Absent, parents=_rcv.Absent, sha=_rcv.Absent, stats=_rcv.Absent, **kwds):
        import PyGithub.Blocking.GitCommit
        import PyGithub.Blocking.User
        super(Commit, self)._initAttributes(**kwds)
        self.__author = _rcv.Attribute("Commit.author", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), author)
        self.__comments_url = _rcv.Attribute("Commit.comments_url", _rcv.StringConverter, comments_url)
        self.__commit = _rcv.Attribute("Commit.commit", _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit), commit)
        self.__committer = _rcv.Attribute("Commit.committer", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), committer)
        self.__files = _rcv.Attribute("Commit.files", _rcv.ListConverter(_rcv.StructureConverter(self.Session, Commit.CommitFile)), files)
        self.__html_url = _rcv.Attribute("Commit.html_url", _rcv.StringConverter, html_url)
        self.__parents = _rcv.Attribute("Commit.parents", _rcv.ListConverter(_rcv.ClassConverter(self.Session, Commit)), parents)
        self.__sha = _rcv.Attribute("Commit.sha", _rcv.StringConverter, sha)
        self.__stats = _rcv.Attribute("Commit.stats", _rcv.StructureConverter(self.Session, Commit.Stats), stats)

    def _updateAttributes(self, eTag, author=_rcv.Absent, comments_url=_rcv.Absent, commit=_rcv.Absent, committer=_rcv.Absent, files=_rcv.Absent, html_url=_rcv.Absent, parents=_rcv.Absent, sha=_rcv.Absent, stats=_rcv.Absent, **kwds):
        super(Commit, self)._updateAttributes(eTag, **kwds)
        self.__author.update(author)
        self.__comments_url.update(comments_url)
        self.__commit.update(commit)
        self.__committer.update(committer)
        self.__files.update(files)
        self.__html_url.update(html_url)
        self.__parents.update(parents)
        self.__sha.update(sha)
        self.__stats.update(stats)

    @property
    def author(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__author.needsLazyCompletion)
        return self.__author.value

    @property
    def comments_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__comments_url.needsLazyCompletion)
        return self.__comments_url.value

    @property
    def commit(self):
        """
        :type: :class:`.GitCommit`
        """
        self._completeLazily(self.__commit.needsLazyCompletion)
        return self.__commit.value

    @property
    def committer(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__committer.needsLazyCompletion)
        return self.__committer.value

    @property
    def files(self):
        """
        :type: :class:`list` of :class:`.CommitFile`
        """
        self._completeLazily(self.__files.needsLazyCompletion)
        return self.__files.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__html_url.needsLazyCompletion)
        return self.__html_url.value

    @property
    def parents(self):
        """
        :type: :class:`list` of :class:`.Commit`
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
    def stats(self):
        """
        :type: :class:`.Stats`
        """
        self._completeLazily(self.__stats.needsLazyCompletion)
        return self.__stats.value
