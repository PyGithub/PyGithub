############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Pasha Fateev <pasha@autokitteh.com>                           #
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


class Copilot(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org_name = "BeaverSoftware"
        self.copilot = self.g.get_organization(self.org_name).get_copilot()

    def testAttributes(self):
        self.assertEqual(self.copilot.org_name, "BeaverSoftware")
        self.assertEqual(repr(self.copilot), 'Copilot(org_name="BeaverSoftware")')

        seats = list(self.copilot.get_seats())
        self.assertEqual(len(seats), 1)
        seat = seats[0]
        self.assertEqual(seat.created_at, datetime(2010, 7, 9, 6, 10, 6, tzinfo=timezone.utc))
        self.assertEqual(seat.updated_at, datetime(2012, 5, 26, 11, 25, 48, tzinfo=timezone.utc))
        self.assertEqual(seat.pending_cancellation_date, None)
        self.assertEqual(seat.last_activity_at, datetime(2012, 5, 26, 14, 59, 39, tzinfo=timezone.utc))
        self.assertEqual(seat.last_activity_editor, "vscode/1.0.0")
        self.assertEqual(seat.organization.login, self.org_name)
        self.assertEqual(seat.plan_type, "business")
        self.assertEqual(seat.assignee.login, "pashafateev")
        self.assertEqual(repr(seat), 'CopilotSeat(assignee=NamedUser(login="pashafateev"))')

    def testGetSeats(self):
        seats = self.copilot.get_seats()
        self.assertListKeyEqual(seats, lambda s: s.assignee.login, ["pashafateev"])

    def testAddSeats(self):
        seats_created = self.copilot.add_seats(["pashafateev"])
        self.assertEqual(seats_created, 1)

    def testRemoveSeats(self):
        seats_cancelled = self.copilot.remove_seats(["pashafateev"])
        self.assertEqual(seats_cancelled, 1)
