# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.Dir
import PyGithub.Blocking.File
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework


class GitTreeTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        tree = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_git_tree("83e7163e208723d366a758b7cbef1042e77b9e8b")
        # @todoAlpha Implement GitTree.tree. It is a list of a union. Difficult, will require refactoring of Attributes.
        self.assertEqual(tree.sha, "83e7163e208723d366a758b7cbef1042e77b9e8b")
        self.assertEqual(tree.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/trees/83e7163e208723d366a758b7cbef1042e77b9e8b")
