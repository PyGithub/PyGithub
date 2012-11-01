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


class InputGitTreeElement(object):
    def __init__(self, path, mode, type, content=GithubObject.NotSet, sha=GithubObject.NotSet):
        self.__path = path
        self.__mode = mode
        self.__type = type
        self.__content = content
        self.__sha = sha

    @property
    def _identity(self):
        identity = {
            "path": self.__path,
            "mode": self.__mode,
            "type": self.__type,
        }
        if self.__sha is not GithubObject.NotSet:
            identity["sha"] = self.__sha
        if self.__content is not GithubObject.NotSet:
            identity["content"] = self.__content
        return identity
