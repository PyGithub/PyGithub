# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class OrganizationAttributes(TestCase):
    @Enterprise.User(1)
    def testOwnedOrganization(self):
        o = self.g.get_org("ghe-org-1")
        self.assertEqual(o.billing_email, "ghe-org-1@jacquev6.net")
        self.assertEqual(o.members_url, "http://github.home.jacquev6.net/api/v3/orgs/ghe-org-1/members{/member}")
        self.assertEqual(o.public_members_url, "http://github.home.jacquev6.net/api/v3/orgs/ghe-org-1/public_members{/member}")


class OrganizationEdit(TestCase):
    @Enterprise.User(1)
    def testBillingEmail(self):
        o = self.g.get_org("ghe-org-1")
        self.assertEqual(o.billing_email, "ghe-org-1@jacquev6.net")
        o.edit(billing_email="foo@bar.com")
        self.assertEqual(o.billing_email, "foo@bar.com")
        o.edit(billing_email="ghe-org-1@jacquev6.net")
        self.assertEqual(o.billing_email, "ghe-org-1@jacquev6.net")

    @Enterprise.User(1)
    def testBlog(self):
        o = self.g.get_org("ghe-org-1")
        self.assertIsNone(o.blog)
        o.edit(blog="http://jacquev6.net/ghe-org-1")
        self.assertEqual(o.blog, "http://jacquev6.net/ghe-org-1")
        o.edit(blog=PyGithub.Blocking.Reset)
        self.assertIsNone(o.blog)

    @Enterprise.User(1)
    def testCompany(self):
        o = self.g.get_org("ghe-org-1")
        self.assertIsNone(o.company)
        o.edit(company="Amazon")
        self.assertEqual(o.company, "Amazon")
        o.edit(company=PyGithub.Blocking.Reset)
        self.assertIsNone(o.company)

    @Enterprise.User(1)
    def testEmail(self):
        o = self.g.get_org("ghe-org-1")
        self.assertIsNone(o.email)
        o.edit(email="foo@bar.com")
        self.assertEqual(o.email, "foo@bar.com")
        o.edit(email=PyGithub.Blocking.Reset)
        self.assertIsNone(o.email)

    @Enterprise.User(1)
    def testLocation(self):
        o = self.g.get_org("ghe-org-1")
        self.assertIsNone(o.location)
        o.edit(location="Jupiter")
        self.assertEqual(o.location, "Jupiter")
        o.edit(location=PyGithub.Blocking.Reset)
        self.assertIsNone(o.location)

    @Enterprise.User(1)
    def testName(self):
        o = self.g.get_org("ghe-org-1")
        self.assertIsNone(o.name)
        o.edit(name="FooBar Software")
        self.assertEqual(o.name, "FooBar Software")
        o.edit(name=PyGithub.Blocking.Reset)
        self.assertIsNone(o.name)


