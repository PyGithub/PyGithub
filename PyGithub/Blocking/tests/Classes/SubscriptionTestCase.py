# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import PyGithub.Blocking.tests.Framework as Framework


class SubscriptionTestCase(Framework.SimpleLoginTestCase):
    def testEdit(self):
        u = self.g.get_authenticated_user()
        s = u.get_subscription("abersager/PyGithub")
        self.assertEqual(s.subscribed, True)
        self.assertEqual(s.ignored, False)
        s.edit(subscribed=False, ignored=True)
        self.assertEqual(s.subscribed, False)
        self.assertEqual(s.ignored, True)
        s.edit(subscribed=True, ignored=False)
        self.assertEqual(s.subscribed, True)
        self.assertEqual(s.ignored, False)
