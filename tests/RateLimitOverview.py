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

import github
import github.RateLimit
import github.RateLimitOverview

from . import Framework


class RateLimitOverview(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.rate_limit_overview = self.g.get_rate_limit()

    def testResource(self):
        self.assertEqual(self.rate_limit_overview.resources.core.resource, "core")
        self.assertEqual(self.rate_limit_overview.resources.search.resource, "search")
        self.assertEqual(self.rate_limit_overview.resources.graphql.resource, "graphql")

        # the response does not provide this for the rate attribute
        self.assertIsNone(self.rate_limit_overview.rate.resource)

        # raw data of the overview remains the response, only the rate is aware of the resource
        self.assertNotIn("resource", self.rate_limit_overview.raw_data["resources"]["core"])
        self.assertEqual(self.rate_limit_overview.resources.core.raw_data["resource"], "core")

    def testResourceOfAllRates(self):
        resources = [
            "actions_runner_registration",
            "code_scanning_autofix",
            "code_scanning_upload",
            "code_search",
            "core",
            "dependency_sbom",
            "dependency_snapshots",
            "graphql",
            "integration_manifest",
            "scim",
            "search",
            "source_import",
        ]
        rate_limit = github.RateLimit.RateLimit(
            self.g.requester, {}, {resource: {"limit": 1} for resource in resources}
        )
        for resource in resources:
            with self.subTest(resource=resource):
                self.assertEqual(getattr(rate_limit, resource).resource, resource)

    def testResourceWithoutRate(self):
        rate_limit = github.RateLimit.RateLimit(self.g.requester, {}, {"core": None, "search": "not a dict"})
        self.assertIsNone(rate_limit.core)
        with self.assertRaises(github.BadAttributeException):
            rate_limit.search

    def testUpdate(self):
        updated = self.rate_limit_overview.update()

        self.assertIsInstance(updated, github.RateLimitOverview.RateLimitOverview)
        self.assertIsNot(updated, self.rate_limit_overview)
        self.assertEqual(updated.rate.remaining, 4987)
        self.assertEqual(updated.rate.used, 13)
        self.assertEqual(updated.resources.core.remaining, 4987)
        self.assertEqual(updated.resources.core.used, 13)
        self.assertEqual(updated.resources.search.remaining, 29)
        self.assertEqual(updated.resources.search.used, 1)

        # the object itself does not change
        self.assertEqual(self.rate_limit_overview.rate.remaining, 4988)
        self.assertEqual(self.rate_limit_overview.resources.core.remaining, 4988)
        self.assertEqual(self.rate_limit_overview.resources.search.remaining, 30)

        # the requester's values get updated
        self.assertEqual(self.g.requester.current_rate_limits.resources.core.remaining, 4987)
        self.assertEqual(self.g.requester.current_rate_limits.resources.search.remaining, 29)

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
