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


class TestingClass(gho.NonCompletableGithubObject):
    def _initAttributes(self) -> None:
        pass

    def _useAttributes(self, attributes: Any) -> None:
        pass
