############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
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


class CodeownerError(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents errors in the CODEOWNERS file as used by https://docs.github.com/en/rest/repos/repos#list-codeowners-errors. The object reference can be found here https://docs.github.com/en/rest/reference/search#search-topics
    """

    def __repr__(self):
        return self.get__repr__({"message": self._message.value.split('\n')[0]})

    @property
    def line(self):
        """
        :type: int
        """
        return self._line.value

    @property
    def column(self):
        """
        :type: int
        """
        return self._column.value

    @property
    def source(self):
        """
        :type: string
        """
        return self._source.value

    @property
    def kind(self):
        """
        :type: string
        """
        return self._kind.value

    @property
    def suggestion(self):
        """
        :type: string
        """
        return self._suggestion.value

    @property
    def message(self):
        """
        :type: string
        """
        return self._message.value

    @property
    def path(self):
        """
        :type: string
        """
        return self._path.value

    def _initAttributes(self):
        self._line = github.GithubObject.NotSet
        self._column = github.GithubObject.NotSet
        self._source = github.GithubObject.NotSet
        self._kind = github.GithubObject.NotSet
        self._suggestion = github.GithubObject.NotSet
        self._message = github.GithubObject.NotSet
        self._path = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "line" in attributes:  # pragma no branch
            self._line = self._makeIntAttribute(attributes["line"])
        if "column" in attributes:  # pragma no branch
            self._column = self._makeIntAttribute(attributes["column"])
        if "source" in attributes:  # pragma no branch
            self._source = self._makeStringAttribute(attributes["source"])
        if "kind" in attributes:  # pragma no branch
            self._kind = self._makeStringAttribute(attributes["kind"])
        if "suggestion" in attributes:  # pragma no branch
            self._suggestion = self._makeStringAttribute(attributes["suggestion"])
        if "message" in attributes:  # pragma no branch
            self._message = self._makeStringAttribute(attributes["message"])
        if "path" in attributes:  # pragma no branch
            self._path = self._makeStringAttribute(attributes["path"])
