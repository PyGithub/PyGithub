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


class PublicKey(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
    """
    Base class: :class:`.SessionedGithubObject`

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
        self.__id = PyGithub.Blocking.Attributes.Attribute("PublicKey.id", PyGithub.Blocking.Attributes.IntConverter, id)
        self.__key = PyGithub.Blocking.Attributes.Attribute("PublicKey.key", PyGithub.Blocking.Attributes.StringConverter, key)
        self.__title = PyGithub.Blocking.Attributes.Attribute("PublicKey.title", PyGithub.Blocking.Attributes.StringConverter, title)
        self.__url = PyGithub.Blocking.Attributes.Attribute("PublicKey.url", PyGithub.Blocking.Attributes.StringConverter, url)
        self.__verified = PyGithub.Blocking.Attributes.Attribute("PublicKey.verified", PyGithub.Blocking.Attributes.BoolConverter, verified)

    @property
    def id(self):
        """
        :type: :class:`int`
        """
        return self.__id.value

    @property
    def key(self):
        """
        :type: :class:`string`
        """
        return self.__key.value

    @property
    def title(self):
        """
        :type: :class:`string`
        """
        return self.__title.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self.__url.value

    @property
    def verified(self):
        """
        :type: :class:`bool`
        """
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
