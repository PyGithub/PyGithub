# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class PublicKey(_bgo.UpdatableGithubObject):
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

    def _initAttributes(self, id=_rcv.Absent, key=_rcv.Absent, title=_rcv.Absent, url=_rcv.Absent, verified=_rcv.Absent, **kwds):
        super(PublicKey, self)._initAttributes(**kwds)
        self.__id = _rcv.Attribute("PublicKey.id", _rcv.IntConverter, id)
        self.__key = _rcv.Attribute("PublicKey.key", _rcv.StringConverter, key)
        self.__title = _rcv.Attribute("PublicKey.title", _rcv.StringConverter, title)
        self.__url = _rcv.Attribute("PublicKey.url", _rcv.StringConverter, url)
        self.__verified = _rcv.Attribute("PublicKey.verified", _rcv.BoolConverter, verified)

    def _updateAttributes(self, eTag, id=_rcv.Absent, key=_rcv.Absent, title=_rcv.Absent, url=_rcv.Absent, verified=_rcv.Absent, **kwds):  # pragma no cover (PublicKey are always returned fully)
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
        r = self.Session._request("DELETE", url)
