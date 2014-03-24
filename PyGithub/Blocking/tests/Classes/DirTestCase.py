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
        d = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("")[4]
        self.assertEqual(d.path, "a")
        contents = d.get_contents()
        self.assertEqual(len(contents), 5)
        self.assertIsInstance(contents[0], PyGithub.Blocking.Submodule.Submodule)
        self.assertIsInstance(contents[1], PyGithub.Blocking.SymLink.SymLink)
        self.assertIsInstance(contents[2], PyGithub.Blocking.Dir.Dir)
        self.assertIsInstance(contents[3], PyGithub.Blocking.File.File)
        self.assertIsInstance(contents[4], PyGithub.Blocking.File.File)
        self.assertEqual(contents[0].type, "file")  # https://github.com/github/developer.github.com/commit/1b329b04cece9f3087faa7b1e0382317a9b93490
        self.assertEqual(contents[1].type, "symlink")
        self.assertEqual(contents[2].type, "dir")
        self.assertEqual(contents[3].type, "file")
        self.assertEqual(contents[4].type, "file")

    # @todoSomeday We could have a Dir.create_file method
