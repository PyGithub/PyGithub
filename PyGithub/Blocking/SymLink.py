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


class SymLink(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Dir.get_contents`
      * :meth:`.Repository.get_contents`
    """

    def _initAttributes(self, git_url=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, path=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, size=PyGithub.Blocking.Attributes.Absent, target=PyGithub.Blocking.Attributes.Absent, type=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, _links=None, **kwds):
        super(SymLink, self)._initAttributes(**kwds)
        self.__git_url = PyGithub.Blocking.Attributes.StringAttribute("SymLink.git_url", git_url)
        self.__html_url = PyGithub.Blocking.Attributes.StringAttribute("SymLink.html_url", html_url)
        self.__name = PyGithub.Blocking.Attributes.StringAttribute("SymLink.name", name)
        self.__path = PyGithub.Blocking.Attributes.StringAttribute("SymLink.path", path)
        self.__sha = PyGithub.Blocking.Attributes.StringAttribute("SymLink.sha", sha)
        self.__size = PyGithub.Blocking.Attributes.IntAttribute("SymLink.size", size)
        self.__target = PyGithub.Blocking.Attributes.StringAttribute("SymLink.target", target)
        self.__type = PyGithub.Blocking.Attributes.StringAttribute("SymLink.type", type)
        self.__url = PyGithub.Blocking.Attributes.StringAttribute("SymLink.url", url)

    def _updateAttributes(self, eTag, git_url=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, path=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, size=PyGithub.Blocking.Attributes.Absent, target=PyGithub.Blocking.Attributes.Absent, type=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, _links=None, **kwds):
        super(SymLink, self)._updateAttributes(eTag, **kwds)
        self.__git_url.update(git_url)
        self.__html_url.update(html_url)
        self.__name.update(name)
        self.__path.update(path)
        self.__sha.update(sha)
        self.__size.update(size)
        self.__target.update(target)
        self.__type.update(type)
        self.__url.update(url)

    @property
    def git_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_url.needsLazyCompletion)
        return self.__git_url.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__html_url.needsLazyCompletion)
        return self.__html_url.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__name.needsLazyCompletion)
        return self.__name.value

    @property
    def path(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__path.needsLazyCompletion)
        return self.__path.value

    @property
    def sha(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__sha.needsLazyCompletion)
        return self.__sha.value

    @property
    def size(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__size.needsLazyCompletion)
        return self.__size.value

    @property
    def target(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__target.needsLazyCompletion)
        return self.__target.value

    @property
    def type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__type.needsLazyCompletion)
        return self.__type.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value
