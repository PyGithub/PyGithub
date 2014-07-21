# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.tests.Framework as Framework
from PyGithub.Blocking.tests.Framework import *


class CommitAttributes(TestCase):
    @Enterprise.User(1)
    def test(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        c = r.get_commit("7820fadc2429652016611e98fdc21766ba075161")
        self.assertEqual(c.author.login, "ghe-user-1")
        self.assertEqual(c.comments_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/commits/7820fadc2429652016611e98fdc21766ba075161/comments")
        self.assertEqual(c.commit.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/git/commits/7820fadc2429652016611e98fdc21766ba075161")
        self.assertEqual(c.committer.login, "ghe-user-1")
        self.assertEqual(len(c.files), 1)
        self.assertEqual(c.files[0].additions, 2)
        self.assertEqual(c.files[0].blob_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1/blob/7820fadc2429652016611e98fdc21766ba075161/README.md")
        self.assertEqual(c.files[0].changes, 2)
        self.assertEqual(c.files[0].contents_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/contents/README.md?ref=7820fadc2429652016611e98fdc21766ba075161")
        self.assertEqual(c.files[0].deletions, 0)
        self.assertEqual(c.files[0].filename, "README.md")
        self.assertEqual(c.files[0].patch, "@@ -1,2 +1,4 @@\n repo-user-1-1\n =============\n+\n+This is a test repo.")
        self.assertEqual(c.files[0].raw_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1/raw/7820fadc2429652016611e98fdc21766ba075161/README.md")
        self.assertEqual(c.files[0].sha, "23f16058fdd32c76a39c1cbf00a864d8c4fe1162")
        self.assertEqual(c.files[0].status, "modified")
        self.assertEqual(c.html_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1/commit/7820fadc2429652016611e98fdc21766ba075161")
        self.assertEqual(len(c.parents), 1)
        self.assertEqual(c.parents[0].html_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1/commit/e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
        self.assertEqual(c.parents[0].sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
        self.assertEqual(c.parents[0].url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/commits/e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
        self.assertEqual(c.sha, "7820fadc2429652016611e98fdc21766ba075161")
        self.assertEqual(c.stats.additions, 2)
        self.assertEqual(c.stats.deletions, 0)
        self.assertEqual(c.stats.total, 2)
        self.assertEqual(c.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/commits/7820fadc2429652016611e98fdc21766ba075161")
