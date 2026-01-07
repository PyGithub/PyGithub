############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Christoph Reiter <reiter.christoph@gmail.com>                 #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Nicolas Schweitzer <nicolas.schweitzer@datadoghq.com>         #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

from __future__ import annotations

import unittest
from datetime import datetime, timedelta, timezone
from typing import Any
from unittest import mock

import github.Repository
import github.RepositoryDiscussion

from . import Framework

gho = Framework.github.GithubObject
ghusr = Framework.github.NamedUser
ghorg = Framework.github.Organization


class GithubObject(unittest.TestCase):
    def testAttributesAsRest(self):
        _ = gho.as_rest_api_attributes
        self.assertIsNone(_(None))
        self.assertDictEqual(_({}), {})
        self.assertDictEqual(_({"id": "NID", "databaseId": "DBID"}), {"node_id": "NID", "id": "DBID"})
        self.assertDictEqual(_({"someId": "someId"}), {"some_id": "someId"})
        self.assertDictEqual(_({"someObj": {"someId": "someId"}}), {"some_obj": {"some_id": "someId"}})
        self.assertDictEqual(_({"bodyHTML": "<html/>"}), {"body_html": "<html/>"})

    def testApiType(self):
        self.assertEqual(github.Repository.Repository.is_rest(), True)
        self.assertEqual(github.Repository.Repository.is_graphql(), False)

        self.assertEqual(github.RepositoryDiscussion.RepositoryDiscussion.is_rest(), False)
        self.assertEqual(github.RepositoryDiscussion.RepositoryDiscussion.is_graphql(), True)

    def testMakeUnionClassAttributeFromTypeName(self):
        req = mock.Mock(is_not_lazy=False)
        obj = TestingClass(req, {}, {})

        data = {"login": "login"}
        class_and_names = [(ghusr.NamedUser, "User"), (ghorg.Organization, "Organization")]

        def make(type_name: str | None, fallback_type: str | None = "User"):
            return obj._makeUnionClassAttributeFromTypeName(type_name, fallback_type, data, *class_and_names)

        none = make(None)
        usr = make("User")
        org = make("Organization")
        unknown = make("Unknown")
        bad = make("Unknown", None)

        self.assertIsInstance(none, gho._ValuedAttribute)
        self.assertIsInstance(usr, gho._ValuedAttribute)
        self.assertIsInstance(org, gho._ValuedAttribute)
        self.assertIsInstance(unknown, gho._ValuedAttribute)
        self.assertIsInstance(bad, gho._BadAttribute)

        self.assertIsNone(none.value)
        self.assertIsInstance(usr.value, ghusr.NamedUser)
        self.assertIsInstance(org.value, ghorg.Organization)
        self.assertIsInstance(unknown.value, ghusr.NamedUser)

        self.assertEqual(str(usr.value), 'NamedUser(login="login")')
        self.assertEqual(str(org.value), 'Organization(login="login")')
        self.assertEqual(str(unknown.value), 'NamedUser(login="login")')

    def testMakeUnionClassAttributeFromTypeKey(self):
        req = mock.Mock(is_not_lazy=False)
        obj = TestingClass(req, {}, {})

        class_and_names = [(ghusr.NamedUser, "User"), (ghorg.Organization, "Organization")]

        def make(data: dict[str, Any]):
            return obj._makeUnionClassAttributeFromTypeKey("type", "User", data, *class_and_names)

        default = make({"login": "login"})
        usr = make({"login": "login", "type": "User"})
        org = make({"login": "login", "type": "Organization"})
        unknown = make({"login": "login", "type": "Unknown"})

        self.assertIsInstance(default, gho._ValuedAttribute)
        self.assertIsInstance(usr, gho._ValuedAttribute)
        self.assertIsInstance(org, gho._ValuedAttribute)
        self.assertIsInstance(unknown, gho._ValuedAttribute)

        self.assertIsInstance(default.value, ghusr.NamedUser)
        self.assertIsInstance(usr.value, ghusr.NamedUser)
        self.assertIsInstance(org.value, ghorg.Organization)
        self.assertIsInstance(unknown.value, ghusr.NamedUser)

        self.assertEqual(str(default.value), 'NamedUser(login="login")')
        self.assertEqual(str(usr.value), 'NamedUser(login="login")')
        self.assertEqual(str(org.value), 'Organization(login="login")')
        self.assertEqual(str(unknown.value), 'NamedUser(login="login")')

    def testMakeUnionClassAttributeFromTypeKeyAndValueKey(self):
        req = mock.Mock(is_not_lazy=False)
        obj = TestingClass(req, {}, {})

        class_and_names = [(ghusr.NamedUser, "User"), (ghorg.Organization, "Organization")]

        def make(data: dict[str, Any]):
            return obj._makeUnionClassAttributeFromTypeKeyAndValueKey("type", "data", "User", data, *class_and_names)

        default = make({"data": {"login": "login"}})
        usr = make({"data": {"login": "login"}, "type": "User"})
        org = make({"data": {"login": "login"}, "type": "Organization"})
        unknown = make({"data": {"login": "login"}, "type": "Unknown"})

        self.assertIsInstance(default, gho._ValuedAttribute)
        self.assertIsInstance(usr, gho._ValuedAttribute)
        self.assertIsInstance(org, gho._ValuedAttribute)
        self.assertIsInstance(unknown, gho._ValuedAttribute)

        self.assertIsInstance(default.value, ghusr.NamedUser)
        self.assertIsInstance(usr.value, ghusr.NamedUser)
        self.assertIsInstance(org.value, ghorg.Organization)
        self.assertIsInstance(unknown.value, ghusr.NamedUser)

        self.assertEqual(str(default.value), 'NamedUser(login="login")')
        self.assertEqual(str(usr.value), 'NamedUser(login="login")')
        self.assertEqual(str(org.value), 'Organization(login="login")')
        self.assertEqual(str(unknown.value), 'NamedUser(login="login")')

    def testMakeDatetimeAttribute(self):
        for value, expected in [
            (None, None),
            (
                "2021-01-23T12:34:56Z",
                datetime(2021, 1, 23, 12, 34, 56, tzinfo=timezone.utc),
            ),
            (
                "2021-01-23T12:34:56+00:00",
                datetime(2021, 1, 23, 12, 34, 56, tzinfo=timezone.utc),
            ),
            (
                "2021-01-23T12:34:56+01:00",
                datetime(2021, 1, 23, 12, 34, 56, tzinfo=timezone(timedelta(hours=1))),
            ),
            (
                "2021-01-23T12:34:56-06:30",
                datetime(
                    2021,
                    1,
                    23,
                    12,
                    34,
                    56,
                    tzinfo=timezone(timedelta(hours=-6, minutes=-30)),
                ),
            ),
        ]:
            actual = gho.GithubObject._makeDatetimeAttribute(value)
            self.assertEqual(gho._ValuedAttribute, type(actual), value)
            self.assertEqual(expected, actual.value, value)

    def testMakeHttpDatetimeAttribute(self):
        for value, expected in [
            (None, None),
            # https://datatracker.ietf.org/doc/html/rfc7231#section-7.1.1.1
            (
                "Mon, 11 Sep 2023 14:07:29 GMT",
                datetime(2023, 9, 11, 14, 7, 29, tzinfo=timezone.utc),
            ),
            # obsolete formats:
            (
                "Monday, 11-Sep-23 14:07:29 GMT",
                datetime(2023, 9, 11, 14, 7, 29, tzinfo=timezone.utc),
            ),
            (
                "Mon Sep  11 14:07:29 2023",
                datetime(2023, 9, 11, 14, 7, 29, tzinfo=timezone.utc),
            ),
        ]:
            actual = gho.GithubObject._makeHttpDatetimeAttribute(value)
            self.assertEqual(gho._ValuedAttribute, type(actual), value)
            self.assertEqual(expected, actual.value, value)

    def testMakeHttpDatetimeAttributeBadValues(self):
        for value in ["not a timestamp", 1234]:
            actual = gho.GithubObject._makeHttpDatetimeAttribute(value)
            with self.assertRaises(Framework.github.BadAttributeException):
                actual.value

    def testMakeDatetimeAttributeBadValues(self):
        for value in ["not a timestamp", 1234]:
            actual = gho.GithubObject._makeDatetimeAttribute(value)

            self.assertEqual(gho._BadAttribute, type(actual))
            with self.assertRaises(Framework.github.BadAttributeException) as e:
                value = actual.value
            self.assertEqual(value, e.exception.actual_value)
            self.assertEqual(str, e.exception.expected_type)
            if isinstance(value, str):
                self.assertIsNotNone(e.exception.transformation_exception)
            else:
                self.assertIsNone(e.exception.transformation_exception)

    def testMakeTimestampAttribute(self):
        actual = gho.GithubObject._makeTimestampAttribute(None)
        self.assertEqual(gho._ValuedAttribute, type(actual))
        self.assertIsNone(actual.value)

        actual = gho.GithubObject._makeTimestampAttribute(1611405296)
        self.assertEqual(gho._ValuedAttribute, type(actual))
        self.assertEqual(datetime(2021, 1, 23, 12, 34, 56, tzinfo=timezone.utc), actual.value)

    def testMakeTimetsampAttributeBadValues(self):
        for value in ["1611405296", 1234.567]:
            actual = gho.GithubObject._makeTimestampAttribute(value)

            self.assertEqual(gho._BadAttribute, type(actual))
            with self.assertRaises(Framework.github.BadAttributeException) as e:
                value = actual.value
            self.assertEqual(value, e.exception.actual_value)
            self.assertEqual(int, e.exception.expected_type)
            self.assertIsNone(e.exception.transformation_exception)


