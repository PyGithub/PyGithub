############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>                #
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


class AccessToken(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents access tokens.
    """

    def __repr__(self):
        return self.get__repr__(
            {
                "token": f"{self.token[:5]}...",
                "scope": self.scope,
                "type": self.type,
            }
        )

    @property
    def token(self):
        """
        :type: string
        """
        return self._token.value

    @property
    def type(self):
        """
        :type: string
        """
        return self._type.value

    @property
    def scope(self):
        """
        :type: string
        """
        return self._scope.value

    def _initAttributes(self):
        self._token = github.GithubObject.NotSet
        self._type = github.GithubObject.NotSet
        self._scope = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "access_token" in attributes:  # pragma no branch
            self._token = self._makeStringAttribute(attributes["access_token"])
        if "token_type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["token_type"])
        if "scope" in attributes:  # pragma no branch
            self._scope = self._makeStringAttribute(attributes["scope"])
