# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.github.io/PyGithub/v1/index.html                             #
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
import github


class Issue139(Framework.TestCase):  # https://github.com/jacquev6/PyGithub/issues/139
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.user = self.g.get_user().get_repo("PyGithub").get_issue(139).user

    def testCompletion(self):
        self.assertFalse(self.user._CompletableGithubObject__completed)
        self.assertEqual(self.user.name, "Ian Ozsvald")
        self.assertTrue(self.user._CompletableGithubObject__completed)
        self.assertEqual(self.user.plan, None)
