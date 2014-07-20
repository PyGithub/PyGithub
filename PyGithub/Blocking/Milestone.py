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


class Milestone(bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.Issue.milestone`
      * :meth:`.Repository.get_milestone`
    """

    def _initAttributes(self, closed_issues=rcv.Absent, created_at=rcv.Absent, creator=rcv.Absent, description=rcv.Absent, due_on=rcv.Absent, id=rcv.Absent, labels_url=rcv.Absent, number=rcv.Absent, open_issues=rcv.Absent, state=rcv.Absent, title=rcv.Absent, updated_at=rcv.Absent, url=rcv.Absent, **kwds):
        import PyGithub.Blocking.User
        super(Milestone, self)._initAttributes(**kwds)
        self.__closed_issues = rcv.Attribute("Milestone.closed_issues", rcv.IntConverter, closed_issues)
        self.__created_at = rcv.Attribute("Milestone.created_at", rcv.DatetimeConverter, created_at)
        self.__creator = rcv.Attribute("Milestone.creator", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), creator)
        self.__description = rcv.Attribute("Milestone.description", rcv.StringConverter, description)
        self.__due_on = rcv.Attribute("Milestone.due_on", rcv.DatetimeConverter, due_on)
        self.__id = rcv.Attribute("Milestone.id", rcv.IntConverter, id)
        self.__labels_url = rcv.Attribute("Milestone.labels_url", rcv.StringConverter, labels_url)
        self.__number = rcv.Attribute("Milestone.number", rcv.IntConverter, number)
        self.__open_issues = rcv.Attribute("Milestone.open_issues", rcv.IntConverter, open_issues)
        self.__state = rcv.Attribute("Milestone.state", rcv.StringConverter, state)
        self.__title = rcv.Attribute("Milestone.title", rcv.StringConverter, title)
        self.__updated_at = rcv.Attribute("Milestone.updated_at", rcv.DatetimeConverter, updated_at)
        self.__url = rcv.Attribute("Milestone.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, closed_issues=rcv.Absent, created_at=rcv.Absent, creator=rcv.Absent, description=rcv.Absent, due_on=rcv.Absent, id=rcv.Absent, labels_url=rcv.Absent, number=rcv.Absent, open_issues=rcv.Absent, state=rcv.Absent, title=rcv.Absent, updated_at=rcv.Absent, url=rcv.Absent, **kwds):
        super(Milestone, self)._updateAttributes(eTag, **kwds)
        self.__closed_issues.update(closed_issues)
        self.__created_at.update(created_at)
        self.__creator.update(creator)
        self.__description.update(description)
        self.__due_on.update(due_on)
        self.__id.update(id)
        self.__labels_url.update(labels_url)
        self.__number.update(number)
        self.__open_issues.update(open_issues)
        self.__state.update(state)
        self.__title.update(title)
        self.__updated_at.update(updated_at)
        self.__url.update(url)

    @property
    def closed_issues(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__closed_issues.needsLazyCompletion)
        return self.__closed_issues.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def creator(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__creator.needsLazyCompletion)
        return self.__creator.value

    @property
    def description(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__description.needsLazyCompletion)
        return self.__description.value

    @property
    def due_on(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__due_on.needsLazyCompletion)
        return self.__due_on.value

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def labels_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__labels_url.needsLazyCompletion)
        return self.__labels_url.value

    @property
    def number(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__number.needsLazyCompletion)
        return self.__number.value

    @property
    def open_issues(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__open_issues.needsLazyCompletion)
        return self.__open_issues.value

    @property
    def state(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__state.needsLazyCompletion)
        return self.__state.value

    @property
    def title(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__title.needsLazyCompletion)
        return self.__title.value

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
