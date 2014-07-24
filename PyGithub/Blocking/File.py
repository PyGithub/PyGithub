# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class File(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.ContentCommit.content`
      * :meth:`.Dir.get_contents`
      * :meth:`.Repository.get_contents`
      * :meth:`.Repository.get_readme`

    Methods accepting instances of this class as parameter: none.
    """

    def _initAttributes(self, content=_rcv.Absent, encoding=_rcv.Absent, git_url=_rcv.Absent, html_url=_rcv.Absent, name=_rcv.Absent, path=_rcv.Absent, sha=_rcv.Absent, size=_rcv.Absent, type=_rcv.Absent, _links=None, **kwds):
        super(File, self)._initAttributes(**kwds)
        self.__content = _rcv.Attribute("File.content", _rcv.StringConverter, content)
        self.__encoding = _rcv.Attribute("File.encoding", _rcv.StringConverter, encoding)
        self.__git_url = _rcv.Attribute("File.git_url", _rcv.StringConverter, git_url)
        self.__html_url = _rcv.Attribute("File.html_url", _rcv.StringConverter, html_url)
        self.__name = _rcv.Attribute("File.name", _rcv.StringConverter, name)
        self.__path = _rcv.Attribute("File.path", _rcv.StringConverter, path)
        self.__sha = _rcv.Attribute("File.sha", _rcv.StringConverter, sha)
        self.__size = _rcv.Attribute("File.size", _rcv.IntConverter, size)
        self.__type = _rcv.Attribute("File.type", _rcv.StringConverter, type)

    def _updateAttributes(self, eTag, content=_rcv.Absent, encoding=_rcv.Absent, git_url=_rcv.Absent, html_url=_rcv.Absent, name=_rcv.Absent, path=_rcv.Absent, sha=_rcv.Absent, size=_rcv.Absent, type=_rcv.Absent, _links=None, **kwds):
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

    def delete(self, message, author=None, committer=None):
        """
        Calls the `DELETE /repos/:owner/:repo/contents/:path <http://developer.github.com/v3/repos/contents#delete-a-file>`__ end point.

        This is the only method calling this end point.

        :param message: mandatory :class:`string`
        :param author: optional :class:`GitAuthor`
        :param committer: optional :class:`GitAuthor`
        :rtype: :class:`.GitCommit`
        """
        import PyGithub.Blocking.GitCommit

        message = _snd.normalizeString(message)
        if author is not None:
            author = _snd.normalizeGitAuthor(author)
        if committer is not None:
            committer = _snd.normalizeGitAuthor(committer)

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(author=author, committer=committer, message=message, sha=self.sha)
        r = self.Session._request("DELETE", url, postArguments=postArguments)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit)(None, r.json()["commit"])

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
        import PyGithub.Blocking.GitCommit

        message = _snd.normalizeString(message)
        content = _snd.normalizeString(content)
        if author is not None:
            author = _snd.normalizeGitAuthor(author)
        if committer is not None:
            committer = _snd.normalizeGitAuthor(committer)

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(author=author, committer=committer, content=content, message=message, sha=self.sha)
        r = self.Session._request("PUT", url, postArguments=postArguments)
        self._updateAttributes(None, **(r.json()["content"]))
        self.__content.update(content)
        return _rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit)(None, r.json()["commit"])
