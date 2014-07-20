# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import uritemplate

import PyGithub.Blocking._base_github_object as _bgo
import PyGithub.Blocking._send as _snd
import PyGithub.Blocking._receive as _rcv


class Gist(_bgo.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.AuthenticatedUser.create_gist`
      * :meth:`.AuthenticatedUser.get_gists`
      * :meth:`.AuthenticatedUser.get_starred_gists`
      * :meth:`.Gist.create_fork`
      * :attr:`.Gist.fork_of`
      * :attr:`.Gist.forks`
      * :meth:`.Gist.get_forks`
      * :meth:`.Github.create_anonymous_gist`
      * :meth:`.Github.get_gist`
      * :meth:`.Github.get_public_gists`
      * :meth:`.User.get_gists`
    """

    class ChangeStatus(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.GistCommit.change_status`
          * :attr:`.HistoryElement.change_status`
        """

        def _initAttributes(self, additions=None, deletions=None, total=None, **kwds):
            super(Gist.ChangeStatus, self)._initAttributes(**kwds)
            self.__additions = _rcv.Attribute("Gist.ChangeStatus.additions", _rcv.IntConverter, additions)
            self.__deletions = _rcv.Attribute("Gist.ChangeStatus.deletions", _rcv.IntConverter, deletions)
            self.__total = _rcv.Attribute("Gist.ChangeStatus.total", _rcv.IntConverter, total)

        def _updateAttributes(self, additions=None, deletions=None, total=None, **kwds):
            super(Gist.ChangeStatus, self)._updateAttributes(**kwds)
            self.__additions.update(additions)
            self.__deletions.update(deletions)
            self.__total.update(total)

        @property
        def additions(self):
            """
            :type: :class:`int`
            """
            return self.__additions.value

        @property
        def deletions(self):
            """
            :type: :class:`int`
            """
            return self.__deletions.value

        @property
        def total(self):
            """
            :type: :class:`int`
            """
            return self.__total.value

    class GistCommit(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :meth:`.Gist.get_commits`
        """

        def _initAttributes(self, change_status=None, committed_at=None, url=None, user=None, version=None, **kwds):
            import PyGithub.Blocking.User
            super(Gist.GistCommit, self)._initAttributes(**kwds)
            self.__change_status = _rcv.Attribute("Gist.GistCommit.change_status", _rcv.StructureConverter(self.Session, Gist.ChangeStatus), change_status)
            self.__committed_at = _rcv.Attribute("Gist.GistCommit.committed_at", _rcv.DatetimeConverter, committed_at)
            self.__url = _rcv.Attribute("Gist.GistCommit.url", _rcv.StringConverter, url)
            self.__user = _rcv.Attribute("Gist.GistCommit.user", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), user)
            self.__version = _rcv.Attribute("Gist.GistCommit.version", _rcv.StringConverter, version)

        def _updateAttributes(self, change_status=None, committed_at=None, url=None, user=None, version=None, **kwds):
            super(Gist.GistCommit, self)._updateAttributes(**kwds)
            self.__change_status.update(change_status)
            self.__committed_at.update(committed_at)
            self.__url.update(url)
            self.__user.update(user)
            self.__version.update(version)

        @property
        def change_status(self):
            """
            :type: :class:`.ChangeStatus`
            """
            return self.__change_status.value

        @property
        def committed_at(self):
            """
            :type: :class:`datetime`
            """
            return self.__committed_at.value

        @property
        def url(self):
            """
            :type: :class:`string`
            """
            return self.__url.value

        @property
        def user(self):
            """
            :type: :class:`.User`
            """
            return self.__user.value

        @property
        def version(self):
            """
            :type: :class:`string`
            """
            return self.__version.value

    class GistFile(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Gist.files`
        """

        def _initAttributes(self, content=None, filename=None, language=None, raw_url=None, size=None, truncated=None, type=None, **kwds):
            super(Gist.GistFile, self)._initAttributes(**kwds)
            self.__content = _rcv.Attribute("Gist.GistFile.content", _rcv.StringConverter, content)
            self.__filename = _rcv.Attribute("Gist.GistFile.filename", _rcv.StringConverter, filename)
            self.__language = _rcv.Attribute("Gist.GistFile.language", _rcv.StringConverter, language)
            self.__raw_url = _rcv.Attribute("Gist.GistFile.raw_url", _rcv.StringConverter, raw_url)
            self.__size = _rcv.Attribute("Gist.GistFile.size", _rcv.IntConverter, size)
            self.__truncated = _rcv.Attribute("Gist.GistFile.truncated", _rcv.BoolConverter, truncated)
            self.__type = _rcv.Attribute("Gist.GistFile.type", _rcv.StringConverter, type)

        def _updateAttributes(self, content=None, filename=None, language=None, raw_url=None, size=None, truncated=None, type=None, **kwds):
            super(Gist.GistFile, self)._updateAttributes(**kwds)
            self.__content.update(content)
            self.__filename.update(filename)
            self.__language.update(language)
            self.__raw_url.update(raw_url)
            self.__size.update(size)
            self.__truncated.update(truncated)
            self.__type.update(type)

        @property
        def content(self):
            """
            :type: :class:`string`
            """
            return self.__content.value

        @property
        def filename(self):
            """
            :type: :class:`string`
            """
            return self.__filename.value

        @property
        def language(self):
            """
            :type: :class:`string`
            """
            return self.__language.value

        @property
        def raw_url(self):
            """
            :type: :class:`string`
            """
            return self.__raw_url.value

        @property
        def size(self):
            """
            :type: :class:`int`
            """
            return self.__size.value

        @property
        def truncated(self):
            """
            :type: :class:`bool`
            """
            return self.__truncated.value

        @property
        def type(self):
            """
            :type: :class:`string`
            """
            return self.__type.value

    class HistoryElement(_bgo.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.Gist.history`
        """

        def _initAttributes(self, change_status=None, committed_at=None, url=None, user=None, version=None, **kwds):
            import PyGithub.Blocking.User
            super(Gist.HistoryElement, self)._initAttributes(**kwds)
            self.__change_status = _rcv.Attribute("Gist.HistoryElement.change_status", _rcv.StructureConverter(self.Session, Gist.ChangeStatus), change_status)
            self.__committed_at = _rcv.Attribute("Gist.HistoryElement.committed_at", _rcv.DatetimeConverter, committed_at)
            self.__url = _rcv.Attribute("Gist.HistoryElement.url", _rcv.StringConverter, url)
            self.__user = _rcv.Attribute("Gist.HistoryElement.user", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), user)
            self.__version = _rcv.Attribute("Gist.HistoryElement.version", _rcv.StringConverter, version)

        def _updateAttributes(self, change_status=None, committed_at=None, url=None, user=None, version=None, **kwds):
            super(Gist.HistoryElement, self)._updateAttributes(**kwds)
            self.__change_status.update(change_status)
            self.__committed_at.update(committed_at)
            self.__url.update(url)
            self.__user.update(user)
            self.__version.update(version)

        @property
        def change_status(self):
            """
            :type: :class:`.ChangeStatus`
            """
            return self.__change_status.value

        @property
        def committed_at(self):
            """
            :type: :class:`datetime`
            """
            return self.__committed_at.value

        @property
        def url(self):
            """
            :type: :class:`string`
            """
            return self.__url.value

        @property
        def user(self):
            """
            :type: :class:`.User`
            """
            return self.__user.value

        @property
        def version(self):
            """
            :type: :class:`string`
            """
            return self.__version.value

    def _initAttributes(self, comments=_rcv.Absent, comments_url=_rcv.Absent, commits_url=_rcv.Absent, created_at=_rcv.Absent, description=_rcv.Absent, files=_rcv.Absent, fork_of=_rcv.Absent, forks=_rcv.Absent, forks_url=_rcv.Absent, git_pull_url=_rcv.Absent, git_push_url=_rcv.Absent, history=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, owner=_rcv.Absent, public=_rcv.Absent, updated_at=_rcv.Absent, url=_rcv.Absent, user=_rcv.Absent, **kwds):
        import PyGithub.Blocking.User
        super(Gist, self)._initAttributes(**kwds)
        self.__comments = _rcv.Attribute("Gist.comments", _rcv.IntConverter, comments)
        self.__comments_url = _rcv.Attribute("Gist.comments_url", _rcv.StringConverter, comments_url)
        self.__commits_url = _rcv.Attribute("Gist.commits_url", _rcv.StringConverter, commits_url)
        self.__created_at = _rcv.Attribute("Gist.created_at", _rcv.DatetimeConverter, created_at)
        self.__description = _rcv.Attribute("Gist.description", _rcv.StringConverter, description)
        self.__files = _rcv.Attribute("Gist.files", _rcv.DictConverter(_rcv.StringConverter, _rcv.StructureConverter(self.Session, Gist.GistFile)), files)
        self.__fork_of = _rcv.Attribute("Gist.fork_of", _rcv.ClassConverter(self.Session, Gist), fork_of)
        self.__forks = _rcv.Attribute("Gist.forks", _rcv.ListConverter(_rcv.ClassConverter(self.Session, Gist)), forks)
        self.__forks_url = _rcv.Attribute("Gist.forks_url", _rcv.StringConverter, forks_url)
        self.__git_pull_url = _rcv.Attribute("Gist.git_pull_url", _rcv.StringConverter, git_pull_url)
        self.__git_push_url = _rcv.Attribute("Gist.git_push_url", _rcv.StringConverter, git_push_url)
        self.__history = _rcv.Attribute("Gist.history", _rcv.ListConverter(_rcv.StructureConverter(self.Session, Gist.HistoryElement)), history)
        self.__html_url = _rcv.Attribute("Gist.html_url", _rcv.StringConverter, html_url)
        self.__id = _rcv.Attribute("Gist.id", _rcv.StringConverter, id)
        self.__owner = _rcv.Attribute("Gist.owner", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), owner)
        self.__public = _rcv.Attribute("Gist.public", _rcv.BoolConverter, public)
        self.__updated_at = _rcv.Attribute("Gist.updated_at", _rcv.DatetimeConverter, updated_at)
        self.__url = _rcv.Attribute("Gist.url", _rcv.StringConverter, url)
        self.__user = _rcv.Attribute("Gist.user", _rcv.ClassConverter(self.Session, PyGithub.Blocking.User.User), user)

    def _updateAttributes(self, eTag, comments=_rcv.Absent, comments_url=_rcv.Absent, commits_url=_rcv.Absent, created_at=_rcv.Absent, description=_rcv.Absent, files=_rcv.Absent, fork_of=_rcv.Absent, forks=_rcv.Absent, forks_url=_rcv.Absent, git_pull_url=_rcv.Absent, git_push_url=_rcv.Absent, history=_rcv.Absent, html_url=_rcv.Absent, id=_rcv.Absent, owner=_rcv.Absent, public=_rcv.Absent, updated_at=_rcv.Absent, url=_rcv.Absent, user=_rcv.Absent, **kwds):
        super(Gist, self)._updateAttributes(eTag, **kwds)
        self.__comments.update(comments)
        self.__comments_url.update(comments_url)
        self.__commits_url.update(commits_url)
        self.__created_at.update(created_at)
        self.__description.update(description)
        self.__files.update(files)
        self.__fork_of.update(fork_of)
        self.__forks.update(forks)
        self.__forks_url.update(forks_url)
        self.__git_pull_url.update(git_pull_url)
        self.__git_push_url.update(git_push_url)
        self.__history.update(history)
        self.__html_url.update(html_url)
        self.__id.update(id)
        self.__owner.update(owner)
        self.__public.update(public)
        self.__updated_at.update(updated_at)
        self.__url.update(url)
        self.__user.update(user)

    @property
    def comments(self):
        """
        :type: :class:`int`
        """
        self._completeLazily(self.__comments.needsLazyCompletion)
        return self.__comments.value

    @property
    def comments_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__comments_url.needsLazyCompletion)
        return self.__comments_url.value

    @property
    def commits_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__commits_url.needsLazyCompletion)
        return self.__commits_url.value

    @property
    def created_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__created_at.needsLazyCompletion)
        return self.__created_at.value

    @property
    def description(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__description.needsLazyCompletion)
        return self.__description.value

    @property
    def files(self):
        """
        :type: :class:`dict` of :class:`string` to :class:`.GistFile`
        """
        self._completeLazily(self.__files.needsLazyCompletion)
        return self.__files.value

    @property
    def fork_of(self):
        """
        :type: :class:`.Gist`
        """
        self._completeLazily(self.__fork_of.needsLazyCompletion)
        return self.__fork_of.value

    @property
    def forks(self):
        """
        :type: :class:`list` of :class:`.Gist`
        """
        self._completeLazily(self.__forks.needsLazyCompletion)
        return self.__forks.value

    @property
    def forks_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__forks_url.needsLazyCompletion)
        return self.__forks_url.value

    @property
    def git_pull_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_pull_url.needsLazyCompletion)
        return self.__git_pull_url.value

    @property
    def git_push_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__git_push_url.needsLazyCompletion)
        return self.__git_push_url.value

    @property
    def history(self):
        """
        :type: :class:`list` of :class:`.HistoryElement`
        """
        self._completeLazily(self.__history.needsLazyCompletion)
        return self.__history.value

    @property
    def html_url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__html_url.needsLazyCompletion)
        return self.__html_url.value

    @property
    def id(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__id.needsLazyCompletion)
        return self.__id.value

    @property
    def owner(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__owner.needsLazyCompletion)
        return self.__owner.value

    @property
    def public(self):
        """
        :type: :class:`bool`
        """
        self._completeLazily(self.__public.needsLazyCompletion)
        return self.__public.value

    @property
    def updated_at(self):
        """
        :type: :class:`datetime`
        """
        self._completeLazily(self.__updated_at.needsLazyCompletion)
        return self.__updated_at.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value

    @property
    def user(self):
        """
        :type: :class:`.User`
        """
        self._completeLazily(self.__user.needsLazyCompletion)
        return self.__user.value

    def create_fork(self):
        """
        Calls the `POST /gists/:id/forks <http://developer.github.com/v3/gists#fork-a-gist>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`.Gist`
        """

        url = uritemplate.expand(self.forks_url)
        r = self.Session._request("POST", url)
        return _rcv.ClassConverter(self.Session, Gist)(None, r.json(), r.headers.get("ETag"))

    def delete(self):
        """
        Calls the `DELETE /gists/:id <http://developer.github.com/v3/gists#delete-a-gist>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand(self.url)
        r = self.Session._request("DELETE", url)

    def edit(self, description=None, files=None):
        """
        Calls the `PATCH /gists/:id <http://developer.github.com/v3/gists#edit-a-gist>`__ end point.

        This is the only method calling this end point.

        :param description: optional :class:`string`
        :param files: optional :class:`bool`
        :rtype: None
        """

        if description is not None:
            description = _snd.normalizeString(description)

        url = uritemplate.expand(self.url)
        postArguments = _snd.dictionary(description=description, files=files)
        r = self.Session._request("PATCH", url, postArguments=postArguments)
        self._updateAttributes(r.headers.get("ETag"), **r.json())

    def get_commits(self, per_page=None):
        """
        Calls the `GET /gists/:id/commits <http://developer.github.com/v3/gists#list-gist-commits>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.GistCommit`
        """

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.commits_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.StructureConverter(self.Session, Gist.GistCommit))(None, r)

    def get_forks(self, per_page=None):
        """
        Calls the `GET /gists/:id/forks <http://developer.github.com/v3/gists#list-gist-forks>`__ end point.

        This is the only method calling this end point.

        :param per_page: optional :class:`int`
        :rtype: :class:`.PaginatedList` of :class:`.Gist`
        """

        if per_page is None:
            per_page = self.Session.PerPage
        else:
            per_page = _snd.normalizeInt(per_page)

        url = uritemplate.expand(self.forks_url)
        urlArguments = _snd.dictionary(per_page=per_page)
        r = self.Session._request("GET", url, urlArguments=urlArguments)
        return _rcv.PaginatedListConverter(self.Session, _rcv.ClassConverter(self.Session, Gist))(None, r)

    def is_starred(self):
        """
        Calls the `GET /gists/:id/star <http://developer.github.com/v3/gists#check-if-a-gist-is-starred>`__ end point.

        This is the only method calling this end point.

        :rtype: :class:`bool`
        """

        url = uritemplate.expand("https://api.github.com/gists/{id}/star", id=self.id)
        r = self.Session._request("GET", url, accept404=True)
        return _rcv.BoolConverter(None, r.status_code == 204)

    def reset_starred(self):
        """
        Calls the `DELETE /gists/:id/star <http://developer.github.com/v3/gists#unstar-a-gist>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand("https://api.github.com/gists/{id}/star", id=self.id)
        r = self.Session._request("DELETE", url)

    def set_starred(self):
        """
        Calls the `PUT /gists/:id/star <http://developer.github.com/v3/gists#star-a-gist>`__ end point.

        This is the only method calling this end point.

        :rtype: None
        """

        url = uritemplate.expand("https://api.github.com/gists/{id}/star", id=self.id)
        r = self.Session._request("PUT", url)
