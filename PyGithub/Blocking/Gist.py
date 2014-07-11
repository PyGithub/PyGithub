# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.PaginatedList
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv


class Gist(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.create_gist`
      * :meth:`.Github.get_gist`
    """

    class ChangeStatus(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.HistoryElement.change_status`
        """

        def _initAttributes(self, additions=None, deletions=None, total=None, **kwds):
            super(Gist.ChangeStatus, self)._initAttributes(**kwds)
            self.__additions = rcv.Attribute("Gist.ChangeStatus.additions", rcv.IntConverter, additions)
            self.__deletions = rcv.Attribute("Gist.ChangeStatus.deletions", rcv.IntConverter, deletions)
            self.__total = rcv.Attribute("Gist.ChangeStatus.total", rcv.IntConverter, total)

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

    class HistoryElement(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Gist.history`
        """

        def _initAttributes(self, change_status=None, committed_at=None, url=None, user=None, version=None, **kwds):
            super(Gist.HistoryElement, self)._initAttributes(**kwds)
            self.__change_status = rcv.Attribute("Gist.HistoryElement.change_status", rcv.StructureConverter(self.Session, Gist.ChangeStatus), change_status)
            self.__committed_at = rcv.Attribute("Gist.HistoryElement.committed_at", rcv.DatetimeConverter, committed_at)
            self.__url = rcv.Attribute("Gist.HistoryElement.url", rcv.StringConverter, url)
            self.__user = rcv.Attribute("Gist.HistoryElement.user", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), user)
            self.__version = rcv.Attribute("Gist.HistoryElement.version", rcv.StringConverter, version)

        @property
        def change_status(self):
            """
            :type: :class:`.ChangeStatus`
            """
            return self.__change_status.value

        @property
        def committed_at(self):
            """
            :type: :class:`datetime`
            """
            return self.__committed_at.value

        @property
        def url(self):
            """
            :type: :class:`string`
            """
            return self.__url.value

        @property
        def user(self):
            """
            :type: :class:`.User`
            """
            return self.__user.value

        @property
        def version(self):
            """
            :type: :class:`string`
            """
            return self.__version.value

    def _initAttributes(self, comments=rcv.Absent, comments_url=rcv.Absent, commits_url=rcv.Absent, created_at=rcv.Absent, description=rcv.Absent, forks_url=rcv.Absent, git_pull_url=rcv.Absent, git_push_url=rcv.Absent, history=rcv.Absent, html_url=rcv.Absent, id=rcv.Absent, owner=rcv.Absent, public=rcv.Absent, updated_at=rcv.Absent, url=rcv.Absent, user=rcv.Absent, files=None, fork_of=None, forks=None, **kwds):
        import PyGithub.Blocking.User
        super(Gist, self)._initAttributes(**kwds)
        self.__comments = rcv.Attribute("Gist.comments", rcv.IntConverter, comments)
        self.__comments_url = rcv.Attribute("Gist.comments_url", rcv.StringConverter, comments_url)
        self.__commits_url = rcv.Attribute("Gist.commits_url", rcv.StringConverter, commits_url)
        self.__created_at = rcv.Attribute("Gist.created_at", rcv.DatetimeConverter, created_at)
        self.__description = rcv.Attribute("Gist.description", rcv.StringConverter, description)
        self.__forks_url = rcv.Attribute("Gist.forks_url", rcv.StringConverter, forks_url)
        self.__git_pull_url = rcv.Attribute("Gist.git_pull_url", rcv.StringConverter, git_pull_url)
        self.__git_push_url = rcv.Attribute("Gist.git_push_url", rcv.StringConverter, git_push_url)
        self.__history = rcv.Attribute("Gist.history", rcv.ListConverter(rcv.StructureConverter(self.Session, Gist.HistoryElement)), history)
        self.__html_url = rcv.Attribute("Gist.html_url", rcv.StringConverter, html_url)
        self.__id = rcv.Attribute("Gist.id", rcv.StringConverter, id)
        self.__owner = rcv.Attribute("Gist.owner", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), owner)
        self.__public = rcv.Attribute("Gist.public", rcv.BoolConverter, public)
        self.__updated_at = rcv.Attribute("Gist.updated_at", rcv.DatetimeConverter, updated_at)
        self.__url = rcv.Attribute("Gist.url", rcv.StringConverter, url)
        self.__user = rcv.Attribute("Gist.user", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), user)

    def _updateAttributes(self, eTag, comments=rcv.Absent, comments_url=rcv.Absent, commits_url=rcv.Absent, created_at=rcv.Absent, description=rcv.Absent, forks_url=rcv.Absent, git_pull_url=rcv.Absent, git_push_url=rcv.Absent, history=rcv.Absent, html_url=rcv.Absent, id=rcv.Absent, owner=rcv.Absent, public=rcv.Absent, updated_at=rcv.Absent, url=rcv.Absent, user=rcv.Absent, files=None, fork_of=None, forks=None, **kwds):
        super(Gist, self)._updateAttributes(eTag, **kwds)
        self.__comments.update(comments)
        self.__comments_url.update(comments_url)
        self.__commits_url.update(commits_url)
        self.__created_at.update(created_at)
        self.__description.update(description)
        self.__forks_url.update(forks_url)
        self.__git_pull_url.update(git_pull_url)
        self.__git_push_url.update(git_push_url)
        self.__history.update(history)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__owner.update(owner)
        self.__public.update(public)
        self.__updated_at.update(updated_at)
        self.__url.update(url)
        self.__user.update(user)

    @property
    def comments(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__comments.needsLazyCompletion)
        return self.__comments.value

    @property
    def comments_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__comments_url.needsLazyCompletion)
        return self.__comments_url.value

    @property
    def commits_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__commits_url.needsLazyCompletion)
        return self.__commits_url.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def description(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__description.needsLazyCompletion)
        return self.__description.value

    @property
    def forks_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__forks_url.needsLazyCompletion)
        return self.__forks_url.value

    @property
    def git_pull_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_pull_url.needsLazyCompletion)
        return self.__git_pull_url.value

    @property
    def git_push_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_push_url.needsLazyCompletion)
        return self.__git_push_url.value

    @property
    def history(self):
        """
        :type: :class:`list` of :class:`.HistoryElement`
        """
        self._completeLazily(self.__history.needsLazyCompletion)
        return self.__history.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__html_url.needsLazyCompletion)
        return self.__html_url.value

    @property
    def id(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def owner(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__owner.needsLazyCompletion)
        return self.__owner.value

    @property
    def public(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__public.needsLazyCompletion)
        return self.__public.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value

    @property
    def user(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__user.needsLazyCompletion)
        return self.__user.value

    def delete(self):
        """
        Calls the `DELETE /gists/:id <http://developer.github.com/v3/gists#delete-a-gist>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        r = self.Session._request("DELETE", url)
