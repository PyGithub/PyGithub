# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class GitRef(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.create_git_ref`
      * :meth:`.Repository.get_git_ref`
      * :meth:`.Repository.get_git_refs`
    """

    def _initAttributes(self, object=_rcv.Absent, ref=_rcv.Absent, url=_rcv.Absent, **kwds):
        import PyGithub.Blocking.GitCommit
        super(GitRef, self)._initAttributes(**kwds)
        self.__object = _rcv.Attribute("GitRef.object", _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit), object)
        self.__ref = _rcv.Attribute("GitRef.ref", _rcv.StringConverter, ref)
        self.__url = _rcv.Attribute("GitRef.url", _rcv.StringConverter, url)

    def _updateAttributes(self, eTag, object=_rcv.Absent, ref=_rcv.Absent, url=_rcv.Absent, **kwds):
        super(GitRef, self)._updateAttributes(eTag, **kwds)
        self.__object.update(object)
        self.__ref.update(ref)
        self.__url.update(url)

    @property
    def object(self):
        """
        :type: :class:`.GitCommit`
        """
        self._completeLazily(self.__object.needsLazyCompletion)
        return self.__object.value

    @property
    def ref(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__ref.needsLazyCompletion)
        return self.__ref.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value

    def delete(self):
        """
        Calls the `DELETE /repos/:owner/:repo/git/refs/:ref <http://developer.github.com/v3/git/refs#delete-a-reference>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        r = self.Session._request("DELETE", url)

    def edit(self, sha, force=None):
        """
        Calls the `PATCH /repos/:owner/:repo/git/refs/:ref <http://developer.github.com/v3/git/refs#update-a-reference>`__ end point.

        This is the only method calling this end point.

        :param sha: mandatory :class:`string`
        :param force: optional :class:`bool`
        :rtype: None
        """

        sha = _snd.normalizeString(sha)
        if force is not None:
            force = _snd.normalizeBool(force)

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(force=force, sha=sha)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())
