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

import PyGithub.Blocking.GitCommit


class File(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.ContentCommit.content`
      * :meth:`.Dir.get_content`
      * :meth:`.Repository.get_dir_content`
      * :meth:`.Repository.get_file_content`
      * :meth:`.Repository.get_readme`
    """

    def _initAttributes(self, content=PyGithub.Blocking.Attributes.Absent, encoding=PyGithub.Blocking.Attributes.Absent, git_url=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, path=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, size=PyGithub.Blocking.Attributes.Absent, type=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, _links=None, **kwds):
        super(File, self)._initAttributes(**kwds)
        self.__content = PyGithub.Blocking.Attributes.StringAttribute("File.content", content)
        self.__encoding = PyGithub.Blocking.Attributes.StringAttribute("File.encoding", encoding)
        self.__git_url = PyGithub.Blocking.Attributes.StringAttribute("File.git_url", git_url)
        self.__html_url = PyGithub.Blocking.Attributes.StringAttribute("File.html_url", html_url)
        self.__name = PyGithub.Blocking.Attributes.StringAttribute("File.name", name)
        self.__path = PyGithub.Blocking.Attributes.StringAttribute("File.path", path)
        self.__sha = PyGithub.Blocking.Attributes.StringAttribute("File.sha", sha)
        self.__size = PyGithub.Blocking.Attributes.IntAttribute("File.size", size)
        self.__type = PyGithub.Blocking.Attributes.StringAttribute("File.type", type)
        self.__url = PyGithub.Blocking.Attributes.StringAttribute("File.url", url)

    def _updateAttributes(self, eTag, content=PyGithub.Blocking.Attributes.Absent, encoding=PyGithub.Blocking.Attributes.Absent, git_url=PyGithub.Blocking.Attributes.Absent, html_url=PyGithub.Blocking.Attributes.Absent, name=PyGithub.Blocking.Attributes.Absent, path=PyGithub.Blocking.Attributes.Absent, sha=PyGithub.Blocking.Attributes.Absent, size=PyGithub.Blocking.Attributes.Absent, type=PyGithub.Blocking.Attributes.Absent, url=PyGithub.Blocking.Attributes.Absent, _links=None, **kwds):
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

        message = PyGithub.Blocking.Parameters.normalizeString(message)
        if author is not None:
            author = PyGithub.Blocking.Parameters.normalizeGitAuthor(author)
        if committer is not None:
            committer = PyGithub.Blocking.Parameters.normalizeGitAuthor(committer)

        url = uritemplate.expand(self.url)
        postArguments = PyGithub.Blocking.Parameters.dictionary(sha=self.sha, message=message, committer=committer, author=author)
        r = self.Session._request("DELETE", url, postArguments=postArguments)
        return PyGithub.Blocking.GitCommit.GitCommit(self.Session, r.json()["commit"], None)

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

        message = PyGithub.Blocking.Parameters.normalizeString(message)
        content = PyGithub.Blocking.Parameters.normalizeString(content)
        if author is not None:
            author = PyGithub.Blocking.Parameters.normalizeGitAuthor(author)
        if committer is not None:
            committer = PyGithub.Blocking.Parameters.normalizeGitAuthor(committer)

        url = uritemplate.expand(self.url)
        postArguments = PyGithub.Blocking.Parameters.dictionary(sha=self.sha, message=message, content=content, committer=committer, author=author)
        r = self.Session._request("PUT", url, postArguments=postArguments)
        self._updateAttributes(None, **(r.json()["content"]))
        self.__content.update(content)
        return PyGithub.Blocking.GitCommit.GitCommit(self.Session, r.json()["commit"], None)
