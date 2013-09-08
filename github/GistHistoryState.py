# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import github.GithubObject

import github.NamedUser
import github.CommitStats
import github.Gist


class GistHistoryState(github.GithubObject.CompletableGithubObject):
    """
    This class represents GistHistoryStates as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def change_status(self):
        """
        :type: :class:`github.CommitStats.CommitStats`
        """
        self._completeIfNotSet(self._change_status)
        return self._NoneIfNotSet(self._change_status)

    @property
    def comments(self):
        """
        :type: integer
        """
        self._completeIfNotSet(self._comments)
        return self._NoneIfNotSet(self._comments)

    @property
    def comments_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._comments_url)
        return self._NoneIfNotSet(self._comments_url)

    @property
    def commits_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._commits_url)
        return self._NoneIfNotSet(self._commits_url)

    @property
    def committed_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._committed_at)
        return self._NoneIfNotSet(self._committed_at)

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def description(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._description)
        return self._NoneIfNotSet(self._description)

    @property
    def files(self):
        """
        :type: dict of string to :class:`github.GistFile.GistFile`
        """
        self._completeIfNotSet(self._files)
        return self._NoneIfNotSet(self._files)

    @property
    def forks(self):
        """
        :type: list of :class:`github.Gist.Gist`
        """
        self._completeIfNotSet(self._forks)
        return self._NoneIfNotSet(self._forks)

    @property
    def forks_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._forks_url)
        return self._NoneIfNotSet(self._forks_url)

    @property
    def git_pull_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._git_pull_url)
        return self._NoneIfNotSet(self._git_pull_url)

    @property
    def git_push_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._git_push_url)
        return self._NoneIfNotSet(self._git_push_url)

    @property
    def history(self):
        """
        :type: list of :class:`GistHistoryState`
        """
        self._completeIfNotSet(self._history)
        return self._NoneIfNotSet(self._history)

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def id(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def public(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._public)
        return self._NoneIfNotSet(self._public)

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._NoneIfNotSet(self._updated_at)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    @property
    def user(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._user)
        return self._NoneIfNotSet(self._user)

    @property
    def version(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._version)
        return self._NoneIfNotSet(self._version)

    def _initAttributes(self):
        self._change_status = github.GithubObject.NotSet
        self._comments = github.GithubObject.NotSet
        self._comments_url = github.GithubObject.NotSet
        self._commits_url = github.GithubObject.NotSet
        self._committed_at = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._description = github.GithubObject.NotSet
        self._files = github.GithubObject.NotSet
        self._forks = github.GithubObject.NotSet
        self._forks_url = github.GithubObject.NotSet
        self._git_pull_url = github.GithubObject.NotSet
        self._git_push_url = github.GithubObject.NotSet
        self._history = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._public = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._user = github.GithubObject.NotSet
        self._version = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "change_status" in attributes:  # pragma no branch
            assert attributes["change_status"] is None or isinstance(attributes["change_status"], dict), attributes["change_status"]
            self._change_status = None if attributes["change_status"] is None else github.CommitStats.CommitStats(self._requester, self._headers, attributes["change_status"], completed=False)
        if "comments" in attributes:  # pragma no branch
            assert attributes["comments"] is None or isinstance(attributes["comments"], (int, long)), attributes["comments"]
            self._comments = attributes["comments"]
        if "comments_url" in attributes:  # pragma no branch
            assert attributes["comments_url"] is None or isinstance(attributes["comments_url"], (str, unicode)), attributes["comments_url"]
            self._comments_url = attributes["comments_url"]
        if "commits_url" in attributes:  # pragma no branch
            assert attributes["commits_url"] is None or isinstance(attributes["commits_url"], (str, unicode)), attributes["commits_url"]
            self._commits_url = attributes["commits_url"]
        if "committed_at" in attributes:  # pragma no branch
            assert attributes["committed_at"] is None or isinstance(attributes["committed_at"], (str, unicode)), attributes["committed_at"]
            self._committed_at = self._parseDatetime(attributes["committed_at"])
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "description" in attributes:  # pragma no branch
            assert attributes["description"] is None or isinstance(attributes["description"], (str, unicode)), attributes["description"]
            self._description = attributes["description"]
        if "files" in attributes:  # pragma no branch
            assert attributes["files"] is None or all(isinstance(element, dict) for element in attributes["files"].itervalues()), attributes["files"]
            self._files = None if attributes["files"] is None else dict(
                (key, github.GistFile.GistFile(self._requester, self._headers, element, completed=False))
                for key, element in attributes["files"].iteritems()
            )
        if "forks" in attributes:  # pragma no branch
            assert attributes["forks"] is None or all(isinstance(element, dict) for element in attributes["forks"]), attributes["forks"]
            self._forks = None if attributes["forks"] is None else [
                github.Gist.Gist(self._requester, self._headers, element, completed=False)
                for element in attributes["forks"]
            ]
        if "forks_url" in attributes:  # pragma no branch
            assert attributes["forks_url"] is None or isinstance(attributes["forks_url"], (str, unicode)), attributes["forks_url"]
            self._forks_url = attributes["forks_url"]
        if "git_pull_url" in attributes:  # pragma no branch
            assert attributes["git_pull_url"] is None or isinstance(attributes["git_pull_url"], (str, unicode)), attributes["git_pull_url"]
            self._git_pull_url = attributes["git_pull_url"]
        if "git_push_url" in attributes:  # pragma no branch
            assert attributes["git_push_url"] is None or isinstance(attributes["git_push_url"], (str, unicode)), attributes["git_push_url"]
            self._git_push_url = attributes["git_push_url"]
        if "history" in attributes:  # pragma no branch
            assert attributes["history"] is None or all(isinstance(element, dict) for element in attributes["history"]), attributes["history"]
            self._history = None if attributes["history"] is None else [
                GistHistoryState(self._requester, self._headers, element, completed=False)
                for element in attributes["history"]
            ]
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (str, unicode)), attributes["id"]
            self._id = attributes["id"]
        if "public" in attributes:  # pragma no branch
            assert attributes["public"] is None or isinstance(attributes["public"], bool), attributes["public"]
            self._public = attributes["public"]
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
        if "user" in attributes:  # pragma no branch
            assert attributes["user"] is None or isinstance(attributes["user"], dict), attributes["user"]
            self._user = None if attributes["user"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["user"], completed=False)
        if "version" in attributes:  # pragma no branch
            assert attributes["version"] is None or isinstance(attributes["version"], (str, unicode)), attributes["version"]
            self._version = attributes["version"]
