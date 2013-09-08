# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 martinqt <m.ki2@laposte.net>                                  #
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
import github.PaginatedList

import github.GitCommit
import github.NamedUser
import github.CommitStatus
import github.File
import github.CommitStats
import github.CommitComment


class Commit(github.GithubObject.CompletableGithubObject):
    """
    This class represents Commits. The reference can be found here http://developer.github.com/v3/git/commits/
    """

    @property
    def author(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._author)
        return self._NoneIfNotSet(self._author)

    @property
    def comments_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._comments_url)
        return self._NoneIfNotSet(self._comments_url)

    @property
    def commit(self):
        """
        :type: :class:`github.GitCommit.GitCommit`
        """
        self._completeIfNotSet(self._commit)
        return self._NoneIfNotSet(self._commit)

    @property
    def committer(self):
        """
        :type: :class:`github.NamedUser.NamedUser`
        """
        self._completeIfNotSet(self._committer)
        return self._NoneIfNotSet(self._committer)

    @property
    def files(self):
        """
        :type: list of :class:`github.File.File`
        """
        self._completeIfNotSet(self._files)
        return self._NoneIfNotSet(self._files)

    @property
    def html_url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def parents(self):
        """
        :type: list of :class:`github.Commit.Commit`
        """
        self._completeIfNotSet(self._parents)
        return self._NoneIfNotSet(self._parents)

    @property
    def sha(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._sha)
        return self._NoneIfNotSet(self._sha)

    @property
    def stats(self):
        """
        :type: :class:`github.CommitStats.CommitStats`
        """
        self._completeIfNotSet(self._stats)
        return self._NoneIfNotSet(self._stats)

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def create_comment(self, body, line=github.GithubObject.NotSet, path=github.GithubObject.NotSet, position=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/commits/:sha/comments <http://developer.github.com/v3/repos/comments>`_
        :param body: string
        :param line: integer
        :param path: string
        :param position: integer
        :rtype: :class:`github.CommitComment.CommitComment`
        """
        assert isinstance(body, (str, unicode)), body
        assert line is github.GithubObject.NotSet or isinstance(line, (int, long)), line
        assert path is github.GithubObject.NotSet or isinstance(path, (str, unicode)), path
        assert position is github.GithubObject.NotSet or isinstance(position, (int, long)), position
        post_parameters = {
            "body": body,
        }
        if line is not github.GithubObject.NotSet:
            post_parameters["line"] = line
        if path is not github.GithubObject.NotSet:
            post_parameters["path"] = path
        if position is not github.GithubObject.NotSet:
            post_parameters["position"] = position
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/comments",
            input=post_parameters
        )
        return github.CommitComment.CommitComment(self._requester, headers, data, completed=True)

    def create_status(self, state, target_url=github.GithubObject.NotSet, description=github.GithubObject.NotSet):
        """
        :calls: `POST /repos/:owner/:repo/statuses/:sha <http://developer.github.com/v3/repos/statuses>`_
        :param state: string
        :param target_url: string
        :param description: string
        :rtype: :class:`github.CommitStatus.CommitStatus`
        """
        assert isinstance(state, (str, unicode)), state
        assert target_url is github.GithubObject.NotSet or isinstance(target_url, (str, unicode)), target_url
        assert description is github.GithubObject.NotSet or isinstance(description, (str, unicode)), description
        post_parameters = {
            "state": state,
        }
        if target_url is not github.GithubObject.NotSet:
            post_parameters["target_url"] = target_url
        if description is not github.GithubObject.NotSet:
            post_parameters["description"] = description
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self._parentUrl(self._parentUrl(self.url)) + "/statuses/" + self.sha,
            input=post_parameters
        )
        return github.CommitStatus.CommitStatus(self._requester, headers, data, completed=True)

    def get_comments(self):
        """
        :calls: `GET /repos/:owner/:repo/commits/:sha/comments <http://developer.github.com/v3/repos/comments>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.CommitComment.CommitComment`
        """
        return github.PaginatedList.PaginatedList(
            github.CommitComment.CommitComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_statuses(self):
        """
        :calls: `GET /repos/:owner/:repo/statuses/:ref <http://developer.github.com/v3/repos/statuses>`_
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.CommitStatus.CommitStatus`
        """
        return github.PaginatedList.PaginatedList(
            github.CommitStatus.CommitStatus,
            self._requester,
            self._parentUrl(self._parentUrl(self.url)) + "/statuses/" + self.sha,
            None
        )

    @property
    def _identity(self):
        return self.sha

    def _initAttributes(self):
        self._author = github.GithubObject.NotSet
        self._comments_url = github.GithubObject.NotSet
        self._commit = github.GithubObject.NotSet
        self._committer = github.GithubObject.NotSet
        self._files = github.GithubObject.NotSet
        self._html_url = github.GithubObject.NotSet
        self._parents = github.GithubObject.NotSet
        self._sha = github.GithubObject.NotSet
        self._stats = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "author" in attributes:  # pragma no branch
            assert attributes["author"] is None or isinstance(attributes["author"], dict), attributes["author"]
            self._author = None if attributes["author"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["author"], completed=False)
        if "comments_url" in attributes:  # pragma no branch
            assert attributes["comments_url"] is None or isinstance(attributes["comments_url"], (str, unicode)), attributes["comments_url"]
            self._comments_url = attributes["comments_url"]
        if "commit" in attributes:  # pragma no branch
            assert attributes["commit"] is None or isinstance(attributes["commit"], dict), attributes["commit"]
            self._commit = None if attributes["commit"] is None else github.GitCommit.GitCommit(self._requester, self._headers, attributes["commit"], completed=False)
        if "committer" in attributes:  # pragma no branch
            assert attributes["committer"] is None or isinstance(attributes["committer"], dict), attributes["committer"]
            self._committer = None if attributes["committer"] is None else github.NamedUser.NamedUser(self._requester, self._headers, attributes["committer"], completed=False)
        if "files" in attributes:  # pragma no branch
            assert attributes["files"] is None or all(isinstance(element, dict) for element in attributes["files"]), attributes["files"]
            self._files = None if attributes["files"] is None else [
                github.File.File(self._requester, self._headers, element, completed=False)
                for element in attributes["files"]
            ]
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "parents" in attributes:  # pragma no branch
            assert attributes["parents"] is None or all(isinstance(element, dict) for element in attributes["parents"]), attributes["parents"]
            self._parents = None if attributes["parents"] is None else [
                Commit(self._requester, self._headers, element, completed=False)
                for element in attributes["parents"]
            ]
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "stats" in attributes:  # pragma no branch
            assert attributes["stats"] is None or isinstance(attributes["stats"], dict), attributes["stats"]
            self._stats = None if attributes["stats"] is None else github.CommitStats.CommitStats(self._requester, self._headers, attributes["stats"], completed=False)
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
