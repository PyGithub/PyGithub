############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Pavan Kunisetty <nagapavan@users.noreply.github.com>          #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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


class GitMembership(Framework.TestCase):
    def testGetMembership(self):
        octocat = self.g.get_user()
        self.assertEqual(octocat.login, "octocat")
        membership_data = octocat.get_organization_membership("github")
        self.assertEqual(membership_data.user.login, "octocat")
        self.assertEqual(membership_data.role, "admin")
        self.assertEqual(membership_data.organization.login, "github")
