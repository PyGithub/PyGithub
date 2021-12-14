############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Tal Peleg <tal@polyrize.com>                                  #
# Copyright 2021 James Simpson <james@snowterminal.com>                        #
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

from . import Framework


class Organization2072(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("TestOrganization2072")

    def testGranularOrganizationContentCreationAttributes(self):
        self.assertTrue(self.org.members_can_create_public_repositories)
        self.assertTrue(self.org.members_can_create_private_repositories)
        self.assertIs(self.org.members_can_create_internal_repositories, False)
        self.assertTrue(self.org.members_can_create_public_pages)
        self.assertTrue(self.org.members_can_create_private_pages)
        self.assertEqual(self.org.members_allowed_repository_creation_type, "all")
