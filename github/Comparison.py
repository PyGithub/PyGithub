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

import Commit
import File


class Comparison(GithubObject.GithubObject):
    @property
    def ahead_by(self):
        self._completeIfNotSet(self._ahead_by)
        return self._NoneIfNotSet(self._ahead_by)

    @property
    def base_commit(self):
        self._completeIfNotSet(self._base_commit)
        return self._NoneIfNotSet(self._base_commit)

    @property
    def behind_by(self):
        self._completeIfNotSet(self._behind_by)
        return self._NoneIfNotSet(self._behind_by)

    @property
    def commits(self):
        self._completeIfNotSet(self._commits)
        return self._NoneIfNotSet(self._commits)

    @property
    def diff_url(self):
        self._completeIfNotSet(self._diff_url)
        return self._NoneIfNotSet(self._diff_url)

    @property
    def files(self):
        self._completeIfNotSet(self._files)
        return self._NoneIfNotSet(self._files)

    @property
    def html_url(self):
        self._completeIfNotSet(self._html_url)
        return self._NoneIfNotSet(self._html_url)

    @property
    def patch_url(self):
        self._completeIfNotSet(self._patch_url)
        return self._NoneIfNotSet(self._patch_url)

    @property
    def permalink_url(self):
        self._completeIfNotSet(self._permalink_url)
        return self._NoneIfNotSet(self._permalink_url)

    @property
    def status(self):
        self._completeIfNotSet(self._status)
        return self._NoneIfNotSet(self._status)

    @property
    def total_commits(self):
        self._completeIfNotSet(self._total_commits)
        return self._NoneIfNotSet(self._total_commits)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def _initAttributes(self):
        self._ahead_by = GithubObject.NotSet
        self._base_commit = GithubObject.NotSet
        self._behind_by = GithubObject.NotSet
        self._commits = GithubObject.NotSet
        self._diff_url = GithubObject.NotSet
        self._files = GithubObject.NotSet
        self._html_url = GithubObject.NotSet
        self._patch_url = GithubObject.NotSet
        self._permalink_url = GithubObject.NotSet
        self._status = GithubObject.NotSet
        self._total_commits = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "ahead_by" in attributes:  # pragma no branch
            assert attributes["ahead_by"] is None or isinstance(attributes["ahead_by"], (int, long)), attributes["ahead_by"]
            self._ahead_by = attributes["ahead_by"]
        if "base_commit" in attributes:  # pragma no branch
            assert attributes["base_commit"] is None or isinstance(attributes["base_commit"], dict), attributes["base_commit"]
            self._base_commit = None if attributes["base_commit"] is None else Commit.Commit(self._requester, attributes["base_commit"], completed=False)
        if "behind_by" in attributes:  # pragma no branch
            assert attributes["behind_by"] is None or isinstance(attributes["behind_by"], (int, long)), attributes["behind_by"]
            self._behind_by = attributes["behind_by"]
        if "commits" in attributes:  # pragma no branch
            assert attributes["commits"] is None or all(isinstance(element, dict) for element in attributes["commits"]), attributes["commits"]
            self._commits = None if attributes["commits"] is None else [
                Commit.Commit(self._requester, element, completed=False)
                for element in attributes["commits"]
            ]
        if "diff_url" in attributes:  # pragma no branch
            assert attributes["diff_url"] is None or isinstance(attributes["diff_url"], (str, unicode)), attributes["diff_url"]
            self._diff_url = attributes["diff_url"]
        if "files" in attributes:  # pragma no branch
            assert attributes["files"] is None or all(isinstance(element, dict) for element in attributes["files"]), attributes["files"]
            self._files = None if attributes["files"] is None else [
                File.File(self._requester, element, completed=False)
                for element in attributes["files"]
            ]
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "patch_url" in attributes:  # pragma no branch
            assert attributes["patch_url"] is None or isinstance(attributes["patch_url"], (str, unicode)), attributes["patch_url"]
            self._patch_url = attributes["patch_url"]
        if "permalink_url" in attributes:  # pragma no branch
            assert attributes["permalink_url"] is None or isinstance(attributes["permalink_url"], (str, unicode)), attributes["permalink_url"]
            self._permalink_url = attributes["permalink_url"]
        if "status" in attributes:  # pragma no branch
            assert attributes["status"] is None or isinstance(attributes["status"], (str, unicode)), attributes["status"]
            self._status = attributes["status"]
        if "total_commits" in attributes:  # pragma no branch
            assert attributes["total_commits"] is None or isinstance(attributes["total_commits"], (int, long)), attributes["total_commits"]
            self._total_commits = attributes["total_commits"]
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
