# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework


class SubmoduleTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        s = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("PyGithub")
        self.assertEqual(s.git_url, "https://api.github.com/repos/jacquev6/PyGithub/git/trees/5e7d45a2f8c09757a0ce6d0bf37a8eec31791578")
        self.assertEqual(s.html_url, "https://github.com/jacquev6/PyGithub/tree/5e7d45a2f8c09757a0ce6d0bf37a8eec31791578")
        self.assertEqual(s.name, "PyGithub")
        self.assertEqual(s.path, "PyGithub")
        self.assertEqual(s.sha, "5e7d45a2f8c09757a0ce6d0bf37a8eec31791578")
        self.assertEqual(s.size, 0)
        self.assertEqual(s.submodule_git_url, "git@github.com:jacquev6/PyGithub")
        self.assertEqual(s.type, "submodule")
        self.assertEqual(s.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/PyGithub?ref=master")

    def testLazyCompletion(self):
        s = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("")[1]
        self.assertEqual(s.submodule_git_url, "git@github.com:jacquev6/PyGithub")
