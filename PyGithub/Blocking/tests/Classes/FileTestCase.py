# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework


class FileTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_file_content("README.md")
        self.assertEqual(len(f.content), 151)
        self.assertEqual(f.encoding, "base64")
        self.assertEqual(f.git_url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/blobs/76a7c87928c256c0dec34784ffaf9b936162bfa3")
        self.assertEqual(f.html_url, "https://github.com/jacquev6/PyGithubIntegrationTests/blob/master/README.md")
        self.assertEqual(f.name, "README.md")
        self.assertEqual(f.path, "README.md")
        self.assertEqual(f.sha, "76a7c87928c256c0dec34784ffaf9b936162bfa3")
        self.assertEqual(f.size, 109)
        self.assertEqual(f.type, "file")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/README.md?ref=master")

    def testLazyCompletion(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_dir_content("")[0]
        self.assertEqual(f.size, 109)
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/README.md?ref=master")
        self.assertEqual(len(f.content), 151)
