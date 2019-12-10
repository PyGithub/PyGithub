# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Hugo <hugovk@users.noreply.github.com>                        #
# Copyright 2018 R1kk3r <R1kk3r@users.noreply.github.com>                      #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

from __future__ import absolute_import

import logging
import sys

import github

from . import Framework

python2 = sys.hexversion < 0x03000000


class Logging(Framework.BasicTestCase):
    class MockHandler:
        def __init__(self):
            self.level = logging.DEBUG
            self.handled = None

        def handle(self, record):
            self.handled = record.getMessage()

    def setUp(self):
        Framework.BasicTestCase.setUp(self)
        logger = logging.getLogger("github")
        logger.setLevel(logging.DEBUG)
        self.__handler = self.MockHandler()
        logger.addHandler(self.__handler)

    def testLoggingWithBasicAuthentication(self):
        self.assertEqual(
            github.Github(self.login, self.password).get_user().name, "Vincent Jacques"
        )

    def testLoggingWithOAuthAuthentication(self):
        self.assertEqual(
            github.Github(self.oauth_token).get_user().name, "Vincent Jacques"
        )

    def testLoggingWithoutAuthentication(self):
        self.assertEqual(github.Github().get_user("jacquev6").name, "Vincent Jacques")

    def testLoggingWithBaseUrl(self):
        # ReplayData forged, not recorded
        self.assertEqual(
            github.Github(base_url="http://my.enterprise.com/my/prefix")
            .get_user("jacquev6")
            .name,
            "Vincent Jacques",
        )
