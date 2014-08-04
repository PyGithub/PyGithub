# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GitTreeAttributes(TestCase):
    @Enterprise("electra")
    def test(self):
        t = self.g.get_repo(("electra", "git-objects")).get_git_tree("634dab7d85ae09ce816910b45ed19cd362148c21")
        self.assertEqual(t.mode, None)
        self.assertEqual(t.path, None)
        self.assertEqual(t.sha, "634dab7d85ae09ce816910b45ed19cd362148c21")
        self.assertEqual(len(t.tree), 4)
        self.assertEqual(t.tree[0].path, "blob")
        self.assertIsInstance(t.tree[0], PyGithub.Blocking.GitBlob.GitBlob)
        self.assertEqual(t.tree[1].path, "submodule")
        self.assertEqual(t.tree[1].mode, "160000")
        self.assertEqual(t.tree[1].sha, "5e7d45a2f8c09757a0ce6d0bf37a8eec31791578")
        self.assertEqual(t.tree[1].type, "commit")
        self.assertIsInstance(t.tree[1], PyGithub.Blocking.GitTree.GitTree.GitSubmodule)
        self.assertEqual(t.tree[2].path, "symlink")
        self.assertIsInstance(t.tree[2], PyGithub.Blocking.GitBlob.GitBlob)
        self.assertEqual(t.tree[3].path, "tree")
        self.assertIsInstance(t.tree[3], PyGithub.Blocking.GitTree.GitTree)
        self.assertEqual(t.type, None)

    @Enterprise("electra")
    def testInTree(self):
        b = self.g.get_repo(("electra", "git-objects")).get_git_tree("634dab7d85ae09ce816910b45ed19cd362148c21").tree[3]
        self.assertEqual(b.mode, "040000")
        self.assertEqual(b.path, "tree")
        self.assertEqual(b.type, "tree")


class GitTreeMisc(TestCase):
    @Enterprise("electra")
    def testCreateModifiedCopy(self):
        t = self.g.get_repo(("electra", "git-objects")).get_git_tree("65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        modified = t.create_modified_copy(tree=[{"path": "other_test.txt", "mode": "100644", "type": "blob", "content": "Another blob"}])
        self.assertEqual(len(modified.tree), 2)


class GitTreeUpdate(TestCase):
    @Enterprise("electra")
    def testThroughLazyCompletion(self):
        t = self.g.get_repo(("electra", "git-objects")).get_git_tree("634dab7d85ae09ce816910b45ed19cd362148c21").tree[3]
        self.assertEqual(t.path, "tree")
        self.assertEqual(t.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(len(t.tree), 1)
        self.assertEqual(t.path, "tree")  # Not lost after lazy completion

    @Enterprise("electra")
    def testArtifical(self):
        # GitSubmodule are always returned completely so there is no other way to cover _updateAttributes
        t = self.g.get_repo(("electra", "git-objects")).get_git_tree("634dab7d85ae09ce816910b45ed19cd362148c21")
        t.tree[1]._updateAttributes()
