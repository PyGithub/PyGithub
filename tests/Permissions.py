############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Karsten Wagner <39054096+karsten-wagner@users.noreply.github.c#
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


class Permissions(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.userRepo = self.g.get_repo("PyGithub/PyGithub")

    def testUserRepoPermissionAttributes(self):
        self.assertEqual(self.userRepo.permissions.admin, False)
        # Attribute is not present for users (only for teams)
        self.assertEqual(self.userRepo.permissions.maintain, None)
        self.assertEqual(self.userRepo.permissions.pull, True)
        self.assertEqual(self.userRepo.permissions.push, False)
        # Attribute is not present for users (only for teams)
        self.assertEqual(self.userRepo.permissions.triage, None)

    def testUserRepoPermissionRepresentation(self):
        self.assertEqual(
            repr(self.userRepo.permissions),
            "Permissions(triage=None, push=False, pull=True, maintain=None, admin=False)",
        )
