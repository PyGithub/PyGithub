# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import logging

import PyGithub.Blocking
import PyGithub.Blocking.tests.Framework as Framework


@Framework.UsesSpecificData
class UnusualErrorsTestCase(Framework.SimpleLoginTestCase):
    def testInternalError(self):
        with self.assertRaises(PyGithub.Blocking.ServerErrorException) as cm:
            self.g.get_authenticated_user()
        self.assertEqual(
            cm.exception.args,
            (
                502,
                {"date": "Sun, 22 Dec 2013 22:50:19 GMT", "content-length": "32", "content-type": "application/json", "server": "GitHub.com"},
                {"message": "Server Error"}
            )
        )
