# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

"""
Access to the session
---------------------

All objects returned by PyGithub have a :attr:`.Session` attribute. You can use it to access session-wide
information, like your `rate limit <http://developer.github.com/v3/#rate-limiting>`_ in :attr:`.RateLimit`.


Conditional requests
--------------------

Many objects returned by PyGithub have a :meth:`.update` method.
You can use it to make a `conditional request <http://developer.github.com/v3/#conditional-requests>`_.
The object's attributes will be updated, and your rate limit consumed, only if the object has changed since it
was created or last updated.
"""

import logging
log = logging.getLogger(__name__)

import PyGithub.Blocking._exceptions as _exn
import PyGithub.Blocking._receive as _rcv


class SessionedGithubObject(object):
    """
    You should not manipulate this class directly. It is public only to document its :attr:`.Session`
    attribute, but this is an implementation detail. The :attr:`.Session` attribute may be moved to another class
    or duplicated in concrete subclasses.
    """

    def __init__(self, session, attributes):
        self.__session = session
        self._initAttributes(**attributes)

    def _initAttributes(self, **kwds):
        self._logUnexpectedAttributes(kwds)

    def _updateAttributes(self, **kwds):
        self._logUnexpectedAttributes(kwds)

    def _logUnexpectedAttributes(self, unexpected):
        for name, value in unexpected.iteritems():
            log.info(self.__class__.__name__ + " received an unexpected attribute: '" + name + "' with value " + repr(value))

    @property
    def Session(self):
        """
        You can use this shared attribute to access session-wide information, like your
        `rate limit <http://developer.github.com/v3/#rate-limiting>`_ in :attr:`.RateLimit`
        """
        return self.__session


class UpdatableGithubObject(SessionedGithubObject):
    """
    You should not manipulate this class directly. It is public only to document its :meth:`.update`
    method, but this is an implementation detail. The :meth:`.update` method may be moved to another class
    or duplicated in concrete subclasses.
    """

    def __init__(self, session, attributes, eTag):
        self.__eTag = eTag
        super(UpdatableGithubObject, self).__init__(session, attributes)

    def _initAttributes(self, url=None, **kwds):
        super(UpdatableGithubObject, self)._initAttributes(**kwds)
        if url is None:
            log.warn("GitHub API v3 did not return a url")
        self.__url = _rcv.Attribute("UpdatableGithubObject.url", _rcv.StringConverter, url)

    def _updateAttributes(self, eTag, url=None, **kwds):
        super(UpdatableGithubObject, self)._updateAttributes(**kwds)
        if url is None:
            log.warn("GitHub API v3 did not return a url")
        self.__eTag = eTag
        self.__url.update(url)

    def _completeLazily(self, attributeNeedsCompletion):
        if self.__eTag is None and attributeNeedsCompletion:
            self.update()

    def update(self):
        """
        Makes a `conditional request <http://developer.github.com/v3/#conditional-requests>`_ and updates the object.

        Returns True if the the update was needed.
        """
        if self.url is None:
            raise _exn.BadAttributeException("UpdatableGithubObject.url", "basestring", None)
        r = self.Session._request("GET", self.url, headers={"If-None-Match": self.__eTag})
        if r.status_code == 304:
            return False
        else:
            self._updateAttributes(r.headers.get("ETag"), **r.json())
            return True

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self.__url.value
