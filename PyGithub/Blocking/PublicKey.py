# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

########################################################################
###### This file is generated. Manual changes will likely be lost. #####
########################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.Parameters
import PyGithub.Blocking.Attributes


class PublicKey(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.create_key`
      * :meth:`.AuthenticatedUser.get_key`
      * :meth:`.AuthenticatedUser.get_keys`
      * :meth:`.Repository.create_key`
      * :meth:`.Repository.get_key`
      * :meth:`.Repository.get_keys`
      * :meth:`.User.get_keys`
    """

    def _initAttributes(self, id=PyGithub.Blocking.Attributes.Absent, key=PyGithub.Blocking.Attributes.Absent, title=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, verified=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(PublicKey, self)._initAttributes(**kwds)
        self.__id = self._createIntAttribute("PublicKey.id", id)
        self.__key = self._createStringAttribute("PublicKey.key", key)
        self.__title = self._createStringAttribute("PublicKey.title", title)
        self.__url = self._createStringAttribute("PublicKey.url", url)
        self.__verified = self._createBoolAttribute("PublicKey.verified", verified)

    def _updateAttributes(self, eTag, id=PyGithub.Blocking.Attributes.Absent, key=PyGithub.Blocking.Attributes.Absent, title=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, verified=PyGithub.Blocking.Attributes.Absent, **kwds):
        super(PublicKey, self)._updateAttributes(eTag, **kwds)
        self.__id.update(id)
        self.__key.update(key)
        self.__title.update(title)
        self.__url.update(url)
        self.__verified.update(verified)

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def key(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__key.needsLazyCompletion)
        return self.__key.value

    @property
    def title(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__title.needsLazyCompletion)
        return self.__title.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value

    @property
    def verified(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__verified.needsLazyCompletion)
        return self.__verified.value

    def delete(self):
        """
        Calls the `DELETE /repos/:owner/:repo/keys/:id <http://developer.github.com/v3/repos/keys#delete>`__ end point.

        This is the only method calling this end point.

        Calls the `DELETE /user/keys/:id <http://developer.github.com/v3/users/keys#delete-a-public-key>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        self._triggerSideEffect("DELETE", url)
