# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class PullRequestAttributes(TestCase):
    @Enterprise("electra")
    def testMergeable(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(2)
        self.assertEqual(p.additions, 1)
        self.assertEqual(p.base.label, "electra:master")
        self.assertEqual(p.base.ref, "master")
        self.assertEqual(p.base.repo.full_name, "electra/pulls")
        self.assertEqual(p.base.sha, "06881a3f386de126ad34e176fe1fd6eedd61816c")
        self.assertEqual(p.base.user.login, "electra")
        self.assertEqual(p.body, None)
        self.assertEqual(p.body_html, None)
        self.assertEqual(p.body_text, None)
        self.assertEqual(p.changed_files, 1)
        self.assertEqual(p.closed_at, None)
        self.assertEqual(p.comments, 0)
        self.assertEqual(p.comments_url, "http://github.home.jacquev6.net/api/v3/repos/electra/pulls/issues/2/comments")
        self.assertEqual(p.commits, 1)
        self.assertEqual(p.commits_url, "http://github.home.jacquev6.net/api/v3/repos/electra/pulls/pulls/2/commits")
        self.assertEqual(p.created_at, datetime.datetime(2014, 8, 4, 0, 22, 56))
        self.assertEqual(p.deletions, 0)
        self.assertEqual(p.diff_url, "http://github.home.jacquev6.net/electra/pulls/pull/2.diff")
        self.assertEqual(p.head.label, "penelope:mergeable")
        self.assertEqual(p.head.ref, "mergeable")
        self.assertEqual(p.head.repo.full_name, "penelope/pulls")
        self.assertEqual(p.head.sha, "c604e9a2f1daf7bf9f96338a2d1899cf9dbb86cf")
        self.assertEqual(p.head.user.login, "penelope")
        self.assertEqual(p.html_url, "http://github.home.jacquev6.net/electra/pulls/pull/2")
        self.assertEqual(p.id, 8)
        self.assertEqual(p.issue_url, "http://github.home.jacquev6.net/api/v3/repos/electra/pulls/issues/2")
        self.assertEqual(p.merge_commit_sha, "13397d77177214cf32898094aada673b503becc3")
        self.assertEqual(p.mergeable, True)
        self.assertEqual(p.mergeable_state, "clean")
        self.assertEqual(p.merged, False)
        self.assertEqual(p.merged_at, None)
        self.assertEqual(p.merged_by, None)
        self.assertEqual(p.number, 2)
        self.assertEqual(p.patch_url, "http://github.home.jacquev6.net/electra/pulls/pull/2.patch")
        self.assertEqual(p.review_comment_url, "http://github.home.jacquev6.net/api/v3/repos/electra/pulls/pulls/comments/{number}")
        self.assertEqual(p.review_comments, 0)
        self.assertEqual(p.review_comments_url, "http://github.home.jacquev6.net/api/v3/repos/electra/pulls/pulls/2/comments")
        self.assertEqual(p.state, "open")
        self.assertEqual(p.statuses_url, "http://github.home.jacquev6.net/api/v3/repos/electra/pulls/statuses/c604e9a2f1daf7bf9f96338a2d1899cf9dbb86cf")
        self.assertEqual(p.title, "Mergeable pull")
        self.assertEqual(p.updated_at, datetime.datetime(2014, 8, 4, 0, 22, 57))
        self.assertEqual(p.user.login, "penelope")

    @Enterprise("electra")
    def testNotMergeable(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(3)
        self.assertEqual(p.mergeable, False)
        self.assertEqual(p.mergeable_state, "dirty")
        self.assertEqual(p.merge_commit_sha, None)

    @Enterprise("electra")
    def testMerged(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(1)
        self.assertEqual(p.mergeable, None)
        self.assertEqual(p.closed_at, datetime.datetime(2014, 8, 4, 0, 25, 5))
        self.assertEqual(p.merged, True)
        self.assertEqual(p.merged_at, datetime.datetime(2014, 8, 4, 0, 25, 5))
        self.assertEqual(p.merged_by.login, "electra")
        self.assertEqual(p.merge_commit_sha, "f313eab27360cce420c53de213aaf2a23de23a90")
        self.assertEqual(p.mergeable_state, "unknown")
        self.assertEqual(p.state, "closed")


class PullRequestCommits(TestCase):
    @Enterprise("electra")
    def testGetCommits(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(2)
        commits = p.get_commits()
        self.assertEqual([c.sha for c in commits], ["c604e9a2f1daf7bf9f96338a2d1899cf9dbb86cf"])


class PullRequestEdit(TestCase):
    @Enterprise("electra")
    def testTitle(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(4)
        self.assertEqual(p.title, "Mutable pull")
        p.edit(title="Mutable pull!")
        self.assertEqual(p.title, "Mutable pull!")
        p.edit(title="Mutable pull")
        self.assertEqual(p.title, "Mutable pull")

    @Enterprise("electra")
    def testBody(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(4)
        self.assertEqual(p.body, None)
        p.edit(body="This should be mergeable")
        self.assertEqual(p.body, "This should be mergeable")
        self.assertEqual(p.body_text, "This should be mergeable")
        self.assertEqual(p.body_html, "<p>This should be mergeable</p>")
        p.edit(body=PyGithub.Blocking.Reset)
        self.assertEqual(p.body, None)

    @Enterprise("electra")
    def testState(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(4)
        self.assertEqual(p.state, "open")
        p.edit(state="closed")
        self.assertEqual(p.state, "closed")
        p.edit(state="open")
        self.assertEqual(p.state, "open")

    @Enterprise("electra")
    def testAssignee(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(4)
        self.assertEqual(p.assignee, None)
        p.get_issue().edit(assignee="electra")
        self.assertTrue(p.update())
        self.assertEqual(p.assignee.login, "electra")
        p.get_issue().edit(assignee=PyGithub.Blocking.Reset)
        self.assertTrue(p.update())
        self.assertEqual(p.assignee, None)

    @Enterprise("electra")
    def testMilestone(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(4)
        self.assertEqual(p.milestone, None)
        p.get_issue().edit(milestone=1)
        self.assertTrue(p.update())
        self.assertEqual(p.milestone.number, 1)
        p.get_issue().edit(milestone=PyGithub.Blocking.Reset)
        self.assertTrue(p.update())
        self.assertEqual(p.milestone, None)


class PullRequestFiles(TestCase):
    @Enterprise("electra")
    def testGetFiles(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(2)
        files = p.get_files()
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0].additions, 1)
        self.assertEqual(files[0].blob_url, "http://github.home.jacquev6.net/electra/pulls/blob/c604e9a2f1daf7bf9f96338a2d1899cf9dbb86cf/mergeable.md")
        self.assertEqual(files[0].changes, 1)
        # @todoAlpha Should we add a get_contents method? And more generaly, we have objects with attributes like contents_url, merge_commit_sha, etc. Should we add get_xxx methods?
        self.assertEqual(files[0].contents_url, "http://github.home.jacquev6.net/api/v3/repos/electra/pulls/contents/mergeable.md?ref=c604e9a2f1daf7bf9f96338a2d1899cf9dbb86cf")
        self.assertEqual(files[0].deletions, 0)
        self.assertEqual(files[0].filename, "mergeable.md")
        self.assertEqual(files[0].patch, "@@ -0,0 +1 @@\n+merge\n\\ No newline at end of file")
        self.assertEqual(files[0].raw_url, "http://github.home.jacquev6.net/electra/pulls/raw/c604e9a2f1daf7bf9f96338a2d1899cf9dbb86cf/mergeable.md")
        self.assertEqual(files[0].sha, "53c8664db3f1e9559d637c4f5b41d4b258f15dd3")
        self.assertEqual(files[0].status, "added")


class PullRequestMerge(TestCase):
    @Enterprise("electra")
    def testGetIsMerged(self):
        self.assertFalse(self.g.get_repo(("electra", "pulls")).get_pull(2).get_is_merged())
        self.assertTrue(self.g.get_repo(("electra", "pulls")).get_pull(1).get_is_merged())

    @Enterprise("electra")
    def testMergeUnmergeable(self):
        p = self.g.get_repo(("electra", "pulls")).get_pull(3)
        self.assertEqual(p.mergeable, False)
        with self.assertRaises(PyGithub.Blocking.MethodNotAllowedException) as cm:
            p.merge()
        self.assertEqual(cm.exception.args[2]["documentation_url"], "https://developer.github.com/v3/pulls/#merge-a-pull-request-merge-button")
        self.assertEqual(cm.exception.args[2]["message"], "Pull Request is not mergeable")

    @Enterprise("electra")
    def testMergeMergeable(self):
        repo = self.g.get_repo(("electra", "pulls"))
        ephemeral = repo.create_git_ref("refs/heads/ephemeral", repo.get_git_ref("refs/heads/master").object.sha)
        p = repo.create_pull("Merge pull", "penelope:mergeable", "ephemeral")
        self.assertEqual(p.mergeable, None)
        # time.sleep(5)
        p.update()
        self.assertEqual(p.mergeable, True)
        r = p.merge()
        self.assertEqual(r.merged, True)
        self.assertEqual(r.message, "Pull Request successfully merged")
        self.assertEqual(r.sha, "a34257f72bbda674155899c6c7dc2ab255da3a05")
        ephemeral.delete()

    @Enterprise("electra")
    def testMergeMergeable_allParameters(self):
        repo = self.g.get_repo(("electra", "pulls"))
        ephemeral = repo.create_git_ref("refs/heads/ephemeral", repo.get_git_ref("refs/heads/master").object.sha)
        p = repo.create_pull("Merge pull", "penelope:mergeable", "ephemeral")
        self.assertEqual(p.mergeable, None)
        # time.sleep(5)
        p.update()
        self.assertEqual(p.mergeable, True)
        r = p.merge("Commit message")
        ephemeral.delete()
