############################ Copyrights and license ############################
#                                                                              #
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

from __future__ import annotations

from . import Framework


class OrganizationInvitation(Framework.TestCase):
    def setUp(self):
        super().setUp()
        # TODO: create an instance of type OrganizationInvitation and assign to self.attr, then run:
        #   pytest tests/OrganizationInvitation.py -k testAttributes --record --auth_with_token
        #   sed -i -e "s/token private_token_removed/Basic login_and_password_removed/" tests/ReplayData/OrganizationInvitation.setUp.txt
        #   ./scripts/update-assertions.sh tests/OrganizationInvitation.py testAttributes
        self.attr = None

    def testAttributes(self):
        self.assertIsNotNone(self.attr)
        self.assertEqual(self.attr.created_at, "")
        self.assertEqual(self.attr.email, "")
        self.assertEqual(self.attr.failed_at, "")
        self.assertEqual(self.attr.failed_reason, "")
        self.assertEqual(self.attr.id, 0)
        self.assertEqual(self.attr.invitation_source, "")
        self.assertEqual(self.attr.invitation_teams_url, "")
        self.assertEqual(self.attr.inviter.login, "")
        self.assertEqual(self.attr.login, "")
        self.assertEqual(self.attr.node_id, "")
        self.assertEqual(self.attr.role, "")
        self.assertEqual(self.attr.team_count, 0)
        self.assertIsNotNone(self.attr.url)
