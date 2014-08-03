# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class OrganizationAttributes(TestCase):
    @Enterprise("zeus")
    def testOwnedOrganization(self):
        o = self.g.get_org("olympus")
        self.assertEqual(o.avatar_url, "http://github.home.jacquev6.net/identicons/6f4922f45568161a8cdf4ad2299f6d23.png")
        self.assertEqual(o.billing_email, "ghe-olympus@jacquev6.net")
        self.assertEqual(o.blog, None)
        self.assertEqual(o.collaborators, 0)
        self.assertEqual(o.company, None)
        self.assertEqual(o.created_at, datetime.datetime(2014, 8, 2, 18, 44, 42))
        self.assertEqual(o.disk_usage, 0)
        self.assertEqual(o.email, None)
        self.assertEqual(o.events_url, "http://github.home.jacquev6.net/api/v3/orgs/olympus/events")
        self.assertEqual(o.html_url, "http://github.home.jacquev6.net/olympus")
        self.assertEqual(o.id, 18)
        self.assertEqual(o.location, None)
        self.assertEqual(o.login, "olympus")
        self.assertEqual(o.members_url, "http://github.home.jacquev6.net/api/v3/orgs/olympus/members{/member}")
        self.assertEqual(o.name, None)
        self.assertEqual(o.owned_private_repos, 0)
        self.assertEqual(o.plan.name, "enterprise")
        self.assertEqual(o.plan.private_repos, 999999999999)
        self.assertEqual(o.plan.space, 976562499)
        self.assertEqual(o.plan.collaborators, None)
        self.assertEqual(o.private_gists, 0)
        self.assertEqual(o.public_gists, 0)
        self.assertEqual(o.public_members_url, "http://github.home.jacquev6.net/api/v3/orgs/olympus/public_members{/member}")
        self.assertEqual(o.public_repos, 0)
        self.assertEqual(o.repos_url, "http://github.home.jacquev6.net/api/v3/orgs/olympus/repos")
        self.assertEqual(o.total_private_repos, 0)
        self.assertEqual(o.type, "Organization")
        self.assertEqual(o.updated_at, datetime.datetime(2014, 8, 2, 19, 58, 49))


class OrganizationEdit(TestCase):
    @Enterprise("zeus")
    def testBillingEmail(self):
        o = self.g.get_org("olympus")
        self.assertEqual(o.billing_email, "ghe-olympus@jacquev6.net")
        o.edit(billing_email="foo@bar.com")
        self.assertEqual(o.billing_email, "foo@bar.com")
        o.edit(billing_email="ghe-olympus@jacquev6.net")
        self.assertEqual(o.billing_email, "ghe-olympus@jacquev6.net")

    @Enterprise("zeus")
    def testBlog(self):
        o = self.g.get_org("olympus")
        self.assertEqual(o.blog, None)
        o.edit(blog="http://jacquev6.net/olympus")
        self.assertEqual(o.blog, "http://jacquev6.net/olympus")
        o.edit(blog=PyGithub.Blocking.Reset)
        self.assertEqual(o.blog, None)

    @Enterprise("zeus")
    def testCompany(self):
        o = self.g.get_org("olympus")
        self.assertEqual(o.company, None)
        o.edit(company="Olympus Software Inc.")
        self.assertEqual(o.company, "Olympus Software Inc.")
        o.edit(company=PyGithub.Blocking.Reset)
        self.assertEqual(o.company, None)

    @Enterprise("zeus")
    def testEmail(self):
        o = self.g.get_org("olympus")
        self.assertEqual(o.email, None)
        o.edit(email="foo@bar.com")
        self.assertEqual(o.email, "foo@bar.com")
        o.edit(email=PyGithub.Blocking.Reset)
        self.assertEqual(o.email, None)

    @Enterprise("zeus")
    def testLocation(self):
        o = self.g.get_org("olympus")
        self.assertEqual(o.location, None)
        o.edit(location="Mount Olympus")
        self.assertEqual(o.location, "Mount Olympus")
        o.edit(location=PyGithub.Blocking.Reset)
        self.assertEqual(o.location, None)

    @Enterprise("zeus")
    def testName(self):
        o = self.g.get_org("olympus")
        self.assertEqual(o.name, None)
        o.edit(name="Olympus Software")
        self.assertEqual(o.name, "Olympus Software")
        o.edit(name=PyGithub.Blocking.Reset)
        self.assertEqual(o.name, None)


