############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2016 mattjmorrison <mattjmorrison@mattjmorrison.com>               #
# Copyright 2018 Isuru Fernando <isuruf@gmail.com>                             #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 James D'Amato <james.j.damato@gmail.com>                      #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Tim Boring <tboring@hearst.com>                               #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Adam Baratz <adam.baratz@gmail.com>                           #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Adrian Bridgett <58699309+tl-adrian-bridgett@users.noreply.github.com>#
# Copyright 2020 Andy Grunwald <andygrunwald@gmail.com>                        #
# Copyright 2020 Gilad Shefer <giladshefer@gmail.com>                          #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Tal Machani <12785464+talmachani@users.noreply.github.com>    #
# Copyright 2021 秋葉 <ambiguous404@gmail.com>                                   #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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


import warnings
from datetime import datetime, timezone

from . import Framework


class Team(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("BeaverSoftware")
        self.team = self.org.get_team(189850)

    def testAttributes(self):
        self.assertEqual(self.team.id, 189850)
        self.assertEqual(self.team.members_count, 0)
        self.assertEqual(self.team.name, "Team created by PyGithub")
        self.assertEqual(self.team.permission, "pull")
        self.assertEqual(self.team.repos_count, 0)
        self.assertEqual(self.team.url, "https://api.github.com/teams/189850")
        self.assertEqual(self.team.organization, self.org)
        self.assertEqual(self.team.privacy, "closed")
        self.assertEqual(self.team.parent, None)
        self.assertEqual(repr(self.team), 'Team(name="Team created by PyGithub", id=189850)')
        self.assertEqual(self.team.html_url, "https://github.com/orgs/BeaverSoftware/teams/core")

    def testDiscussions(self):
        discussions = list(self.team.get_discussions())
        self.assertEqual(len(discussions), 1)

        d = discussions[0]
        self.assertEqual(d.author.login, "jacquev6")
        self.assertEqual(d.body, "BODY")
        self.assertEqual(d.body_html, "<p>BODY</p>")
        self.assertEqual(d.body_version, "bedf0740b01d2d758cff9873c2387817")
        self.assertEqual(d.comments_count, 0)
        self.assertEqual(d.comments_url, "https://api.github.com/teams/189850/discussions/1/comments")
        self.assertEqual(d.created_at, datetime(2019, 10, 8, 21, 3, 36, tzinfo=timezone.utc))
        self.assertEqual(
            d.html_url,
            "https://github.com/orgs/BeaverSoftware/teams/Team/discussions/1",
        )
        self.assertEqual(d.last_edited_at, None)
        self.assertEqual(d.node_id, "MDE0OlRlYW1EaXNjdXNzaW9uMzA=")
        self.assertEqual(d.number, 1)
        self.assertEqual(d.pinned, True)
        self.assertEqual(d.private, False)
        self.assertEqual(d.team_url, "https://api.github.com/teams/189850")
        self.assertEqual(d.title, "TITLE")
        self.assertEqual(d.updated_at, datetime(2019, 10, 8, 21, 3, 36, tzinfo=timezone.utc))
        self.assertEqual(d.url, "https://api.github.com/teams/189850/discussions/1")
        self.assertEqual(repr(d), 'TeamDiscussion(title="TITLE", number=1)')

    def testMembers(self):
        user = self.g.get_user("jacquev6")
        self.assertListKeyEqual(self.team.get_members(), None, [])
        self.assertFalse(self.team.has_in_members(user))
        self.team.add_to_members(user)
        self.assertListKeyEqual(self.team.get_members(), lambda u: u.login, ["jacquev6"])
        self.assertTrue(self.team.has_in_members(user))
        self.team.remove_from_members(user)
        self.assertListKeyEqual(self.team.get_members(), None, [])
        self.assertFalse(self.team.has_in_members(user))
        self.team.add_membership(user, "maintainer")
        self.assertRaises(AssertionError, self.team.add_membership, user, "admin")
        self.team.remove_membership(user)

    def testTeamMembership(self):
        user = self.g.get_user("jacquev6")
        self.assertEqual(list(self.team.get_members()), [])
        self.assertFalse(self.team.has_in_members(user))
        self.team.add_membership(user)
        self.assertListKeyEqual(self.team.get_members(), lambda u: u.login, ["jacquev6"])
        self.assertTrue(self.team.has_in_members(user))
        membership_data = self.team.get_team_membership(user)
        self.assertEqual(membership_data.user.login, "jacquev6")
        self.assertEqual(membership_data.role, "member")
        self.assertEqual(membership_data.organization.login, "BeaverSoftware")

    def testRepoPermission(self):
        repo = self.org.get_repo("FatherBeaver")
        # Ignore the warning since this method is deprecated
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.team.set_repo_permission(repo, "admin")
        warnings.resetwarnings()

    def testUpdateTeamRepository(self):
        repo = self.org.get_repo("FatherBeaver")
        self.assertTrue(self.team.update_team_repository(repo, "admin"))

    def testRepos(self):
        repo = self.org.get_repo("FatherBeaver")
        self.assertListKeyEqual(self.team.get_repos(), None, [])
        self.assertFalse(self.team.has_in_repos(repo))
        self.assertIsNone(self.team.get_repo_permission(repo))
        self.team.add_to_repos(repo)
        self.assertListKeyEqual(self.team.get_repos(), lambda r: r.name, ["FatherBeaver"])
        self.assertTrue(self.team.has_in_repos(repo))
        permissions = self.team.get_repo_permission(repo)
        self.assertTrue(permissions.pull)
        self.team.remove_from_repos(repo)
        self.assertListKeyEqual(self.team.get_repos(), None, [])
        self.assertFalse(self.team.has_in_repos(repo))

    def testEditWithoutArguments(self):
        self.team.edit("Name edited by PyGithub")
        self.assertEqual(self.team.name, "Name edited by PyGithub")

    def testEditWithAllArguments(self):
        self.team.edit(
            "Name edited twice by PyGithub",
            "Description edited by PyGithub",
            "admin",
            "secret",
        )
        self.assertEqual(self.team.name, "Name edited twice by PyGithub")
        self.assertEqual(self.team.description, "Description edited by PyGithub")
        self.assertEqual(self.team.permission, "admin")
        self.assertEqual(self.team.privacy, "secret")

    def testGetTeams(self):
        nested_teams = self.team.get_teams()
        self.assertListKeyEqual(nested_teams, lambda t: t.name, ["DummyTeam1", "DummyTeam2", "DummyTeam3"])
        parent = nested_teams[0].parent
        self.assertEqual(self.team.name, parent.name)
        self.assertEqual(self.team.id, parent.id)

    def testDelete(self):
        self.team.delete()
