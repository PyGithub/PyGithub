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
        rateLimit = self.g.get_rate_limit()
        self.assertEqual(
            repr(rateLimit),
            "RateLimit(core=Rate(reset=2023-05-15 23:57:21+00:00, remaining=4904, limit=5000))",
        )
        self.assertEqual(
            repr(rateLimit.core),
            "Rate(reset=2023-05-15 23:57:21+00:00, remaining=4904, limit=5000)",
        )
        self.assertEqual(rateLimit.core.limit, 5000)
        self.assertEqual(rateLimit.core.remaining, 4904)
        self.assertEqual(rateLimit.core.used, 96)
        self.assertEqual(rateLimit.core.reset, datetime(2023, 5, 15, 23, 57, 21, tzinfo=timezone.utc))
