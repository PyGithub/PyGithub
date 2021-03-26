############################ Copyrights and license ###########################
#                                                                             #
# Copyright 2019 Rigas Papathanasopoulos <rigaspapas@gmail.com>               #
#                                                                             #
# This file is part of PyGithub.                                              #
# http://pygithub.readthedocs.io/                                             #
#                                                                             #
# PyGithub is free software: you can redistribute it and/or modify it under   #
# the terms of the GNU Lesser General Public License as published by the Free #
# Software Foundation, either version 3 of the License, or (at your option)   #
# any later version.                                                          #
#                                                                             #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS   #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more#
# details.                                                                    #
#                                                                             #
# You should have received a copy of the GNU Lesser General Public License    #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.            #
#                                                                             #
###############################################################################

import urllib

import github.GithubObject
from github.AccessToken import AccessToken


class ApplicationOAuth(github.GithubObject.NonCompletableGithubObject):
    """
    This class is used for identifying and authorizing users for Github Apps.
    The reference can be found at https://docs.github.com/en/developers/apps/identifying-and-authorizing-users-for-github-apps
    """

    def __repr__(self):
        return self.get__repr__({"client_id": self._client_id.value})

    @property
    def client_id(self):
        return self._client_id.value

    @property
    def client_secret(self):
        return self._client_secret.value

    def _initAttributes(self):
        self._client_id = github.GithubObject.NotSet
        self._client_secret = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "client_id" in attributes:  # pragma no branch
            self._client_id = self._makeStringAttribute(attributes["client_id"])
        if "client_secret" in attributes:  # pragma no branch
            self._client_secret = self._makeStringAttribute(attributes["client_secret"])

    def get_login_url(self, redirect_uri=None, state=None, login=None):
        """
        Return the URL you need to redirect a user to in order to authorize
        your App.
        :type: string
        """
        parameters = {"client_id": self.client_id}
        if redirect_uri is not None:
            assert isinstance(redirect_uri, str), redirect_uri
            parameters["redirect_uri"] = redirect_uri
        if state is not None:
            assert isinstance(state, str), state
            parameters["state"] = state
        if login is not None:
            assert isinstance(login, str), login
            parameters["login"] = login

        parameters = urllib.parse.urlencode(parameters)

        base_url = "https://github.com/login/oauth/authorize"
        return f"{base_url}?{parameters}"

    def get_access_token(self, code, state=None):
        """
        :calls: `POST /login/oauth/access_token <https://docs.github.com/en/developers/apps/identifying-and-authorizing-users-for-github-apps>`_
        :param code: string
        :param state: string
        """
        assert isinstance(code, str), code
        post_parameters = {
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        if state is not None:
            post_parameters["state"] = state

        self._requester._Requester__authorizationHeader = None
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            "https://github.com/login/oauth/access_token",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "PyGithub/Python",
            },
            input=post_parameters,
        )

        return AccessToken(
            requester=self._requester,
            # not required, this is a NonCompletableGithubObject
            headers={},
            attributes=data,
            completed=False,
        )
