# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class AuthenticatedUserEdit(TestCase):
    @Enterprise.User(1)
    def testName(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.name, "One Ghe")
        u.edit(name=PyGithub.Blocking.Reset)
        self.assertIsNone(u.name)
        u.edit(name="One Ghe")
        self.assertEqual(u.name, "One Ghe")

    @Enterprise.User(1)
    def testEmail(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.email, "ghe-user-1@jacquev6.net")
        u.edit(email=PyGithub.Blocking.Reset)
        self.assertIsNone(u.email)
        u.edit(email="ghe-user-1@jacquev6.net")
        self.assertEqual(u.email, "ghe-user-1@jacquev6.net")

    @Enterprise.User(1)
    def testBlog(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.blog, "http://jacquev6.net/ghe-user-1")
        u.edit(blog=PyGithub.Blocking.Reset)
        self.assertIsNone(u.blog)
        u.edit(blog="http://jacquev6.net/ghe-user-1")
        self.assertEqual(u.blog, "http://jacquev6.net/ghe-user-1")

    @Enterprise.User(1)
    def testCompany(self):
        u = self.g.get_authenticated_user()
        self.assertIsNone(u.company)
        u.edit(company="FooBar Software")
        self.assertEqual(u.company, "FooBar Software")
        u.edit(company=PyGithub.Blocking.Reset)
        self.assertIsNone(u.company)

    @Enterprise.User(1)
    def testLocation(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.location, "Venus")
        u.edit(location=PyGithub.Blocking.Reset)
        self.assertIsNone(u.location)
        u.edit(location="Venus")
        self.assertEqual(u.location, "Venus")

    @Enterprise.User(1)
    def testHireable(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.hireable, False)
        u.edit(hireable=PyGithub.Blocking.Reset)
        self.assertIsNone(u.hireable)
        u.edit(hireable=False)
        self.assertEqual(u.hireable, False)


class AuthenticatedUserFollowing(TestCase):
    @Enterprise.User(1)
    def testGetFollowing(self):
        u = self.g.get_authenticated_user()
        following = u.get_following()
        self.assertEqual([f.login for f in following], ["ghe-admin-1", "ghe-user-2", "ghe-user-3", "ghe-admin-2"])

    @Enterprise.User(1)
    def testGetFollowing_allParameters(self):
        u = self.g.get_authenticated_user()
        following = u.get_following(per_page=2)
        self.assertEqual([f.login for f in following], ["ghe-admin-1", "ghe-user-2", "ghe-user-3", "ghe-admin-2"])

    @Enterprise.User(1)
    def testAddToAndRemoveFromFollowing(self):
        u = self.g.get_authenticated_user()
        self.assertTrue(u.has_in_following("ghe-user-2"))
        u.remove_from_following("ghe-user-2")
        self.assertFalse(u.has_in_following("ghe-user-2"))
        u.add_to_following("ghe-user-2")
        self.assertTrue(u.has_in_following("ghe-user-2"))

    @Enterprise.User(3)
    def testGetFollowers(self):
        u = self.g.get_authenticated_user()
        followers = u.get_followers()
        self.assertEqual([f.login for f in followers], ["ghe-user-1", "ghe-admin-1", "ghe-admin-2", "ghe-user-2"])

    @Enterprise.User(3)
    def testGetFollowers_allParameters(self):
        u = self.g.get_authenticated_user()
        followers = u.get_followers(per_page=2)
        self.assertEqual([f.login for f in followers], ["ghe-user-1", "ghe-admin-1", "ghe-admin-2", "ghe-user-2"])


