# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.tests.Framework as Framework
from PyGithub.Blocking.tests.Framework import *

# @todoAlpha Put back in RepositoryTestCase.py


class TagAttributes(TestCase):
    @Enterprise.User(1)
    def testCommitTag(self):
        # @todoAlpha testTreeTag and testBlobTag?
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        tag = r.get_tags()[0]
        self.assertEqual(tag.commit.sha, "7820fadc2429652016611e98fdc21766ba075161")
        self.assertEqual(tag.commit.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/commits/7820fadc2429652016611e98fdc21766ba075161")
        self.assertEqual(tag.name, "v0.1-beta.2")
        self.assertEqual(tag.tarball_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/tarball/v0.1-beta.2")
        self.assertEqual(tag.zipball_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/zipball/v0.1-beta.2")
