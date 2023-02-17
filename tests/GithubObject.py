############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

import unittest
from datetime import datetime, timedelta, timezone

from dateutil.tz.tz import tzoffset

from . import Framework

gho = Framework.github.GithubObject


class GithubObject(unittest.TestCase):
    def testMakeDatetimeAttribute(self):
        for value, expected in [
            (None, None),
            (
                "2021-01-23T12:34:56Z",
                datetime(2021, 1, 23, 12, 34, 56, tzinfo=timezone.utc),
            ),
            (
                "2021-01-23T12:34:56.000Z",
                datetime(2021, 1, 23, 12, 34, 56, tzinfo=timezone.utc),
            ),
            (
                "2021-01-23T12:34:56.000Z",
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
            (
                "2021-01-23T12:34:56.000+00:00",
                datetime(2021, 1, 23, 12, 34, 56, tzinfo=timezone.utc),
            ),
            (
                "2021-01-23T12:34:56.000+01:00",
                datetime(2021, 1, 23, 12, 34, 56, tzinfo=timezone(timedelta(hours=1))),
            ),
            (
                "2021-01-23T12:34:56.000-06:00",
                datetime(2021, 1, 23, 12, 34, 56, tzinfo=tzoffset(None, -21600)),
            ),
        ]:
            actual = gho.GithubObject._makeDatetimeAttribute(value)
            self.assertEqual(gho._ValuedAttribute, type(actual), value)
            self.assertEqual(expected, actual.value, value)

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
        self.assertEqual(
            datetime(2021, 1, 23, 12, 34, 56, tzinfo=timezone.utc), actual.value
        )

    def testMakeTimetsampAttributeBadValues(self):
        for value in ["1611405296", 1234.567]:
            actual = gho.GithubObject._makeTimestampAttribute(value)

            self.assertEqual(gho._BadAttribute, type(actual))
            with self.assertRaises(Framework.github.BadAttributeException) as e:
                value = actual.value
            self.assertEqual(value, e.exception.actual_value)
            self.assertEqual(int, e.exception.expected_type)
            self.assertIsNone(e.exception.transformation_exception)