class AuthenticatedUserGists(TestCase):
    @Enterprise.User(1)
    def testGetGists(self):
        u = self.g.get_authenticated_user()
        gists = u.get_gists()
        self.assertEqual([g.description for g in gists], ["gist-user-1-2", "gist-user-1-1"])

    @Enterprise.User(1)
    def testGetGists_allParameters(self):
        u = self.g.get_authenticated_user()
        gists = u.get_gists(since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([g.description for g in gists], ["gist-user-1-2", "gist-user-1-1"])

    @Enterprise.User(3)
    def testGetStarredGists(self):
        u = self.g.get_authenticated_user()
        gists = u.get_starred_gists()
        self.assertEqual([g.description for g in gists], ["gist-user-1-2", "gist-user-1-1"])

    @Enterprise.User(3)
    def testGetStarredGists_allParameters(self):
        u = self.g.get_authenticated_user()
        gists = u.get_starred_gists(since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([g.description for g in gists], ["gist-user-1-2", "gist-user-1-1"])

    @Enterprise.User(3)
    def testAddToAndRemoveFromStarredGists(self):
        u = self.g.get_authenticated_user()
        self.assertTrue(u.has_in_starred_gists("e7f47a1723963f11cc01"))
        u.remove_from_starred_gists("e7f47a1723963f11cc01")
        self.assertFalse(u.has_in_starred_gists("e7f47a1723963f11cc01"))
        u.add_to_starred_gists("e7f47a1723963f11cc01")
        self.assertTrue(u.has_in_starred_gists("e7f47a1723963f11cc01"))

    @Enterprise.User(3)
    def testCreateGistFork(self):
        u = self.g.get_authenticated_user()
        g = u.create_gist_fork("e7f47a1723963f11cc01")
        self.assertEqual(g.description, "gist-user-1-2")
        self.assertEqual(g.owner.login, "ghe-user-3")
        g.delete()

    @Enterprise.User(1)
    def testCreateGist(self):
        # @todoAlpha Create input class for files
        u = self.g.get_authenticated_user()
        g = u.create_gist(files={"foo.txt": {"content": "barbaz"}})
        self.assertIsNone(g.description)
        self.assertEqual(g.public, False)
        g.delete()

    @Enterprise.User(1)
    def testCreateGist_allParameters(self):
        u = self.g.get_authenticated_user()
        g = u.create_gist(files={"foo.txt": {"content": "barbaz"}, "bar.txt": {"content": "tartempion"}}, public=True, description="Gist created by PyGithub")
        self.assertEqual(g.description, "Gist created by PyGithub")
        self.assertEqual(g.public, True)
        g.delete()


class AuthenticatedUserKeys(TestCase):
    @Enterprise.User(1)
    def testGetKeys(self):
        u = self.g.get_authenticated_user()
        keys = u.get_keys()
        self.assertEqual([k.id for k in keys], [1, 3])

    @Enterprise.User(1)
    def testGetKey(self):
        u = self.g.get_authenticated_user()
        k = u.get_key(3)
        self.assertEqual(k.title, "key-1-2")

    @Enterprise.User(1)
    def testCreateKey(self):
        u = self.g.get_authenticated_user()
        k = u.create_key("key-1-3", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCvxan/6YaX3rIQaQFMAXiyNimJ1tsOwsxQMTBciHN6NbPuFReIELsOdzM+r6IP7cVmKacli03BD/oRQ90SZS91b2YMc0RRvtfwr5P8JnFysDXj9TgnEcJ1DjV0xLYvg4yr3L+xJFS4kEdfIiYnbqVhRqTm7liUvpjrW5uwYJSRWvcL6BZz2GnTakRVL53SckWykeFxoXX7JPTj+QOpRZlnz7/n00LZ6mVw3djga5ybyYol4LVkExQ3Vffstdz983DSOf4iScU1heQtv5sCA5JDtlQFxSY9SIPr8C/eri9vogwGGk65UhPF49ssNh/jidoaehRVVz3C2bUFPm2xtn4p")
        self.assertEqual(k.title, "key-1-3")
        k.delete()


class AuthenticatedUserOrganizations(TestCase):
    @Enterprise.User(1)
    def testGetOrgs(self):
        u = self.g.get_authenticated_user()
        orgs = u.get_orgs()
        self.assertEqual([o.login for o in orgs], ["ghe-org-1", "ghe-org-2"])

    @Enterprise.User(1)
    def testGetOrgs_allParameters(self):
        u = self.g.get_authenticated_user()
        orgs = u.get_orgs(per_page=1)
        self.assertEqual([o.login for o in orgs], ["ghe-org-1", "ghe-org-2"])

    @Enterprise.User(1)
    def testGetTeams(self):
        u = self.g.get_authenticated_user()
        teams = u.get_teams()
        self.assertEqual([t.name for t in teams], ["Owners", "A-team", "German Soccer Team"])

    @Enterprise.User(1)
    def testGetTeams_allParameters(self):
        u = self.g.get_authenticated_user()
        teams = u.get_teams(per_page=1)
        self.assertEqual([t.name for t in teams], ["Owners", "A-team", "German Soccer Team"])


class AuthenticatedUserRepositories(TestCase):
    @Enterprise.User(1)
    def testGetRepo(self):
        u = self.g.get_authenticated_user()
        r = u.get_repo("repo-user-1-1")
        self.assertEqual(r.full_name, "ghe-user-1/repo-user-1-1")

    @Enterprise.User(1)
    def testGetRepos(self):
        u = self.g.get_authenticated_user()
        repos = u.get_repos()
        self.assertEqual([r.name for r in repos], ["repo-user-1-1", "repo-user-1-2", "repo-user-1-3"])

    @Enterprise.User(1)
    def testGetRepos_allParameters(self):
        u = self.g.get_authenticated_user()
        repos = u.get_repos(type="public", sort="pushed", direction="asc", per_page=1)
        self.assertEqual([r.name for r in repos], ["repo-user-1-2", "repo-user-1-1"])

    @Enterprise.User(3)
    def testGetStarred(self):
        u = self.g.get_authenticated_user()
        repos = u.get_starred()
        self.assertEqual([r.full_name for r in repos], ["ghe-user-1/repo-user-1-2", "ghe-user-1/repo-user-1-1"])

    @Enterprise.User(3)
    def testGetStarred_allParameters(self):
        u = self.g.get_authenticated_user()
        repos = u.get_starred(sort="updated", direction="asc", per_page=1)
        self.assertEqual([r.full_name for r in repos], ["ghe-user-1/repo-user-1-2", "ghe-user-1/repo-user-1-1"])

    @Enterprise.User(3)
    def testAddToAndRemoveFromStarred(self):
        u = self.g.get_authenticated_user()
        self.assertTrue(u.has_in_starred(("ghe-user-1", "repo-user-1-2")))
        u.remove_from_starred(("ghe-user-1", "repo-user-1-2"))
        self.assertFalse(u.has_in_starred(("ghe-user-1", "repo-user-1-2")))
        u.add_to_starred(("ghe-user-1", "repo-user-1-2"))
        self.assertTrue(u.has_in_starred(("ghe-user-1", "repo-user-1-2")))

    @Enterprise.User(1)
    def testCreateRepo(self):
        u = self.g.get_authenticated_user()
        r = u.create_repo("spawncamping-wallhack")
        self.assertEqual(r.name, "spawncamping-wallhack")
        self.assertIsNone(r.description)
        self.assertIsNone(r.homepage)
        self.assertEqual(r.private, False)
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        r.delete()

    @Enterprise.User(1)
    def testCreateRepo_allParameters(self):
        u = self.g.get_authenticated_user()
        r = u.create_repo("spawncamping-wallhack", description="Something weird", homepage="http://bar.com", private=True, has_issues=False, has_wiki=False, auto_init=True, gitignore_template="Python", license_template="mit")
        self.assertEqual(r.name, "spawncamping-wallhack")
        self.assertEqual(r.description, "Something weird")
        self.assertEqual(r.homepage, "http://bar.com")
        self.assertEqual(r.private, True)
        self.assertEqual(r.has_issues, False)
        self.assertEqual(r.has_wiki, False)
        r.delete()

    @Enterprise.User(1)
    def testCreateFork(self):
        u = self.g.get_authenticated_user()
        r = u.create_fork(("ghe-org-1", "repo-org-1-2"))
        self.assertEqual(r.full_name, "ghe-user-1/repo-org-1-2")
        r.delete()


class AuthenticatedUserSubscriptions(TestCase):
    @Enterprise.User(2)
    def testGetSubscriptions(self):
        u = self.g.get_authenticated_user()
        subs = u.get_subscriptions()
        self.assertEqual([r.name for r in subs], ["repo-user-1-1", "repo-user-1-2"])

    @Enterprise.User(2)
    def testGetSubscriptions_allParameters(self):
        u = self.g.get_authenticated_user()
        subs = u.get_subscriptions(per_page=1)
        self.assertEqual([r.name for r in subs], ["repo-user-1-1", "repo-user-1-2"])

    @Enterprise.User(2)
    def testGetSubscription(self):
        u = self.g.get_authenticated_user()
        s = u.get_subscription(("ghe-user-1", "repo-user-1-1"))
        self.assertEqual(s.repository_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1")

    @Enterprise.User(2)
    def testCreateSubscription(self):
        u = self.g.get_authenticated_user()
        s = u.create_subscription(("ghe-user-1", "repo-user-1-1"), subscribed=False, ignored=True)
        self.assertEqual(s.subscribed, False)
        self.assertEqual(s.ignored, True)
        s = u.create_subscription(("ghe-user-1", "repo-user-1-1"), subscribed=False, ignored=False)
        self.assertEqual(s.subscribed, True)
        self.assertEqual(s.ignored, False)
