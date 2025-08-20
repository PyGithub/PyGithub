############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Michell Stuttgart <michellstut@gmail.com>                     #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from datetime import date, datetime, timezone

from . import Framework


class Milestone(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.milestone = self.g.get_repo("PyGithub/PyGithub").get_milestone(1)

    def testAttributes(self):
        self.assertEqual(self.milestone.closed_at, datetime(2012, 3, 12, 22, 18, 49, tzinfo=timezone.utc))
        self.assertEqual(self.milestone.closed_issues, 2)
        self.assertEqual(self.milestone.created_at, datetime(2012, 3, 8, 12, 22, 10, tzinfo=timezone.utc))
        self.assertEqual(self.milestone.creator.login, "jacquev6")
        self.assertEqual(self.milestone.description, "")
        self.assertEqual(self.milestone.due_on, datetime(2012, 3, 13, 7, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(self.milestone.html_url, "https://github.com/PyGithub/PyGithub/milestone/1")
        self.assertEqual(self.milestone.id, 93546)
        self.assertEqual(
            self.milestone.labels_url, "https://api.github.com/repos/PyGithub/PyGithub/milestones/1/labels"
        )
        self.assertEqual(self.milestone.node_id, "MDk6TWlsZXN0b25lOTM1NDY=")
        self.assertEqual(self.milestone.number, 1)
        self.assertEqual(self.milestone.open_issues, 0)
        self.assertEqual(self.milestone.state, "closed")
        self.assertEqual(self.milestone.title, "Version 0.4")
        self.assertEqual(self.milestone.updated_at, datetime(2012, 9, 11, 18, 48, 34, tzinfo=timezone.utc))
        self.assertEqual(self.milestone.url, "https://api.github.com/repos/PyGithub/PyGithub/milestones/1")
        self.assertEqual(self.milestone.creator.login, "jacquev6")
        self.assertEqual(repr(self.milestone), 'Milestone(title="Version 0.4", number=1)')

    def testEditWithMinimalParameters(self):
        self.milestone.edit("Title edited by PyGithub")
        self.assertEqual(self.milestone.title, "Title edited by PyGithub")

    def testEditWithAllParameters(self):
        self.milestone.edit(
            "Title edited twice by PyGithub",
            "closed",
            "Description edited by PyGithub",
            due_on=date(2012, 6, 16),
        )
        self.assertEqual(self.milestone.title, "Title edited twice by PyGithub")
        self.assertEqual(self.milestone.state, "closed")
        self.assertEqual(self.milestone.description, "Description edited by PyGithub")
        self.assertEqual(
            self.milestone.due_on,
            datetime(2012, 6, 16, 7, 0, 0, tzinfo=timezone.utc),
        )

    def testGetLabels(self):
        self.assertListKeyEqual(
            self.milestone.get_labels(),
            lambda lb: lb.name,
            ["Public interface", "Project management"],
        )

    def testDelete(self):
        self.milestone.delete()
