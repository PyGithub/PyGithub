# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class EntityAttributes(TestCase):
    @Enterprise("zeus")
    def testEnterpriseUser(self):
        u = self.g.get_user("antigone")
        self.assertEqual(u.avatar_url, "http://github.home.jacquev6.net/identicons/9bf31c7ff062936a96d3c8bd1f8f2ff3.png")
        self.assertEqual(u.blog, "http://jacquev6.net/antigone")
        self.assertEqual(u.collaborators, 0)
        self.assertEqual(u.company, "Antigone Software")
        self.assertEqual(u.created_at, datetime.datetime(2014, 8, 2, 16, 54, 38))
        self.assertEqual(u.disk_usage, 0)
        self.assertEqual(u.email, "ghe-antigone@jacquev6.net")
        self.assertEqual(u.events_url, "http://github.home.jacquev6.net/api/v3/users/antigone/events{/privacy}")
        self.assertEqual(u.followers, 0)
        self.assertEqual(u.following, 0)
        self.assertEqual(u.html_url, "http://github.home.jacquev6.net/antigone")
        self.assertEqual(u.id, 15)
        self.assertEqual(u.location, "Greece")
        self.assertEqual(u.login, "antigone")
        self.assertEqual(u.name, "Antigone")
        self.assertEqual(u.owned_private_repos, 0)
        self.assertEqual(u.plan, None)
        self.assertEqual(u.private_gists, 0)
        self.assertEqual(u.public_gists, 0)
        self.assertEqual(u.public_repos, 0)
        self.assertEqual(u.repos_url, "http://github.home.jacquev6.net/api/v3/users/antigone/repos")
        self.assertEqual(u.total_private_repos, 0)
        self.assertEqual(u.type, "User")
        self.assertEqual(u.updated_at, datetime.datetime(2014, 8, 2, 18, 6))

    @DotCom
    def testDotComUser(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.company, "Amazon")
        self.assertEqual(u.plan.collaborators, 0)
        self.assertEqual(u.plan.name, "micro")
        self.assertEqual(u.plan.private_repos, 5)
        self.assertEqual(u.plan.space, 614400)


class EntityUpdate(TestCase):
    @Enterprise.User(1)
    def testThroughEdit(self):
        o = self.g.get_org("ghe-org-1")
        o.edit()
