# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import logging

import PyGithub.Blocking.tests.Framework as Framework


@Framework.UsesForgedData
class UnexpectedAttributeTestCase(Framework.SimpleLoginTestCase):
    def testUnexpectedInt(self):
        self.expectLog(logging.INFO, "User received an unexpected attribute: 'unexpected_int' with value 42")
        user = self.g.get_user("jacquev6")

    def testUnexpectedDict(self):
        self.expectLog(
            logging.INFO,
            "User received an unexpected attribute: 'unexpected_dict' with value {u'foo': u'bar', u'baz': 42}",
            "User received an unexpected attribute: 'unexpected_dict' with value {'baz': 42, 'foo': 'bar'}",
            "User received an unexpected attribute: 'unexpected_dict' with value {'foo': 'bar', 'baz': 42}",
        )
        user = self.g.get_user("jacquev6")
