# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.tests.Framework as Framework


class UserTestCase(Framework.SimpleLoginTestCase):
    def testAttributesOfAuthenticatedUser(self):
        u = self.g.get_user("jacquev6")
        self.assertEqual(u.avatar_url, "https://gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https%3A%2F%2Fidenticons.github.com%2Ffadfb5f7088ef66579d198a3c9a4935e.png&r=x")
        self.assertEqual(u.blog, "http://vincent-jacques.net")
        self.assertEqual(u.collaborators, 0)
        self.assertEqual(u.company, "Amazon")
        self.assertEqual(u.created_at, datetime.datetime(2010, 7, 9, 6, 10, 6))
        self.assertEqual(u.disk_usage, 91985)
        self.assertEqual(u.email, "vincent@vincent-jacques.net")
        self.assertEqual(u.events_url, "https://api.github.com/users/jacquev6/events{/privacy}")
        self.assertEqual(u.followers, 30)
        self.assertEqual(u.followers_url, "https://api.github.com/users/jacquev6/followers")
        self.assertEqual(u.following, 43)
        self.assertEqual(u.following_url, "https://api.github.com/users/jacquev6/following{/other_user}")
        self.assertEqual(u.gists_url, "https://api.github.com/users/jacquev6/gists{/gist_id}")
        self.assertEqual(u.gravatar_id, "b68de5ae38616c296fa345d2b9df2225")
        self.assertEqual(u.hireable, False)
        self.assertEqual(u.html_url, "https://github.com/jacquev6")
        self.assertEqual(u.id, 327146)
        self.assertEqual(u.location, "Seattle, WA, United States")
        self.assertEqual(u.login, "jacquev6")
        self.assertEqual(u.name, "Vincent Jacques")
        self.assertEqual(u.organizations_url, "https://api.github.com/users/jacquev6/orgs")
        self.assertEqual(u.owned_private_repos, 3)
        self.assertEqual(u.plan.collaborators, 1)
        self.assertEqual(u.plan.name, "micro")
        self.assertEqual(u.plan.private_repos, 5)
        self.assertEqual(u.plan.space, 614400)
        self.assertEqual(u.private_gists, 6)
        self.assertEqual(u.public_gists, 5)
        self.assertEqual(u.public_repos, 19)
        self.assertEqual(u.received_events_url, "https://api.github.com/users/jacquev6/received_events")
        self.assertEqual(u.repos_url, "https://api.github.com/users/jacquev6/repos")
        self.assertEqual(u.site_admin, False)
        self.assertEqual(u.starred_url, "https://api.github.com/users/jacquev6/starred{/owner}{/repo}")
        self.assertEqual(u.subscriptions_url, "https://api.github.com/users/jacquev6/subscriptions")
        self.assertEqual(u.total_private_repos, 3)
        self.assertEqual(u.type, "User")
        self.assertEqual(u.updated_at, datetime.datetime(2013, 12, 20, 6, 28, 1))
        self.assertEqual(u.url, "https://api.github.com/users/jacquev6")

    def testAttributesOfOtherUser(self):
        u = self.g.get_user("nvie")
        self.assertEqual(u.avatar_url, "https://gravatar.com/avatar/466ef7561a0b100dc5a1021959962d28?d=https%3A%2F%2Fidenticons.github.com%2Fe6d0513ce49cc06cb956251623cb8fd9.png&r=x")
        self.assertEqual(u.blog, "http://nvie.com")
        self.assertEqual(u.collaborators, None)
        self.assertEqual(u.company, "3rd Cloud")
        self.assertEqual(u.created_at, datetime.datetime(2009, 5, 12, 21, 19, 38))
        self.assertEqual(u.disk_usage, None)
        self.assertEqual(u.email, "vincent@3rdcloud.com")
        self.assertEqual(u.events_url, "https://api.github.com/users/nvie/events{/privacy}")
        self.assertEqual(u.followers, 605)
        self.assertEqual(u.followers_url, "https://api.github.com/users/nvie/followers")
        self.assertEqual(u.following, 45)
        self.assertEqual(u.following_url, "https://api.github.com/users/nvie/following{/other_user}")
        self.assertEqual(u.gists_url, "https://api.github.com/users/nvie/gists{/gist_id}")
        self.assertEqual(u.gravatar_id, "466ef7561a0b100dc5a1021959962d28")
        self.assertEqual(u.hireable, True)
        self.assertEqual(u.html_url, "https://github.com/nvie")
        self.assertEqual(u.id, 83844)
        self.assertEqual(u.location, "Netherlands")
        self.assertEqual(u.login, "nvie")
        self.assertEqual(u.name, "Vincent Driessen")
        self.assertEqual(u.organizations_url, "https://api.github.com/users/nvie/orgs")
        self.assertEqual(u.owned_private_repos, None)
        self.assertEqual(u.plan, None)
        self.assertEqual(u.private_gists, None)
        self.assertEqual(u.public_gists, 39)
        self.assertEqual(u.public_repos, 92)
        self.assertEqual(u.received_events_url, "https://api.github.com/users/nvie/received_events")
        self.assertEqual(u.repos_url, "https://api.github.com/users/nvie/repos")
        self.assertEqual(u.site_admin, False)
        self.assertEqual(u.starred_url, "https://api.github.com/users/nvie/starred{/owner}{/repo}")
        self.assertEqual(u.subscriptions_url, "https://api.github.com/users/nvie/subscriptions")
        self.assertEqual(u.total_private_repos, None)
        self.assertEqual(u.type, "User")
        self.assertEqual(u.updated_at, datetime.datetime(2013, 12, 20, 6, 27, 56))
        self.assertEqual(u.url, "https://api.github.com/users/nvie")

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
