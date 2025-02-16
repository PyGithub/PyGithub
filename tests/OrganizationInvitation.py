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
        self.org = self.g.get_organization("TestOrganization2072")
        self.invitations = list(self.org.invitations())
        self.assertGreater(len(self.invitations), 0)
        self.invitation = self.invitations[0]

    def testAttributes(self):
        self.assertIsNotNone(self.invitation)
        self.assertEqual(self.invitation.created_at, "")
        self.assertEqual(self.invitation.email, "")
        self.assertEqual(self.invitation.failed_at, "")
        self.assertEqual(self.invitation.failed_reason, "")
        self.assertEqual(self.invitation.id, 0)
        self.assertEqual(self.invitation.invitation_source, "")
        self.assertEqual(self.invitation.invitation_teams_url, "")
        self.assertEqual(self.invitation.inviter.login, "")
        self.assertEqual(self.invitation.login, "")
        self.assertEqual(self.invitation.node_id, "")
        self.assertEqual(self.invitation.role, "")
        self.assertEqual(self.invitation.team_count, 0)
        self.assertEqual(self.invitation.url, "")

    def testCancel(self):
        self.assertFalse(any([i for i in self.org.invitations() if i.email == "foo@bar.org"]))
        self.org.invite_user(email="foo@bar.org")
        self.assertTrue(any([i for i in self.org.invitations() if i.email == "foo@bar.org"]))
        invitation = [i for i in self.org.invitations() if i.email == "foo@bar.org"][0]
        self.assertTrue(self.org.cancel_invitation(invitation))
