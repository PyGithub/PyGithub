############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
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


class CommitStatus(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.statuses = list(
            self.g.get_user().get_repo("PyGithub").get_commit("1292bf0e22c796e91cc3d6e24b544aece8c21f2a").get_statuses()
        )

    def testAttributes(self):
        self.assertEqual(
            self.statuses[0].created_at,
            datetime(2012, 9, 8, 11, 30, 56, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.statuses[0].updated_at,
            datetime(2012, 9, 8, 11, 30, 56, tzinfo=timezone.utc),
        )
        self.assertEqual(self.statuses[0].creator.login, "jacquev6")
        self.assertEqual(self.statuses[0].description, "Status successfuly created by PyGithub")
        self.assertEqual(self.statuses[1].description, None)
        self.assertEqual(self.statuses[0].id, 277040)
        self.assertEqual(self.statuses[0].state, "success")
        self.assertEqual(self.statuses[1].state, "pending")
        self.assertEqual(self.statuses[0].context, "build")
        self.assertEqual(
            self.statuses[0].target_url,
            "https://github.com/jacquev6/PyGithub/issues/67",
        )
        self.assertEqual(self.statuses[1].target_url, None)
        self.assertEqual(
            repr(self.statuses[0]),
            'CommitStatus(state="success", id=277040, context="build")',
        )
