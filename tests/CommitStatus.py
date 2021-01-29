############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Martijn Koster <mak-github@greenhills.co.uk>                  #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

import datetime

from . import Framework


class CommitStatus(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.statuses = list(
            self.g.get_user()
            .get_repo("PyGithub")
            .get_commit("1292bf0e22c796e91cc3d6e24b544aece8c21f2a")
            .get_statuses()
        )

    def testAttributes(self):
        self.assertEqual(
            self.statuses[0].created_at,
            datetime.datetime(2012, 9, 8, 11, 30, 56, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.statuses[0].updated_at,
            datetime.datetime(2012, 9, 8, 11, 30, 56, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.statuses[0].creator.login, "jacquev6")
        self.assertEqual(
            self.statuses[0].description, "Status successfuly created by PyGithub"
        )
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
