# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.tests.Framework as Framework


@Framework.UsesSpecificData
class RateLimitingTestCase(Framework.SimpleAnonymousTestCase):
    def testConsumeRateLimit(self):
        self.g.get_user("nvie")
        self.assertEqual(self.g.Session.RateLimit.limit, 60)
        self.assertEqual(self.g.Session.RateLimit.remaining, 18)
        self.assertEqual(self.g.Session.RateLimit.reset, datetime.datetime(2013, 12, 22, 20, 45, 26))

        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")

        self.g.get_user("nvie")
        self.assertEqual(self.g.Session.RateLimit.limit, 60)
        self.assertEqual(self.g.Session.RateLimit.remaining, 10)
        self.assertEqual(self.g.Session.RateLimit.reset, datetime.datetime(2013, 12, 22, 20, 45, 26))

        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")
        self.g.get_user("nvie")

        self.g.get_user("nvie")
        self.assertEqual(self.g.Session.RateLimit.limit, 60)
        self.assertEqual(self.g.Session.RateLimit.remaining, 1)
        self.assertEqual(self.g.Session.RateLimit.reset, datetime.datetime(2013, 12, 22, 20, 45, 26))

        self.g.get_user("nvie")
        self.assertEqual(self.g.Session.RateLimit.limit, 60)
        self.assertEqual(self.g.Session.RateLimit.remaining, 0)
        self.assertEqual(self.g.Session.RateLimit.reset, datetime.datetime(2013, 12, 22, 20, 45, 26))

        with self.assertRaises(PyGithub.Blocking.RateLimitExceededException):
            self.g.get_user("nvie")
        self.assertEqual(self.g.Session.RateLimit.limit, 60)
        self.assertEqual(self.g.Session.RateLimit.remaining, 0)
        self.assertEqual(self.g.Session.RateLimit.reset, datetime.datetime(2013, 12, 22, 20, 45, 26))

    def testGetRateLimit(self):
        limit = self.g.get_rate_limit()
        self.assertEqual(limit.resources.core.limit, 60)
        self.assertEqual(limit.resources.core.remaining, 60)
        self.assertEqual(limit.resources.core.reset, datetime.datetime(2013, 12, 22, 22, 3, 37))
        self.assertEqual(limit.resources.search.limit, 5)
        self.assertEqual(limit.resources.search.remaining, 5)
        self.assertEqual(limit.resources.search.reset, datetime.datetime(2013, 12, 22, 21, 4, 37))

    def testRateLimitOnFreshSession(self):
        self.assertEqual(self.g.Session.RateLimit.limit, 60)
        self.assertEqual(self.g.Session.RateLimit.remaining, 60)
        self.assertEqual(self.g.Session.RateLimit.reset, datetime.datetime(2013, 12, 22, 23, 0, 25))
