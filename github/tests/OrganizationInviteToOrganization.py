# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2016 Benjamin Hicks <benjamin.w.hicks@gmail.com                    #
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
# #############################################################################

import Framework


class OrganizationInviteToOrganization(Framework.TestCase):

    def setUp(self):
        Framework.TestCase.setUp(self)
        self.user = self.g.get_user('benjaminwhicks')
        self.org = self.g.get_organization('AardvarkInc')

    def testInviteToOrganization(self):
        self.assertTrue(self.org.invite_to_organization(self.user))

    def testInviteToOrganizationAdmin(self):
        self.assertTrue(self.org.invite_to_organization(self.user, admin=True))
