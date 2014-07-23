# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking

import PyGithub.Blocking.tests.Framework as Framework


class AuthenticatedUserTestCase(Framework.SimpleLoginTestCase):
    def testGetSubscriptions(self):
        repos = self.g.get_authenticated_user().get_subscriptions()
        self.assertEqual(repos[0].full_name, "jacquev6/ViDE")
        self.assertEqual(repos[1].full_name, "jacquev6/Boost.HierarchicalEnum")

    def testGetSubscriptions_allParameters(self):
        repos = self.g.get_authenticated_user().get_subscriptions(per_page=3)
        self.assertEqual(repos[0].full_name, "jacquev6/ViDE")
        self.assertEqual(repos[1].full_name, "jacquev6/Boost.HierarchicalEnum")

    def testGetSubscription(self):
        u = self.g.get_authenticated_user()
        s = u.get_subscription("abersager/PyGithub")
        self.assertEqual(s.subscribed, True)
        self.assertEqual(s.ignored, False)
        self.assertEqual(s.url, "https://api.github.com/repos/abersager/PyGithub/subscription")
        self.assertEqual(s.repository_url, "https://api.github.com/repos/abersager/PyGithub")
        self.assertEqual(s.reason, None)
        self.assertEqual(s.created_at, datetime.datetime(2013, 12, 20, 6, 27, 57))

    def testGetUnexistingSubscription(self):
        u = self.g.get_authenticated_user()
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            s = u.get_subscription("wootook/wootook")

    def testDeleteSetSubscription(self):
        u = self.g.get_authenticated_user()
        s = u.get_subscription("abersager/PyGithub")
        s.delete()
        s = u.create_subscription("abersager/PyGithub", subscribed=True, ignored=False)
        self.assertEqual(s.subscribed, True)
        self.assertEqual(s.ignored, False)
        self.assertEqual(s.created_at, datetime.datetime(2013, 12, 22, 22, 48, 41))
