############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Denis Blanchette <dblanchette@coveo.com>                      #
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


class SelfHostedActionsRunnerRegistrationToken(github.GithubObject.NonCompletableGithubObject):
    def __repr__(self):
        return self.get__repr__({"expires_at": self._expires_at.value})

    @property
    def token(self):
        """
        :type: string
        """
        return self._token.value

    @property
    def expires_at(self):
        """
        :type: datetime
        """
        return self._expires_at.value

    def _initAttributes(self):
        self._token = github.GithubObject.NotSet
        self._expires_at = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "token" in attributes:
            self._token = self._makeStringAttribute(attributes["token"])
        if "expires_at" in attributes:
            self._expires_at = self._makeDatetimeAttribute(attributes["expires_at"])
