# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
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
# ##############################################################################

import urllib

import github.GithubObject
import github.Requester

DEFAULT_TIMEOUT = 30
DEFAULT_USER_AGENT = 'PyGithub/Python'
BASE_URL = 'https://github.com/login'
AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
TOKEN_URL = 'https://github.com/login/oauth/access_token'


class OAuth(github.GithubObject.GithubObject):
    """Implement OAuth flow for GitHub, given an application and its
    credentials.
    """

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self.requester = github.Requester.Requester(
            client_id=self.client_id, client_secret=self.client_secret,
            base_url=BASE_URL, login_or_token=None, password=None,
            timeout=DEFAULT_TIMEOUT, user_agent=DEFAULT_USER_AGENT, per_page=0)

    def authorize_url(self, **kwargs):
        """First step of the authentication process -
            Redirect user to request GitHub access.
        """
        kwargs.update({'client_id': self.client_id})
        return AUTHORIZE_URL + "?" + urllib.urlencode(kwargs)

    def get_access_token(self, code):
        """Second step of the authentication process -
            GitHub redirects back to your site.
        A temporary `code` is given after the first step is successfully
        completed. Use the code to request an access token for the user.

        """
        params = {'client_id': self.client_id,
                  'client_secret': self.client_secret,
                  'code': code
                }
        headers, data = self.requester.requestJsonAndCheck(
            verb="POST", url=TOKEN_URL, parameters=params)
        return data['data'].split('&')[0].split('=')[-1]
