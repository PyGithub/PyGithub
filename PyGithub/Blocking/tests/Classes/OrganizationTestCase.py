# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking

import PyGithub.Blocking.tests.Framework as Framework


class OrganizationTestCase(Framework.SimpleLoginTestCase):
    def testAttributesOfOwnedOrganization(self):
        o = self.g.get_org("BeaverSoftware")
        self.assertEqual(o.avatar_url, "https://gravatar.com/avatar/d563e337cac2fdc644e2aaaad1e23266?d=https%3A%2F%2Fidenticons.github.com%2Fde8dec416975d0a85845b1b88385b9d5.png&r=x")
        self.assertEqual(o.billing_email, "BeaverSoftware@vincent-jacques.net")
        self.assertEqual(o.blog, None)
        self.assertEqual(o.collaborators, 0)
        self.assertEqual(o.company, None)
        self.assertEqual(o.created_at, datetime.datetime(2012, 2, 9, 19, 20, 12))
        self.assertEqual(o.disk_usage, 84)
        self.assertEqual(o.email, None)
        self.assertEqual(o.events_url, "https://api.github.com/orgs/BeaverSoftware/events")
        self.assertEqual(o.followers, 0)
        self.assertEqual(o.following, 0)
        self.assertEqual(o.html_url, "https://github.com/BeaverSoftware")
        self.assertEqual(o.id, 1424031)
        self.assertEqual(o.location, "Paris, France")
        self.assertEqual(o.login, "BeaverSoftware")
        self.assertEqual(o.members_url, "https://api.github.com/orgs/BeaverSoftware/members{/member}")
        self.assertEqual(o.name, None)
        self.assertEqual(o.owned_private_repos, 0)
        self.assertEqual(o.plan.collaborators, None)
        self.assertEqual(o.plan.name, "free")
        self.assertEqual(o.plan.private_repos, 0)
        self.assertEqual(o.plan.space, 307200)
        self.assertEqual(o.private_gists, 0)
        self.assertEqual(o.public_gists, 0)
        self.assertEqual(o.public_members_url, "https://api.github.com/orgs/BeaverSoftware/public_members{/member}")
        self.assertEqual(o.public_repos, 1)
        self.assertEqual(o.repos_url, "https://api.github.com/orgs/BeaverSoftware/repos")
        self.assertEqual(o.total_private_repos, 0)
        self.assertEqual(o.type, "Organization")
        self.assertEqual(o.updated_at, datetime.datetime(2013, 12, 20, 5, 40, 14))
        self.assertEqual(o.url, "https://api.github.com/orgs/BeaverSoftware")

    def testAttributesOfOtherOrganization(self):
        o = self.g.get_org("github")
        self.assertEqual(o.avatar_url, "https://gravatar.com/avatar/61024896f291303615bcd4f7a0dcfb74?d=https%3A%2F%2Fidenticons.github.com%2Fae816a80e4c1c56caa2eb4e1819cbb2f.png&r=x")
        self.assertEqual(o.billing_email, None)
        self.assertEqual(o.blog, "https://github.com/about")
        self.assertEqual(o.collaborators, None)
        self.assertEqual(o.company, None)
        self.assertEqual(o.created_at, datetime.datetime(2008, 5, 11, 4, 37, 31))
        self.assertEqual(o.disk_usage, None)
        self.assertEqual(o.email, "support@github.com")
        self.assertEqual(o.events_url, "https://api.github.com/orgs/github/events")
        self.assertEqual(o.followers, 12)
        self.assertEqual(o.following, 0)
        self.assertEqual(o.html_url, "https://github.com/github")
        self.assertEqual(o.id, 9919)
        self.assertEqual(o.location, "San Francisco, CA")
        self.assertEqual(o.login, "github")
        self.assertEqual(o.members_url, "https://api.github.com/orgs/github/members{/member}")
        self.assertEqual(o.name, "GitHub")
        self.assertEqual(o.owned_private_repos, None)
        self.assertEqual(o.plan, None)
        self.assertEqual(o.private_gists, None)
        self.assertEqual(o.public_gists, 0)
        self.assertEqual(o.public_members_url, "https://api.github.com/orgs/github/public_members{/member}")
        self.assertEqual(o.public_repos, 117)
        self.assertEqual(o.repos_url, "https://api.github.com/orgs/github/repos")
        self.assertEqual(o.total_private_repos, None)
        self.assertEqual(o.type, "Organization")
        self.assertEqual(o.updated_at, datetime.datetime(2013, 12, 20, 6, 26, 10))
        self.assertEqual(o.url, "https://api.github.com/orgs/github")

    def testGetMembers(self):
        users = self.g.get_org("github").get_members()
        # @todoSomeday Open an issue, http://developer.github.com/v3/orgs/members/#members-list says there should be a redirection
        self.assertEqual(users[0].login, "mojombo")
        self.assertEqual(users[1].login, "defunkt")

    def testGetMembers_allParameters(self):
        users = self.g.get_org("github").get_members(per_page=3, filter="all")
        self.assertEqual(users[0].login, "mojombo")
        self.assertEqual(users[1].login, "defunkt")

    def testGetPublicMembers(self):
        users = self.g.get_org("github").get_public_members()
        self.assertEqual(users[0].login, "Caged")
        self.assertEqual(users[1].login, "ChrisLundquist")

    def testGetPublicMembers_allParameters(self):
        users = self.g.get_org("github").get_public_members(per_page=3)
        self.assertEqual(users[0].login, "Caged")
        self.assertEqual(users[1].login, "ChrisLundquist")

    def testGetRepos(self):
        repos = self.g.get_org("github").get_repos()
        self.assertEqual(repos[0].name, "media")
        self.assertTrue(isinstance(repos[0].owner, PyGithub.Blocking.Organization.Organization))
        self.assertEqual(repos[1].name, "albino")

    def testGetRepos_allParameters(self):
        repos = self.g.get_org("github").get_repos(type="private", per_page=3)
        self.assertEqual(len(list(repos)), 0)

    def testGetRepo(self):
        repo = self.g.get_org("github").get_repo("albino")
        self.assertTrue(isinstance(repo.owner, PyGithub.Blocking.Organization.Organization))
        self.assertEqual(repo.full_name, "github/albino")

    def testHasInMembers(self):
        org = self.g.get_org("github")
        self.assertTrue(org.has_in_members("defunkt"))
        self.assertFalse(org.has_in_members("nvie"))
        self.assertFalse(org.has_in_members("jacquev6"))

    def testHasInPublicMembers(self):
        org = self.g.get_org("github")
        self.assertTrue(org.has_in_public_members("defunkt"))
        self.assertFalse(org.has_in_public_members("nvie"))
        self.assertFalse(org.has_in_public_members("jacquev6"))

    def testEditLocation(self):
        org = self.g.get_org("BeaverSoftware")
        self.assertEqual(org.location, "Paris, France")
        org.edit(location=PyGithub.Blocking.Reset)
        self.assertEqual(org.location, None)
        org.edit(location="Paris, France")
        self.assertEqual(org.location, "Paris, France")

    def testEditEmail(self):
        org = self.g.get_org("BeaverSoftware")
        self.assertEqual(org.email, None)
        org.edit(email="foo@vincent-jacques.net")
        self.assertEqual(org.email, "foo@vincent-jacques.net")
        org.edit(email=PyGithub.Blocking.Reset)
        self.assertEqual(org.email, None)

    def testEditBlog(self):
        org = self.g.get_org("BeaverSoftware")
        self.assertEqual(org.blog, None)
        org.edit(blog="http://vincent-jacques.net/foo")
        self.assertEqual(org.blog, "http://vincent-jacques.net/foo")
        org.edit(blog=PyGithub.Blocking.Reset)
        self.assertEqual(org.blog, None)

    def testEditCompany(self):
        org = self.g.get_org("BeaverSoftware")
        self.assertEqual(org.company, None)
        org.edit(company="Beaver Software Inc.")
        self.assertEqual(org.company, "Beaver Software Inc.")
        org.edit(company=PyGithub.Blocking.Reset)
        self.assertEqual(org.company, None)

    def testEditName(self):
        org = self.g.get_org("BeaverSoftware")
        self.assertEqual(org.name, None)
        org.edit(name="Beaver Software")
        self.assertEqual(org.name, "Beaver Software")
        org.edit(name=PyGithub.Blocking.Reset)
        self.assertEqual(org.name, None)

    def testEditBillingEmail(self):
        org = self.g.get_org("BeaverSoftware")
        self.assertEqual(org.billing_email, "BeaverSoftware@vincent-jacques.net")
        org.edit(billing_email="bar@vincent-jacques.net")
        self.assertEqual(org.billing_email, "bar@vincent-jacques.net")
        org.edit(billing_email="BeaverSoftware@vincent-jacques.net")
        self.assertEqual(org.billing_email, "BeaverSoftware@vincent-jacques.net")
        with self.assertRaises(TypeError):
            org.edit(billing_email=PyGithub.Blocking.Reset)

    def testEditNothing(self):
        org = self.g.get_org("BeaverSoftware")
        org.edit()

    def testCreateFork(self):
        org = self.g.get_org("BeaverSoftware")
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            org.get_repo("whisper")
        fork = org.create_fork("graphite-project/whisper")
        self.assertEqual(fork.full_name, "BeaverSoftware/whisper")
        fork.delete()

    def testCreateRepo(self):
        org = self.g.get_org("BeaverSoftware")
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            org.get_repo("turbo-octo-ironman")
        repo = org.create_repo("turbo-octo-ironman")
        self.assertEqual(repo.full_name, "BeaverSoftware/turbo-octo-ironman")
        repo.delete()

    def testCreateRepo_allParameters(self):
        org = self.g.get_org("BeaverSoftware")
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            org.get_repo("potential-octo-lana")
        repo = org.create_repo("potential-octo-lana", description="Created with PyGithub v2", has_issues=False, has_wiki=False, private=False, auto_init=True, gitignore_template="C", homepage="http://foo.bar", has_downloads=False, team_id=141496, license_template="mit")
        self.assertEqual(repo.full_name, "BeaverSoftware/potential-octo-lana")
        repo.delete()

    def testAddToPublicMembersFailsForOtherUser(self):
        org = self.g.get_org("BeaverSoftware")
        self.assertTrue(org.has_in_members("Lyloa"))
        with self.assertRaises(PyGithub.Blocking.ForbiddenException):
            org.add_to_public_members("Lyloa")

    def testAddRemovePublicMembers(self):
        org = self.g.get_org("BeaverSoftware")
        self.assertTrue(org.has_in_members("jacquev6"))
        self.assertFalse(org.has_in_public_members("jacquev6"))
        org.add_to_public_members("jacquev6")
        self.assertTrue(org.has_in_public_members("jacquev6"))
        org.remove_from_public_members("jacquev6")
        self.assertFalse(org.has_in_public_members("jacquev6"))

    def testRemoveFromMembers(self):
        org = self.g.get_org("BeaverSoftware")
        self.assertTrue(org.has_in_members("Lyloa"))
        org.remove_from_members("Lyloa")
        self.assertFalse(org.has_in_members("Lyloa"))

    def testGetTeams(self):
        teams = self.g.get_org("BeaverSoftware").get_teams()
        self.assertEqual(teams[0].name, "Owners")
        self.assertEqual(teams[1].name, "Members")

    def testGetTeams_allParameters(self):
        teams = self.g.get_org("BeaverSoftware").get_teams(per_page=3)
        self.assertEqual(teams[0].name, "Owners")
        self.assertEqual(teams[1].name, "Members")

    def testCreateTeam(self):
        org = self.g.get_org("BeaverSoftware")
        team = org.create_team("Testers")
        self.assertEqual(team.name, "Testers")
        self.assertEqual(team.permission, "pull")
        team.delete()

    def testCreateTeamThatAlreadyExists(self):
        org = self.g.get_org("BeaverSoftware")
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            org.create_team("Members")

    def testCreateTeam_allParameters(self):
        org = self.g.get_org("BeaverSoftware")
        team = org.create_team("Testers", permission="push", repo_names=["BeaverSoftware/FatherBeaver"])
        self.assertEqual(team.name, "Testers")
        self.assertEqual(team.permission, "push")
        self.assertTrue(team.has_in_repos("BeaverSoftware/FatherBeaver"))
        team.delete()
