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
# Copyright 2025 odedperezcodes <oded.perez.codes@gmail.com>                   #
# Copyright 2026 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2026 Mikhail f. Shiryaev <mr.felixoid@gmail.com>                   #
# Copyright 2026 Nayak <omk.nyk2729@gmail.com>                                 #
# Copyright 2026 Noethix <ryuga.rago1111@gmail.com>                            #
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

import pickle
from datetime import datetime, timezone
from unittest import mock

import github.GithubObject
import github.Rate
from github.PaginatedList import Page
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
        users = self.licenses.users
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

    def assertPages(self, paginated_list, sizes):
        pages = list(paginated_list.pages())
        for page in pages:
            self.assertIsInstance(page, Page)
            self.assertIsInstance(page, list)
        self.assertListEqual([len(page) for page in pages], sizes)
        return pages

    def testGetPageReturnsPage(self):
        with self.replayData("PaginatedList.testGetFirstPage.txt"):
            page = self.list.get_page(0)
        self.assertIsInstance(page, Page)
        self.assertEqual(len(page), 25)
        self.assertEqual(page[0].id, 4772349)

    def testPages(self):
        with self.replayData("PaginatedList.testIteration.txt"):
            with self.captureRequests() as requests:
                pages = self.assertPages(self.list, [25] * 13 + [8])
            self.assertEqual(len(requests), 14)

        # pages and iteration share fetched pages and elements
        with self.captureRequests() as requests:
            self.assertListEqual([element for page in pages for element in page], list(self.list))
            again = self.assertPages(self.list, [25] * 13 + [8])
        self.assertEqual(len(requests), 0)
        self.assertListEqual(pages, again)

    def testPagesAreFetchedLazily(self):
        with self.replayData("PaginatedList.testSliceIndexingUntilFourthPage.txt"):
            with self.captureRequests() as requests:
                pages = self.list.pages()
                self.assertEqual(len(requests), 0)
                for expected_requests, expected_index in enumerate((0, 25, 50, 75), start=1):
                    page = next(pages)
                    self.assertEqual(len(requests), expected_requests)
                    self.assertIs(page[0], self.list[expected_index])

    def testPagesAfterIndexing(self):
        with self.replayData("PaginatedList.testIntIndexingInThirdPage.txt"):
            # this fetches the first two pages, pages() starts from the first page without fetching them again
            element = self.list[30]
            with self.captureRequests() as requests:
                pages = self.list.pages()
                first = next(pages)
                second = next(pages)
                self.assertEqual(len(requests), 0)
                self.assertEqual(len(next(pages)), 25)
                self.assertEqual(len(requests), 1)
        self.assertIs(first[0], self.list[0])
        self.assertIs(second[5], element)

    def testPagesInterleavedWithIndexing(self):
        with self.replayData("PaginatedList.testSliceIndexingUntilFourthPage.txt"):
            pages = self.list.pages()
            first = next(pages)
            # this fetches further pages while pages() is iterating
            element = self.list[90]
            with self.captureRequests() as requests:
                second, third, fourth = next(pages), next(pages), next(pages)
            self.assertEqual(len(requests), 0)
        self.assertIs(first[0], self.list[0])
        self.assertIs(second[0], self.list[25])
        self.assertIs(third[0], self.list[50])
        self.assertIs(fourth[15], element)

    def testPageCopy(self):
        with self.replayData("PaginatedList.testGetFirstPage.txt"):
            page = self.list.get_page(0)
        copy = page.copy()
        self.assertIsInstance(copy, Page)
        self.assertIsNot(copy, page)
        self.assertListEqual(copy, page)
        self.assertIs(copy[0], page[0])

    def testModifyingPageDoesNotModifyList(self):
        with self.replayData("PaginatedList.testGetFirstPage.txt"):
            page = next(self.list.pages())
        page.clear()
        self.assertEqual(self.list[0].id, 4772349)
        # later calls still provide the unmodified page
        self.assertEqual(next(self.list.pages())[0].id, 4772349)

    def testPagesReversed(self):
        with self.replayData("PaginatedList.testCustomPerPageReversedIteration.txt"):
            self.g.per_page = 3
            repo = self.g.get_repo("PyGithub/PyGithub")
            comments = repo.get_issue(1136).get_comments().reversed
            pages = self.assertPages(comments, [1, 3, 3])
        self.assertListEqual(
            [comment.created_at for comment in pages[0]],
            [datetime(2024, 3, 24, 13, 58, 57, tzinfo=timezone.utc)],
        )
        self.assertListEqual([element for page in pages for element in page], list(comments))

    def testPagesWithFirstPage(self):
        with self.replayData("PaginatedList.testWithFirstPage.txt"):
            repo = self.g.withLazy(True).get_repo("PyGithub/PyGithub")
            commit = repo.get_commit("e359b83a04e8f34bedab0f2180169012d238a135", commit_files_per_page=3)
            commit.complete()
            files = commit.files
            with self.captureRequests() as requests:
                first = next(files.pages())
            self.assertEqual(len(requests), 0)
            self.assertEqual(len(first), 3)
            pages = self.assertPages(files, [3, 3, 1])
        self.assertListEqual(pages[0], first)
        self.assertListEqual([element for page in pages for element in page], list(files))

    def testPagesReversedWithFirstPage(self):
        with self.replayData("PaginatedList.testReversedWithFirstPage.txt"):
            repo = self.g.withLazy(True).get_repo("PyGithub/PyGithub")
            commit = repo.get_commit("e359b83a04e8f34bedab0f2180169012d238a135", commit_files_per_page=3)
            commit.complete()
            files = commit.files.reversed
            pages = self.assertPages(files, [1, 3, 3])
        self.assertListEqual([element for page in pages for element in page], list(files))

    def testPagesReversedWithFirstSinglePage(self):
        with self.replayData("PaginatedList.testReversedWithFirstSinglePage.txt"):
            repo = self.g.withLazy(True).get_repo("PyGithub/PyGithub")
            commit = repo.get_commit("f5f9756a1dd52a53820cc54927abb34725377987", commit_files_per_page=3)
            commit.complete()
            files = commit.files.reversed
            with self.captureRequests() as requests:
                pages = self.assertPages(files, [3])
            self.assertEqual(len(requests), 0)
        self.assertListEqual(
            [file.filename for file in pages[0]],
            ["tests/GithubObject.py", "github/GithubObject.py", "github/GithubApp.py"],
        )

    RATE_LIMIT_HEADERS = {
        "x-ratelimit-limit": "5000",
        "x-ratelimit-remaining": "4999",
        "x-ratelimit-used": "1",
        "x-ratelimit-reset": "1700000000",
        "x-ratelimit-resource": "core",
    }

    def assertPageRateLimit(self, page, resource="core"):
        rate = page.rate_limit
        self.assertIsInstance(rate, github.Rate.Rate)
        self.assertEqual(rate.resource, resource)
        self.assertEqual(rate.limit, 5000)
        self.assertEqual(rate.remaining, 4999)
        self.assertEqual(rate.used, 1)
        self.assertEqual(rate.reset, datetime(2023, 11, 14, 22, 13, 20, tzinfo=timezone.utc))

    def testPagesProvideRateLimitOfTheirResponse(self):
        with self.replayData("PaginatedList.testIteration.txt"):
            pages = list(self.list.pages())
        self.assertListEqual([page.rate_limit.remaining for page in pages[:4]], [4927, 4942, 4941, 4940])
        self.assertTrue(all(page.rate_limit.limit == 5000 for page in pages))

    def testGetPageProvidesRateLimit(self):
        with self.replayData("PaginatedList.testGetFirstPage.txt"):
            page = self.list.get_page(0)
        self.assertEqual(page.rate_limit.remaining, 4927)
        self.assertEqual(page.rate_limit.limit, 5000)

    def testPageRateLimitDoesNotSendRequest(self):
        with self.replayData("PaginatedList.testGetFirstPage.txt"):
            page = self.list.get_page(0)
        with self.captureRequests() as requests:
            page.rate_limit
        self.assertEqual(len(requests), 0)

    def testPageRateLimitWithFirstPage(self):
        paginated_list = PaginatedListImpl(
            github.Rate.Rate, mock.Mock(), firstData=[{"limit": 1}], firstHeaders=self.RATE_LIMIT_HEADERS
        )
        self.assertPageRateLimit(next(paginated_list.pages()))

    def testPageRateLimitOfReversedFetchedPages(self):
        paginated_list = PaginatedListImpl(
            github.Rate.Rate, mock.Mock(), firstData=[{"limit": 1}, {"limit": 2}], firstHeaders=self.RATE_LIMIT_HEADERS
        )
        paginated_list._reverse()
        page = next(paginated_list.pages())
        self.assertListEqual([rate.limit for rate in page], [2, 1])
        self.assertPageRateLimit(page)

    def testPageRateLimitOfReversedList(self):
        with self.replayData("PaginatedList.testCustomPerPageReversedIteration.txt"):
            self.g.per_page = 3
            repo = self.g.get_repo("PyGithub/PyGithub")
            comments = repo.get_issue(1136).get_comments().reversed
            pages = list(comments.pages())
        self.assertListEqual([page.rate_limit.remaining for page in pages], [4990, 4989, 4988])

    def testPageRateLimitOfCopy(self):
        self.assertPageRateLimit(Page([], mock.Mock(), self.RATE_LIMIT_HEADERS).copy())

    def testPageRateLimitWithFloatHeaderValues(self):
        headers = {**self.RATE_LIMIT_HEADERS, "x-ratelimit-limit": "5000.0", "x-ratelimit-reset": "1700000000.0"}
        self.assertPageRateLimit(Page([], mock.Mock(), headers))

    def testPageRateLimitWithoutHeaders(self):
        self.assertIsNone(Page([], mock.Mock(), None).rate_limit)
        self.assertIsNone(Page([], mock.Mock(), {}).rate_limit)
        self.assertIsNone(Page([], mock.Mock(), {"x-ratelimit-resource": "core"}).rate_limit)

    def testPageRateLimitAfterPickle(self):
        page = pickle.loads(pickle.dumps(Page([], self.g.requester, self.RATE_LIMIT_HEADERS)))
        # the test framework cannot relate these headers to any recorded response
        with mock.patch.object(github.GithubObject.GithubObject, "CHECK_AFTER_INIT_FLAG", False):
            self.assertPageRateLimit(page)

    def testPageRateLimitWithGraphQl(self):
        requester = mock.Mock(per_page=30)
        headers = {**self.RATE_LIMIT_HEADERS, "x-ratelimit-resource": "graphql"}
        requester.graphql_query.return_value = (
            headers,
            {
                "data": {
                    "repository": {
                        "discussions": {
                            "totalCount": 1,
                            "pageInfo": {
                                "startCursor": "start",
                                "endCursor": "end",
                                "hasNextPage": False,
                                "hasPreviousPage": False,
                            },
                            "nodes": [{"limit": 1}],
                        }
                    }
                }
            },
        )
        paginated_list = PaginatedListImpl(
            github.Rate.Rate,
            requester,
            graphql_query="query",
            graphql_variables={},
            list_item=["repository", "discussions"],
        )
        page = next(paginated_list.pages())
        self.assertPageRateLimit(page, resource="graphql")

        # elements provide the rate limit of their response as well
        self.assertPageRateLimit(page[0], resource="graphql")
        self.assertEqual(page[0].raw_headers, headers)

    def testHasUnfetchedPages(self):
        with self.replayData("PaginatedList.testIteration.txt"):
            self.assertTrue(self.list.has_unfetched_pages)
            with self.captureRequests() as requests:
                self.assertTrue(self.list.has_unfetched_pages)
            self.assertEqual(len(requests), 0)

            states = [self.list.has_unfetched_pages for _ in self.list.pages()]
        self.assertListEqual(states, [True] * 13 + [False])

        # all pages have been fetched, iterating them again does not send requests
        self.assertFalse(self.list.has_unfetched_pages)
        with self.captureRequests() as requests:
            self.assertEqual(len(list(self.list.pages())), 14)
        self.assertEqual(len(requests), 0)
        self.assertFalse(self.list.has_unfetched_pages)

    def testHasUnfetchedPagesWhenReversed(self):
        with self.replayData("PaginatedList.testCustomPerPageReversedIteration.txt"):
            self.g.per_page = 3
            repo = self.g.get_repo("PyGithub/PyGithub")
            comments = repo.get_issue(1136).get_comments().reversed
            states = [comments.has_unfetched_pages for _ in comments.pages()]
        self.assertListEqual(states, [True, True, False])

    def testHasUnfetchedPagesWithFirstPage(self):
        paginated_list = PaginatedListImpl(github.Rate.Rate, mock.Mock(), firstData=[{"limit": 1}], firstHeaders={})
        self.assertFalse(paginated_list.has_unfetched_pages)

    def testHasUnfetchedPagesWithGraphQl(self):
        with self.replayData("PaginatedList.testGraphQlPagination.txt"):
            repo = self.g.get_repo("PyGithub/PyGithub")
            discussions = repo.get_discussions("id number")
            rev = discussions.reversed
            for paginated_list in [discussions, rev]:
                self.assertTrue(paginated_list.has_unfetched_pages)
                states = [paginated_list.has_unfetched_pages for _ in paginated_list.pages()]
                self.assertGreater(len(states), 1)
                self.assertListEqual(states, [True] * (len(states) - 1) + [False])

            # consumes the remaining replay data
            self.assertEqual(repo.get_discussions("id number").totalCount, 65)

    def testPagesOfEmptyList(self):
        with self.replayData("PaginatedList.testNoFirstPage.txt"):
            self.assertPages(self.list, [0])

    def testPagesWithGraphQl(self):
        with self.replayData("PaginatedList.testGraphQlPagination.txt"):
            repo = self.g.get_repo("PyGithub/PyGithub")
            discussions = repo.get_discussions("id number")
            rev = discussions.reversed

            pages = list(discussions.pages())
            self.assertGreater(len(pages), 1)
            self.assertTrue(all(isinstance(page, Page) for page in pages))
            for page in pages:
                self.assertEqual(page.rate_limit.resource, "graphql")
                for element in page:
                    self.assertEqual(element.rate_limit.remaining, page.rate_limit.remaining)
            discussions_list = [element for page in pages for element in page]
            self.assertEqual(len(discussions_list), 65)
            self.assertListEqual(discussions_list, list(discussions))

            rev_pages = list(rev.pages())
            self.assertListEqual(
                [d.number for page in rev_pages for d in page],
                [d.number for d in reversed(discussions_list)],
            )

            # consumes the remaining replay data
            self.assertEqual(repo.get_discussions("id number").totalCount, 65)

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

    def testTotalCountWithLastPageAndPageFirst(self):
        # the last link may list page before per_page, totalCount must still parse
        repos = self.g.get_repos()
        self.assertEqual(42, repos.totalCount)

    def testTotalCountWithDictionary(self):
        # PullRequest.get_review_requests() actually returns a dictionary that
        # we fudge into two lists, which means data is a dict, not a list.
        # We should check the member, not data itself for totalCount.
        pr = self.g.get_repo("PyGithub/PyGithub").get_pull(2078)
        review_requests = pr.get_review_requests()
        self.assertEqual(review_requests[0].totalCount, 0)
        self.assertEqual(review_requests[1].totalCount, 0)

    def testTotalCountWithDeprecationLink(self):
        # Test the original reported scenario: search_issues with commit SHA
        issues = self.g.search_issues("commit:example_sha")
        # Should return the actual count from JSON, not 0
        self.assertEqual(issues.totalCount, 1)

    def doTestSearchCompleteness(self, incomplete_results: bool):
        self.g.per_page = 5

        with self.captureRequests() as requests:
            # starting iteration fetches the first page which contains totalCount and incomplete_results
            results = self.g.search_code('"profile = black" in:file language:toml')
            self.assertEqual(len(requests), 0)

            self.assertEqual(iter(results).__next__().score, 1.0)
            self.assertEqual(len(requests), 1)

            self.assertEqual(results.totalCount, 7)
            self.assertEqual(results.incomplete_results, incomplete_results)
            self.assertEqual(len(requests), 1)

            # exhaustive iteration fetches all pages, totalCount and incomplete_results should stay the same
            self.assertEqual(len(list(results)), 7)
            self.assertEqual(len(requests), 2)

            self.assertEqual(results.totalCount, 7)
            self.assertEqual(results.incomplete_results, incomplete_results)
            self.assertEqual(len(requests), 2)

        with self.captureRequests() as requests:
            # fetching a specific page provides totalCount and incomplete_results
            results = self.g.search_code('"profile = black" in:file language:toml')
            self.assertEqual(len(requests), 0)

            results.get_page(0)
            self.assertEqual(len(requests), 1)

            self.assertEqual(results.totalCount, 7)
            self.assertEqual(results.incomplete_results, incomplete_results)
            self.assertEqual(len(requests), 1)

        with self.captureRequests() as requests:
            # accessing totalCount first fetches totalCount and incomplete_results in a different code path
            results = self.g.search_code('"profile = black" in:file language:toml')
            self.assertEqual(len(requests), 0)

            # accessing the totalCount fetches incomplete_results as well
            self.assertEqual(results.totalCount, 7)
            self.assertEqual(len(requests), 1)
            self.assertIn("?per_page=1&", requests[0].url)

            self.assertEqual(results.incomplete_results, incomplete_results)
            self.assertEqual(len(requests), 1)

            # exhaustive iteration fetches all pages, totalCount and incomplete_results should stay the same
            self.assertEqual(len(list(results)), 7)
            self.assertEqual(len(requests), 3)
            self.assertIn("?per_page=5&", requests[1].url)
            self.assertIn("&per_page=5&", requests[2].url)

            self.assertEqual(results.totalCount, 7)
            self.assertEqual(results.incomplete_results, incomplete_results)
            self.assertEqual(len(requests), 3)

        with self.captureRequests() as requests:
            # accessing incomplete_results first fetches totalCount and incomplete_results in a different code path
            results = self.g.search_code('"profile = black" in:file language:toml')
            self.assertEqual(len(requests), 0)

            # accessing the incomplete_results fetches totalCount as well
            self.assertEqual(results.incomplete_results, incomplete_results)
            self.assertEqual(len(requests), 1)
            self.assertIn("?per_page=1&", requests[0].url)

            self.assertEqual(results.totalCount, 7)
            self.assertEqual(len(requests), 1)

            # exhaustive iteration fetches all pages, totalCount and incomplete_results should stay the same
            self.assertEqual(len(list(results)), 7)
            self.assertEqual(len(requests), 3)
            self.assertIn("?per_page=5&", requests[1].url)
            self.assertIn("&per_page=5&", requests[2].url)

            self.assertEqual(results.totalCount, 7)
            self.assertEqual(results.incomplete_results, incomplete_results)
            self.assertEqual(len(requests), 3)

        if not incomplete_results:
            # non-search result paginated lists have None incomplete_results
            labels = self.repo.get_labels()
            self.assertEqual(labels.totalCount, 57)
            self.assertIsNone(labels.incomplete_results)

    def testSearchWithCompleteResults(self):
        self.doTestSearchCompleteness(incomplete_results=False)

    def testSearchWithIncompleteResults(self):
        # test data for this test are copied from testSearchWithCompleteResults and manually modified:
        # sed -e 's/"incomplete_results":false/"incomplete_results":true/' tests/ReplayData/PaginatedList.testSearchWithCompleteResults.txt | head -n -11 > tests/ReplayData/PaginatedList.testSearchWithIncompleteResults.txt
        self.doTestSearchCompleteness(incomplete_results=True)

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

    def testCustomPerPageReversedIterationSinglePage(self):
        self.g.per_page = 4
        repo = self.g.get_repo("PyGithub/PyGithub")
        comments = repo.get_issue(3372).get_comments().reversed
        self.assertEqual(
            [
                datetime(2025, 9, 17, 19, 49, 40, tzinfo=timezone.utc),
                datetime(2025, 9, 17, 8, 44, 18, tzinfo=timezone.utc),
                datetime(2025, 9, 16, 19, 22, 2, tzinfo=timezone.utc),
                datetime(2025, 9, 15, 12, 15, 13, tzinfo=timezone.utc),
            ],
            [comment.created_at for comment in comments],
        )

    # more custom per page tests in CompletableGithubObjectWithPaginatedProperty

    def testWithFirstPage(self):
        # fetching the commit also fetches the fist page of files
        with self.captureRequests() as requests:
            repo = self.g.withLazy(True).get_repo("PyGithub/PyGithub")
            commit = repo.get_commit("e359b83a04e8f34bedab0f2180169012d238a135", commit_files_per_page=3)
            # repo is lazy, so this commit is also lazy, here we test with an eager (fetched) commit
            commit.complete()
            files = commit.files
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            ["/repos/PyGithub/PyGithub/commits/e359b83a04e8f34bedab0f2180169012d238a135?page=1&per_page=3"],
        )

        # consuming the first page of files should not fire a request
        with self.captureRequests() as requests:
            self.assertEqual(files[0].filename, "github/GeneratedReleaseNotes.py")
            self.assertEqual(files[1].filename, "github/Repository.py")
            self.assertEqual(files[2].filename, "pyproject.toml")
        self.assertEqual(len(requests), 0)

        # consuming items of the second page fetches the second page
        with self.captureRequests() as requests:
            self.assertEqual(files[3].filename, "tests/ReplayData/Repository.testGenerateReleaseNotes.txt")
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            ["/repositories/3544490/commits/e359b83a04e8f34bedab0f2180169012d238a135?page=2&per_page=3"],
        )

        # consuming further items of the second page does not fire a request
        with self.captureRequests() as requests:
            self.assertEqual(
                files[4].filename, "tests/ReplayData/Repository.testGenerateReleaseNotesWithAllArguments.txt"
            )
            self.assertEqual(files[5].filename, "tests/Repository.py")
        self.assertEqual(len(requests), 0)

        # consuming items of the last page fetches the that page
        with self.captureRequests() as requests:
            self.assertEqual(files[6].filename, "tests/test_release_notes.yml")
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            ["/repositories/3544490/commits/e359b83a04e8f34bedab0f2180169012d238a135?page=3&per_page=3"],
        )

    def testWithFirstSinglePage(self):
        # fetching the commit also fetches the fist page of files
        with self.captureRequests() as requests:
            repo = self.g.withLazy(True).get_repo("PyGithub/PyGithub")
            commit = repo.get_commit("f5f9756a1dd52a53820cc54927abb34725377987", commit_files_per_page=3)
            # repo is lazy, so this commit is also lazy, here we test with an eager (fetched) commit
            commit.complete()
            files = commit.files
            # with a single page we by now know the total count without firing a request
            self.assertEqual(files.totalCount, 3)
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            ["/repos/PyGithub/PyGithub/commits/f5f9756a1dd52a53820cc54927abb34725377987?page=1&per_page=3"],
        )

        # consuming the first page of files should not fire a request
        with self.captureRequests() as requests:
            self.assertEqual(files[0].filename, "github/GithubApp.py")
            self.assertEqual(files[1].filename, "github/GithubObject.py")
            self.assertEqual(files[2].filename, "tests/GithubObject.py")
        self.assertEqual(len(requests), 0)

    def testReversedWithFirstPage(self):
        # this is all lazy, no requests fired
        with self.captureRequests() as requests:
            repo = self.g.withLazy(True).get_repo("PyGithub/PyGithub")
            commit = repo.get_commit("e359b83a04e8f34bedab0f2180169012d238a135", commit_files_per_page=3)
            # repo is lazy, so this commit is also lazy, here we test with an eager (fetched) commit
            commit.complete()
            files = commit.files
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            ["/repos/PyGithub/PyGithub/commits/e359b83a04e8f34bedab0f2180169012d238a135?page=1&per_page=3"],
        )

        # reversing files does not fire a request because there is a last Link header in the first response
        with self.captureRequests() as requests:
            files = files.reversed
        self.assertEqual(len(requests), 0)

        # consuming the first page of the reversed files fetches the "last" URL
        with self.captureRequests() as requests:
            self.assertEqual(files[0].filename, "tests/test_release_notes.yml")
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            ["/repositories/3544490/commits/e359b83a04e8f34bedab0f2180169012d238a135?page=3&per_page=3"],
        )

        # consuming items of the second page fetches the second page
        with self.captureRequests() as requests:
            self.assertEqual(files[1].filename, "tests/Repository.py")
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            ["/repositories/3544490/commits/e359b83a04e8f34bedab0f2180169012d238a135?page=2&per_page=3"],
        )
        # consuming further items of the second page does not fire a request
        with self.captureRequests() as requests:
            self.assertEqual(
                files[2].filename, "tests/ReplayData/Repository.testGenerateReleaseNotesWithAllArguments.txt"
            )
            self.assertEqual(files[3].filename, "tests/ReplayData/Repository.testGenerateReleaseNotes.txt")
        self.assertEqual(len(requests), 0)

        # consuming items of the last page fetches the that page
        with self.captureRequests() as requests:
            self.assertEqual(files[4].filename, "pyproject.toml")
            self.assertEqual(files[5].filename, "github/Repository.py")
            self.assertEqual(files[6].filename, "github/GeneratedReleaseNotes.py")
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            ["/repositories/3544490/commits/e359b83a04e8f34bedab0f2180169012d238a135?page=1&per_page=3"],
        )

    def testReversedWithFirstSinglePage(self):
        # fetching the commit also fetches the fist page of files
        with self.captureRequests() as requests:
            repo = self.g.withLazy(True).get_repo("PyGithub/PyGithub")
            commit = repo.get_commit("f5f9756a1dd52a53820cc54927abb34725377987", commit_files_per_page=3)
            # repo is lazy, so this commit is also lazy, here we test with an eager (fetched) commit
            commit.complete()
            files = commit.files
            # with a single page we by now know the total count without firing a request
            self.assertEqual(files.totalCount, 3)
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/commits/f5f9756a1dd52a53820cc54927abb34725377987?page=1&per_page=3",
            ],
        )

        # reversing files fires another request because there were no Link headers in the first response
        with self.captureRequests() as requests:
            files = files.reversed
        self.assertListKeyEqual(
            requests, lambda r: r.url, ["/repos/PyGithub/PyGithub/commits/f5f9756a1dd52a53820cc54927abb34725377987"]
        )

        # consuming the first page of files should not fire a request
        with self.captureRequests() as requests:
            self.assertEqual(files[0].filename, "tests/GithubObject.py")
            self.assertEqual(files[1].filename, "github/GithubObject.py")
            self.assertEqual(files[2].filename, "github/GithubApp.py")
        self.assertEqual(len(requests), 0)

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
