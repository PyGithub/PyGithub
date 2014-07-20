# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Issue(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.create_issue`
      * :meth:`.Repository.get_issue`
      * :meth:`.Repository.get_issues`
    """

    def _initAttributes(self, assignee=_rcv.Absent, body=_rcv.Absent, body_html=_rcv.Absent, body_text=_rcv.Absent, closed_at=_rcv.Absent, closed_by=_rcv.Absent, comments=_rcv.Absent, comments_url=_rcv.Absent, created_at=_rcv.Absent, events_url=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, labels=_rcv.Absent, labels_url=_rcv.Absent, milestone=_rcv.Absent, number=_rcv.Absent, state=_rcv.Absent, title=_rcv.Absent, updated_at=_rcv.Absent, url=_rcv.Absent, user=_rcv.Absent, **kwds):
        import PyGithub.Blocking.Label
        import PyGithub.Blocking.Milestone
        import PyGithub.Blocking.User
        super(Issue, self)._initAttributes(**kwds)
        self.__assignee = _rcv.Attribute("Issue.assignee", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), assignee)
        self.__body = _rcv.Attribute("Issue.body", _rcv.StringConverter, body)
        self.__body_html = _rcv.Attribute("Issue.body_html", _rcv.StringConverter, body_html)
        self.__body_text = _rcv.Attribute("Issue.body_text", _rcv.StringConverter, body_text)
        self.__closed_at = _rcv.Attribute("Issue.closed_at", _rcv.DatetimeConverter, closed_at)
        self.__closed_by = _rcv.Attribute("Issue.closed_by", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), closed_by)
        self.__comments = _rcv.Attribute("Issue.comments", _rcv.IntConverter, comments)
        self.__comments_url = _rcv.Attribute("Issue.comments_url", _rcv.StringConverter, comments_url)
        self.__created_at = _rcv.Attribute("Issue.created_at", _rcv.DatetimeConverter, created_at)
        self.__events_url = _rcv.Attribute("Issue.events_url", _rcv.StringConverter, events_url)
        self.__html_url = _rcv.Attribute("Issue.html_url", _rcv.StringConverter, html_url)
        self.__id = _rcv.Attribute("Issue.id", _rcv.IntConverter, id)
        self.__labels = _rcv.Attribute("Issue.labels", _rcv.ListConverter(_rcv.ClassConverter(self.Session, PyGithub.Blocking.Label.Label)), labels)
        self.__labels_url = _rcv.Attribute("Issue.labels_url", _rcv.StringConverter, labels_url)
        self.__milestone = _rcv.Attribute("Issue.milestone", _rcv.ClassConverter(self.Session, PyGithub.Blocking.Milestone.Milestone), milestone)
        self.__number = _rcv.Attribute("Issue.number", _rcv.IntConverter, number)
        self.__state = _rcv.Attribute("Issue.state", _rcv.StringConverter, state)
        self.__title = _rcv.Attribute("Issue.title", _rcv.StringConverter, title)
        self.__updated_at = _rcv.Attribute("Issue.updated_at", _rcv.DatetimeConverter, updated_at)
        self.__url = _rcv.Attribute("Issue.url", _rcv.StringConverter, url)
        self.__user = _rcv.Attribute("Issue.user", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), user)

    def _updateAttributes(self, eTag, assignee=_rcv.Absent, body=_rcv.Absent, body_html=_rcv.Absent, body_text=_rcv.Absent, closed_at=_rcv.Absent, closed_by=_rcv.Absent, comments=_rcv.Absent, comments_url=_rcv.Absent, created_at=_rcv.Absent, events_url=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, labels=_rcv.Absent, labels_url=_rcv.Absent, milestone=_rcv.Absent, number=_rcv.Absent, state=_rcv.Absent, title=_rcv.Absent, updated_at=_rcv.Absent, url=_rcv.Absent, user=_rcv.Absent, **kwds):
        super(Issue, self)._updateAttributes(eTag, **kwds)
        self.__assignee.update(assignee)
        self.__body.update(body)
        self.__body_html.update(body_html)
        self.__body_text.update(body_text)
        self.__closed_at.update(closed_at)
        self.__closed_by.update(closed_by)
        self.__comments.update(comments)
        self.__comments_url.update(comments_url)
        self.__created_at.update(created_at)
        self.__events_url.update(events_url)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__labels.update(labels)
        self.__labels_url.update(labels_url)
        self.__milestone.update(milestone)
        self.__number.update(number)
        self.__state.update(state)
        self.__title.update(title)
        self.__updated_at.update(updated_at)
        self.__url.update(url)
        self.__user.update(user)

    @property
    def assignee(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__assignee.needsLazyCompletion)
        return self.__assignee.value

    @property
    def body(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__body.needsLazyCompletion)
        return self.__body.value

    @property
    def body_html(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__body_html.needsLazyCompletion)
        return self.__body_html.value

    @property
    def body_text(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__body_text.needsLazyCompletion)
        return self.__body_text.value

    @property
    def closed_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__closed_at.needsLazyCompletion)
        return self.__closed_at.value

    @property
    def closed_by(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__closed_by.needsLazyCompletion)
        return self.__closed_by.value

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
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def events_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__events_url.needsLazyCompletion)
        return self.__events_url.value

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
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def labels(self):
        """
        :type: :class:`list` of :class:`.Label`
        """
        self._completeLazily(self.__labels.needsLazyCompletion)
        return self.__labels.value

    @property
    def labels_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__labels_url.needsLazyCompletion)
        return self.__labels_url.value

    @property
    def milestone(self):
        """
        :type: :class:`.Milestone`
        """
        self._completeLazily(self.__milestone.needsLazyCompletion)
        return self.__milestone.value

    @property
    def number(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__number.needsLazyCompletion)
        return self.__number.value

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

    @property
    def user(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__user.needsLazyCompletion)
        return self.__user.value

    def edit(self, title=None, body=None, assignee=None, state=None, milestone=None, labels=None):
        """
        Calls the `PATCH /repos/:owner/:repo/issues/:number <http://developer.github.com/v3/issues#edit-an-issue>`__ end point.

        This is the only method calling this end point.

        :param title: optional :class:`string`
        :param body: optional :class:`string`
        :param assignee: optional :class:`.User` or :class:`string` (its :attr:`.Entity.login`) or :class:`Reset`
        :param state: optional "closed" or "open"
        :param milestone: optional :class:`.Milestone` or :class:`int` (its :attr:`.Milestone.number`) or :class:`Reset`
        :param labels: optional :class:`list` of :class:`.Label` or :class:`string` (its :attr:`.Label.name`)
        :rtype: None
        """

        if title is not None:
            title = _snd.normalizeString(title)
        if body is not None:
            body = _snd.normalizeString(body)
        if assignee is not None:
            assignee = _snd.normalizeUserLoginReset(assignee)
        if state is not None:
            state = _snd.normalizeEnum(state, "closed", "open")
        if milestone is not None:
            milestone = _snd.normalizeMilestoneNumberReset(milestone)
        if labels is not None:
            labels = _snd.normalizeList(_snd.normalizeLabelName, labels)

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(assignee=assignee, body=body, labels=labels, milestone=milestone, state=state, title=title)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())
