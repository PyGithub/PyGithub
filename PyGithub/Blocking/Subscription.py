# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Subscription(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.create_subscription`
      * :meth:`.AuthenticatedUser.get_subscription`
    """

    def _initAttributes(self, created_at=_rcv.Absent, ignored=_rcv.Absent, reason=_rcv.Absent, repository_url=_rcv.Absent, subscribed=_rcv.Absent, **kwds):
        super(Subscription, self)._initAttributes(**kwds)
        self.__created_at = _rcv.Attribute("Subscription.created_at", _rcv.DatetimeConverter, created_at)
        self.__ignored = _rcv.Attribute("Subscription.ignored", _rcv.BoolConverter, ignored)
        self.__reason = _rcv.Attribute("Subscription.reason", _rcv.StringConverter, reason)
        self.__repository_url = _rcv.Attribute("Subscription.repository_url", _rcv.StringConverter, repository_url)
        self.__subscribed = _rcv.Attribute("Subscription.subscribed", _rcv.BoolConverter, subscribed)

    def _updateAttributes(self, eTag, created_at=_rcv.Absent, ignored=_rcv.Absent, reason=_rcv.Absent, repository_url=_rcv.Absent, subscribed=_rcv.Absent, **kwds):
        super(Subscription, self)._updateAttributes(eTag, **kwds)
        self.__created_at.update(created_at)
        self.__ignored.update(ignored)
        self.__reason.update(reason)
        self.__repository_url.update(repository_url)
        self.__subscribed.update(subscribed)

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

        subscribed = _snd.normalizeBool(subscribed)
        ignored = _snd.normalizeBool(ignored)

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(ignored=ignored, subscribed=subscribed)
        r = self.Session._request("PUT", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())
