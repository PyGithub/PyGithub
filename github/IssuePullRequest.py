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


class IssuePullRequest(GithubObject.BasicGithubObject):
    @property
    def diff_url(self):
        return self._NoneIfNotSet(self._diff_url)

    @property
    def html_url(self):
        return self._NoneIfNotSet(self._html_url)

    @property
    def patch_url(self):
        return self._NoneIfNotSet(self._patch_url)

    def _initAttributes(self):
        self._diff_url = GithubObject.NotSet
        self._html_url = GithubObject.NotSet
        self._patch_url = GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "diff_url" in attributes:  # pragma no branch
            assert attributes["diff_url"] is None or isinstance(attributes["diff_url"], (str, unicode)), attributes["diff_url"]
            self._diff_url = attributes["diff_url"]
        if "html_url" in attributes:  # pragma no branch
            assert attributes["html_url"] is None or isinstance(attributes["html_url"], (str, unicode)), attributes["html_url"]
            self._html_url = attributes["html_url"]
        if "patch_url" in attributes:  # pragma no branch
            assert attributes["patch_url"] is None or isinstance(attributes["patch_url"], (str, unicode)), attributes["patch_url"]
            self._patch_url = attributes["patch_url"]
