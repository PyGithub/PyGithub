# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.tests.Framework as Framework
from PyGithub.Blocking.tests.Framework import *


class GitTagAttributes(TestCase):
    @Enterprise.User(1)
    def testCommitTag(self):
        # @todoAlpha testTreeTag and testBlobTag
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        t = r.get_git_tag("43bafe50b11378c5546dbef02032941bb8a46099")
        self.assertEqual(t.message, "Heavy tag\n")
        self.assertEqual(t.object.type, "commit")
        self.assertEqual(t.object.sha, "7820fadc2429652016611e98fdc21766ba075161")
        self.assertEqual(t.object.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/git/commits/7820fadc2429652016611e98fdc21766ba075161")
        self.assertEqual(t.sha, "43bafe50b11378c5546dbef02032941bb8a46099")
        self.assertEqual(t.tag, "v0.1-beta.2")
        self.assertEqual(t.tagger.name, "Vincent Jacques")
        self.assertEqual(t.tagger.email, "vincent@vincent-jacques.net")
        self.assertEqual(t.tagger.date, datetime.datetime(2014, 7, 18, 2, 30, 36))
        self.assertEqual(t.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/git/tags/43bafe50b11378c5546dbef02032941bb8a46099")
