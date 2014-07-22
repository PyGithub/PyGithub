# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class ContributorAttributes(TestCase):
    @Enterprise.User(1)
    def test(self):
        c = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_contributors()[0]
        self.assertEqual(c.contributions, 1)


class ContributorUpdate(TestCase):
    @Enterprise.User(1)
    def testUpdatePartialObject(self):
        c = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_contributors()[0]
        self.assertTrue(c.update())
