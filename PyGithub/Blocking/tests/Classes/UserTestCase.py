# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


# @todoAlpha What is happening when a suspended enterprise user tries to do anything?

class UserAttributes(TestCase):
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


class UserTestCase(SimpleLoginTestCase):
    def testGetFollowers(self):
        followers = self.g.get_user("nvie").get_followers()
        self.assertEqual(followers[0].login, "vidbina")
        self.assertEqual(followers[1].login, "nirmalkumarv")

    def testGetFollowers_allParameters(self):
        followers = self.g.get_user("nvie").get_followers(per_page=3)
        self.assertEqual(followers[0].login, "vidbina")
        self.assertEqual(followers[1].login, "nirmalkumarv")

    def testGetFollowing(self):
        following = self.g.get_user("nvie").get_following()
        self.assertEqual(following[0].login, "defunkt")
        self.assertEqual(following[1].login, "brosner")

    def testGetFollowing_allParameters(self):
        following = self.g.get_user("nvie").get_following(per_page=3)
        self.assertEqual(following[0].login, "defunkt")
        self.assertEqual(following[1].login, "brosner")

    def testGetOrgs(self):
        orgs = self.g.get_user("defunkt").get_orgs()
        self.assertEqual(orgs[0].login, "github")
        self.assertEqual(orgs[1].login, "mustache")

    def testGetOrgs_allParameters(self):
        orgs = self.g.get_user("defunkt").get_orgs(per_page=3)
        self.assertEqual(orgs[0].login, "github")
        self.assertEqual(orgs[1].login, "mustache")

    def testGetRepo(self):
        repo = self.g.get_user("nvie").get_repo("gitflow")
        self.assertEqual(repo.full_name, "nvie/gitflow")

    def testGetRepos(self):
        repos = self.g.get_user("nvie").get_repos()
        self.assertEqual(repos[0].name, "activerecord-fetching-for-core-data")
        self.assertEqual(repos[1].name, "ADCtheme")

    def testGetRepos_allParameters(self):
        repos = self.g.get_user("nvie").get_repos(type="forks", sort="created", direction="desc", per_page=3)
        self.assertEqual(repos[0].name, "pyflakes")
        self.assertEqual(repos[1].name, "homebrew-autoenv")

    def testGetStarred(self):
        repos = self.g.get_user("nvie").get_starred()
        self.assertEqual(repos[0].full_name, "alfredodeza/pytest.vim")
        self.assertEqual(repos[1].full_name, "AndrewDryga/jQuery.Textarea.Autoresize")

    def testGetStarred_allParameters(self):
        repos = self.g.get_user("nvie").get_starred(sort="updated", direction="desc", per_page=3)
        self.assertEqual(repos[0].full_name, "github/hub")
        self.assertEqual(repos[1].full_name, "holman/spark")

    def testGetSubscriptions(self):
        repos = self.g.get_user("nvie").get_subscriptions()
        self.assertEqual(repos[0].full_name, "ask/carrot")
        self.assertEqual(repos[1].full_name, "nvie/git-it")

    def testGetSubscriptions_allParameters(self):
        repos = self.g.get_user("nvie").get_subscriptions(per_page=3)
        self.assertEqual(repos[0].full_name, "ask/carrot")
        self.assertEqual(repos[1].full_name, "nvie/git-it")

    def testHasInFollowing(self):
        nvie = self.g.get_user("nvie")
        jacquev6 = self.g.get_user("jacquev6")
        self.assertTrue(jacquev6.has_in_following("nvie"))
        self.assertFalse(nvie.has_in_following("jacquev6"))

    def testGetKeys(self):
        keys = self.g.get_user("nvie").get_keys()
        self.assertEqual(len(keys), 5)
        self.assertEqual(keys[0].id, 112610)
        self.assertEqual(keys[1].id, 116764)

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