class OrganizationMembers(TestCase):
    @Enterprise("zeus")
    def testGetPublicMembers(self):
        o = self.g.get_org("olympus")
        public_members = o.get_public_members()
        self.assertEqual([m.login for m in public_members], ["antigone", "poseidon", "zeus"])

    @Enterprise("zeus")
    def testGetPublicMembers_allParameters(self):
        o = self.g.get_org("olympus")
        public_members = o.get_public_members(per_page=1)
        self.assertEqual([m.login for m in public_members], ["antigone", "poseidon", "zeus"])

    @Enterprise("zeus")
    def testHasInMembersAndPublicMembersFromOwner(self):
        o = self.g.get_org("olympus")
        # Not member
        self.assertFalse(o.has_in_public_members("penelope"))
        self.assertFalse(o.has_in_members("penelope"))
        # Private member
        self.assertFalse(o.has_in_public_members("electra"))
        self.assertTrue(o.has_in_members("electra"))
        # Public member
        self.assertTrue(o.has_in_public_members("antigone"))
        self.assertTrue(o.has_in_members("antigone"))

    @Enterprise("antigone")
    def testHasInMembersAndPublicMembersFromMember(self):
        o = self.g.get_org("olympus")
        # Not member
        self.assertFalse(o.has_in_public_members("penelope"))
        self.assertFalse(o.has_in_members("penelope"))
        # Private member
        self.assertFalse(o.has_in_public_members("electra"))
        self.assertTrue(o.has_in_members("electra"))
        # Public member
        self.assertTrue(o.has_in_public_members("antigone"))
        self.assertTrue(o.has_in_members("antigone"))

    @Enterprise("penelope")
    def testHasInMembersAndPublicMembersFromExternal(self):
        o = self.g.get_org("olympus")
        # Not member
        self.assertFalse(o.has_in_public_members("penelope"))
        self.assertFalse(o.has_in_members("penelope"))
        # Private member
        self.assertFalse(o.has_in_public_members("electra"))
        self.assertFalse(o.has_in_members("electra"))
        # Public member
        self.assertTrue(o.has_in_public_members("antigone"))
        # @todoAlpha Change to assertTrue once GitHub fixes
        # Request #13733 "Bug in API redirect"
        # The redirection points to
        # http://github.home.jacquev6.net/organizations/18/public_members/antigone
        # instead of
        # http://github.home.jacquev6.net/api/v3/organizations/18/public_members/antigone
        # so we get a 404 and return False
        self.assertFalse(o.has_in_members("antigone"))

    @Enterprise("zeus")
    def testGetMembers(self):
        o = self.g.get_org("olympus")
        members = o.get_members()
        self.assertEqual([m.login for m in members], ["antigone", "electra", "poseidon", "zeus"])

    @Enterprise("zeus")
    def testGetMembers_allParameters(self):
        o = self.g.get_org("olympus")
        members = o.get_members(filter="all", per_page=1)
        self.assertEqual([m.login for m in members], ["antigone", "electra", "poseidon", "zeus"])

    @Enterprise("electra")
    def testAddToAndRemoveSelfFromPublicMembers(self):
        o = self.g.get_org("olympus")
        self.assertFalse(o.has_in_public_members("electra"))
        o.add_to_public_members("electra")
        self.assertTrue(o.has_in_public_members("electra"))
        o.remove_from_public_members("electra")
        self.assertFalse(o.has_in_public_members("electra"))
        # @todoAlpha Test if owners can remove_from_public_members someone else (They can in the GUI.)

    @Enterprise("zeus")
    def testRemoveFromMembers(self):
        o = self.g.get_org("olympus")
        self.assertFalse(o.has_in_members("penelope"))
        o.get_teams()[0].add_to_members("penelope")
        self.assertTrue(o.has_in_members("penelope"))
        o.remove_from_members("penelope")
        self.assertFalse(o.has_in_members("penelope"))

    @Enterprise("zeus")
    def testGetTeams(self):
        o = self.g.get_org("olympus")
        teams = o.get_teams()
        self.assertEqual([t.name for t in teams], ["Owners", "Gods", "Humans"])

    @Enterprise("zeus")
    def testGetTeams_allParameters(self):
        o = self.g.get_org("olympus")
        teams = o.get_teams(per_page=1)
        self.assertEqual([t.name for t in teams], ["Owners", "Gods", "Humans"])

    @Enterprise("zeus")
    def testCreateTeam(self):
        o = self.g.get_org("olympus")
        t = o.create_team("Titans")
        self.assertEqual(t.name, "Titans")
        self.assertEqual(t.permission, "pull")
        self.assertEqual(t.repos_count, 0)
        t.delete()

    @Enterprise("zeus")
    def testCreateTeam_allParameters(self):
        o = self.g.get_org("olympus")
        repo = o.create_repo("trojan-war")
        t = o.create_team("Titans", repo_names=[repo], permission="push")
        self.assertEqual(t.name, "Titans")
        self.assertEqual(t.permission, "push")
        self.assertEqual(t.repos_count, 1)
        t.delete()
        repo.delete()


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
