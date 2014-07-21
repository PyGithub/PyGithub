# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


# @todoAlpha What is happening when a suspended enterprise user tries to do anything?

class UserAttributes(TestCase):
    """
    Preconditions on GitHub Enterprise:
    * ghe-user-2 has set their name/location/blog
    * ghe-user-3 has not
    * ghe-suspended-1 is suspended (!)
    """

    @Enterprise.User(1)
    def testEnterpriseUserOnUser(self):
        u = self.g.get_user("ghe-user-2")
        self.assertEqual(u.avatar_url, "http://github.home.jacquev6.net/identicons/e4da3b7fbbce2345d7772b0674a318d5.png")
        self.assertEqual(u.blog, "http://jacquev6.net/ghe-user-2")
        self.assertIsNone(u.collaborators)
        self.assertIsNone(u.company)
        self.assertEqual(u.created_at, datetime.datetime(2014, 7, 13, 1, 36, 27))
        self.assertIsNone(u.disk_usage)
        self.assertEqual(u.email, "ghe-user-2@jacquev6.net")
        self.assertEqual(u.events_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-2/events{/privacy}")
        self.assertEqual(u.followers, 0)
        self.assertEqual(u.followers_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-2/followers")
        self.assertEqual(u.following, 0)
        self.assertEqual(u.following_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-2/following{/other_user}")
        self.assertEqual(u.gists_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-2/gists{/gist_id}")
        self.assertEqual(u.gravatar_id, "193685b48463fc3ddb5d694e80118276")
        self.assertFalse(u.hireable)
        self.assertEqual(u.html_url, "http://github.home.jacquev6.net/ghe-user-2")
        self.assertEqual(u.id, 5)
        self.assertEqual(u.location, "Earth")
        self.assertEqual(u.login, "ghe-user-2")
        self.assertEqual(u.name, "Two Ghe")
        self.assertEqual(u.organizations_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-2/orgs")
        self.assertIsNone(u.owned_private_repos)
        self.assertIsNone(u.plan)
        self.assertIsNone(u.private_gists)
        self.assertEqual(u.public_gists, 0)
        self.assertEqual(u.public_repos, 0)
        self.assertEqual(u.received_events_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-2/received_events")
        self.assertEqual(u.repos_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-2/repos")
        self.assertFalse(u.site_admin)
        self.assertEqual(u.starred_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-2/starred{/owner}{/repo}")
        self.assertEqual(u.subscriptions_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-2/subscriptions")
        self.assertIsNone(u.suspended_at)
        self.assertEqual(u.type, "User")
        self.assertEqual(u.updated_at, datetime.datetime(2014, 7, 13, 14, 7, 2))
        self.assertEqual(u.url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-2")

    @Enterprise.User(2)
    def testEnterpriseUserOnSelf(self):
        u = self.g.get_user("ghe-user-2")
        self.assertEqual(u.collaborators, 0)
        self.assertEqual(u.disk_usage, 0)
        self.assertEqual(u.owned_private_repos, 0)
        self.assertEqual(u.private_gists, 0)
        self.assertEqual(u.total_private_repos, 0)

    @Enterprise.User(1)
    def testEnterpriseUserOnSuspendedUser(self):
        u = self.g.get_user("ghe-suspended-1")
        self.assertEqual(u.suspended_at, datetime.datetime(2014, 7, 13, 13, 56, 27))

    @Enterprise.User(1)
    def testEnterpriseUserOnDiscreteUser(self):
        u = self.g.get_user("ghe-user-3")
        self.assertIsNone(u.name)
        self.assertIsNone(u.location)
        self.assertIsNone(u.email)
        self.assertIsNone(u.blog)
        self.assertIsNone(u.hireable)

    @Enterprise.User(1)
    def testEnterpriseUserOnAdmin(self):
        u = self.g.get_user("ghe-admin-1")
        self.assertTrue(u.site_admin)

    @DotCom
    def testDotComUserOnUser(self):
        u = self.g.get_user("nvie")
        self.assertEqual(u.url, "https://api.github.com/users/nvie")
        self.assertEqual(u.company, "3rd Cloud")
        self.assertTrue(u.hireable)
        self.assertIsNone(u.suspended_at)

    @DotCom
    def testDotComUserOnSelf(self):
        u = self.g.get_user("jacquev6")
        self.assertEqual(u.plan.collaborators, 0)
        self.assertEqual(u.plan.name, "micro")
        self.assertEqual(u.plan.private_repos, 5)
        self.assertEqual(u.plan.space, 614400)


class UserFollowing(TestCase):
    """
    Preconditions on GitHub Enterprise:
    * ghe-user-1 is following everyone
    * everyone follows ghe-user-3
    """

    @Enterprise.User(2)
    def testGetFollowing(self):
        user = self.g.get_user("ghe-user-1")
        self.assertEqual(user.following, 4)
        following = user.get_following()
        self.assertEqual([f.login for f in following], ["ghe-admin-1", "ghe-user-2", "ghe-user-3", "ghe-admin-2"])

    @Enterprise.User(2)
    def testGetFollowing_allParameters(self):
        user = self.g.get_user("ghe-user-1")
        self.assertEqual(user.following, 4)
        following = user.get_following(per_page=2)
        self.assertEqual([f.login for f in following], ["ghe-admin-1", "ghe-user-2", "ghe-user-3", "ghe-admin-2"])

    @Enterprise.User(2)
    def testGetFollowers(self):
        user = self.g.get_user("ghe-user-3")
        self.assertEqual(user.followers, 4)
        followers = user.get_followers()
        self.assertEqual([f.login for f in followers], ["ghe-admin-1", "ghe-user-1", "ghe-user-2", "ghe-admin-2"])

    @Enterprise.User(2)
    def testGetFollowers_allParameters(self):
        user = self.g.get_user("ghe-user-3")
        self.assertEqual(user.followers, 4)
        followers = user.get_followers(per_page=2)
        self.assertEqual([f.login for f in followers], ["ghe-user-1", "ghe-admin-1", "ghe-admin-2", "ghe-user-2"])

    @Enterprise.User(2)
    def testHasInFollowing(self):
        user1 = self.g.get_user("ghe-user-1")
        user3 = self.g.get_user("ghe-user-3")
        self.assertTrue(user1.has_in_following(user3))
        self.assertFalse(user3.has_in_following(user1))


class UserMisc(TestCase):
    """
    Preconditions on GitHub Enterprise:
    * ghe-user-1 has two keys
    """

    @DotCom  # To cover updating the 'plan' attribute
    def testUpdate(self):
        user = self.g.get_user("jacquev6")
        authUser = self.g.get_authenticated_user()
        self.assertEqual(user.name, "Vincent Jacques")
        authUser.edit(name="Vincent Jacques - edited")
        self.assertTrue(user.update())
        self.assertEqual(user.name, "Vincent Jacques - edited")
        self.assertFalse(user.update())
        authUser.edit(name="Vincent Jacques")

    @Enterprise.User(2)
    def testGetKeys(self):
        user = self.g.get_user("ghe-user-1")
        keys = user.get_keys()
        self.assertEqual([k.id for k in keys], [1, 3])


class UserOrganizations(TestCase):
    """
    Preconditions on GitHub Enterprise:
    * ghe-user-1 is a private member of ghe-org-1 and a public member of ghe-org-2
    """

    @Enterprise.User(2)
    def testGetOrgs(self):
        user = self.g.get_user("ghe-user-1")
        orgs = user.get_orgs()
        self.assertEqual([o.login for o in orgs], ["ghe-org-2"])

    @Enterprise.User(1)
    def testGetSelfOrgs_allParameters(self):
        user = self.g.get_user("ghe-user-1")
        orgs = user.get_orgs(per_page=1)
        self.assertEqual([o.login for o in orgs], ["ghe-org-1", "ghe-org-2"])


class UserRepositories(TestCase):
    """
    Preconditions on GitHub Enterprise:
    * ghe-user-1 has a two public repos repo-user-1-1 and repo-user-1-2 and one private repo repo-user-1-3
    * ghe-user-3 has starred repo-user-1-1 and starred and subscribed to repo-user-1-2
    """

    @Enterprise.User(2)
    def testGetRepo(self):
        repo = self.g.get_user("ghe-user-1").get_repo("repo-user-1-1")
        self.assertEqual(repo.full_name, "ghe-user-1/repo-user-1-1")

    @Enterprise.User(2)
    def testGetOrgs(self):
        user = self.g.get_user("ghe-user-1")
        repos = user.get_repos()
        self.assertEqual([r.name for r in repos], ["repo-user-1-1", "repo-user-1-2"])

    @Enterprise.User(1)
    def testGetSelfRepos_allParameters(self):
        user = self.g.get_user("ghe-user-1")
        repos = user.get_repos(type="sources", sort="created", direction="desc", per_page=1)
        self.assertEqual([r.name for r in repos], ["repo-user-1-2", "repo-user-1-1"])

    @Enterprise.User(2)
    def testGetStarred(self):
        user = self.g.get_user("ghe-user-3")
        repos = user.get_starred()
        self.assertEqual([r.name for r in repos], ["repo-user-1-2", "repo-user-1-1"])

    @Enterprise.User(2)
    def testGetStarred_allParameters(self):
        user = self.g.get_user("ghe-user-3")
        repos = user.get_starred(sort="updated", direction="asc", per_page=3)
        self.assertEqual([r.name for r in repos], ["repo-user-1-1", "repo-user-1-2"])

    @Enterprise.User(2)
    def testGetSubscriptions(self):
        user = self.g.get_user("ghe-user-3")
        repos = user.get_subscriptions()
        self.assertEqual([r.name for r in repos], ["repo-user-1-2"])

    @Enterprise.User(2)
    def testGetSubscriptions_allParameters(self):
        user = self.g.get_user("ghe-user-3")
        repos = user.get_subscriptions(per_page=3)
        self.assertEqual([r.name for r in repos], ["repo-user-1-2"])


class UserTestCase(SimpleLoginTestCase):
    def testGetGists(self):
        gists = list(self.g.get_user("nvie").get_gists())
        self.assertEqual(len(gists), 39)
        self.assertEqual(gists[0].created_at, datetime.datetime(2013, 11, 29, 8, 59, 2))
        self.assertEqual(gists[38].created_at, datetime.datetime(2009, 12, 17, 9, 15, 52))
        self.assertEqual(gists[0].updated_at, datetime.datetime(2014, 4, 22, 10, 2, 20))
        self.assertEqual(gists[38].updated_at, datetime.datetime(2009, 12, 17, 9, 25, 29))

    def testGetGists_allParameters(self):
        gists = list(self.g.get_user("nvie").get_gists(per_page=3, since=datetime.datetime(2014, 1, 1, 0, 0, 0)))
        self.assertEqual(len(gists), 4)
        self.assertEqual(gists[0].created_at, datetime.datetime(2013, 11, 29, 8, 59, 2))
        self.assertEqual(gists[3].created_at, datetime.datetime(2012, 5, 22, 15, 11, 17))
        self.assertEqual(gists[0].updated_at, datetime.datetime(2014, 4, 22, 10, 2, 20))
        self.assertEqual(gists[3].updated_at, datetime.datetime(2014, 1, 29, 14, 12, 19))
