# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

########################################################################
###### This file is generated. Manual changes will likely be lost. #####
########################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.PaginatedList
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv


class Subscription(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.create_subscription`
      * :meth:`.AuthenticatedUser.get_subscription`
    """

    def _initAttributes(self, created_at=rcv.Absent, ignored=rcv.Absent, reason=rcv.Absent, repository_url=rcv.Absent, subscribed=rcv.Absent, url=rcv.Absent, **kwds):
        super(Subscription, self)._initAttributes(**kwds)
        self.__created_at = rcv.Attribute("Subscription.created_at", rcv.DatetimeConverter, created_at)
        self.__ignored = rcv.Attribute("Subscription.ignored", rcv.BoolConverter, ignored)
        self.__reason = rcv.Attribute("Subscription.reason", rcv.StringConverter, reason)
        self.__repository_url = rcv.Attribute("Subscription.repository_url", rcv.StringConverter, repository_url)
        self.__subscribed = rcv.Attribute("Subscription.subscribed", rcv.BoolConverter, subscribed)
        self.__url = rcv.Attribute("Subscription.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, created_at=rcv.Absent, ignored=rcv.Absent, reason=rcv.Absent, repository_url=rcv.Absent, subscribed=rcv.Absent, url=rcv.Absent, **kwds):
        super(Subscription, self)._updateAttributes(eTag, **kwds)
        self.__created_at.update(created_at)
        self.__ignored.update(ignored)
        self.__reason.update(reason)
        self.__repository_url.update(repository_url)
        self.__subscribed.update(subscribed)
        self.__url.update(url)

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def ignored(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__ignored.needsLazyCompletion)
        return self.__ignored.value

    @property
    def reason(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__reason.needsLazyCompletion)
        return self.__reason.value

    @property
    def repository_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__repository_url.needsLazyCompletion)
        return self.__repository_url.value

    @property
    def subscribed(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__subscribed.needsLazyCompletion)
        return self.__subscribed.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value

    def delete(self):
        """
        Calls the `DELETE /repos/:owner/:repo/subscription <http://developer.github.com/v3/activity/watching#delete-a-repository-subscription>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        r = self.Session._request("DELETE", url)

    def edit(self, subscribed, ignored):
        """
        Calls the `PUT /repos/:owner/:repo/subscription <http://developer.github.com/v3/activity/watching#set-a-repository-subscription>`__ end point.

        The following methods also call this end point:
          * :meth:`.AuthenticatedUser.create_subscription`

        :param subscribed: mandatory :class:`bool`
        :param ignored: mandatory :class:`bool`
        :rtype: None
        """

        subscribed = snd.normalizeBool(subscribed)
        ignored = snd.normalizeBool(ignored)

        url = uritemplate.expand(self.url)
        postArguments = snd.dictionary(subscribed=subscribed, ignored=ignored)
        r = self.Session._request("PUT", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())
