############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Shibasis Patel <smartshibasish@gmail.com>                     #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
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


class Issue823(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("p-society")
        self.team = self.org.get_team(2745783)
        self.pending_invitations = self.team.invitations()

    def testGetPendingInvitationAttributes(self):
        team_url = self.pending_invitations[0].invitation_teams_url
        self.assertEqual(
            team_url,
            "https://api.github.com/organizations/29895434/invitations/6080804/teams",
        )
        inviter = self.pending_invitations[0].inviter.login
        self.assertEqual(inviter, "palash25")
        role = self.pending_invitations[0].role
        self.assertEqual(role, "direct_member")
        team_count = self.pending_invitations[0].team_count
        self.assertEqual(team_count, 1)
