############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 davidbrai <davidbrai@gmail.com>                               #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Eliot Walker <eliot@lyft.com>                                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2022 Liuyang Wan <tsfdye@gmail.com>                                #
# Copyright 2023 Andrew Dawes <53574062+AndrewJDawes@users.noreply.github.com> #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 YugoHino <henom06@gmail.com>                                  #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Kian-Meng Ang <kianmeng.ang@gmail.com>                        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Matej Focko <mfocko@users.noreply.github.com>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from datetime import datetime, timezone

from github.PaginatedList import PaginatedList as PaginatedListImpl

from . import Framework


class PaginatedList(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user("openframeworks").get_repo("openFrameworks")
        self.list = self.repo.get_issues()
        self.licenses = self.g.get_enterprise("beaver-group").get_consumed_licenses()

    def testIsApiType(self):
        self.assertTrue(self.list.is_rest)
        self.assertFalse(self.list.is_graphql)

    def testIteration(self):
        self.assertEqual(len(list(self.list)), 333)

    def testIterationWithPrefetchedFirstPage(self):
        # test data taken from EnterpriseAdmin.testGetEnterpriseUsers
        users = self.licenses.get_users()
        self.assertEqual(len(list(users)), 102)
        self.assertEqual(len({user.github_com_login for user in users}), 102)

    def testSeveralIterations(self):
        with self.replayData("PaginatedList.testIteration.txt"):
            self.assertEqual(len(list(self.list)), 333)
            self.assertEqual(len(list(self.list)), 333)
            self.assertEqual(len(list(self.list)), 333)
            self.assertEqual(len(list(self.list)), 333)

    def testIntIndexingInFirstPage(self):
        with self.replayData("PaginatedList.testGetFirstPage.txt"):
            self.assertEqual(self.list[0].id, 4772349)
            self.assertEqual(self.list[24].id, 4286936)

    def testReversedIterationWithSinglePage(self):
        r = self.list.reversed
        self.assertEqual(r[0].id, 4286936)
        self.assertEqual(r[1].id, 4317009)

    def testReversedIterationWithMultiplePages(self):
        r = self.list.reversed
        self.assertEqual(r[0].id, 94898)
        self.assertEqual(r[1].id, 104702)
        self.assertEqual(r[13].id, 166211)
        self.assertEqual(r[14].id, 166212)
        self.assertEqual(r[15].id, 166214)

    def testReversedIterationSupportsIterator(self):
        # reuse identical test data of testReversedIterationWithSinglePage
        with self.replayData("PaginatedList.testReversedIterationWithSinglePage.txt"):
            r = self.list.reversed
            for i in r:
                self.assertEqual(i.id, 4286936)
                return
            self.fail("empty iterator")

    def testReversedIterationSupportsBuiltinReversed(self):
        # reuse identical test data of testReversedIterationWithSinglePage
        with self.replayData("PaginatedList.testReversedIterationWithSinglePage.txt"):
            for i in reversed(self.list):
                self.assertEqual(i.id, 4286936)
                return
            self.fail("empty iterator")

    def testGettingTheReversedListDoesNotModifyTheOriginalList(self):
        self.assertEqual(self.list[0].id, 18345408)
        self.assertEqual(self.list[30].id, 17916118)
        r = self.list.reversed
        self.assertEqual(self.list[0].id, 18345408)
        self.assertEqual(self.list[30].id, 17916118)
        self.assertEqual(r[0].id, 132373)
        self.assertEqual(r[30].id, 543694)

    def testIntIndexingInThirdPage(self):
        self.assertEqual(self.list[50].id, 3911629)
        self.assertEqual(self.list[74].id, 3605277)

    def testGetFirstPage(self):
        self.assertListKeyEqual(
            self.list.get_page(0),
            lambda i: i.id,
            [
                4772349,
                4767675,
                4758608,
                4700182,
                4662873,
                4608132,
                4604661,
                4588997,
                4557803,
                4554058,
                4539985,
                4507572,
                4507492,
                4507416,
                4447561,
                4406584,
                4384548,
                4383465,
                4373361,
                4373201,
                4370619,
                4356530,
                4352401,
                4317009,
                4286936,
            ],
        )

    def testGetThirdPage(self):
        self.assertListKeyEqual(
            self.list.get_page(2),
            lambda i: i.id,
            [
                3911629,
                3911537,
                3910580,
                3910555,
                3910549,
                3897090,
                3883598,
                3856005,
                3850655,
                3825582,
                3813852,
                3812318,
                3812275,
                3807459,
                3799872,
                3799653,
                3795495,
                3754055,
                3710293,
                3662214,
                3647640,
                3631618,
                3627067,
                3614231,
                3605277,
            ],
        )

    def testIntIndexingAfterIteration(self):
        with self.replayData("PaginatedList.testIteration.txt"):
            self.assertEqual(len(list(self.list)), 333)
            self.assertEqual(self.list[11].id, 4507572)
            self.assertEqual(self.list[73].id, 3614231)
            self.assertEqual(self.list[332].id, 94898)

    def testSliceIndexingInFirstPage(self):
        with self.replayData("PaginatedList.testGetFirstPage.txt"):
            self.assertListKeyEqual(
                self.list[:13],
                lambda i: i.id,
                [
                    4772349,
                    4767675,
                    4758608,
                    4700182,
                    4662873,
                    4608132,
                    4604661,
                    4588997,
                    4557803,
                    4554058,
                    4539985,
                    4507572,
                    4507492,
                ],
            )
            self.assertListKeyEqual(
                self.list[:13:3],
                lambda i: i.id,
                [4772349, 4700182, 4604661, 4554058, 4507492],
            )
            self.assertListKeyEqual(self.list[10:13], lambda i: i.id, [4539985, 4507572, 4507492])
            self.assertListKeyEqual(self.list[5:13:3], lambda i: i.id, [4608132, 4557803, 4507572])

    def testSliceIndexingUntilFourthPage(self):
        self.assertListKeyEqual(
            self.list[:99:10],
            lambda i: i.id,
            [
                4772349,
                4539985,
                4370619,
                4207350,
                4063366,
                3911629,
                3813852,
                3647640,
                3528378,
                3438233,
            ],
        )
        self.assertListKeyEqual(
            self.list[73:78],
            lambda i: i.id,
            [3614231, 3605277, 3596240, 3594731, 3593619],
        )
        self.assertListKeyEqual(
            self.list[70:80:2],
            lambda i: i.id,
            [3647640, 3627067, 3605277, 3594731, 3593430],
        )

    def testSliceIndexingUntilEnd(self):
        with self.replayData("PaginatedList.testIteration.txt"):
            self.assertListKeyEqual(
                self.list[310::3],
                lambda i: i.id,
                [268332, 204247, 169176, 166211, 165898, 163959, 132373, 104702],
            )
            self.assertListKeyEqual(
                self.list[310:],
                lambda i: i.id,
                [
                    268332,
                    211418,
                    205935,
                    204247,
                    172424,
                    171615,
                    169176,
                    166214,
                    166212,
                    166211,
                    166209,
                    166208,
                    165898,
                    165537,
                    165409,
                    163959,
                    132671,
                    132377,
                    132373,
                    130269,
                    111018,
                    104702,
                    94898,
                ],
            )

    def testInterruptedIteration(self):
        # No asserts, but checks that only three pages are fetched
        count = 0
        for element in self.list:  # pragma no branch (exits only by break)
            count += 1
            if count == 75:
                break

    def testInterruptedIterationInSlice(self):
        # reuse identical test data of testInterruptedIteration
        with self.replayData("PaginatedList.testInterruptedIteration.txt"):
            # No asserts, but checks that only three pages are fetched
            count = 0
            # pragma no branch (exits only by break)
            for element in self.list[:100]:
                count += 1
                if count == 75:
                    break

    def testTotalCountWithNoLastPage(self):
        # Fudged replay data, we don't need the data, only the headers
        repos = self.g.get_repos()
        self.assertEqual(0, repos.totalCount)

    def testTotalCountWithDictionary(self):
        # PullRequest.get_review_requests() actually returns a dictionary that
        # we fudge into two lists, which means data is a dict, not a list.
        # We should check the member, not data itself for totalCount.
        pr = self.g.get_repo("PyGithub/PyGithub").get_pull(2078)
        review_requests = pr.get_review_requests()
        self.assertEqual(review_requests[0].totalCount, 0)
        self.assertEqual(review_requests[1].totalCount, 0)

    def testCustomPerPage(self):
        self.assertEqual(self.g.per_page, 30)
        self.g.per_page = 100
        self.assertEqual(self.g.per_page, 100)
        self.assertEqual(len(list(self.repo.get_issues())), 456)

    def testCustomPerPageWithNoUrlParams(self):
        self.g.per_page = 100
        self.assertEqual(len(list(self.repo.get_comments())), 325)

    def testCustomPerPageWithGetPage(self):
        self.g.per_page = 100
        self.assertEqual(len(self.repo.get_issues().get_page(2)), 100)

    def testCustomPerPageIteration(self):
        self.g.per_page = 3
        repo = self.g.get_repo("PyGithub/PyGithub")
        comments = repo.get_issue(1136).get_comments()
        self.assertEqual(
            [
                datetime(2019, 8, 10, 18, 16, 46, tzinfo=timezone.utc),
                datetime(2024, 1, 6, 16, 4, 34, tzinfo=timezone.utc),
                datetime(2024, 1, 6, 17, 34, 11, tzinfo=timezone.utc),
                datetime(2024, 3, 20, 15, 24, 15, tzinfo=timezone.utc),
                datetime(2024, 3, 21, 10, 55, 14, tzinfo=timezone.utc),
                datetime(2024, 3, 21, 14, 2, 22, tzinfo=timezone.utc),
                datetime(2024, 3, 24, 13, 58, 57, tzinfo=timezone.utc),
            ],
            [comment.created_at for comment in comments],
        )

    def testCustomPerPageReversedIteration(self):
        self.g.per_page = 3
        repo = self.g.get_repo("PyGithub/PyGithub")
        comments = repo.get_issue(1136).get_comments().reversed
        self.assertEqual(
            [
                datetime(2024, 3, 24, 13, 58, 57, tzinfo=timezone.utc),
                datetime(2024, 3, 21, 14, 2, 22, tzinfo=timezone.utc),
                datetime(2024, 3, 21, 10, 55, 14, tzinfo=timezone.utc),
                datetime(2024, 3, 20, 15, 24, 15, tzinfo=timezone.utc),
                datetime(2024, 1, 6, 17, 34, 11, tzinfo=timezone.utc),
                datetime(2024, 1, 6, 16, 4, 34, tzinfo=timezone.utc),
                datetime(2019, 8, 10, 18, 16, 46, tzinfo=timezone.utc),
            ],
            [comment.created_at for comment in comments],
        )

    def testNoFirstPage(self):
        self.assertFalse(next(iter(self.list), None))

    def testMergeDicts(self):
        self.assertDictEqual(
            PaginatedListImpl.merge_dicts(
                {"a": 1, "b": 2, "c": 3},
                {"c": 4, "d": 5, "e": 6},
            ),
            {"a": 1, "b": 2, "c": 4, "d": 5, "e": 6},
        )

    def testOverrideAttributes(self):
        input_dict = {"a": 1, "b": 2, "c": 3}
        overrides_dict = {"c": 4, "d": 5, "e": 6}
        transformer = PaginatedListImpl.override_attributes(overrides_dict)
        self.assertDictEqual(transformer(input_dict), {"a": 1, "b": 2, "c": 4, "d": 5, "e": 6})

    def testGraphQlPagination(self):
        repo = self.g.get_repo("PyGithub/PyGithub")
        discussions = repo.get_discussions("id number")
        self.assertFalse(discussions.is_rest)
        self.assertTrue(discussions.is_graphql)
        rev = discussions.reversed

        discussions_list = list(discussions)
        self.assertEqual(discussions.totalCount, 65)
        self.assertEqual(len(discussions_list), 65)
        self.assertEqual(discussions_list[0].number, 3044)
        self.assertEqual(discussions_list[-1].number, 1780)

        reversed_list = list(rev)
        self.assertEqual(rev.totalCount, 65)
        self.assertEqual(len(reversed_list), 65)
        self.assertListEqual([d.number for d in reversed_list], [d.number for d in reversed(discussions_list)])

        # accessing totalCount before iterating the PaginatedList triggers another request
        self.assertEqual(repo.get_discussions("id number").totalCount, 65)
