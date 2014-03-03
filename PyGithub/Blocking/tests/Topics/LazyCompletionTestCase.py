# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import PyGithub.Blocking.tests.Framework as Framework


class LazyCompletionTestCase(Framework.SimpleLoginTestCase):
    def testNoLazyCompletionNeeded(self):
        user = self.g.get_user("jacquev6")
        self.assertIsNotNone(user.plan)

    def testNoLazyCompletionNeededEvenIfAttributeIsNone(self):
        user = self.g.get_user("Lyloa")
        self.assertIsNone(user.plan)

    def testBasicLazyCompletion(self):
        user = self.g.get_repo("jacquev6/PyGithub").owner
        self.assertIsNotNone(user.plan)

    def testLazyCompletionIsDoneOnlyOnce(self):
        user = self.g.get_repo("nvie/gitflow").owner
        self.assertIsNone(user.plan)
        self.assertIsNone(user.plan)

    def testNoLazyCompletionForAttributesAlreadyRetrieved(self):
        user = self.g.get_repo("jacquev6/PyGithub").owner
        self.assertIsNotNone(user.gravatar_id)
