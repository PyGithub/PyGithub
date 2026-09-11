############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 myhelix <https://github.com/myhelix>                          #
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

from . import Framework


class AuditLog(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("BeaverSoftware")

    def testGetAuditLog(self):
        events = list(self.org.get_audit_log())
        self.assertEqual(len(events), 2)

        event = events[0]
        self.assertEqual(event.action, "repo.create")
        self.assertEqual(event.actor, "octocat")
        self.assertEqual(event.actor_id, 1)
        self.assertEqual(event.actor_ip, "1.2.3.4")
        self.assertEqual(event.actor_location, {"country_name": "United States"})
        self.assertEqual(event.org, "BeaverSoftware")
        self.assertEqual(event.org_id, 21341965)
        self.assertEqual(event.repo, "BeaverSoftware/new-repo")
        self.assertEqual(event.user, "octocat")
        self.assertEqual(event.timestamp, 1700000001000)
        self.assertEqual(repr(event), 'AuditLog(action="repo.create")')

        event2 = events[1]
        self.assertEqual(event2.action, "org.add_member")
        self.assertEqual(event2.actor, "admin-user")
        self.assertEqual(event2.user, "new-member")

    def testGetAuditLogWithAllArguments(self):
        events = list(self.org.get_audit_log(phrase="actor:octocat", include="all", order="asc", per_page=50))
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].action, "repo.create")
        self.assertEqual(events[0].actor, "octocat")

    def testGetAuditLogInvalidInclude(self):
        with self.assertRaises(AssertionError):
            self.org.get_audit_log(include="invalid")

    def testGetAuditLogInvalidOrder(self):
        with self.assertRaises(AssertionError):
            self.org.get_audit_log(order="random")