class CompletableGithubObjectWithPaginatedProperty(Framework.TestCase):
    # TODO: have lazy and eger tests
    def testSetValuesIfNotSet(self):
        set_value = gho.CompletableGithubObjectWithPaginatedProperty.set_values_if_not_set
        self.assertIsNone(set_value(None, per_page=123))
        self.assertEqual(set_value("/path/to/resource", per_page=123), "/path/to/resource?per_page=123")
        self.assertEqual(
            set_value("https://host/path/to/resource", per_page=123), "https://host/path/to/resource?per_page=123"
        )
        self.assertEqual(
            set_value("https://host/path/to/resource?param=one&param=2", per_page=123),
            "https://host/path/to/resource?param=one&param=2&per_page=123",
        )

        for url in [
            "/path/to/resource",
            "https://host/path/to/resource",
            "https://host/path/to/resource?param=one&param=2",
        ]:
            # add per_page to url, which is ignored since parameter exists already
            url = f"{url}{'&' if '?' in url else '?'}per_page=42"
            self.assertEqual(set_value(url, per_page=123), url)

            # add per_page to url, which is ignored since page exists already
            url = f"{url}{'&' if '?' in url else '?'}page=1"
            self.assertEqual(set_value(url, unless={"page"}, per_page=123), url)

    def testRepoCommitFilesDefault(self):
        with self.captureRequests() as requests:
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            commit = repo.get_commit("3253acaabd86de12b73d0a24c98eb9c13d1987b5")
            files = list(commit.files)

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            ["/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1"],
        )

    def testRepoCommitFiles(self):
        with self.captureRequests() as requests:
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            commit = repo.get_commit("3253acaabd86de12b73d0a24c98eb9c13d1987b5")
            files = list(commit.files)

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            ["/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1&per_page=2"],
        )

    def testRepoCommitFilesWithPerPage(self):
        with self.captureRequests() as requests:
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            commit = repo.get_commit("3253acaabd86de12b73d0a24c98eb9c13d1987b5", commit_files_per_page=3)
            files = list(commit.files)

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?per_page=3&page=1",
                "/repositories/3544490/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?per_page=3&page=2",
            ],
        )

    def testRepoCommitGetFilesDefault(self):
        with self.captureRequests() as requests:
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            commit = repo.get_commit("3253acaabd86de12b73d0a24c98eb9c13d1987b5")
            files = list(commit.get_files())

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1",
            ],
        )

    def testRepoCommitGetFiles(self):
        with self.captureRequests() as requests:
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            commit = repo.get_commit("3253acaabd86de12b73d0a24c98eb9c13d1987b5")
            files = list(commit.get_files())

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1&per_page=2",
            ],
        )

    def testRepoCommitGetFilesWithPerPage(self):
        with self.captureRequests() as requests:
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            commit = repo.get_commit("3253acaabd86de12b73d0a24c98eb9c13d1987b5", commit_files_per_page=1)
            files = list(commit.get_files(commit_files_per_page=3))

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1&per_page=3",
                "/repositories/3544490/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=2&per_page=3",
            ],
        )

    def testRepoCommitsFiles(self):
        with self.captureRequests() as requests:
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            commits = repo.get_commits(sha="dependabot/github_actions/actions/setup-python-6")
            commit = commits[0]
            files = list(commit.files)

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )

        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/commits?sha=dependabot%2Fgithub_actions%2Factions%2Fsetup-python-6&per_page=2",
                "/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1&per_page=2",
            ],
        )

    def testRepoComparisonCommitsFilesDefault(self):
        # replay data modified after record with
        # cat -n tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesDefault.txt | while read -r lineno line; do if [ $(( lineno % 11 )) -eq 10 ]; then jq . | sed -E -e 's/"patch":\s*".*[^\\]"/"patch":"…"/g' -e 's/"([^"]+_url)":\s*".*[^\\]"/"\1":"…"/g' | jq -c; else cat; fi <<< "$line"; done > tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesDefault.txt.bak
        # mv tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesDefault.txt.bak tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesDefault.txt
        with self.captureRequests() as requests:
            # tests paginated property of Comparison.commits and Commit.files
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            comparison = repo.compare(
                "6cfe46b712e2bf65560bd8189c4654cd6c56eeca", "cef98416f45a9cdaf84d7f53cea13ac074a2c05d"
            )
            # PaginatedList commits should use default per_page
            commits = list(comparison.commits)
            self.assertEqual(len(commits), 7)
            commit = commits[4]
            self.assertEqual(commit.sha, "cbfe8d0f623ca29d984ec09d2b566e9ab10ae024")
            # PaginatedList files should use default per_page
            files = list(commit.files)

        self.assertEqual(len(files), 371)
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/compare/6cfe46b712e2bf65560bd8189c4654cd6c56eeca...cef98416f45a9cdaf84d7f53cea13ac074a2c05d?page=1",
                "/repos/PyGithub/PyGithub/commits/cbfe8d0f623ca29d984ec09d2b566e9ab10ae024?page=1",
                "/repositories/3544490/commits/cbfe8d0f623ca29d984ec09d2b566e9ab10ae024?page=2",
            ],
        )

    def testRepoComparisonCommitsFiles(self):
        # replay data modified after record with
        # cat -n tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFiles.txt | while read -r lineno line; do if [ $(( lineno % 11 )) -eq 10 ]; then jq . | sed -E -e 's/"patch":\s*".*[^\\]"/"patch":"…"/g' -e 's/"([^"]+_url)":\s*".*[^\\]"/"\1":"…"/g' | jq -c; else cat; fi <<< "$line"; done > tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFiles.txt.bak
        # mv tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFiles.txt.bak tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFiles.txt
        with self.captureRequests() as requests:
            # tests paginated property of Comparison.commits and Commit.files
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            comparison = repo.compare(
                "19e1c5032397a95c58fe25760723ffc24cbe0ec8",
                "4bf07a2f5123f78fc6759bc2ade0c74154c1ba86",
            )
            # PaginatedList commits should respect configured per_page
            commits = list(comparison.commits)
            self.assertEqual(len(commits), 4)
            commit = commits[3]
            self.assertEqual(commit.sha, "4bf07a2f5123f78fc6759bc2ade0c74154c1ba86")
            # PaginatedList files should respect configured per_page
            files = list(commit.files)

        self.assertEqual(len(files), 6)
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/compare/19e1c5032397a95c58fe25760723ffc24cbe0ec8...4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=1&per_page=2",
                "/repositories/3544490/compare/19e1c5032397a95c58fe25760723ffc24cbe0ec8...4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=2&per_page=2",
                "/repos/PyGithub/PyGithub/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=1&per_page=2",
                "/repositories/3544490/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=2&per_page=2",
                "/repositories/3544490/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=3&per_page=2",
            ],
        )

    def testRepoComparisonCommitsFilesWithPerPage(self):
        # replay data modified after record with
        # cat -n tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesWithPerPage.txt | while read -r lineno line; do if [ $(( lineno % 11 )) -eq 10 ]; then jq . | sed -E -e 's/"patch":\s*".*[^\\]"/"patch":"…"/g' -e 's/"([^"]+_url)":\s*".*[^\\]"/"\1":"…"/g' | jq -c; else cat; fi <<< "$line"; done > tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesWithPerPage.txt.bak
        # mv tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesWithPerPage.txt.bak tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesWithPerPage.txt
        with self.captureRequests() as requests:
            # tests paginated property of Comparison.commits and Commit.files
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            comparison = repo.compare(
                "19e1c5032397a95c58fe25760723ffc24cbe0ec8",
                "4bf07a2f5123f78fc6759bc2ade0c74154c1ba86",
                comparison_commits_per_page=3,
            )
            # PaginatedList commits should use given per_page
            commits = list(comparison.commits)
            self.assertEqual(len(commits), 4)
            commit = commits[3]
            self.assertEqual(commit.sha, "4bf07a2f5123f78fc6759bc2ade0c74154c1ba86")
            # PaginatedList files should respect configured per_page
            files = list(commit.files)

        self.assertEqual(len(files), 6)
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/compare/19e1c5032397a95c58fe25760723ffc24cbe0ec8...4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?per_page=3&page=1",
                "/repositories/3544490/compare/19e1c5032397a95c58fe25760723ffc24cbe0ec8...4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?per_page=3&page=2",
                "/repos/PyGithub/PyGithub/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=1&per_page=2",
                "/repositories/3544490/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=2&per_page=2",
                "/repositories/3544490/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=3&per_page=2",
            ],
        )

    def testRepoComparisonCommitsFilesReversed(self):
        # replay data modified after record with
        # cat -n tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesReversed.txt | while read -r lineno line; do if [ $(( lineno % 11 )) -eq 10 ]; then jq . | sed -E -e 's/"patch":\s*".*[^\\]"/"patch":"…"/g' -e 's/"([^"]+_url)":\s*".*[^\\]"/"\1":"…"/g' | jq -c; else cat; fi <<< "$line"; done > tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesReversed.txt.bak
        # mv tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesReversed.txt.bak tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesReversed.txt
        with self.captureRequests() as requests:
            # tests paginated property of Comparison.commits and Commit.files
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            comparison = repo.compare(
                "19e1c5032397a95c58fe25760723ffc24cbe0ec8",
                "4bf07a2f5123f78fc6759bc2ade0c74154c1ba86",
            )
            # PaginatedList commits should respect configured per_page
            commits = list(reversed(comparison.commits))
            self.assertEqual(len(commits), 4)
            commit = commits[0]
            self.assertEqual(commit.sha, "4bf07a2f5123f78fc6759bc2ade0c74154c1ba86")
            # PaginatedList files should respect configured per_page
            files = list(reversed(commit.files))

        self.assertEqual(len(files), 6)
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/compare/19e1c5032397a95c58fe25760723ffc24cbe0ec8...4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=1&per_page=2",
                "/repositories/3544490/compare/19e1c5032397a95c58fe25760723ffc24cbe0ec8...4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=2&per_page=2",
                "/repositories/3544490/compare/19e1c5032397a95c58fe25760723ffc24cbe0ec8...4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=1&per_page=2",
                "/repos/PyGithub/PyGithub/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=1&per_page=2",
                "/repositories/3544490/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=3&per_page=2",
                "/repositories/3544490/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=2&per_page=2",
                "/repositories/3544490/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=1&per_page=2",
            ],
        )

    def testRepoComparisonCommitsFilesReversedWithPerPage(self):
        # replay data modified after record with
        # cat -n tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesReversedWithPerPage.txt | while read -r lineno line; do if [ $(( lineno % 11 )) -eq 10 ]; then jq . | sed -E -e 's/"patch":\s*".*[^\\]"/"patch":"…"/g' -e 's/"([^"]+_url)":\s*".*[^\\]"/"\1":"…"/g' | jq -c; else cat; fi <<< "$line"; done > tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesReversedWithPerPage.txt.bak
        # mv tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesReversedWithPerPage.txt.bak tests/ReplayData/CompletableGithubObjectWithPaginatedProperty.testRepoComparisonCommitsFilesReversedWithPerPage.txt
        with self.captureRequests() as requests:
            # tests paginated property of Comparison.commits and Commit.files
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            comparison = repo.compare(
                "19e1c5032397a95c58fe25760723ffc24cbe0ec8",
                "4bf07a2f5123f78fc6759bc2ade0c74154c1ba86",
                comparison_commits_per_page=3,
            )
            # PaginatedList commits should use given per_page
            commits = list(reversed(comparison.commits))
            self.assertEqual(len(commits), 4)
            commit = commits[0]
            self.assertEqual(commit.sha, "4bf07a2f5123f78fc6759bc2ade0c74154c1ba86")
            # PaginatedList files should respect configured per_page
            files = list(reversed(commit.files))

        self.assertEqual(len(files), 6)
        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/compare/19e1c5032397a95c58fe25760723ffc24cbe0ec8...4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?per_page=3&page=1",
                "/repositories/3544490/compare/19e1c5032397a95c58fe25760723ffc24cbe0ec8...4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?per_page=3&page=2",
                "/repositories/3544490/compare/19e1c5032397a95c58fe25760723ffc24cbe0ec8...4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?per_page=3&page=1",
                "/repos/PyGithub/PyGithub/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=1&per_page=2",
                "/repositories/3544490/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=3&per_page=2",
                "/repositories/3544490/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=2&per_page=2",
                "/repositories/3544490/commits/4bf07a2f5123f78fc6759bc2ade0c74154c1ba86?page=1&per_page=2",
            ],
        )

    def testPullCommitsFilesDefault(self):
        with self.captureRequests() as requests:
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            pull = repo.get_pull(3370)
            # PaginatedList commits should use default per_page
            commits = list(pull.get_commits())
            self.assertEqual(len(commits), 1)
            commit = commits[0]
            # PaginatedList files should use default per_page
            files = list(commit.files)

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )

        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/pulls/3370/commits",
                "/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1",
            ],
        )

    def testPullCommitsFiles(self):
        with self.captureRequests() as requests:
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            pull = repo.get_pull(3370)
            # PaginatedList commits should respect configured per_page
            commits = list(pull.get_commits())
            self.assertEqual(len(commits), 1)
            commit = commits[0]
            # PaginatedList files should respect configured per_page
            files = list(commit.files)

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )

        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/pulls/3370/commits?per_page=2",
                "/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1&per_page=2",
            ],
        )

    def testPullCommitsGetFilesDefault(self):
        with self.captureRequests() as requests:
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            pull = repo.get_pull(3370)
            # PaginatedList commits should respect configured per_page
            commits = list(pull.get_commits())
            self.assertEqual(len(commits), 1)
            commit = commits[0]
            # PaginatedList commits should use given per_page
            files = list(commit.get_files(commit_files_per_page=100))

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )

        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/pulls/3370/commits",
                "/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1&per_page=100",
            ],
        )

    def testPullCommitsGetFiles(self):
        with self.captureRequests() as requests:
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            pull = repo.get_pull(3370)
            # PaginatedList commits should respect configured per_page
            commits = list(pull.get_commits())
            self.assertEqual(len(commits), 1)
            commit = commits[0]
            # PaginatedList commits should respect configured per_page
            files = list(commit.get_files())

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )

        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/pulls/3370/commits?per_page=2",
                "/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1&per_page=2",
                "/repositories/3544490/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=2&per_page=2",
            ],
        )

    def testPullCommitsGetFilesWithPerPage(self):
        with self.captureRequests() as requests:
            self.g.per_page = 2
            repo = self.g.get_repo("PyGithub/PyGithub", lazy=True)
            pull = repo.get_pull(3370)
            # PaginatedList commits should respect configured per_page
            commits = list(pull.get_commits())
            self.assertEqual(len(commits), 1)
            commit = commits[0]
            # PaginatedList commits should use given per_page
            files = list(commit.get_files(commit_files_per_page=100))

        self.assertEqual(len(files), 4)
        self.assertListKeyEqual(
            files,
            lambda f: f.filename,
            [
                ".github/workflows/_build-pkg.yml",
                ".github/workflows/ci.yml",
                ".github/workflows/lint.yml",
                ".github/workflows/openapi.yml",
            ],
        )

        self.assertListKeyEqual(
            requests,
            lambda r: r.url,
            [
                "/repos/PyGithub/PyGithub/pulls/3370/commits?per_page=2",
                "/repos/PyGithub/PyGithub/commits/3253acaabd86de12b73d0a24c98eb9c13d1987b5?page=1&per_page=100",
            ],
        )


class TestingClass(gho.NonCompletableGithubObject):
    def _initAttributes(self) -> None:
        pass

    def _useAttributes(self, attributes: Any) -> None:
        pass


# TODO check replay data respect per_page
