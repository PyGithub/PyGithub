# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Dir(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Dir.get_contents`
      * :meth:`.Repository.get_contents`

    Methods accepting instances of this class as parameter: none.
    """

    def _initAttributes(self, git_url=_rcv.Absent, html_url=_rcv.Absent, name=_rcv.Absent, path=_rcv.Absent, sha=_rcv.Absent, size=_rcv.Absent, type=_rcv.Absent, _links=None, **kwds):
        super(Dir, self)._initAttributes(**kwds)
        self.__git_url = _rcv.Attribute("Dir.git_url", _rcv.StringConverter, git_url)
        self.__html_url = _rcv.Attribute("Dir.html_url", _rcv.StringConverter, html_url)
        self.__name = _rcv.Attribute("Dir.name", _rcv.StringConverter, name)
        self.__path = _rcv.Attribute("Dir.path", _rcv.StringConverter, path)
        self.__sha = _rcv.Attribute("Dir.sha", _rcv.StringConverter, sha)
        self.__size = _rcv.Attribute("Dir.size", _rcv.IntConverter, size)
        self.__type = _rcv.Attribute("Dir.type", _rcv.StringConverter, type)

    def _updateAttributes(self, eTag, git_url=_rcv.Absent, html_url=_rcv.Absent, name=_rcv.Absent, path=_rcv.Absent, sha=_rcv.Absent, size=_rcv.Absent, type=_rcv.Absent, _links=None, **kwds):
        super(Dir, self)._updateAttributes(eTag, **kwds)
        self.__git_url.update(git_url)
        self.__html_url.update(html_url)
        self.__name.update(name)
        self.__path.update(path)
        self.__sha.update(sha)
        self.__size.update(size)
        self.__type.update(type)

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
    def type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__type.needsLazyCompletion)
        return self.__type.value

    def get_contents(self):
        """
        Calls the `GET /repos/:owner/:repo/contents/:path <http://developer.github.com/v3/repos/contents#get-contents>`__ end point.

        The following methods also call this end point:
          * :meth:`.Repository.get_contents`

        :rtype: :class:`list` of :class:`~.File.File` or :class:`.Dir` or :class:`.Submodule` or :class:`.SymLink`
        """
        import PyGithub.Blocking.File
        import PyGithub.Blocking.Submodule
        import PyGithub.Blocking.SymLink

        url = uritemplate.expand(self.url)
        r = self.Session._request("GET", url)
        return _rcv.ListConverter(_rcv.FileDirSubmoduleSymLinkUnionConverter(_rcv.ClassConverter(self.Session, PyGithub.Blocking.File.File), _rcv.ClassConverter(self.Session, Dir), _rcv.ClassConverter(self.Session, PyGithub.Blocking.Submodule.Submodule), _rcv.ClassConverter(self.Session, PyGithub.Blocking.SymLink.SymLink)))(None, r.json())
