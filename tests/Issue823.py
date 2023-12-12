############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 AetherDeity <aetherdeity+github@gmail.com>                    #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Shibasis Patel <smartshibasish@gmail.com>                     #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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
