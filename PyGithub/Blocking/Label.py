# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Label(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.Issue.labels`
      * :meth:`.Repository.get_label`

    Methods accepting instances of this class as parameter:
      * :meth:`.AuthenticatedUser.get_issues`
      * :meth:`.Issue.edit`
      * :meth:`.Repository.create_issue`
      * :meth:`.Repository.get_issues`
    """

    def _initAttributes(self, color=_rcv.Absent, name=_rcv.Absent, **kwds):
        super(Label, self)._initAttributes(**kwds)
        self.__color = _rcv.Attribute("Label.color", _rcv.StringConverter, color)
        self.__name = _rcv.Attribute("Label.name", _rcv.StringConverter, name)

    def _updateAttributes(self, eTag, color=_rcv.Absent, name=_rcv.Absent, **kwds):
        super(Label, self)._updateAttributes(eTag, **kwds)
        self.__color.update(color)
        self.__name.update(name)

    @property
    def color(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__color.needsLazyCompletion)
        return self.__color.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    def edit(self, name=None, color=None):
        """
        Calls the `PATCH /repos/:owner/:repo/labels/:name <http://developer.github.com/v3/issues/labels#update-a-label>`__ end point.

        This is the only method calling this end point.

        :param name: optional :class:`string`
        :param color: optional :class:`string`
        :rtype: None
        """

        if name is not None:
            name = _snd.normalizeString(name)
        if color is not None:
            color = _snd.normalizeString(color)

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(color=color, name=name)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())
