# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.GitBlob
import PyGithub.Blocking.GitTree

import PyGithub.Blocking.tests.Framework as Framework


class GitCommitTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        commit = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_git_commit("a374d0e06608e6ba661ae3246bff1d16aa3ab58b")
        self.assertEqual(commit.author.date, datetime.datetime(2014, 3, 24, 1, 59, 3))
        self.assertEqual(commit.author.email, "vincent@vincent-jacques.net")
        self.assertEqual(commit.author.name, "Vincent Jacques")
        self.assertEqual(commit.committer.date, datetime.datetime(2014, 3, 24, 1, 59, 3))
        self.assertEqual(commit.committer.email, "vincent@vincent-jacques.net")
        self.assertEqual(commit.committer.name, "Vincent Jacques")
        self.assertEqual(commit.html_url, "https://github.com/jacquev6/PyGithubIntegrationTests/commit/a374d0e06608e6ba661ae3246bff1d16aa3ab58b")
        self.assertEqual(commit.message, "Add new symlink and submodule")
        self.assertEqual(len(commit.parents), 1)
        self.assertEqual(commit.parents[0].sha, "1fe338c35777c1f27dd0e43931fb08cd5bb89063")
        self.assertEqual(commit.sha, "a374d0e06608e6ba661ae3246bff1d16aa3ab58b")
        self.assertEqual(commit.tree.sha, "83e7163e208723d366a758b7cbef1042e77b9e8b")
        self.assertEqual(commit.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/commits/a374d0e06608e6ba661ae3246bff1d16aa3ab58b")

    def testLazyCompletion(self):
        commit = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_git_commit("a374d0e06608e6ba661ae3246bff1d16aa3ab58b").parents[0]
        self.assertEqual(commit.sha, "1fe338c35777c1f27dd0e43931fb08cd5bb89063")
        self.assertEqual(commit.tree.sha, "5d3d2a823b637c002d07c4733fa0ed0ef2b73795")
