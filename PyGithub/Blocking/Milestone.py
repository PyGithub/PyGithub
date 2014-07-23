# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Milestone(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.Issue.milestone`
      * :meth:`.Repository.get_milestone`
    """

    def _initAttributes(self, closed_issues=_rcv.Absent, created_at=_rcv.Absent, creator=_rcv.Absent, description=_rcv.Absent, due_on=_rcv.Absent, id=_rcv.Absent, labels_url=_rcv.Absent, number=_rcv.Absent, open_issues=_rcv.Absent, state=_rcv.Absent, title=_rcv.Absent, updated_at=_rcv.Absent, **kwds):
        import PyGithub.Blocking.User
        super(Milestone, self)._initAttributes(**kwds)
        self.__closed_issues = _rcv.Attribute("Milestone.closed_issues", _rcv.IntConverter, closed_issues)
        self.__created_at = _rcv.Attribute("Milestone.created_at", _rcv.DatetimeConverter, created_at)
        self.__creator = _rcv.Attribute("Milestone.creator", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), creator)
        self.__description = _rcv.Attribute("Milestone.description", _rcv.StringConverter, description)
        self.__due_on = _rcv.Attribute("Milestone.due_on", _rcv.DatetimeConverter, due_on)
        self.__id = _rcv.Attribute("Milestone.id", _rcv.IntConverter, id)
        self.__labels_url = _rcv.Attribute("Milestone.labels_url", _rcv.StringConverter, labels_url)
        self.__number = _rcv.Attribute("Milestone.number", _rcv.IntConverter, number)
        self.__open_issues = _rcv.Attribute("Milestone.open_issues", _rcv.IntConverter, open_issues)
        self.__state = _rcv.Attribute("Milestone.state", _rcv.StringConverter, state)
        self.__title = _rcv.Attribute("Milestone.title", _rcv.StringConverter, title)
        self.__updated_at = _rcv.Attribute("Milestone.updated_at", _rcv.DatetimeConverter, updated_at)

    def _updateAttributes(self, eTag, closed_issues=_rcv.Absent, created_at=_rcv.Absent, creator=_rcv.Absent, description=_rcv.Absent, due_on=_rcv.Absent, id=_rcv.Absent, labels_url=_rcv.Absent, number=_rcv.Absent, open_issues=_rcv.Absent, state=_rcv.Absent, title=_rcv.Absent, updated_at=_rcv.Absent, **kwds):
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
