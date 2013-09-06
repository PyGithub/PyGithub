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


class File(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents Files as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def additions(self):
        """
        :type: integer
        """
        return self._NoneIfNotSet(self._additions)

    @property
    def blob_url(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._blob_url)

    @property
    def changes(self):
        """
        :type: integer
        """
        return self._NoneIfNotSet(self._changes)

    @property
    def contents_url(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._contents_url)

    @property
    def deletions(self):
        """
        :type: integer
        """
        return self._NoneIfNotSet(self._deletions)

    @property
    def filename(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._filename)

    @property
    def patch(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._patch)

    @property
    def raw_url(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._raw_url)

    @property
    def sha(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._sha)

    @property
    def status(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._status)

    def _initAttributes(self):
        self._additions = github.GithubObject.NotSet
        self._blob_url = github.GithubObject.NotSet
        self._changes = github.GithubObject.NotSet
        self._contents_url = github.GithubObject.NotSet
        self._deletions = github.GithubObject.NotSet
        self._filename = github.GithubObject.NotSet
        self._patch = github.GithubObject.NotSet
        self._raw_url = github.GithubObject.NotSet
        self._sha = github.GithubObject.NotSet
        self._status = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "additions" in attributes:  # pragma no branch
            assert attributes["additions"] is None or isinstance(attributes["additions"], (int, long)), attributes["additions"]
            self._additions = attributes["additions"]
        if "blob_url" in attributes:  # pragma no branch
            assert attributes["blob_url"] is None or isinstance(attributes["blob_url"], (str, unicode)), attributes["blob_url"]
            self._blob_url = attributes["blob_url"]
        if "changes" in attributes:  # pragma no branch
            assert attributes["changes"] is None or isinstance(attributes["changes"], (int, long)), attributes["changes"]
            self._changes = attributes["changes"]
        if "contents_url" in attributes:  # pragma no branch
            assert attributes["contents_url"] is None or isinstance(attributes["contents_url"], (str, unicode)), attributes["contents_url"]
            self._contents_url = attributes["contents_url"]
        if "deletions" in attributes:  # pragma no branch
            assert attributes["deletions"] is None or isinstance(attributes["deletions"], (int, long)), attributes["deletions"]
            self._deletions = attributes["deletions"]
        if "filename" in attributes:  # pragma no branch
            assert attributes["filename"] is None or isinstance(attributes["filename"], (str, unicode)), attributes["filename"]
            self._filename = attributes["filename"]
        if "patch" in attributes:  # pragma no branch
            assert attributes["patch"] is None or isinstance(attributes["patch"], (str, unicode)), attributes["patch"]
            self._patch = attributes["patch"]
        if "raw_url" in attributes:  # pragma no branch
            assert attributes["raw_url"] is None or isinstance(attributes["raw_url"], (str, unicode)), attributes["raw_url"]
            self._raw_url = attributes["raw_url"]
        if "sha" in attributes:  # pragma no branch
            assert attributes["sha"] is None or isinstance(attributes["sha"], (str, unicode)), attributes["sha"]
            self._sha = attributes["sha"]
        if "status" in attributes:  # pragma no branch
            assert attributes["status"] is None or isinstance(attributes["status"], (str, unicode)), attributes["status"]
            self._status = attributes["status"]
