# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import logging

import PyGithub.Blocking
import PyGithub.Blocking.tests.Framework as Framework


class AuthenticationTestCase(Framework.SimpleAnonymousTestCase):
    def testAnonymousAccessToUser(self):
        with self.assertRaises(PyGithub.Blocking.UnauthorizedException):
            self.g.get_authenticated_user()
        self.assertEqual(self.g.Session.OAuthScopes, None)
        self.assertEqual(self.g.Session.AcceptedOAuthScopes, None)


class OAuthWithoutScopesTestCase(Framework.SimpleOAuthWithoutScopesTestCase):
    def testGetAuthenticatedUser(self):
        self.assertEqual("jacquev6", self.g.get_authenticated_user().login)
        self.assertEqual(self.g.Session.OAuthScopes, [])
        self.assertEqual(self.g.Session.AcceptedOAuthScopes, [])

    def testModifySomething(self):
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException) as cm:
            self.g.get_authenticated_user().edit(location="The Moon")
        self.assertEqual(self.g.Session.OAuthScopes, [])


class OAuthWithScopesTestCase(Framework.SimpleOAuthWithScopesTestCase):
    def testEditAuthentic(self):
        self.g.get_authenticated_user().edit(location="The Moon")
        self.assertEqual(self.g.Session.OAuthScopes, ["repo", "user"])
        self.assertEqual(self.g.Session.AcceptedOAuthScopes, ["user"])
