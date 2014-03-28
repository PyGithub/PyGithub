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

import PyGithub.Blocking.File
import PyGithub.Blocking.Submodule
import PyGithub.Blocking.SymLink


class Dir(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
    """
    Base class: :class:`.SessionedGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Dir.get_contents`
      * :meth:`.Repository.get_contents`
    """

    def _initAttributes(self, git_url=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, path=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, size=PyGithub.Blocking.Attributes.Absent, type=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, _links=None, **kwds):
        super(Dir, self)._initAttributes(**kwds)
        self.__git_url = PyGithub.Blocking.Attributes.Attribute("Dir.git_url", PyGithub.Blocking.Attributes.StringConverter, git_url)
        self.__html_url = PyGithub.Blocking.Attributes.Attribute("Dir.html_url", PyGithub.Blocking.Attributes.StringConverter, html_url)
        self.__name = PyGithub.Blocking.Attributes.Attribute("Dir.name", PyGithub.Blocking.Attributes.StringConverter, name)
        self.__path = PyGithub.Blocking.Attributes.Attribute("Dir.path", PyGithub.Blocking.Attributes.StringConverter, path)
        self.__sha = PyGithub.Blocking.Attributes.Attribute("Dir.sha", PyGithub.Blocking.Attributes.StringConverter, sha)
        self.__size = PyGithub.Blocking.Attributes.Attribute("Dir.size", PyGithub.Blocking.Attributes.IntConverter, size)
        self.__type = PyGithub.Blocking.Attributes.Attribute("Dir.type", PyGithub.Blocking.Attributes.StringConverter, type)
        self.__url = PyGithub.Blocking.Attributes.Attribute("Dir.url", PyGithub.Blocking.Attributes.StringConverter, url)

    @property
    def git_url(self):
        """
        :type: :class:`string`
        """
        return self.__git_url.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        return self.__html_url.value

    @property
    def name(self):
        """
        :type: :class:`string`
        """
        return self.__name.value

    @property
    def path(self):
        """
        :type: :class:`string`
        """
        return self.__path.value

    @property
    def sha(self):
        """
        :type: :class:`string`
        """
        return self.__sha.value

    @property
    def size(self):
        """
        :type: :class:`int`
        """
        return self.__size.value

    @property
    def type(self):
        """
        :type: :class:`string`
        """
        return self.__type.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self.__url.value

    def get_contents(self):
        """
        Calls the `GET /repos/:owner/:repo/contents/:path <http://developer.github.com/v3/repos/contents#get-contents>`__ end point.

        The following methods also call this end point:
          * :meth:`.Repository.get_contents`

        :rtype: :class:`list` of :class:`.File` or :class:`.Dir` or :class:`.Submodule` or :class:`.SymLink`
        """

        url = uritemplate.expand(self.url)
        r = self.Session._request("GET", url)
        ret = []
        for d in r.json():
            if d["type"] == "file" and "/git/trees/" in d["git_url"]:  # https://github.com/github/developer.github.com/commit/1b329b04cece9f3087faa7b1e0382317a9b93490
                c = PyGithub.Blocking.Submodule.Submodule(self.Session, d, None)
            elif d["type"] == "file":
                c = PyGithub.Blocking.File.File(self.Session, d, None)
            elif d["type"] == "symlink":
                c = PyGithub.Blocking.SymLink.SymLink(self.Session, d, None)
            elif d["type"] == "dir":  # pragma no branch (defensive programming)
                c = PyGithub.Blocking.Dir.Dir(self.Session, d)
            ret.append(c)
        return ret
