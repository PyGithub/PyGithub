# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.GitBlob
import PyGithub.Blocking.GitTree

import PyGithub.Blocking.tests.Framework as Framework


class GitTreeTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        tree = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_git_tree("83e7163e208723d366a758b7cbef1042e77b9e8b")
        self.assertEqual(tree.mode, None)
        self.assertEqual(tree.path, None)
        self.assertEqual(tree.sha, "83e7163e208723d366a758b7cbef1042e77b9e8b")
        self.assertEqual(len(tree.tree), 5)
        self.assertIsInstance(tree.tree[0], PyGithub.Blocking.GitBlob.GitBlob)
        self.assertEqual(tree.tree[0].mode, "100644")
        self.assertEqual(tree.tree[0].path, ".gitmodules")
        self.assertEqual(tree.tree[0].sha, "f19d8d5a2f42ba86f19c2ecd6dfa6e28d1c2fb94")
        self.assertEqual(tree.tree[0].size, 164)
        self.assertEqual(tree.tree[0].type, "blob")
        self.assertEqual(tree.tree[0].url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/blobs/f19d8d5a2f42ba86f19c2ecd6dfa6e28d1c2fb94")
        self.assertIsInstance(tree.tree[1], PyGithub.Blocking.GitTree.GitTree.GitSubmodule)
        self.assertEqual(tree.tree[1].mode, "160000")
        self.assertEqual(tree.tree[1].path, "PyGithub")
        self.assertEqual(tree.tree[1].sha, "5e7d45a2f8c09757a0ce6d0bf37a8eec31791578")
        self.assertEqual(tree.tree[1].type, "commit")
        self.assertIsInstance(tree.tree[4], PyGithub.Blocking.GitTree.GitTree)
        self.assertEqual(tree.tree[4].mode, "040000")
        self.assertEqual(tree.tree[4].path, "a")
        self.assertEqual(tree.tree[4].sha, "6b5ca5c8c64026f92666ae9f36efff478e7117a4")
        self.assertEqual(tree.tree[4].type, "tree")
        self.assertEqual(tree.tree[4].url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/trees/6b5ca5c8c64026f92666ae9f36efff478e7117a4")
        self.assertEqual(tree.type, None)
        self.assertEqual(tree.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/trees/83e7163e208723d366a758b7cbef1042e77b9e8b")

    def testLazyCompletion(self):
        tree = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_git_tree("83e7163e208723d366a758b7cbef1042e77b9e8b").tree[4]
        self.assertEqual(tree.path, "a")
        self.assertEqual(tree.sha, "6b5ca5c8c64026f92666ae9f36efff478e7117a4")
        self.assertEqual(len(tree.tree), 5)
        self.assertEqual(tree.path, "a")  # Not lost after lazy completion
