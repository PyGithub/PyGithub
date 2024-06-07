############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 karthik-kadajji <60779081+karthik-kadajji@users.noreply.github.com>#
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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
from unittest.mock import Mock

import github
from github.Auth import Auth
from tests import Framework


class CustomAuth(Auth):
    @property
    def token_type(self) -> str:
        return "custom auth"

    @property
    def token(self) -> str:
        return "Custom token"

    def authentication(self, headers):
        headers["Custom key"] = self.token

    def mask_authentication(self, headers):
        headers["Custom key"] = "Masked custom header"


class Issue2971(Framework.BasicTestCase):
    def testIssue2971AddingCustomHeaders(self):
        requester = github.Github(auth=CustomAuth())._Github__requester

        def requestRaw(cnx, verb, url, requestHeaders, encoded_input):
            self.modifiedHeaders = requestHeaders
            return Mock(), {}, Mock()

        requester._Requester__requestRaw = requestRaw
        requestHeaders = {"Custom key": "secret"}
        requester._Requester__requestEncode(None, "GET", "http://github.com", None, requestHeaders, None, Mock())

        self.assertEqual("Custom token", self.modifiedHeaders["Custom key"])
