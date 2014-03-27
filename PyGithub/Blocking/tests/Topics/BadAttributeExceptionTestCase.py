# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime
import logging

import PyGithub.Blocking.User
import PyGithub.Blocking.Repository

import PyGithub.Blocking.tests.Framework as Framework


@Framework.UsesForgedData
class BadAttributeExceptionTestCase(Framework.SimpleLoginTestCase):
    # Most data for this test case is forged based on hypothetical failures of
    # GitHub API v3

    def testBadBuiltinAttribute(self):
        self.expectLog(
            logging.WARNING,
            "Attribute Repository.forks_count is expected to be a int but GitHub API v3 returned u'abcd'",
            "Attribute Repository.forks_count is expected to be a int but GitHub API v3 returned 'abcd'",
        )
        r = self.g.get_repo("jacquev6/PyGithub")

        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            r.forks_count
        self.assertEqual(cm.exception.args, ("Repository.forks_count", int, "abcd"))
        self.assertIn(
            str(cm.exception),
            [
                "Attribute Repository.forks_count is expected to be a int but GitHub API v3 returned u'abcd'",
                "Attribute Repository.forks_count is expected to be a int but GitHub API v3 returned 'abcd'",
            ]
        )

    def testBadBuiltinAttributeInStruct(self):
        self.expectLog(
            logging.WARNING,
            "Attribute Repository.Permissions.pull is expected to be a bool but GitHub API v3 returned 42",
        )
        r = self.g.get_repo("jacquev6/PyGithub")

        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            r.permissions.pull
        self.assertEqual(cm.exception.args, ("Repository.Permissions.pull", bool, 42))
        self.assertEqual(str(cm.exception), "Attribute Repository.Permissions.pull is expected to be a bool but GitHub API v3 returned 42")

    def testBadClassAttribute(self):
        self.expectLog(
            logging.WARNING,
            "Attribute Repository.parent is expected to be a Repository but GitHub API v3 returned u'abcd'",
            "Attribute Repository.parent is expected to be a Repository but GitHub API v3 returned 'abcd'",
        )
        r = self.g.get_repo("jacquev6/PyGithub")

        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            r.parent
        self.assertEqual(cm.exception.args, ("Repository.parent", PyGithub.Blocking.Repository.Repository, "abcd"))
        self.assertIn(
            str(cm.exception),
            [
                "Attribute Repository.parent is expected to be a Repository but GitHub API v3 returned u'abcd'",
                "Attribute Repository.parent is expected to be a Repository but GitHub API v3 returned 'abcd'",
            ]
        )

    def testBadUnionAttribute(self):
        self.expectLog(
            logging.WARNING,
            "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned u'abcd'",
            "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned 'abcd'",
        )
        r = self.g.get_repo("jacquev6/PyGithub")

        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            r.owner
        self.assertEqual(cm.exception.args, ("Repository.owner", [PyGithub.Blocking.Organization.Organization, PyGithub.Blocking.User.User], "abcd"))
        self.assertIn(
            str(cm.exception),
            [
                "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned u'abcd'",
                "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned 'abcd'",
            ]
        )

    def testUnionAttributeWithBadType(self):
        self.expectLog(
            logging.WARNING,
            "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned {u'type': u'FooBar'}",
            "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned {'type': 'FooBar'}",
        )
        r = self.g.get_repo("jacquev6/PyGithub")

        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            r.owner
        self.assertEqual(cm.exception.args, ("Repository.owner", [PyGithub.Blocking.Organization.Organization, PyGithub.Blocking.User.User], {"type": "FooBar"}))
        self.assertIn(
            str(cm.exception),
            [
                "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned {u'type': u'FooBar'}",
                "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned {'type': 'FooBar'}",
            ]
        )

    def testUnionAttributeWithNoType(self):
        self.expectLog(
            logging.WARNING,
            "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned {u'no_type': True}",
            "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned {'no_type': True}",
        )
        r = self.g.get_repo("jacquev6/PyGithub")

        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            r.owner
        self.assertEqual(cm.exception.args, ("Repository.owner", [PyGithub.Blocking.Organization.Organization, PyGithub.Blocking.User.User], {"no_type": True}))
        self.assertIn(
            str(cm.exception),
            [
                "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned {u'no_type': True}",
                "Attribute Repository.owner is expected to be a Organization or User but GitHub API v3 returned {'no_type': True}",
            ]
        )

    def testBadStructAttribute(self):
        self.expectLog(
            logging.WARNING,
            "Attribute Repository.permissions is expected to be a Permissions but GitHub API v3 returned u'abcd'",
            "Attribute Repository.permissions is expected to be a Permissions but GitHub API v3 returned 'abcd'",
        )
        r = self.g.get_repo("jacquev6/PyGithub")

        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            r.permissions
        self.assertEqual(cm.exception.args, ("Repository.permissions", PyGithub.Blocking.Repository.Repository.Permissions, "abcd"))
        self.assertIn(
            str(cm.exception),
            [
                "Attribute Repository.permissions is expected to be a Permissions but GitHub API v3 returned u'abcd'",
                "Attribute Repository.permissions is expected to be a Permissions but GitHub API v3 returned 'abcd'",
            ]
        )

    def testBadDatetimeAttribute(self):
        self.expectLog(
            logging.WARNING,
            "Attribute Repository.pushed_at is expected to be a datetime but GitHub API v3 returned {}",
        )
        self.expectLog(
            logging.WARNING,
            "Attribute Repository.updated_at is expected to be a datetime but GitHub API v3 returned u'abcd'",
            "Attribute Repository.updated_at is expected to be a datetime but GitHub API v3 returned 'abcd'",
        )
        r = self.g.get_repo("jacquev6/PyGithub")

        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            r.updated_at
        self.assertEqual(cm.exception.args, ("Repository.updated_at", datetime.datetime, "abcd"))
        self.assertIn(
            str(cm.exception),
            [
                "Attribute Repository.updated_at is expected to be a datetime but GitHub API v3 returned u'abcd'",
                "Attribute Repository.updated_at is expected to be a datetime but GitHub API v3 returned 'abcd'",
            ]
        )

        with self.assertRaises(PyGithub.Blocking.BadAttributeException) as cm:
            r.pushed_at
        self.assertEqual(cm.exception.args, ("Repository.pushed_at", datetime.datetime, {}))
        self.assertEqual(str(cm.exception), "Attribute Repository.pushed_at is expected to be a datetime but GitHub API v3 returned {}")

    def testAbsentBuiltinAttribute(self):
        r = self.g.get_repo("jacquev6/PyGithub")

        self.assertEqual(r.owner, None)

    def testAbsentClassAttribute(self):
        r = self.g.get_repo("jacquev6/PyGithub")

        self.assertEqual(r.owner, None)

    def testAbsentStructAttribute(self):
        r = self.g.get_repo("jacquev6/PyGithub")

        self.assertEqual(r.permissions, None)

    def testAbsentDatetimeAttribute(self):
        r = self.g.get_repo("jacquev6/PyGithub")

        self.assertEqual(r.updated_at, None)
