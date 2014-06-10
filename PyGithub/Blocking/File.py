# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.PaginatedList
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv

import PyGithub.Blocking.GitCommit


class File(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.ContentCommit.content`
      * :meth:`.Dir.get_contents`
      * :meth:`.Repository.get_contents`
      * :meth:`.Repository.get_readme`
    """

    def _initAttributes(self, content=rcv.Absent, encoding=rcv.Absent, git_url=rcv.Absent, html_url=rcv.Absent, name=rcv.Absent, path=rcv.Absent, sha=rcv.Absent, size=rcv.Absent, type=rcv.Absent, url=rcv.Absent, _links=None, **kwds):
        super(File, self)._initAttributes(**kwds)
        self.__content = rcv.Attribute("File.content", rcv.StringConverter, content)
        self.__encoding = rcv.Attribute("File.encoding", rcv.StringConverter, encoding)
        self.__git_url = rcv.Attribute("File.git_url", rcv.StringConverter, git_url)
        self.__html_url = rcv.Attribute("File.html_url", rcv.StringConverter, html_url)
        self.__name = rcv.Attribute("File.name", rcv.StringConverter, name)
        self.__path = rcv.Attribute("File.path", rcv.StringConverter, path)
        self.__sha = rcv.Attribute("File.sha", rcv.StringConverter, sha)
        self.__size = rcv.Attribute("File.size", rcv.IntConverter, size)
        self.__type = rcv.Attribute("File.type", rcv.StringConverter, type)
        self.__url = rcv.Attribute("File.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, content=rcv.Absent, encoding=rcv.Absent, git_url=rcv.Absent, html_url=rcv.Absent, name=rcv.Absent, path=rcv.Absent, sha=rcv.Absent, size=rcv.Absent, type=rcv.Absent, url=rcv.Absent, _links=None, **kwds):
        super(File, self)._updateAttributes(eTag, **kwds)
        self.__content.update(content)
        self.__encoding.update(encoding)
        self.__git_url.update(git_url)
        self.__html_url.update(html_url)
        self.__name.update(name)
        self.__path.update(path)
        self.__sha.update(sha)
        self.__size.update(size)
        self.__type.update(type)
        self.__url.update(url)

    @property
    def content(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__content.needsLazyCompletion)
        return self.__content.value

    @property
    def encoding(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__encoding.needsLazyCompletion)
        return self.__encoding.value

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

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value

    def delete(self, message, author=None, committer=None):
        """
        Calls the `DELETE /repos/:owner/:repo/contents/:path <http://developer.github.com/v3/repos/contents#delete-a-file>`__ end point.

        This is the only method calling this end point.

        :param message: mandatory :class:`string`
        :param author: optional :class:`GitAuthor`
        :param committer: optional :class:`GitAuthor`
        :rtype: :class:`.GitCommit`
        """

        message = snd.normalizeString(message)
        if author is not None:
            author = snd.normalizeGitAuthor(author)
        if committer is not None:
            committer = snd.normalizeGitAuthor(committer)

        url = uritemplate.expand(self.url)
        postArguments = snd.dictionary(sha=self.sha, message=message, committer=committer, author=author)
        r = self.Session._request("DELETE", url, postArguments=postArguments)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit)(None, r.json()["commit"])

    def edit(self, message, content, author=None, committer=None):
        """
        Calls the `PUT /repos/:owner/:repo/contents/:path <http://developer.github.com/v3/repos/contents#update-a-file>`__ end point.

        The following methods also call this end point:
          * :meth:`.Repository.create_file`

        :param message: mandatory :class:`string`
        :param content: mandatory :class:`string`
        :param author: optional :class:`GitAuthor`
        :param committer: optional :class:`GitAuthor`
        :rtype: :class:`.GitCommit`
        """

        message = snd.normalizeString(message)
        content = snd.normalizeString(content)
        if author is not None:
            author = snd.normalizeGitAuthor(author)
        if committer is not None:
            committer = snd.normalizeGitAuthor(committer)

        url = uritemplate.expand(self.url)
        postArguments = snd.dictionary(sha=self.sha, message=message, content=content, committer=committer, author=author)
        r = self.Session._request("PUT", url, postArguments=postArguments)
        self._updateAttributes(None, **(r.json()["content"]))
        self.__content.update(content)
        return rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit)(None, r.json()["commit"])
