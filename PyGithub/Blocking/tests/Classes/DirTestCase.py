# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework


class DirTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_dir_content("")[1]
        self.assertEqual(f.git_url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/trees/1b5e66c31c97d735d6c35beecca1e2a783ab8151")
        self.assertEqual(f.html_url, "https://github.com/jacquev6/PyGithubIntegrationTests/tree/master/a")
        self.assertEqual(f.name, "a")
        self.assertEqual(f.path, "a")
        self.assertEqual(f.sha, "1b5e66c31c97d735d6c35beecca1e2a783ab8151")
        self.assertEqual(f.size, None)
        self.assertEqual(f.type, "dir")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/a?ref=master")
