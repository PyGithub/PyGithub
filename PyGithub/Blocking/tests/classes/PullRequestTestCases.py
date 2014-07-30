# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class PullRequestAttributes(TestCase):
    @Enterprise.User(1)
    def testMergeable(self):
        p = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(7)
        self.assertEqual(p.additions, 1)
        self.assertEqual(p.changed_files, 1)
        self.assertEqual(p.commits, 1)
        self.assertEqual(p.commits_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/pulls/7/commits")
        self.assertEqual(p.deletions, 0)
        self.assertEqual(p.diff_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1/pull/7.diff")
        self.assertEqual(p.issue_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/issues/7")
        self.assertEqual(p.merge_commit_sha, "2fb73bbdf3adbe5e8b80975a1b4ca779206bd563")
        self.assertEqual(p.mergeable, True)
        self.assertEqual(p.mergeable_state, "clean")
        self.assertEqual(p.merged, False)
        self.assertIsNone(p.merged_at)
        self.assertIsNone(p.merged_by)
        self.assertEqual(p.patch_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1/pull/7.patch")
        self.assertEqual(p.review_comment_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/pulls/comments/{number}")
        self.assertEqual(p.review_comments, 0)
        self.assertEqual(p.review_comments_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/pulls/7/comments")
        self.assertEqual(p.statuses_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/statuses/a2684f57cb83a2ee716774b18a43dc16f9d82570")
        self.assertEqual(p.head.label, "ghe-org-1:feature1")
        self.assertEqual(p.head.ref, "feature1")
        self.assertEqual(p.head.repo.full_name, "ghe-org-1/repo-user-1-1")
        self.assertEqual(p.head.sha, "a2684f57cb83a2ee716774b18a43dc16f9d82570")
        self.assertEqual(p.head.user.login, "ghe-org-1")
        self.assertEqual(p.base.label, "ghe-user-1:master")
        self.assertEqual(p.base.ref, "master")
        self.assertEqual(p.base.repo.full_name, "ghe-user-1/repo-user-1-1")
        self.assertEqual(p.base.sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
        self.assertEqual(p.base.user.login, "ghe-user-1")

    @Enterprise.User(1)
    def testNotMergeable(self):
        p = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(6)
        self.assertEqual(p.mergeable, False)
        self.assertEqual(p.mergeable_state, "dirty")
        self.assertIsNone(p.merge_commit_sha)

    @Enterprise.User(1)
    def testMerged(self):
        p = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(8)
        self.assertIsNone(p.mergeable)
        self.assertEqual(p.merged, True)
        self.assertEqual(p.merged_at, datetime.datetime(2014, 7, 30, 5, 42, 44))
        self.assertEqual(p.merged_by.login, "ghe-user-1")
        self.assertEqual(p.merge_commit_sha, "6416457e04cb9fcb06f9e9d5c9db6fdb49c77c56")
        self.assertEqual(p.mergeable_state, "unknown")


class PullRequestCommits(TestCase):
    @Enterprise.User(1)
    def testGetCommits(self):
        p = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(7)
        commits = p.get_commits()
        self.assertEqual([c.sha for c in commits], ["a2684f57cb83a2ee716774b18a43dc16f9d82570"])


class PullRequestEdit(TestCase):
    @Enterprise.User(1)
    def testTitle(self):
        p = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(7)
        self.assertEqual(p.title, "Create foo.cpp without conflict")
        p.edit(title="Create foo.cpp without conflict!")
        self.assertEqual(p.title, "Create foo.cpp without conflict!")
        p.edit(title="Create foo.cpp without conflict")
        self.assertEqual(p.title, "Create foo.cpp without conflict")

    @Enterprise.User(1)
    def testBody(self):
        p = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(7)
        self.assertEqual(p.body, "This should be mergeable")
        p.edit(body=PyGithub.Blocking.Reset)
        self.assertIsNone(p.body)
        p.edit(body="This should be mergeable")
        self.assertEqual(p.body, "This should be mergeable")

    @Enterprise.User(1)
    def testState(self):
        p = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(7)
        self.assertEqual(p.state, "open")
        p.edit(state="closed")
        self.assertEqual(p.state, "closed")
        p.edit(state="open")
        self.assertEqual(p.state, "open")


class PullRequestFiles(TestCase):
    @Enterprise.User(1)
    def testGetFiles(self):
        p = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(7)
        files = p.get_files()
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0].additions, 1)
        self.assertEqual(files[0].blob_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1/blob/a2684f57cb83a2ee716774b18a43dc16f9d82570/foo.cpp")
        self.assertEqual(files[0].changes, 1)
        # @todoAlpha Should we add a get_contents method? And more generaly, we have objects with attributes like contents_url, merge_commit_sha, etc. Should we add get_xxx methods?
        self.assertEqual(files[0].contents_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/contents/foo.cpp?ref=a2684f57cb83a2ee716774b18a43dc16f9d82570")
        self.assertEqual(files[0].deletions, 0)
        self.assertEqual(files[0].filename, "foo.cpp")
        self.assertEqual(files[0].patch, "@@ -0,0 +1 @@\n+#define FOO bar")
        self.assertEqual(files[0].raw_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1/raw/a2684f57cb83a2ee716774b18a43dc16f9d82570/foo.cpp")
        self.assertEqual(files[0].sha, "193ea20b0ac65e80b05eb9ad1b9c56ab888f3ba4")
        self.assertEqual(files[0].status, "added")


class PullRequestMerge(TestCase):
    @Enterprise.User(1)
    def testGetIsMerged(self):
        self.assertFalse(self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(7).get_is_merged())
        self.assertTrue(self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(8).get_is_merged())

    @Enterprise.User(1)
    def testMergeUnmergeable(self):
        p = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_pull(6)
        self.assertEqual(p.mergeable, False)
        r = p.merge()
        self.assertEqual(r.documentation_url, "https://developer.github.com/v3/pulls/#merge-a-pull-request-merge-button")
        self.assertIsNone(r.merged)
        self.assertEqual(r.message, "Pull Request is not mergeable")
        self.assertIsNone(r.sha)

    # @todoAlpha testMergeMergeable
    # @todoAlpha testMergeMergeable_allParameters
