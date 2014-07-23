# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class EntityAttributes(TestCase):
    @Enterprise.User(1)
    def testEnterpriseUser(self):
        u = self.g.get_user("ghe-user-1")
        self.assertEqual(u.avatar_url, "http://github.home.jacquev6.net/identicons/a87ff679a2f3e71d9181a67b7542122c.png")
        self.assertEqual(u.blog, "http://jacquev6.net/ghe-user-1")
        self.assertEqual(u.collaborators, 0)
        self.assertIsNone(u.company)
        self.assertEqual(u.created_at, datetime.datetime(2014, 7, 13, 0, 50, 43))
        self.assertEqual(u.disk_usage, 436)
        self.assertEqual(u.email, "ghe-user-1@jacquev6.net")
        self.assertEqual(u.events_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-1/events{/privacy}")
        self.assertEqual(u.followers, 0)
        self.assertEqual(u.following, 4)
        self.assertEqual(u.html_url, "http://github.home.jacquev6.net/ghe-user-1")
        self.assertEqual(u.id, 4)
        self.assertEqual(u.location, "Venus")
        self.assertEqual(u.login, "ghe-user-1")
        self.assertEqual(u.name, "One Ghe")
        self.assertEqual(u.owned_private_repos, 1)
        self.assertIsNone(u.plan)
        self.assertEqual(u.private_gists, 0)
        self.assertEqual(u.public_gists, 0)
        self.assertEqual(u.public_repos, 2)
        self.assertEqual(u.repos_url, "http://github.home.jacquev6.net/api/v3/users/ghe-user-1/repos")
        self.assertIsNone(u.suspended_at)
        self.assertEqual(u.total_private_repos, 1)
        self.assertEqual(u.type, "User")
        self.assertEqual(u.updated_at, datetime.datetime(2014, 7, 22, 3, 1, 15))

    @Enterprise.Admin(1)
    def testEnterpriseSuspendedUser(self):
        u = self.g.get_user("ghe-suspended-1")
        self.assertEqual(u.suspended_at, datetime.datetime(2014, 7, 13, 13, 56, 27))

    @Enterprise.User(1)
    def testEnterpriseOrg(self):
        o = self.g.get_org("ghe-org-1")
        self.assertIsNone(o.plan.collaborators)
        self.assertEqual(o.plan.name, "enterprise")
        self.assertEqual(o.plan.private_repos, 999999999999)
        self.assertEqual(o.plan.space, 976562499)

    @DotCom
    def testDotComUser(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.company, "Amazon")
        self.assertEqual(u.plan.collaborators, 0)


class EntityUpdate(TestCase):
    @Enterprise.User(1)
    def testThroughEdit(self):
        o = self.g.get_org("ghe-org-1")
        o.edit()
