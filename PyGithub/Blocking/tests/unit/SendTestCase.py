# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from __future__ import print_function

import datetime
import unittest

import PyGithub.Blocking
import PyGithub.Blocking._send as snd


class NormalizationTestCase(unittest.TestCase):
    def testDictionary(self):
        self.assertEqual(snd.dictionary(), dict())
        self.assertEqual(snd.dictionary(foo="bar"), dict(foo="bar"))
        self.assertEqual(snd.dictionary(foo=None), dict())
        self.assertEqual(snd.dictionary(foo=PyGithub.Blocking.Reset), dict(foo=None))

    def testNormalizeGistId(self):
        self.assertEqual(snd.normalizeGistId("foo"), "foo")
        self.assertEqual(snd.normalizeGistId(PyGithub.Blocking.Gist.Gist(None, dict(url="url", id="foo"), None)), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeGistId(42)
        with self.assertRaises(TypeError):
            snd.normalizeGistId(PyGithub.Blocking.Reset)

    def testNormalizeLabelName(self):
        self.assertEqual(snd.normalizeLabelName("foo"), "foo")
        self.assertEqual(snd.normalizeLabelName(PyGithub.Blocking.Label.Label(None, dict(url="url", name="foo"), None)), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeLabelName(42)
        with self.assertRaises(TypeError):
            snd.normalizeLabelName(PyGithub.Blocking.Reset)

    def testNormalizeUserLogin(self):
        self.assertEqual(snd.normalizeUserLogin("foo"), "foo")
        self.assertEqual(snd.normalizeUserLogin(PyGithub.Blocking.User.User(None, dict(url="url", login="foo"), None)), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeUserLogin(42)
        with self.assertRaises(TypeError):
            snd.normalizeUserLogin(PyGithub.Blocking.Reset)

    def testNormalizeUserLoginReset(self):
        self.assertEqual(snd.normalizeUserLoginReset("foo"), "foo")
        self.assertEqual(snd.normalizeUserLoginReset(PyGithub.Blocking.Reset), PyGithub.Blocking.Reset)
        self.assertEqual(snd.normalizeUserLoginReset(PyGithub.Blocking.User.User(None, dict(url="url", login="foo"), None)), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeUserLoginReset(42)

    def testNormalizeAuthenticatedUserLogin(self):
        self.assertEqual(snd.normalizeAuthenticatedUserLogin("foo"), "foo")
        self.assertEqual(snd.normalizeAuthenticatedUserLogin(PyGithub.Blocking.AuthenticatedUser.AuthenticatedUser(None, dict(url="url", login="foo"), None)), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeAuthenticatedUserLogin(42)
        with self.assertRaises(TypeError):
            snd.normalizeAuthenticatedUserLogin(PyGithub.Blocking.Reset)

    def testNormalizeAuthenticatedUserLoginReset(self):
        self.assertEqual(snd.normalizeAuthenticatedUserLoginReset("foo"), "foo")
        self.assertEqual(snd.normalizeAuthenticatedUserLoginReset(PyGithub.Blocking.Reset), PyGithub.Blocking.Reset)
        self.assertEqual(snd.normalizeAuthenticatedUserLoginReset(PyGithub.Blocking.AuthenticatedUser.AuthenticatedUser(None, dict(url="url", login="foo"), None)), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeAuthenticatedUserLoginReset(42)

    def testNormalizeUserLoginAuthenticatedUserLogin(self):
        self.assertEqual(snd.normalizeUserLoginAuthenticatedUserLogin("foo"), "foo")
        self.assertEqual(snd.normalizeUserLoginAuthenticatedUserLogin(PyGithub.Blocking.User.User(None, dict(url="url", login="foo"), None)), "foo")
        self.assertEqual(snd.normalizeUserLoginAuthenticatedUserLogin(PyGithub.Blocking.AuthenticatedUser.AuthenticatedUser(None, dict(url="url", login="foo"), None)), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeUserLoginAuthenticatedUserLogin(42)
        with self.assertRaises(TypeError):
            snd.normalizeUserLoginAuthenticatedUserLogin(PyGithub.Blocking.Reset)

    def testNormalizeUserLoginAuthenticatedUserLoginReset(self):
        self.assertEqual(snd.normalizeUserLoginAuthenticatedUserLoginReset("foo"), "foo")
        self.assertEqual(snd.normalizeUserLoginAuthenticatedUserLoginReset(PyGithub.Blocking.Reset), PyGithub.Blocking.Reset)
        self.assertEqual(snd.normalizeUserLoginAuthenticatedUserLoginReset(PyGithub.Blocking.User.User(None, dict(url="url", login="foo"), None)), "foo")
        self.assertEqual(snd.normalizeUserLoginAuthenticatedUserLoginReset(PyGithub.Blocking.AuthenticatedUser.AuthenticatedUser(None, dict(url="url", login="foo"), None)), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeUserLoginAuthenticatedUserLoginReset(42)

    def testNormalizeUserId(self):
        self.assertEqual(snd.normalizeUserId(42), 42)
        self.assertEqual(snd.normalizeUserId(PyGithub.Blocking.User.User(None, dict(url="url", id=42), None)), 42)
        with self.assertRaises(TypeError):
            snd.normalizeUserId("foo")
        with self.assertRaises(TypeError):
            snd.normalizeUserId(PyGithub.Blocking.Reset)

    def testNormalizeTeamId(self):
        self.assertEqual(snd.normalizeTeamId(42), 42)
        self.assertEqual(snd.normalizeTeamId(PyGithub.Blocking.Team.Team(None, dict(url="url", id=42), None)), 42)
        with self.assertRaises(TypeError):
            snd.normalizeTeamId("foo")
        with self.assertRaises(TypeError):
            snd.normalizeTeamId(PyGithub.Blocking.Reset)

    def testNormalizeRepositoryId(self):
        self.assertEqual(snd.normalizeRepositoryId(42), 42)
        self.assertEqual(snd.normalizeRepositoryId(PyGithub.Blocking.Repository.Repository(None, dict(url="url", id=42), None)), 42)
        with self.assertRaises(TypeError):
            snd.normalizeRepositoryId("foo")
        with self.assertRaises(TypeError):
            snd.normalizeRepositoryId(PyGithub.Blocking.Reset)

    def testNormalizeRepositoryFullName(self):
        self.assertEqual(snd.normalizeRepositoryFullName(("foo", "bar")), ("foo", "bar"))
        self.assertEqual(snd.normalizeRepositoryFullName("foo/bar"), ("foo", "bar"))
        self.assertEqual(snd.normalizeRepositoryFullName(PyGithub.Blocking.Repository.Repository(None, dict(url="url", owner=dict(url="url", login="foo", type="User"), name="bar"), None)), ("foo", "bar"))
        with self.assertRaises(TypeError):
            snd.normalizeRepositoryFullName("foo")
        with self.assertRaises(TypeError):
            snd.normalizeRepositoryFullName("foo/bar/baz")
        with self.assertRaises(TypeError):
            snd.normalizeRepositoryFullName(("foo", "bar", "baz"))
        with self.assertRaises(TypeError):
            snd.normalizeRepositoryFullName(("foo", 42))
        with self.assertRaises(TypeError):
            snd.normalizeRepositoryFullName(("foo", "bar/baz"))
        with self.assertRaises(TypeError):
            snd.normalizeRepositoryFullName(("foo/baz", "bar"))
        with self.assertRaises(TypeError):
            snd.normalizeRepositoryFullName(42)
        with self.assertRaises(TypeError):
            snd.normalizeRepositoryFullName(PyGithub.Blocking.Reset)

    def testNormalizeTwoStringsString(self):
        self.assertEqual(snd.normalizeTwoStringsString(("foo", "bar")), ("foo", "bar"))
        self.assertEqual(snd.normalizeTwoStringsString("foo/bar"), ("foo", "bar"))
        with self.assertRaises(TypeError):
            snd.normalizeTwoStringsString("foo")
        with self.assertRaises(TypeError):
            snd.normalizeTwoStringsString("foo/bar/baz")
        with self.assertRaises(TypeError):
            snd.normalizeTwoStringsString(("foo", "bar", "baz"))
        with self.assertRaises(TypeError):
            snd.normalizeTwoStringsString(("foo", 42))
        with self.assertRaises(TypeError):
            snd.normalizeTwoStringsString(("foo", "bar/baz"))
        with self.assertRaises(TypeError):
            snd.normalizeTwoStringsString(("foo/baz", "bar"))
        with self.assertRaises(TypeError):
            snd.normalizeTwoStringsString(42)
        with self.assertRaises(TypeError):
            snd.normalizeTwoStringsString(PyGithub.Blocking.Reset)

    def testNormalizeMilestoneNumber(self):
        self.assertEqual(snd.normalizeMilestoneNumber(42), 42)
        self.assertEqual(snd.normalizeMilestoneNumber(PyGithub.Blocking.Milestone.Milestone(None, dict(url="url", number=42), None)), 42)
        with self.assertRaises(TypeError):
            snd.normalizeMilestoneNumber("foo")
        with self.assertRaises(TypeError):
            snd.normalizeMilestoneNumber(PyGithub.Blocking.Reset)

    def testNormalizeMilestoneNumberReset(self):
        self.assertEqual(snd.normalizeMilestoneNumberReset(42), 42)
        self.assertEqual(snd.normalizeMilestoneNumberReset(PyGithub.Blocking.Reset), PyGithub.Blocking.Reset)
        self.assertEqual(snd.normalizeMilestoneNumberReset(PyGithub.Blocking.Milestone.Milestone(None, dict(url="url", number=42), None)), 42)
        with self.assertRaises(TypeError):
            snd.normalizeMilestoneNumberReset("foo")

    def testNormalizeGitTreeSha(self):
        self.assertEqual(snd.normalizeGitTreeSha("foo"), "foo")
        self.assertEqual(snd.normalizeGitTreeSha(PyGithub.Blocking.GitTree.GitTree(None, dict(url="url", sha="foo"), None)), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeGitTreeSha(42)
        with self.assertRaises(TypeError):
            snd.normalizeGitTreeSha(PyGithub.Blocking.Reset)

    def testNormalizeGitCommitSha(self):
        self.assertEqual(snd.normalizeGitCommitSha("foo"), "foo")
        self.assertEqual(snd.normalizeGitCommitSha(PyGithub.Blocking.GitCommit.GitCommit(None, dict(url="url", sha="foo"), None)), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeGitCommitSha(42)
        with self.assertRaises(TypeError):
            snd.normalizeGitCommitSha(PyGithub.Blocking.Reset)

    def testNormalizeGitIgnoreTemplateName(self):
        self.assertEqual(snd.normalizeGitIgnoreTemplateName("foo"), "foo")
        self.assertEqual(snd.normalizeGitIgnoreTemplateName(PyGithub.Blocking.Github.Github.GitIgnoreTemplate(None, dict(name="foo"))), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeGitIgnoreTemplateName(42)
        with self.assertRaises(TypeError):
            snd.normalizeGitIgnoreTemplateName(PyGithub.Blocking.Reset)

    def testNormalizeEnum(self):
        self.assertEqual(snd.normalizeEnum("foo", "foo", "bar"), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeEnum("baz", "foo", "bar")
        with self.assertRaises(TypeError):
            snd.normalizeEnum(42, "foo", "bar")
        with self.assertRaises(TypeError):
            snd.normalizeEnum(PyGithub.Blocking.Reset, "foo", "bar")

    def testNormalizeInt(self):
        self.assertEqual(snd.normalizeInt(42), 42)
        with self.assertRaises(TypeError):
            snd.normalizeInt("foo")
        with self.assertRaises(TypeError):
            snd.normalizeInt(PyGithub.Blocking.Reset)

    def testNormalizeBool(self):
        self.assertEqual(snd.normalizeBool(True), True)
        self.assertEqual(snd.normalizeBool(False), False)
        with self.assertRaises(TypeError):
            snd.normalizeBool(42)
        with self.assertRaises(TypeError):
            snd.normalizeBool(PyGithub.Blocking.Reset)

    def testNormalizeBoolReset(self):
        self.assertEqual(snd.normalizeBoolReset(True), True)
        self.assertEqual(snd.normalizeBoolReset(False), False)
        self.assertEqual(snd.normalizeBoolReset(PyGithub.Blocking.Reset), PyGithub.Blocking.Reset)
        with self.assertRaises(TypeError):
            snd.normalizeBoolReset(42)

    def testNormalizeString(self):
        self.assertEqual(snd.normalizeString("foo"), "foo")
        with self.assertRaises(TypeError):
            snd.normalizeString(42)
        with self.assertRaises(TypeError):
            snd.normalizeString(PyGithub.Blocking.Reset)

    def testNormalizeStringReset(self):
        self.assertEqual(snd.normalizeStringReset("foo"), "foo")
        self.assertEqual(snd.normalizeStringReset(PyGithub.Blocking.Reset), PyGithub.Blocking.Reset)
        with self.assertRaises(TypeError):
            snd.normalizeStringReset(42)

    def testNormalizeList(self):
        self.assertEqual(snd.normalizeList(snd.normalizeRepositoryFullName, [("foo", "bar")]), ["foo/bar"])
        self.assertEqual(snd.normalizeList(snd.normalizeBool, [True, False, True]), [True, False, True])
        with self.assertRaises(TypeError):
            snd.normalizeList(snd.normalizeBool, 42)
        with self.assertRaises(TypeError):
            snd.normalizeList(snd.normalizeBool, {})
        with self.assertRaises(TypeError):
            snd.normalizeList(snd.normalizeBool, PyGithub.Blocking.Reset)
        with self.assertRaises(TypeError):
            snd.normalizeList(snd.normalizeBool, [True, 42])
        with self.assertRaises(TypeError):
            snd.normalizeList(snd.normalizeBool, [True, {}])
        with self.assertRaises(TypeError):
            snd.normalizeList(snd.normalizeBool, [True, PyGithub.Blocking.Reset])

    def testNormalizeGitAuthor(self):
        # @todoAlpha Really normalize input types
        self.assertEqual(snd.normalizeGitAuthor(42), 42)

    def testNormalizeDict(self):
        # @todoAlpha Really normalize input types
        self.assertEqual(snd.normalizeDict(42), 42)

    def testNormalizeDatetime(self):
        self.assertEqual(snd.normalizeDatetime("foo"), "foo")
        self.assertEqual(snd.normalizeDatetime(datetime.datetime(2014, 6, 18, 12, 12, 15)), "2014-06-18T12:12:15Z")
        with self.assertRaises(TypeError):
            snd.normalizeDatetime(PyGithub.Blocking.Reset)

    def testNormalizeDatetimeReset(self):
        self.assertEqual(snd.normalizeDatetimeReset("foo"), "foo")
        self.assertEqual(snd.normalizeDatetimeReset(datetime.datetime(2014, 6, 18, 12, 12, 15)), "2014-06-18T12:12:15Z")
        self.assertEqual(snd.normalizeDatetimeReset(PyGithub.Blocking.Reset), PyGithub.Blocking.Reset)
        with self.assertRaises(TypeError):
            snd.normalizeDatetimeReset(42)
