# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework


class SymLinkTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        s = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("SymLink.rst")
        self.assertEqual(s.git_url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/blobs/e1f48bdf8333eb390019334db4ba2ad35b63ef36")
        self.assertEqual(s.html_url, "https://github.com/jacquev6/PyGithubIntegrationTests/blob/master/SymLink.rst")
        self.assertEqual(s.name, "SymLink.rst")
        self.assertEqual(s.path, "SymLink.rst")
        self.assertEqual(s.sha, "e1f48bdf8333eb390019334db4ba2ad35b63ef36")
        self.assertEqual(s.size, 22)
        self.assertEqual(s.target, "../PyGithub/README.rst")
        self.assertEqual(s.type, "symlink")
        self.assertEqual(s.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/SymLink.rst?ref=master")

    def testLazyCompletion(self):
        s = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("")[3]
        self.assertEqual(s.target, "../PyGithub/README.rst")
