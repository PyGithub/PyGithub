# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking

import PyGithub.Blocking.tests.Framework as Framework


class AuthenticatedUserTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        u = self.g.get_authenticated_user()
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
        self.assertEqual(u.updated_at, datetime.datetime(2013, 12, 20, 6, 27, 49))
        self.assertEqual(u.url, "https://api.github.com/users/jacquev6")

    def testGetFollowers(self):
        followers = self.g.get_authenticated_user().get_followers()
        self.assertEqual(followers[0].login, "regisb")
        self.assertEqual(followers[1].login, "jnorthrup")

    def testGetFollowers_allParameters(self):
        followers = self.g.get_authenticated_user().get_followers(per_page=3)
        self.assertEqual(followers[0].login, "regisb")
        self.assertEqual(followers[1].login, "jnorthrup")

    def testGetFollowing(self):
        following = self.g.get_authenticated_user().get_following()
        self.assertEqual(following[0].login, "schacon")
        self.assertEqual(following[1].login, "chad")

    def testGetFollowing_allParameters(self):
        following = self.g.get_authenticated_user().get_following(per_page=3)
        self.assertEqual(following[0].login, "schacon")
        self.assertEqual(following[1].login, "chad")

    def testGetOrgs(self):
        orgs = self.g.get_authenticated_user().get_orgs()
        self.assertEqual(orgs[0].login, "BeaverSoftware")

    def testGetOrgs_allParameters(self):
        orgs = self.g.get_authenticated_user().get_orgs(per_page=3)
        self.assertEqual(orgs[0].login, "BeaverSoftware")

    def testGetRepo(self):
        repo = self.g.get_authenticated_user().get_repo("PyGithub")
        self.assertEqual(repo.full_name, "jacquev6/PyGithub")

    def testGetRepos(self):
        repos = self.g.get_authenticated_user().get_repos()
        self.assertEqual(repos[0].name, "ActionTree")
        self.assertEqual(repos[1].name, "AnotherPyGraphvizAgain")

    def testGetRepos_allParameters(self):
        repos = self.g.get_authenticated_user().get_repos(type="private", sort="created", direction="desc", per_page=3)
        self.assertEqual(repos[0].name, "Hacking")
        self.assertEqual(repos[1].name, "vincent-jacques.net")

    def testGetStarred(self):
        repos = self.g.get_authenticated_user().get_starred()
        self.assertEqual(repos[0].full_name, "nvie/gitflow")
        self.assertEqual(repos[1].full_name, "idank/explainshell")

    def testGetStarred_allParameters(self):
        repos = self.g.get_authenticated_user().get_starred(sort="updated", direction="desc", per_page=3)
        self.assertEqual(repos[0].full_name, "django/django")
        self.assertEqual(repos[1].full_name, "github/hub")

    def testGetSubscriptions(self):
        repos = self.g.get_authenticated_user().get_subscriptions()
        self.assertEqual(repos[0].full_name, "jacquev6/ViDE")
        self.assertEqual(repos[1].full_name, "jacquev6/Boost.HierarchicalEnum")

    def testGetSubscriptions_allParameters(self):
        repos = self.g.get_authenticated_user().get_subscriptions(per_page=3)
        self.assertEqual(repos[0].full_name, "jacquev6/ViDE")
        self.assertEqual(repos[1].full_name, "jacquev6/Boost.HierarchicalEnum")

    def testAddRemoveFollowing(self):
        u = self.g.get_authenticated_user()
        self.assertTrue(u.has_in_following("Lyloa"))
        u.remove_from_following("Lyloa")
        self.assertFalse(u.has_in_following("Lyloa"))
        u.add_to_following("Lyloa")
        self.assertTrue(u.has_in_following("Lyloa"))

    def testAddRemoveStarred(self):
        u = self.g.get_authenticated_user()
        self.assertTrue(u.has_in_starred("nvie/gitflow"))
        u.remove_from_starred("nvie/gitflow")
        self.assertFalse(u.has_in_starred("nvie/gitflow"))
        u.add_to_starred("nvie/gitflow")
        self.assertTrue(u.has_in_starred("nvie/gitflow"))

    def testAddRemoveSubscriptions(self):
        u = self.g.get_authenticated_user()
        self.assertTrue(u.has_in_subscriptions("abersager/PyGithub"))
        u.remove_from_subscriptions("abersager/PyGithub")
        self.assertFalse(u.has_in_subscriptions("abersager/PyGithub"))
        u.add_to_subscriptions("abersager/PyGithub")
        self.assertTrue(u.has_in_subscriptions("abersager/PyGithub"))

    def testGetSubscription(self):
        u = self.g.get_authenticated_user()
        s = u.get_subscription("abersager/PyGithub")
        self.assertEqual(s.subscribed, True)
        self.assertEqual(s.ignored, False)
        self.assertEqual(s.url, "https://api.github.com/repos/abersager/PyGithub/subscription")
        self.assertEqual(s.repository_url, "https://api.github.com/repos/abersager/PyGithub")
        self.assertEqual(s.reason, None)
        self.assertEqual(s.created_at, datetime.datetime(2013, 12, 20, 6, 27, 57))

    def testGetUnexistingSubscription(self):
        u = self.g.get_authenticated_user()
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            s = u.get_subscription("wootook/wootook")

    def testDeleteSetSubscription(self):
        u = self.g.get_authenticated_user()
        s = u.get_subscription("abersager/PyGithub")
        s.delete()
        s = u.create_subscription("abersager/PyGithub", subscribed=True, ignored=False)
        self.assertEqual(s.subscribed, True)
        self.assertEqual(s.ignored, False)
        self.assertEqual(s.created_at, datetime.datetime(2013, 12, 22, 22, 48, 41))

    def testEditName(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.name, "Vincent Jacques")
        u.edit(name=PyGithub.Blocking.Reset)
        self.assertEqual(u.name, None)
        u.edit(name="Vincent Jacques")
        self.assertEqual(u.name, "Vincent Jacques")

    def testEditEmail(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.email, "vincent@vincent-jacques.net")
        u.edit(email=PyGithub.Blocking.Reset)
        self.assertEqual(u.email, None)
        u.edit(email="vincent@vincent-jacques.net")
        self.assertEqual(u.email, "vincent@vincent-jacques.net")

    def testEditBlog(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.blog, "http://vincent-jacques.net")
        u.edit(blog=PyGithub.Blocking.Reset)
        self.assertEqual(u.blog, None)
        u.edit(blog="http://vincent-jacques.net")
        self.assertEqual(u.blog, "http://vincent-jacques.net")

    def testEditCompany(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.company, "Amazon")
        u.edit(company=PyGithub.Blocking.Reset)
        self.assertEqual(u.company, None)
        u.edit(company="Amazon")
        self.assertEqual(u.company, "Amazon")

    def testEditHireable(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.hireable, False)
        u.edit(hireable=PyGithub.Blocking.Reset)
        self.assertEqual(u.hireable, None)
        u.edit(hireable=False)
        self.assertEqual(u.hireable, False)

    def testEditLocation(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.location, "Seattle, WA, United States")
        u.edit(location=PyGithub.Blocking.Reset)
        self.assertEqual(u.location, None)
        u.edit(location="Seattle, WA, United States")
        self.assertEqual(u.location, "Seattle, WA, United States")

    def testEditNothing(self):
        u = self.g.get_authenticated_user()
        u.edit()

    def testCreateFork(self):
        u = self.g.get_authenticated_user()
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            u.get_repo("whisper")
        fork = u.create_fork("graphite-project/whisper")
        self.assertEqual(fork.full_name, "jacquev6/whisper")
        fork.delete()

    def testCreateRepo(self):
        u = self.g.get_authenticated_user()
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            u.get_repo("turbo-octo-ironman")
        repo = u.create_repo("turbo-octo-ironman")
        self.assertEqual(repo.full_name, "jacquev6/turbo-octo-ironman")
        repo.delete()

    def testCreateRepo_allParameters(self):
        u = self.g.get_authenticated_user()
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            u.get_repo("potential-octo-lana")
        repo = u.create_repo("potential-octo-lana", description="Created with PyGithub v2", has_issues=False, has_wiki=False, private=True, auto_init=True, gitignore_template="C", homepage="http://foo.bar", has_downloads=False, license_template="mozilla")
        self.assertEqual(repo.full_name, "jacquev6/potential-octo-lana")
        repo.delete()

    def testGetTeams(self):
        u = self.g.get_authenticated_user()
        teams = u.get_teams()
        self.assertEqual(teams[0].name, "Owners")
        self.assertEqual(teams[1].name, "Honoraries")

    def testGetTeams_allParameters(self):
        u = self.g.get_authenticated_user()
        teams = u.get_teams(per_page=2)
        self.assertEqual(teams[0].name, "Owners")
        self.assertEqual(teams[1].name, "Honoraries")

    def testGetKeys(self):
        keys = self.g.get_authenticated_user().get_keys()
        self.assertEqual(len(keys), 2)
        self.assertEqual(keys[0].id, 4051357)
        self.assertEqual(keys[1].id, 6227290)

    def testGetKey(self):
        key = self.g.get_authenticated_user().get_key(4051357)
        self.assertEqual(key.title, "vincent@home")

    def testCreateKey(self):
        key = self.g.get_authenticated_user().create_key("vincent@test", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkQih2DtSwBzLUtSNYEKULlI5M1qa6vnq42xt9qZpkLav3G9eD/GqJRST+zZMsyfpP62PtiYKXJdLJX2MQIzUgI2PzNy+iMy+ldiTEABYEOCa+BH9+x2R5xXGlmmCPblpamx3kstGtCTa3LSkyIvxbt5vjbXCyThhJaSKyh+42Uedcz7l0y/TODhnkpid/5eiBz6k0VEbFfhM6h71eBdCFpeMJIhGaPTjbKsEjXIK0SRe0v0UQnpXJQkhAINbm+q/2yjt7zwBF74u6tQjRqJK7vQO2k47ZmFMAGeIxS6GheI+JPmwtHkxvfaJjy2lIGX+rt3lkW8xEUxiMTlxeh+0R")
        self.assertEqual(key.id, 7229148)
