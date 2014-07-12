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


class Issue(bgo.SessionedGithubObject):
    """
    Base class: :class:`.SessionedGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.get_issue`
    """

    def _initAttributes(self, assignee=rcv.Absent, body=rcv.Absent, body_html=rcv.Absent, body_text=rcv.Absent, closed_at=rcv.Absent, closed_by=rcv.Absent, comments=rcv.Absent, comments_url=rcv.Absent, created_at=rcv.Absent, events_url=rcv.Absent, html_url=rcv.Absent, id=rcv.Absent, labels=rcv.Absent, labels_url=rcv.Absent, milestone=rcv.Absent, number=rcv.Absent, state=rcv.Absent, title=rcv.Absent, updated_at=rcv.Absent, url=rcv.Absent, user=rcv.Absent, **kwds):
        import PyGithub.Blocking.Label
        import PyGithub.Blocking.Milestone
        import PyGithub.Blocking.User
        super(Issue, self)._initAttributes(**kwds)
        self.__assignee = rcv.Attribute("Issue.assignee", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), assignee)
        self.__body = rcv.Attribute("Issue.body", rcv.StringConverter, body)
        self.__body_html = rcv.Attribute("Issue.body_html", rcv.StringConverter, body_html)
        self.__body_text = rcv.Attribute("Issue.body_text", rcv.StringConverter, body_text)
        self.__closed_at = rcv.Attribute("Issue.closed_at", rcv.DatetimeConverter, closed_at)
        self.__closed_by = rcv.Attribute("Issue.closed_by", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), closed_by)
        self.__comments = rcv.Attribute("Issue.comments", rcv.IntConverter, comments)
        self.__comments_url = rcv.Attribute("Issue.comments_url", rcv.StringConverter, comments_url)
        self.__created_at = rcv.Attribute("Issue.created_at", rcv.DatetimeConverter, created_at)
        self.__events_url = rcv.Attribute("Issue.events_url", rcv.StringConverter, events_url)
        self.__html_url = rcv.Attribute("Issue.html_url", rcv.StringConverter, html_url)
        self.__id = rcv.Attribute("Issue.id", rcv.IntConverter, id)
        self.__labels = rcv.Attribute("Issue.labels", rcv.ListConverter(rcv.StructureConverter(self.Session, PyGithub.Blocking.Label.Label)), labels)
        self.__labels_url = rcv.Attribute("Issue.labels_url", rcv.StringConverter, labels_url)
        self.__milestone = rcv.Attribute("Issue.milestone", rcv.StructureConverter(self.Session, PyGithub.Blocking.Milestone.Milestone), milestone)
        self.__number = rcv.Attribute("Issue.number", rcv.IntConverter, number)
        self.__state = rcv.Attribute("Issue.state", rcv.StringConverter, state)
        self.__title = rcv.Attribute("Issue.title", rcv.StringConverter, title)
        self.__updated_at = rcv.Attribute("Issue.updated_at", rcv.DatetimeConverter, updated_at)
        self.__url = rcv.Attribute("Issue.url", rcv.StringConverter, url)
        self.__user = rcv.Attribute("Issue.user", rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), user)

    @property
    def assignee(self):
        """
        :type: :class:`.User`
        """
        return self.__assignee.value

    @property
    def body(self):
        """
        :type: :class:`string`
        """
        return self.__body.value

    @property
    def body_html(self):
        """
        :type: :class:`string`
        """
        return self.__body_html.value

    @property
    def body_text(self):
        """
        :type: :class:`string`
        """
        return self.__body_text.value

    @property
    def closed_at(self):
        """
        :type: :class:`datetime`
        """
        return self.__closed_at.value

    @property
    def closed_by(self):
        """
        :type: :class:`.User`
        """
        return self.__closed_by.value

    @property
    def comments(self):
        """
        :type: :class:`int`
        """
        return self.__comments.value

    @property
    def comments_url(self):
        """
        :type: :class:`string`
        """
        return self.__comments_url.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        return self.__created_at.value

    @property
    def events_url(self):
        """
        :type: :class:`string`
        """
        return self.__events_url.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        return self.__html_url.value

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        return self.__id.value

    @property
    def labels(self):
        """
        :type: :class:`list` of :class:`.Label`
        """
        return self.__labels.value

    @property
    def labels_url(self):
        """
        :type: :class:`string`
        """
        return self.__labels_url.value

    @property
    def milestone(self):
        """
        :type: :class:`.Milestone`
        """
        return self.__milestone.value

    @property
    def number(self):
        """
        :type: :class:`int`
        """
        return self.__number.value

    @property
    def state(self):
        """
        :type: :class:`string`
        """
        return self.__state.value

    @property
    def title(self):
        """
        :type: :class:`string`
        """
        return self.__title.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        return self.__updated_at.value

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
