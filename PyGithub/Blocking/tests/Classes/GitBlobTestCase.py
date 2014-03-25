# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.Dir
import PyGithub.Blocking.File
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework


class GitBlobTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        blob = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_git_blob("3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(blob.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")
        self.assertEqual(blob.encoding, "base64")
        self.assertEqual(blob.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(blob.size, 20)
        self.assertEqual(blob.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/blobs/3daf0da6bca38181ab52610dd6af6e92f1a5469d")

    def testLazyCompletion(self):
        blob = self.g.get_repo("jacquev6/PyGithubIntegrationTests").create_git_blob("This is some content", "utf8")
        self.assertEqual(blob.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(blob.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")
