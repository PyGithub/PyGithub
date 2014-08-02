# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GitBlobAttributes(TestCase):
    @Enterprise.User(1)
    def test(self):
        b = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_git_blob("3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(b.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")
        self.assertEqual(b.encoding, "base64")
        self.assertIsNone(b.mode)
        self.assertIsNone(b.path)
        self.assertEqual(b.size, 20)


class GitBlobUpdate(TestCase):
    @Enterprise.User(1)
    def testThroughLazyCompletion(self):
        b = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).create_git_blob("This is some content", "utf8")
        self.assertEqual(b.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(b.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")
