# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework


class DirTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        d = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("")[1]
        self.assertEqual(d.git_url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/trees/1b5e66c31c97d735d6c35beecca1e2a783ab8151")
        self.assertEqual(d.html_url, "https://github.com/jacquev6/PyGithubIntegrationTests/tree/master/a")
        self.assertEqual(d.name, "a")
        self.assertEqual(d.path, "a")
        self.assertEqual(d.sha, "1b5e66c31c97d735d6c35beecca1e2a783ab8151")
        self.assertEqual(d.size, None)
        self.assertEqual(d.type, "dir")
        self.assertEqual(d.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/a?ref=master")

    def testGetContents(self):
        d = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("a")[0]
        self.assertEqual(d.path, "a/b")
        content = d.get_contents()
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0].path, "a/b/c")

    # @todoSomeday We could have a Dir.create_file method
