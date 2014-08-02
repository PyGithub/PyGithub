# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class UserAttributes(TestCase):
    @Enterprise("zeus")
    def testEnterpriseUser(self):
        u = self.g.get_user("antigone")
        self.assertEqual(u.followers_url, "http://github.home.jacquev6.net/api/v3/users/antigone/followers")
        self.assertEqual(u.following_url, "http://github.home.jacquev6.net/api/v3/users/antigone/following{/other_user}")
        self.assertEqual(u.gists_url, "http://github.home.jacquev6.net/api/v3/users/antigone/gists{/gist_id}")
        self.assertEqual(u.gravatar_id, "22204000fcc2173ab585271509092a31")
        self.assertEqual(u.hireable, False)
        self.assertEqual(u.organizations_url, "http://github.home.jacquev6.net/api/v3/users/antigone/orgs")
        self.assertEqual(u.received_events_url, "http://github.home.jacquev6.net/api/v3/users/antigone/received_events")
        self.assertEqual(u.site_admin, False)
        self.assertEqual(u.starred_url, "http://github.home.jacquev6.net/api/v3/users/antigone/starred{/owner}{/repo}")
        self.assertEqual(u.subscriptions_url, "http://github.home.jacquev6.net/api/v3/users/antigone/subscriptions")
        self.assertEqual(u.suspended_at, None)

    @Enterprise("zeus")
    def testEnterpriseAdmin(self):
        u = self.g.get_user("poseidon")
        self.assertEqual(u.site_admin, True)

    @Enterprise("zeus")
    def testEnterpriseSuspendedUser(self):
        u = self.g.get_user("morpheus")
        self.assertEqual(u.suspended_at, datetime.datetime(2014, 8, 2, 16, 49, 10))


class UserFollowing(TestCase):
    @Enterprise.User(2)
    def testGetFollowing(self):
        u = self.g.get_user("ghe-user-1")
        following = u.get_following()
        self.assertEqual([f.login for f in following], ["ghe-admin-1", "ghe-user-2", "ghe-user-3", "ghe-admin-2"])

    @Enterprise.User(2)
    def testGetFollowing_allParameters(self):
        u = self.g.get_user("ghe-user-1")
        following = u.get_following(per_page=2)
        self.assertEqual([f.login for f in following], ["ghe-admin-1", "ghe-user-2", "ghe-user-3", "ghe-admin-2"])

    @Enterprise.User(2)
    def testGetFollowers(self):
        u = self.g.get_user("ghe-user-3")
        followers = u.get_followers()
        self.assertEqual([f.login for f in followers], ["ghe-admin-1", "ghe-user-1", "ghe-user-2", "ghe-admin-2"])

    @Enterprise.User(2)
    def testGetFollowers_allParameters(self):
        u = self.g.get_user("ghe-user-3")
        followers = u.get_followers(per_page=2)
        self.assertEqual([f.login for f in followers], ["ghe-user-1", "ghe-admin-1", "ghe-admin-2", "ghe-user-2"])

    @Enterprise.User(2)
    def testHasInFollowing(self):
        self.assertTrue(self.g.get_user("ghe-user-1").has_in_following("ghe-user-3"))
        self.assertFalse(self.g.get_user("ghe-user-3").has_in_following("ghe-user-1"))


class UserGists(TestCase):
    @Enterprise.User(2)
    def testGetGists(self):
        u = self.g.get_user("ghe-user-1")
        gists = u.get_gists()
        self.assertEqual([g.description for g in gists], ["gist-user-1-2", "gist-user-1-1"])

    @Enterprise.User(2)
    def testGetGists_allParameters(self):
        u = self.g.get_user("ghe-user-1")
        gists = u.get_gists(since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([g.description for g in gists], ["gist-user-1-2", "gist-user-1-1"])


class UserKeys(TestCase):
    @Enterprise.User(2)
    def testGetKeys(self):
        u = self.g.get_user("ghe-user-1")
        keys = u.get_keys()
        self.assertEqual([k.id for k in keys], [1, 3])
        self.assertEqual(keys[0].key, "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCiJEA/bsVMx3SfCH6F8/mh+EtP6/g+G5L862NqdbaAIC0kZr3ZFcmOYIWyed2KAFH4ZT7/7yFyMH1UWQ4s7Z3EHH7jwszk9QRSa7cGz1aLVL2xyPVjeur98nQnNxV6fRZjVA6ujL8hJqPfDbybLBrwgX3p424VGfQjXAugVoKNjtn4BAE4mmpRybNgeFWhMEP5i043n4b4nVz5n+K2iCJ83hvMIO4O7JIakfwZcg0MyXrsVGj30aMboZ3OjmE9rmIFZkUAsb9BCVorql2yx4VeMxzxvTUQnkLNGC5HDb+nceSVUQ5wew+6bS2uOa3so1dQIpIW8FXktPF6mWJfqiJB")


class UserOrganizations(TestCase):
    @Enterprise.User(2)
    def testGetOrgs(self):
        u = self.g.get_user("ghe-user-1")
        orgs = u.get_orgs()
        self.assertEqual([o.login for o in orgs], ["ghe-org-2"])

    @Enterprise.User(1)
    def testGetSelfOrgs_allParameters(self):
        u = self.g.get_user("ghe-user-1")
        orgs = u.get_orgs(per_page=1)
        self.assertEqual([o.login for o in orgs], ["ghe-org-1", "ghe-org-2"])


class UserRepositories(TestCase):
    @Enterprise.User(2)
    def testGetRepo(self):
        r = self.g.get_user("ghe-user-1").get_repo("repo-user-1-1")
        self.assertEqual(r.full_name, "ghe-user-1/repo-user-1-1")

    @Enterprise.User(2)
    def testGetRepos(self):
        u = self.g.get_user("ghe-user-1")
        repos = u.get_repos()
        self.assertEqual([r.name for r in repos], ["repo-user-1-1", "repo-user-1-2"])

    @Enterprise.User(1)
    def testGetSelfRepos_allParameters(self):
        u = self.g.get_user("ghe-user-1")
        repos = u.get_repos(type="sources", sort="created", direction="desc", per_page=1)
        self.assertEqual([r.name for r in repos], ["repo-user-1-2", "repo-user-1-1"])

    @Enterprise.User(2)
    def testGetStarred(self):
        u = self.g.get_user("ghe-user-3")
        repos = u.get_starred()
        self.assertEqual([r.name for r in repos], ["repo-user-1-2", "repo-user-1-1"])

    @Enterprise.User(2)
    def testGetStarred_allParameters(self):
        u = self.g.get_user("ghe-user-3")
        repos = u.get_starred(sort="updated", direction="asc", per_page=3)
        self.assertEqual([r.name for r in repos], ["repo-user-1-2", "repo-user-1-1"])

    @Enterprise.User(2)
    def testGetSubscriptions(self):
        u = self.g.get_user("ghe-user-3")
        repos = u.get_subscriptions()
        self.assertEqual([r.name for r in repos], ["repo-user-1-2"])

    @Enterprise.User(2)
    def testGetSubscriptions_allParameters(self):
        u = self.g.get_user("ghe-user-3")
        repos = u.get_subscriptions(per_page=3)
        self.assertEqual([r.name for r in repos], ["repo-user-1-2"])


class UserUpdate(TestCase):
    @Enterprise.User(1)
    def testThroughEdit(self):
        u = self.g.get_user("ghe-user-1")
        self.g.get_authenticated_user().edit(name="One Ghe")
