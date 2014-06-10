# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.tests.Framework as Framework


class LabelTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        label = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_label("bug")
        self.assertEqual(label.name, "bug")
        self.assertEqual(label.color, "fc2929")
        self.assertEqual(label.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/labels/bug")