class OrganizationMembers(TestCase):
    @Enterprise.User(1)
    def testGetPublicMembers(self):
        o = self.g.get_org("ghe-org-2")
        public_members = o.get_public_members()
        self.assertEqual([m.login for m in public_members], ["ghe-user-1", "ghe-user-3"])

    @Enterprise.User(1)
    def testGetPublicMembers_allParameters(self):
        o = self.g.get_org("ghe-org-2")
        public_members = o.get_public_members(per_page=1)
        self.assertEqual([m.login for m in public_members], ["ghe-user-1", "ghe-user-3"])

    @Enterprise.User(1)
    def testHasInPublicMembers(self):
        self.assertFalse(self.g.get_org("ghe-org-1").has_in_public_members("ghe-user-1"))
        self.assertTrue(self.g.get_org("ghe-org-2").has_in_public_members("ghe-user-1"))

    @Enterprise.User(1)
    def testGetMembers(self):
        o = self.g.get_org("ghe-org-2")
        members = o.get_members()
        self.assertEqual([m.login for m in members], ["ghe-user-1", "ghe-user-2", "ghe-user-3"])

    @Enterprise.User(1)
    def testGetMembers_allParameters(self):
        o = self.g.get_org("ghe-org-2")
        members = o.get_members(filter="all", per_page=1)
        self.assertEqual([m.login for m in members], ["ghe-user-1", "ghe-user-2", "ghe-user-3"])

    @Enterprise.User(1)
    def testHasInMembersFromOwner(self):
        o = self.g.get_org("ghe-org-1")
        self.assertTrue(o.has_in_members("ghe-user-1"))
        self.assertFalse(o.has_in_members("ghe-user-2"))

    @Enterprise.User(1)
    def testHasInMembersFromMember(self):
        self.assertTrue(self.g.get_org("ghe-org-2").has_in_members("ghe-user-2"))

    @Enterprise.User(3)
    def testHasInMembersFromExternal(self):
        self.assertFalse(self.g.get_org("ghe-org-1").has_in_members("ghe-user-1"))

    @Enterprise.User(2)
    def testAddToAndRemoveFromPublicMembers(self):
        o = self.g.get_org("ghe-org-2")
        self.assertFalse(o.has_in_public_members("ghe-user-2"))
        o.add_to_public_members("ghe-user-2")
        self.assertTrue(o.has_in_public_members("ghe-user-2"))
        o.remove_from_public_members("ghe-user-2")
        self.assertFalse(o.has_in_public_members("ghe-user-2"))

    @Enterprise.User(1)
    def testRemoveFromMembers(self):
        o = self.g.get_org("ghe-org-1")
        self.assertFalse(o.has_in_members("ghe-user-2"))
        o.get_teams()[0].add_to_members("ghe-user-2")
        self.assertTrue(o.has_in_members("ghe-user-2"))
        o.remove_from_members("ghe-user-2")
        self.assertFalse(o.has_in_members("ghe-user-2"))

    @Enterprise.User(1)
    def testGetTeams(self):
        o = self.g.get_org("ghe-org-1")
        teams = o.get_teams()
        self.assertEqual([t.name for t in teams], ["Owners", "A-team"])

    @Enterprise.User(1)
    def testGetTeams_allParameters(self):
        o = self.g.get_org("ghe-org-1")
        teams = o.get_teams(per_page=1)
        self.assertEqual([t.name for t in teams], ["Owners", "A-team"])

    @Enterprise.User(1)
    def testCreateTeam(self):
        o = self.g.get_org("ghe-org-1")
        t = o.create_team("Jamaica Bobsleigh Team")
        self.assertEqual(t.name, "Jamaica Bobsleigh Team")
        self.assertEqual(t.permission, "pull")
        self.assertEqual(t.repos_count, 0)
        t.delete()

    @Enterprise.User(1)
    def testCreateTeam_allParameters(self):
        o = self.g.get_org("ghe-org-1")
        t = o.create_team("Jamaica Bobsleigh Team", repo_names=[("ghe-org-1", "repo-org-1-1")], permission="push")
        self.assertEqual(t.name, "Jamaica Bobsleigh Team")
        self.assertEqual(t.permission, "push")
        self.assertEqual(t.repos_count, 1)
        t.delete()


class OrganizationRepositories(TestCase):
    @Enterprise.User(1)
    def testGetRepo(self):
        o = self.g.get_org("ghe-org-1")
        r = o.get_repo("repo-org-1-1")
        self.assertEqual(r.full_name, "ghe-org-1/repo-org-1-1")

    @Enterprise.User(1)
    def testGetRepos(self):
        o = self.g.get_org("ghe-org-1")
        repos = o.get_repos()
        self.assertEqual([r.name for r in repos], ["repo-org-1-1", "repo-org-1-2"])

    @Enterprise.User(1)
    def testGetRepos_allParameters(self):
        o = self.g.get_org("ghe-org-1")
        repos = o.get_repos(type="sources", per_page=1)
        self.assertEqual([r.name for r in repos], ["repo-org-1-1", "repo-org-1-2"])

    @Enterprise.User(1)
    def testCreateRepo(self):
        o = self.g.get_org("ghe-org-1")
        r = o.create_repo("spawncamping-wallhack")
        self.assertEqual(r.name, "spawncamping-wallhack")
        self.assertIsNone(r.description)
        self.assertIsNone(r.homepage)
        self.assertEqual(r.private, False)
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        r.delete()

    @Enterprise.User(1)
    def testCreateRepo_allParameters(self):
        o = self.g.get_org("ghe-org-1")
        r = o.create_repo("spawncamping-wallhack", description="Something weird", homepage="http://bar.com", private=True, has_issues=False, has_wiki=False, team_id=2, auto_init=True, gitignore_template="Python", license_template="mit")
        self.assertEqual(r.name, "spawncamping-wallhack")
        self.assertEqual(r.description, "Something weird")
        self.assertEqual(r.homepage, "http://bar.com")
        self.assertEqual(r.private, True)
        self.assertEqual(r.has_issues, False)
        self.assertEqual(r.has_wiki, False)
        self.assertTrue(self.g.get_team(2).has_in_repos(("ghe-org-1", "spawncamping-wallhack")))
        r.delete()

    @Enterprise.User(1)
    def testCreateFork(self):
        o = self.g.get_org("ghe-org-1")
        r = o.create_fork(("ghe-user-1", "repo-user-1-1"))
        self.assertEqual(r.full_name, "ghe-org-1/repo-user-1-1")
        r.delete()
