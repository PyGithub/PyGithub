# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
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

import Framework
import github.OAuth


class OAuth(Framework.BasicTestCase):

    def setUp(self):
        super(OAuth, self).setUp()
        self.oauth = github.OAuth.OAuth(self.client_id, self.client_secret)

    def testAuthorizeURL(self):
        self.assertEqual(self.oauth.authorize_url(),
            "https://github.com/login/oauth/authorize?client_id=%s" % self.client_id)

    def testGetAccessToken(self):
        self.assertEqual(self.oauth.get_access_token(12345),
                         'e72e16c7e42f292c6912e7710c838347ae178b4a')
