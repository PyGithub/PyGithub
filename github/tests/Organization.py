# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Balázs Rostás <rostas.balazs@gmail.com>                     #
# Copyright 2018 Anton Nguyen <afnguyen85@gmail.com>                           #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

import Framework

import datetime


class Organization(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.org = self.g.get_organization("BeaverSoftware")

    def testAttributes(self):
        self.assertEqual(self.org.avatar_url, "https://avatars1.githubusercontent.com/u/1?v=4")
        self.assertEqual(self.org.billing_email, "foo@example.com")
        self.assertEqual(self.org.blog, "http://www.example.com")
        self.assertEqual(self.org.collaborators, 9)
        self.assertEqual(self.org.company, None)
        self.assertEqual(self.org.created_at, datetime.datetime(2014, 1, 9, 16, 56, 17))
        self.assertEqual(self.org.disk_usage, 2)
        self.assertEqual(self.org.email, '')
        self.assertEqual(self.org.followers, 0)
        self.assertEqual(self.org.following, 0)
        self.assertEqual(self.org.gravatar_id, None)
        self.assertEqual(self.org.html_url, "https://github.com/BeaverSoftware")
        self.assertEqual(self.org.id, 1)
        self.assertEqual(self.org.location, "Paris, France")
        self.assertEqual(self.org.login, "BeaverSoftware")
        self.assertEqual(self.org.name, "BeaverSoftware")
        self.assertEqual(self.org.owned_private_repos, 0)
        self.assertEqual(self.org.plan.name, "free")
        self.assertEqual(self.org.plan.private_repos, 3)
        self.assertEqual(self.org.plan.space, 1)
        self.assertEqual(self.org.private_gists, 0)
        self.assertEqual(self.org.public_gists, 0)
        self.assertEqual(self.org.public_repos, 27)
        self.assertEqual(self.org.total_private_repos, 7)
        self.assertEqual(self.org.type, "Organization")
        self.assertEqual(self.org.url, "https://api.github.com/orgs/BeaverSoftware")

        # test __repr__() based on this attributes
        self.assertEqual(self.org.__repr__(), 'Organization(name="BeaverSoftware", id=1)')

    def testAddMembersDefaultRole(self):
        lyloa = self.g.get_user("lyloa")
        self.assertFalse(self.org.has_in_members(lyloa))
        self.org.add_to_members(lyloa, role='member')
        # 'Pending' members won't be in /orgs/:org/members/:user
        self.assertFalse(self.org.has_in_members(lyloa))
        self.org.remove_from_membership(lyloa)
        self.assertFalse(self.org.has_in_members(lyloa))

    def testAddMembersAdminRole(self):
        lyloa = self.g.get_user("lyloa")
        self.assertFalse(self.org.has_in_members(lyloa))
        self.org.add_to_members(lyloa, role='admin')
        # 'Pending' members won't be in /orgs/:org/members/:user
        self.assertFalse(self.org.has_in_members(lyloa))
        self.org.remove_from_membership(lyloa)
        self.assertFalse(self.org.has_in_members(lyloa))

    def testEditWithoutArguments(self):
        self.org.edit()

    def testEditWithAllArguments(self):
        self.org.edit("BeaverSoftware2@vincent-jacques.net", "http://vincent-jacques.net", "Company edited by PyGithub", "BeaverSoftware2@vincent-jacques.net", "Location edited by PyGithub", "Name edited by PyGithub")
        self.assertEqual(self.org.billing_email, "BeaverSoftware2@vincent-jacques.net")
        self.assertEqual(self.org.blog, "http://vincent-jacques.net")
        self.assertEqual(self.org.company, "Company edited by PyGithub")
        self.assertEqual(self.org.email, "BeaverSoftware2@vincent-jacques.net")
        self.assertEqual(self.org.location, "Location edited by PyGithub")
        self.assertEqual(self.org.name, "Name edited by PyGithub")

    def testEditHookWithMinimalParameters(self):
        hook = self.org.create_hook("web", {"url": "http://foobar.com"})
        hook = self.org.edit_hook(hook.id, "mobile", {"url": "http://barfoo.com"})
        self.assertEqual(hook.name, "mobile")

    def testEditHookWithAllParameters(self):
        hook = self.org.create_hook("web", {"url": "http://foobar.com"}, ["fork"], False)
        hook = self.org.edit_hook(hook.id, "mobile", {"url": "http://barfoo.com"}, ["spoon"], True)
        self.assertEqual(hook.name, "mobile")
        self.assertEqual(hook.events, ["spoon"])
        self.assertEqual(hook.active, True)

    def testCreateTeam(self):
        team = self.org.create_team("Team created by PyGithub")
        self.assertEqual(team.id, 189850)

    def testCreateTeamWithAllArguments(self):
        repo = self.org.get_repo("FatherBeaver")
        team = self.org.create_team("Team also created by PyGithub", [repo], "push", "secret")
        self.assertEqual(team.id, 189852)

    def testDeleteHook(self):
        hook = self.org.create_hook("web", {"url": "http://foobar.com"})
        self.org.delete_hook(hook.id)

    def testPublicMembers(self):
        lyloa = self.g.get_user("Lyloa")
        self.assertFalse(self.org.has_in_public_members(lyloa))
        self.org.add_to_public_members(lyloa)
        self.assertTrue(self.org.has_in_public_members(lyloa))
        self.org.remove_from_public_members(lyloa)
        self.assertFalse(self.org.has_in_public_members(lyloa))

    def testGetPublicMembers(self):
        self.assertListKeyEqual(self.org.get_public_members(), lambda u: u.login, ["jacquev6"])

    def testGetHooks(self):
        self.assertListKeyEqual(self.org.get_hooks(), lambda h: h.id, [257993])

    def testGetIssues(self):
        self.assertListKeyEqual(self.org.get_issues(), lambda i: i.id, [])

    def testGetIssuesWithAllArguments(self):
        requestedByUser = self.g.get_user().get_repo("PyGithub").get_label("Requested by user")
        issues = self.org.get_issues("assigned", "closed", [requestedByUser], "comments", "asc", datetime.datetime(2012, 5, 28, 23, 0, 0))
        self.assertListKeyEqual(issues, lambda i: i.id, [])

    def testGetMembers(self):
        self.assertListKeyEqual(self.org.get_members(), lambda u: u.login, ["cjuniet", "jacquev6", "Lyloa"])

    def testGetOutsideCollaborators(self):
        self.assertListKeyEqual(self.org.get_outside_collaborators(), lambda u: u.login, ["octocat"])

    def testOutsideCollaborators(self):
        octocat = self.g.get_user("octocat")
        self.org.convert_to_outside_collaborator(octocat)
        self.assertListKeyEqual(self.org.get_outside_collaborators(), lambda u: u.login, ["octocat"])
        self.org.remove_outside_collaborator(octocat)
        self.assertEqual(list(self.org.get_outside_collaborators()), [])

    def testMembers(self):
        lyloa = self.g.get_user("Lyloa")
        self.assertTrue(self.org.has_in_members(lyloa))
        self.org.remove_from_members(lyloa)
        self.assertFalse(self.org.has_in_members(lyloa))

    def testGetRepos(self):
        self.assertListKeyEqual(self.org.get_repos(), lambda r: r.name, ["FatherBeaver", "TestPyGithub"])

    def testGetReposWithType(self):
        self.assertListKeyEqual(self.org.get_repos("public"), lambda r: r.name, ["FatherBeaver", "PyGithub"])

    def testGetEvents(self):
        self.assertListKeyEqual(self.org.get_events(), lambda e: e.type, ["CreateEvent", "CreateEvent", "PushEvent", "PushEvent", "DeleteEvent", "DeleteEvent", "PushEvent", "PushEvent", "DeleteEvent", "DeleteEvent", "PushEvent", "PushEvent", "PushEvent", "CreateEvent", "CreateEvent", "CreateEvent", "CreateEvent", "CreateEvent", "PushEvent", "PushEvent", "PushEvent", "PushEvent", "PushEvent", "PushEvent", "ForkEvent", "CreateEvent"])

    def testGetTeams(self):
        self.assertListKeyEqual(self.org.get_teams(), lambda t: t.name, ["Members", "Owners"])

    def testCreateHookWithMinimalParameters(self):
        hook = self.org.create_hook("web", {"url": "http://foobar.com"})
        self.assertEqual(hook.id, 257967)

    def testCreateHookWithAllParameters(self):
        hook = self.org.create_hook("web", {"url": "http://foobar.com"}, ["fork"], False)
        self.assertTrue(hook.active)
        self.assertEqual(hook.id, 257993)

    def testCreateRepoWithMinimalArguments(self):
        repo = self.org.create_repo(name="TestPyGithub")
        self.assertEqual(repo.url, "https://api.github.com/repos/BeaverSoftware/TestPyGithub")

    def testCreateRepoWithAllArguments(self):
        team = self.org.get_team(141496)
        repo = self.org.create_repo(name="TestPyGithub2", description="Repo created by PyGithub", homepage="http://foobar.com",
                                    private=False, has_issues=False, has_wiki=False, has_downloads=False, team_id=team.id)
        self.assertEqual(repo.url, "https://api.github.com/repos/BeaverSoftware/TestPyGithub2")

    def testCreateRepositoryWithAutoInit(self):
        repo = self.org.create_repo(name="TestPyGithub", auto_init=True, gitignore_template="Python")
        self.assertEqual(repo.url, "https://api.github.com/repos/BeaverSoftware/TestPyGithub")

    def testCreateFork(self):
        pygithub = self.g.get_user("jacquev6").get_repo("PyGithub")
        repo = self.org.create_fork(pygithub)
        self.assertEqual(repo.url, "https://api.github.com/repos/BeaverSoftware/PyGithub")
