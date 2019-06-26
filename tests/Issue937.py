# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Vinay Hegde <vinayhegde2010@gmail.com>                        #
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
import Framework


class Issue937(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo("PyGithub")

    def testCollaboratorsAffiliation(self):
        collaborators = self.repo.get_collaborators(affiliation='direct')
        self.assertListKeyEqual(collaborators, lambda u: u.login, ["hegde5"])
        with self.assertRaises(AssertionError):
            self.repo.get_collaborators(affiliation='invalid_option')
