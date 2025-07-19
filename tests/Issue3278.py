############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Zachary Haberman <6599715+interifter@users.noreply.github.com>#
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


class Organization(Framework.TestCase):
    def testIssue3278CreateTeam(self):
        super().setUp()
        team_name = "team-name"
        user_name = "interifter"
        self.user = self.g.get_user(user_name)
        self.org = self.g.get_organization("testinterifter")
        team = self.org.create_team(team_name, maintainers=[user_name])
        team = self.org.get_teams()[0]

        self.assertEqual(team_name, team.name)
        self.assertEqual(user_name, team.get_members(role="maintainer")[0].name)
