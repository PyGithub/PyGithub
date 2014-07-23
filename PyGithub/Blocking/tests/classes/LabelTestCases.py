# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class LabelAttributes(TestCase):
    @Enterprise.User(1)
    def test(self):
        l = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_label("bug")
        self.assertEqual(l.color, "fc2929")
        self.assertEqual(l.name, "bug")
        self.assertEqual(l.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/labels/bug")


class LabelEdit(TestCase):
    @Enterprise.User(1)
    def testName(self):
        l = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_label("bug")
        self.assertEqual(l.name, "bug")
        l.edit(name="feature")
        self.assertEqual(l.name, "feature")
        l.edit(name="bug")
        self.assertEqual(l.name, "bug")

    @Enterprise.User(1)
    def testColor(self):
        l = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_label("bug")
        self.assertEqual(l.color, "fc2929")
        l.edit(color="aabbcc")
        self.assertEqual(l.color, "aabbcc")
        l.edit(color="fc2929")
        self.assertEqual(l.color, "fc2929")
