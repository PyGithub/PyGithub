# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Alexandre Delisle <alexodelisle@gmail.com>                    #
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


class AuthorizationOrganization(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents a credential id.
    """

    def __repr__(self):
        return self.get__repr__(
            {
                "login": self.login,
                "credential_id": self.credential_id,
                "credential_type": self.credential_type,
                "credential_authorized_at": self.credential_authorized_at,
                "credential_accessed_at": self.credential_accessed_at,
                "token_last_eight": self.token_last_eight,
                "scopes": self.scopes
            }
        )

    @property
    def login(self):
        """
        :type: string
        """
        return self._login.value

    @property
    def credential_id(self):
        """
        :type: string
        """
        return self._credential_id.value

    @property
    def credential_type(self):
        """
        :type: string
        """
        return self._credential_type.value

    @property
    def credential_authorized_at(self):
        """
        :type: string
        """
        return self._credential_authorized_at.value

    @property
    def credential_accessed_at(self):
        """
        :type: string
        """
        return self._credential_accessed_at.value

    @property
    def token_last_eight(self):
        """
        :type: string
        """
        return self._token_last_eight.value

    @property
    def scopes(self):
        """
        :type: list
        """
        return self._scopes.value

    def _initAttributes(self):
        self._login = github.GithubObject.NotSet
        self._credential_id = github.GithubObject.NotSet
        self._credential_type = github.GithubObject.NotSet
        self._credential_authorized_at = github.GithubObject.NotSet
        self._credential_accessed_at = github.GithubObject.NotSet
        self._token_last_eight = github.GithubObject.NotSet
        self._scopes = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "login" in attributes:  # pragma no branch
            self._login = self._makeStringAttribute(attributes["login"])
        if "credential_id" in attributes:  # pragma no branch
            self._credential_id = self._makeIntAttribute(attributes["credential_id"])
        if "credential_type" in attributes:  # pragma no branch
            self._credential_type = self._makeStringAttribute(attributes["credential_type"])
        if "credential_authorized_at" in attributes:  # pragma no branch
            self._credential_authorized_at = self._makeDatetimeAttribute(attributes["credential_authorized_at"])
        if "credential_accessed_at" in attributes:  # pragma no branch
            self._credential_accessed_at = self._makeDatetimeAttribute(attributes["credential_accessed_at"])
        if "token_last_eight" in attributes:  # pragma no branch
            self._token_last_eight = self._makeStringAttribute(attributes["token_last_eight"])
        if "scopes" in attributes:  # pragma no branch
            self._scopes = self._makeListOfStringsAttribute(attributes["scopes"])