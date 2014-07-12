# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.tests.Framework as Framework


class PaginationTestCase(Framework.createTestCase(PyGithub.Blocking.Builder.Builder().Login(Framework.login, Framework.password))):
    def testIterationOnMultiplePages(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(len(list(stargazers)), 315)

    def testIterationOnSlice(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual([u.login for u in stargazers[27:33]], ["amokan", "goliatone", "cyraxjoe", "zoni", "dalejung", "reubano"])

    @Framework.SharesDataWith(testIterationOnSlice)
    def testIndexAccess(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(stargazers[42].login, "jandersonfc")

    @Framework.SharesDataWith(testIterationOnSlice)
    def testIterationOnReversedSlice(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual([u.login for u in stargazers[32:26:-1]], ["reubano", "dalejung", "zoni", "cyraxjoe", "goliatone", "amokan"])

    @Framework.SharesDataWith(testIterationOnSlice)
    def testIterationOnSliceWithGaps(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual([u.login for u in stargazers[27:33:2]], ["amokan", "cyraxjoe", "dalejung"])

    @Framework.SharesDataWith(testIterationOnSlice)
    def testIterationOnReversedSliceWithGaps(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual([u.login for u in stargazers[32:26:-2]], ["reubano", "zoni", "goliatone"])

    @Framework.SharesDataWith(testIterationOnMultiplePages)
    def testFullReversedIteration(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()[::-1]
        self.assertEqual(stargazers[0].login, "alfishe")
        self.assertEqual(stargazers[314].login, "ybakos")

    @Framework.SharesDataWith(testIterationOnMultiplePages)
    def testFullReversedIterationWithGaps(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()[::-2]
        self.assertEqual(stargazers[0].login, "alfishe")
        self.assertEqual(stargazers[157].login, "ybakos")

    @Framework.SharesDataWith(testIterationOnMultiplePages)
    def testIterationOfUnboundedSlice(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(len(stargazers[280:]), 35)

    @Framework.SharesDataWith(testIterationOnSlice)
    def testIterationOfUnboundedSlice2(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(len(stargazers[:35]), 35)

    @Framework.SharesDataWith(testIterationOnMultiplePages)
    def testIterationOfUnboundedSlice3(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(len(stargazers[:]), 315)

    def testStopIterationOnEmptyPage(self):
        gists = self.g.get_public_gists(since=datetime.datetime(2014, 7, 12, 2, 30, 0), per_page=10)
        self.assertEqual(len(gists[:]), 32)


class PaginationWithGlobalPerPageTestCase(Framework.createTestCase(PyGithub.Blocking.Builder.Builder().Login(Framework.login, Framework.password).PerPage(100))):
    def testIterationOnMultiplePages(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        stargazers = repo.get_stargazers()
        self.assertEqual(len(list(stargazers)), 321)
