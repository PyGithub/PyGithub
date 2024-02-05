############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 John Eskew <jeskew@edx.org>                                   #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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


class CommitCombinedStatus(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.combined_status = (
            self.g.get_repo("edx/edx-platform", lazy=True)
            .get_commit("74e70119a23fa3ffb3db19d4590eccfebd72b659")
            .get_combined_status()
        )

    def testAttributes(self):
        self.assertEqual(self.combined_status.state, "success")
        self.assertEqual(
            self.combined_status.statuses[0].url,
            "https://api.github.com/repos/edx/edx-platform/statuses/74e70119a23fa3ffb3db19d4590eccfebd72b659",
        )
        self.assertEqual(self.combined_status.statuses[1].id, 390603044)
        self.assertEqual(self.combined_status.statuses[2].state, "success")
        self.assertEqual(self.combined_status.statuses[3].description, "Build finished.")
        self.assertEqual(
            self.combined_status.statuses[4].target_url,
            "https://build.testeng.edx.org/job/edx-platform-python-unittests-pr/10504/",
        )
        self.assertEqual(
            self.combined_status.statuses[4].created_at,
            datetime(2015, 12, 14, 13, 24, 18, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.combined_status.statuses[3].updated_at,
            datetime(2015, 12, 14, 13, 23, 35, tzinfo=timezone.utc),
        )
        self.assertEqual(self.combined_status.sha, "74e70119a23fa3ffb3db19d4590eccfebd72b659")
        self.assertEqual(self.combined_status.total_count, 6)
        self.assertEqual(self.combined_status.repository.id, 10391073)
        self.assertEqual(self.combined_status.repository.full_name, "edx/edx-platform")
        self.assertEqual(
            self.combined_status.commit_url,
            "https://api.github.com/repos/edx/edx-platform/commits/74e70119a23fa3ffb3db19d4590eccfebd72b659",
        )
        self.assertEqual(
            self.combined_status.url,
            "https://api.github.com/repos/edx/edx-platform/commits/74e70119a23fa3ffb3db19d4590eccfebd72b659/status",
        )
        self.assertEqual(
            repr(self.combined_status),
            'CommitCombinedStatus(state="success", sha="74e70119a23fa3ffb3db19d4590eccfebd72b659")',
        )
