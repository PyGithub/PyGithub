# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Alexandre Delisle <alexodelisle@gmail.com>                    #
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

import github

from . import Framework


class OrganizationTeamMgmt(Framework.TestCase):

    teamName = "MyTeam"

    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("ThoughtCamera")

    def test_delete_team_by_id(self):
        self.org.create_team(name=self.teamName, privacy="closed")
        self.MyTeam = self.org.get_team_by_slug(self.teamName)
        self.assertEqual(self.MyTeam.name, self.teamName)

        self.org.remove_team(team_id=self.MyTeam.id)
        with self.assertRaises(github.UnknownObjectException):
            self.org.get_team(id=self.MyTeam.id)

    def test_delete_team_by_slug(self):
        self.org.create_team(name=self.teamName, privacy="closed")
        self.MyTeam = self.org.get_team_by_slug(self.teamName)
        self.assertEqual(self.MyTeam.name, self.teamName)

        self.assertIsNone(self.org.remove_team_by_slug(team_slug=self.MyTeam.slug))
        with self.assertRaises(github.UnknownObjectException):
            self.org.get_team_by_slug(slug=self.MyTeam.slug)

    def test_team_parent(self):
        self.org.create_team(name=self.teamName, privacy="closed")
        self.MyTeam = self.org.get_team_by_slug(self.teamName)
        self.assertEqual(self.MyTeam.name, self.teamName)

        self.org.create_team(name="ChildTeam", parent_team_id=self.MyTeam.id)
        self.assertEqual(self.org.get_team_by_slug("ChildTeam").parent, self.MyTeam)
        self.assertIsNone(self.org.remove_team_by_slug(team_slug=self.MyTeam.slug))
        with self.assertRaises(github.UnknownObjectException):
            self.org.get_team_by_slug(slug=self.MyTeam.slug)
