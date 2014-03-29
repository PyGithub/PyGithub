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

    def _initAttributes(self, git_url=rcv.Absent, html_url=rcv.Absent, name=rcv.Absent, path=rcv.Absent, sha=rcv.Absent, size=rcv.Absent, type=rcv.Absent, url=rcv.Absent, _links=None, **kwds):
        super(Dir, self)._initAttributes(**kwds)
        self.__git_url = rcv.Attribute("Dir.git_url", rcv.StringConverter, git_url)
        self.__html_url = rcv.Attribute("Dir.html_url", rcv.StringConverter, html_url)
        self.__name = rcv.Attribute("Dir.name", rcv.StringConverter, name)
        self.__path = rcv.Attribute("Dir.path", rcv.StringConverter, path)
        self.__sha = rcv.Attribute("Dir.sha", rcv.StringConverter, sha)
        self.__size = rcv.Attribute("Dir.size", rcv.IntConverter, size)
        self.__type = rcv.Attribute("Dir.type", rcv.StringConverter, type)
        self.__url = rcv.Attribute("Dir.url", rcv.StringConverter, url)

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
