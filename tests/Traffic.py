############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Justin Kufro <jkufro@andrew.cmu.edu>                          #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
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

from datetime import datetime, timezone

from . import Framework


class Traffic(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.user = self.g.get_user()
        self.repo = self.user.get_repo("PyGithub")

    def testGetReferrers(self):
        referrerResponse = self.repo.get_top_referrers()
        self.assertGreaterEqual(len(referrerResponse), 1)
        self.assertEqual(referrerResponse[0].uniques, 1)
        self.assertEqual(referrerResponse[0].referrer, "github.com")
        self.assertEqual(referrerResponse[0].count, 5)
        self.assertEqual(
            repr(referrerResponse[0]),
            'Referrer(uniques=1, referrer="github.com", count=5)',
        )

    def testGetPaths(self):
        pathsResponse = self.repo.get_top_paths()
        self.assertEqual(len(pathsResponse), 10)
        self.assertEqual(pathsResponse[0].uniques, 4)
        self.assertEqual(pathsResponse[0].count, 23)
        self.assertEqual(pathsResponse[0].path, "/jkufro/PyGithub")
        self.assertEqual(
            pathsResponse[0].title,
            "jkufro/PyGithub: Typed interactions with the GitHub API v3",
        )
        self.assertEqual(
            repr(pathsResponse[0]),
            'Path(uniques=4, title="jkufro/PyGithub: Typed interactions with the GitHub API v3", path="/jkufro/PyGithub", count=23)',
        )

    def testGetViews(self):
        viewsResponse = self.repo.get_views_traffic()
        self.assertEqual(viewsResponse["count"], 93)
        self.assertEqual(viewsResponse["uniques"], 4)
        self.assertEqual(len(viewsResponse["views"]), 5)
        view_obj = viewsResponse["views"][0]
        self.assertEqual(view_obj.uniques, 4)
        self.assertEqual(
            view_obj.timestamp,
            datetime(2018, 11, 27, 0, 0, tzinfo=timezone.utc),
        )
        self.assertEqual(view_obj.count, 56)
        self.assertEqual(
            repr(view_obj),
            "View(uniques=4, timestamp=2018-11-27 00:00:00+00:00, count=56)",
        )

    def testGetClones(self):
        clonesResponse = self.repo.get_clones_traffic()
        self.assertEqual(clonesResponse["count"], 4)
        self.assertEqual(clonesResponse["uniques"], 4)
        self.assertEqual(len(clonesResponse["clones"]), 1)
        clone_obj = clonesResponse["clones"][0]
        self.assertEqual(clone_obj.uniques, 4)
        self.assertEqual(
            clone_obj.timestamp,
            datetime(2018, 11, 27, 0, 0, tzinfo=timezone.utc),
        )
        self.assertEqual(clone_obj.count, 4)
        self.assertEqual(
            repr(clone_obj),
            "Clones(uniques=4, timestamp=2018-11-27 00:00:00+00:00, count=4)",
        )
