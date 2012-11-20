# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import GithubObject
import PaginatedList

import GitCommit
import NamedUser
import CommitStatus
import File
import CommitStats
import Commit
import CommitComment


class Commit(GithubObject.GithubObject):
    @property
    def author(self):
        self._completeIfNotSet(self._author)
        return self._NoneIfNotSet(self._author)

    @property
    def commit(self):
        self._completeIfNotSet(self._commit)
        return self._NoneIfNotSet(self._commit)

    @property
    def committer(self):
        self._completeIfNotSet(self._committer)
        return self._NoneIfNotSet(self._committer)

    @property
    def files(self):
        self._completeIfNotSet(self._files)
        return self._NoneIfNotSet(self._files)

    @property
    def parents(self):
        self._completeIfNotSet(self._parents)
        return self._NoneIfNotSet(self._parents)

    @property
    def sha(self):
        self._completeIfNotSet(self._sha)
        return self._NoneIfNotSet(self._sha)

    @property
    def stats(self):
        self._completeIfNotSet(self._stats)
        return self._NoneIfNotSet(self._stats)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def create_comment(self, body, line=GithubObject.NotSet, path=GithubObject.NotSet, position=GithubObject.NotSet):
        assert isinstance(body, (str, unicode)), body
        assert line is GithubObject.NotSet or isinstance(line, (int, long)), line
        assert path is GithubObject.NotSet or isinstance(path, (str, unicode)), path
        assert position is GithubObject.NotSet or isinstance(position, (int, long)), position
        post_parameters = {
            "body": body,
        }
        if line is not GithubObject.NotSet:
            post_parameters["line"] = line
        if path is not GithubObject.NotSet:
            post_parameters["path"] = path
        if position is not GithubObject.NotSet:
            post_parameters["position"] = position
        headers, data = self._requester.requestAndCheck(
            "POST",
            self.url + "/comments",
            None,
            post_parameters
        )
        return CommitComment.CommitComment(self._requester, data, completed=True)

    def create_status(self, state, target_url=GithubObject.NotSet, description=GithubObject.NotSet):
        assert isinstance(state, (str, unicode)), state
        assert target_url is GithubObject.NotSet or isinstance(target_url, (str, unicode)), target_url
        assert description is GithubObject.NotSet or isinstance(description, (str, unicode)), description
        post_parameters = {
            "state": state,
        }
        if target_url is not GithubObject.NotSet:
            post_parameters["target_url"] = target_url
        if description is not GithubObject.NotSet:
            post_parameters["description"] = description
        headers, data = self._requester.requestAndCheck(
            "POST",
            self._parentUrl(self._parentUrl(self.url)) + "/statuses/" + self.sha,
            None,
            post_parameters
        )
        return CommitStatus.CommitStatus(self._requester, data, completed=True)

    def get_comments(self):
        return PaginatedList.PaginatedList(
            CommitComment.CommitComment,
            self._requester,
            self.url + "/comments",
            None
        )

    def get_statuses(self):
        return PaginatedList.PaginatedList(
            CommitStatus.CommitStatus,
            self._requester,
            self._parentUrl(self._parentUrl(self.url)) + "/statuses/" + self.sha,
            None
        )

    @property
    def _identity(self):
        return self.sha

    def _initAttributes(self):
        self._author = GithubObject.NotSet
        self._commit = GithubObject.NotSet
        self._committer = GithubObject.NotSet
        self._files = GithubObject.NotSet
        self._parents = GithubObject.NotSet
        self._sha = GithubObject.NotSet
        self._stats = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "author" in attributes:  # pragma no branch
            assert attributes["author"] is None or isinstance(attributes["author"], dict), attributes["author"]
            self._author = None if attributes["author"] is None else NamedUser.NamedUser(self._requester, attributes["author"], completed=False)
        if "commit" in attributes:  # pragma no branch
            assert attributes["commit"] is None or isinstance(attributes["commit"], dict), attributes["commit"]
            self._commit = None if attributes["commit"] is None else GitCommit.GitCommit(self._requester, attributes["commit"], completed=False)
        if "committer" in attributes:  # pragma no branch
            assert attributes["committer"] is None or isinstance(attributes["committer"], dict), attributes["committer"]
            self._committer = None if attributes["committer"] is None else NamedUser.NamedUser(self._requester, attributes["committer"], completed=False)
        if "files" in attributes:  # pragma no branch
            assert attributes["files"] is None or all(isinstance(element, dict) for element in attributes["files"]), attributes["files"]
            self._files = None if attributes["files"] is None else [
                File.File(self._requester, element, completed=False)
                for element in attributes["files"]
            ]
        if "parents" in attributes:  # pragma no branch
            assert attributes["parents"] is None or all(isinstance(element, dict) for element in attributes["parents"]), attributes["parents"]
            self._parents = None if attributes["parents"] is None else [
                Commit(self._requester, element, completed=False)
                for element in attributes["parents"]
            ]
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "stats" in attributes:  # pragma no branch
            assert attributes["stats"] is None or isinstance(attributes["stats"], dict), attributes["stats"]
            self._stats = None if attributes["stats"] is None else CommitStats.CommitStats(self._requester, attributes["stats"], completed=False)
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
