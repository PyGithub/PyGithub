############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

from datetime import datetime, timezone

from . import Framework


class RateLimitOverview(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.rate_limit_overview = self.g.get_rate_limit()

    def testAttributes(self):
        self.assertIsNotNone(self.rate_limit_overview.rate)
        self.assertIsNotNone(self.rate_limit_overview.resources)
        self.assertEqual(self.rate_limit_overview.rate.limit, 5000)
        self.assertEqual(self.rate_limit_overview.rate.remaining, 4988)
        self.assertEqual(self.rate_limit_overview.rate.reset, datetime(2024, 12, 13, 6, 43, 18, tzinfo=timezone.utc))
        self.assertEqual(self.rate_limit_overview.rate.used, 12)

        self.assertEqual(
            str(self.rate_limit_overview.resources.actions_runner_registration),
            "Rate(reset=2024-12-13 07:28:18+00:00, remaining=10000, limit=10000)",
        )
        self.assertEqual(
            str(self.rate_limit_overview.resources.code_scanning_upload),
            "Rate(reset=2024-12-13 07:28:18+00:00, remaining=1000, limit=1000)",
        )
        self.assertEqual(
            str(self.rate_limit_overview.resources.code_search),
            "Rate(reset=2024-12-13 06:29:18+00:00, remaining=10, limit=10)",
        )
        self.assertEqual(
            str(self.rate_limit_overview.resources.core),
            "Rate(reset=2024-12-13 06:43:18+00:00, remaining=4988, limit=5000)",
        )
        self.assertEqual(
            str(self.rate_limit_overview.resources.dependency_snapshots),
            "Rate(reset=2024-12-13 06:29:18+00:00, remaining=100, limit=100)",
        )
        self.assertEqual(
            str(self.rate_limit_overview.resources.graphql),
            "Rate(reset=2024-12-13 06:43:42+00:00, remaining=4808, limit=5000)",
        )
        self.assertEqual(
            str(self.rate_limit_overview.resources.integration_manifest),
            "Rate(reset=2024-12-13 07:28:18+00:00, remaining=5000, limit=5000)",
        )
        self.assertEqual(
            str(self.rate_limit_overview.resources.scim),
            "Rate(reset=2024-12-13 07:28:18+00:00, remaining=15000, limit=15000)",
        )
        self.assertEqual(
            str(self.rate_limit_overview.resources.search),
            "Rate(reset=2024-12-13 06:29:18+00:00, remaining=30, limit=30)",
        )
        self.assertEqual(
            str(self.rate_limit_overview.resources.source_import),
            "Rate(reset=2024-12-13 06:29:18+00:00, remaining=100, limit=100)",
        )
