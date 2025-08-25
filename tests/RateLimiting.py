############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Ed Jackson <ed.jackson@gmail.com>                             #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Nikolay Yurin <yurinnick93@gmail.com>                         #
# Copyright 2024 Bill Napier <napier@pobox.com>                                #
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

from datetime import datetime, timezone

from . import Framework


class RateLimiting(Framework.TestCase):
    def testRateLimiting(self):
        self.assertEqual(self.g.rate_limiting, (4904, 5000))
        self.g.get_user("yurinnick")
        self.assertEqual(self.g.rate_limiting, (4903, 5000))
        self.assertEqual(self.g.rate_limiting_resettime, 1684195041)

    def testResetTime(self):
        self.assertEqual(self.g.rate_limiting_resettime, 1684195041)

    def testGetRateLimit(self):
        rateLimitOverview = self.g.get_rate_limit()

        rate = rateLimitOverview.rate
        self.assertEqual(
            repr(rate),
            "Rate(reset=2024-12-13 06:43:18+00:00, remaining=4988, limit=5000)",
        )
        self.assertEqual(rate.limit, 5000)
        self.assertEqual(rate.remaining, 4988)
        self.assertEqual(rate.used, 12)
        self.assertEqual(rate.reset, datetime(2024, 12, 13, 6, 43, 18, tzinfo=timezone.utc))

        rateLimit = rateLimitOverview.resources
        self.assertEqual(
            repr(rateLimit),
            "RateLimit(core=Rate(reset=2024-12-13 06:43:18+00:00, remaining=4988, limit=5000))",
        )
        self.assertEqual(
            repr(rateLimit.core),
            "Rate(reset=2024-12-13 06:43:18+00:00, remaining=4988, limit=5000)",
        )
        self.assertEqual(rateLimit.core.limit, 5000)
        self.assertEqual(rateLimit.core.remaining, 4988)
        self.assertEqual(rateLimit.core.used, 12)
        self.assertEqual(rateLimit.core.reset, datetime(2024, 12, 13, 6, 43, 18, tzinfo=timezone.utc))

        self.assertEqual(
            repr(rateLimit.actions_runner_registration),
            "Rate(reset=2024-12-13 07:28:18+00:00, remaining=10000, limit=10000)",
        )
        self.assertEqual(
            repr(rateLimit.code_scanning_upload), "Rate(reset=2024-12-13 07:28:18+00:00, remaining=1000, limit=1000)"
        )
        self.assertEqual(repr(rateLimit.code_search), "Rate(reset=2024-12-13 06:29:18+00:00, remaining=10, limit=10)")
        self.assertEqual(
            repr(rateLimit.dependency_snapshots), "Rate(reset=2024-12-13 06:29:18+00:00, remaining=100, limit=100)"
        )
        self.assertEqual(repr(rateLimit.graphql), "Rate(reset=2024-12-13 06:43:42+00:00, remaining=4808, limit=5000)")
        self.assertEqual(
            repr(rateLimit.integration_manifest), "Rate(reset=2024-12-13 07:28:18+00:00, remaining=5000, limit=5000)"
        )
        self.assertEqual(repr(rateLimit.scim), "Rate(reset=2024-12-13 07:28:18+00:00, remaining=15000, limit=15000)")
        self.assertEqual(repr(rateLimit.search), "Rate(reset=2024-12-13 06:29:18+00:00, remaining=30, limit=30)")
        self.assertEqual(
            repr(rateLimit.source_import), "Rate(reset=2024-12-13 06:29:18+00:00, remaining=100, limit=100)"
        )
