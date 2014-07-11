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

    def _initAttributes(self, comments=rcv.Absent, comments_url=rcv.Absent, commits_url=rcv.Absent, created_at=rcv.Absent, description=rcv.Absent, forks_url=rcv.Absent, git_pull_url=rcv.Absent, git_push_url=rcv.Absent, html_url=rcv.Absent, id=rcv.Absent, public=rcv.Absent, updated_at=rcv.Absent, url=rcv.Absent, files=None, fork_of=None, forks=None, history=None, owner=None, user=None, **kwds):
        super(Gist, self)._initAttributes(**kwds)
        self.__comments = rcv.Attribute("Gist.comments", rcv.IntConverter, comments)
        self.__comments_url = rcv.Attribute("Gist.comments_url", rcv.StringConverter, comments_url)
        self.__commits_url = rcv.Attribute("Gist.commits_url", rcv.StringConverter, commits_url)
        self.__created_at = rcv.Attribute("Gist.created_at", rcv.DatetimeConverter, created_at)
        self.__description = rcv.Attribute("Gist.description", rcv.StringConverter, description)
        self.__forks_url = rcv.Attribute("Gist.forks_url", rcv.StringConverter, forks_url)
        self.__git_pull_url = rcv.Attribute("Gist.git_pull_url", rcv.StringConverter, git_pull_url)
        self.__git_push_url = rcv.Attribute("Gist.git_push_url", rcv.StringConverter, git_push_url)
        self.__html_url = rcv.Attribute("Gist.html_url", rcv.StringConverter, html_url)
        self.__id = rcv.Attribute("Gist.id", rcv.StringConverter, id)
        self.__public = rcv.Attribute("Gist.public", rcv.BoolConverter, public)
        self.__updated_at = rcv.Attribute("Gist.updated_at", rcv.DatetimeConverter, updated_at)
        self.__url = rcv.Attribute("Gist.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, comments=rcv.Absent, comments_url=rcv.Absent, commits_url=rcv.Absent, created_at=rcv.Absent, description=rcv.Absent, forks_url=rcv.Absent, git_pull_url=rcv.Absent, git_push_url=rcv.Absent, html_url=rcv.Absent, id=rcv.Absent, public=rcv.Absent, updated_at=rcv.Absent, url=rcv.Absent, files=None, fork_of=None, forks=None, history=None, owner=None, user=None, **kwds):
        super(Gist, self)._updateAttributes(eTag, **kwds)
        self.__comments.update(comments)
        self.__comments_url.update(comments_url)
        self.__commits_url.update(commits_url)
        self.__created_at.update(created_at)
        self.__description.update(description)
        self.__forks_url.update(forks_url)
        self.__git_pull_url.update(git_pull_url)
        self.__git_push_url.update(git_push_url)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__public.update(public)
        self.__updated_at.update(updated_at)
        self.__url.update(url)

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

    def delete(self):
        """
        Calls the `DELETE /gists/:id <http://developer.github.com/v3/gists#delete-a-gist>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        r = self.Session._request("DELETE", url)
