# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.tests.Framework as Framework
from PyGithub.Blocking.tests.Framework import *


class GitRefAttributes(TestCase):
    @Enterprise.User(1)
    def testBranchRef(self):
        # @todoAlpha testTreeRef and testBlobRef?
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        ref = r.get_git_ref("refs/heads/master")
        self.assertEqual(ref.object.type, "commit")
        self.assertEqual(ref.object.sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
        self.assertEqual(ref.object.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/git/commits/e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
        self.assertEqual(ref.ref, "refs/heads/master")
        self.assertEqual(ref.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/git/refs/heads/master")


class GitRefMisc(TestCase):
    @Enterprise.User(1)
    def testEditAndDelete(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        ref = r.create_git_ref(ref="refs/heads/test", sha="7b96628d495239a926958bb5b8b935245668cc6a")
        self.assertEqual(ref.object.sha, "7b96628d495239a926958bb5b8b935245668cc6a")
        ref.edit(sha="c74a21bb2e1a84bd222d09204b2c9abf8a45718b")
        self.assertEqual(ref.object.sha, "c74a21bb2e1a84bd222d09204b2c9abf8a45718b")
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            ref.edit(sha="7b96628d495239a926958bb5b8b935245668cc6a")
        ref.edit(sha="7b96628d495239a926958bb5b8b935245668cc6a", force=True)
        self.assertEqual(ref.object.sha, "7b96628d495239a926958bb5b8b935245668cc6a")
        ref.delete()
