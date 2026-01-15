############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Matthew Davis <35502728+matt-davis27@users.noreply.github.com>#
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

import github.OrganizationCodeScanAlert
import github.PaginatedList
import github.Repository

from . import Framework


class OrganizationCodeScanAlert(Framework.TestCase):
    alert: github.OrganizationCodeScanAlert.OrganizationCodeScanAlert

    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization(
            "github"
        )  # This is a placeholder organization that should always exist, switch this to your own test organization

    def testMultipleAlerts(self):
        multiple_alerts = self.org.get_codescan_alerts()
        self.assertIsInstance(multiple_alerts, github.PaginatedList.PaginatedList)
        self.assertIsInstance(multiple_alerts[0], github.OrganizationCodeScanAlert.OrganizationCodeScanAlert)
        alert_list = [alert for alert in multiple_alerts]
        self.assertEqual(len(alert_list), 2)  # Update this when more alerts are added

        test_alert = alert_list[0]
        self.assertEqual(test_alert.number, 4)
        self.assertEqual(test_alert.created_at, datetime(2020, 2, 13, 12, 29, 18, tzinfo=timezone.utc))
        self.assertEqual(test_alert.updated_at, datetime(2025, 8, 25, 16, 3, 10, tzinfo=timezone.utc))
        self.assertEqual(test_alert.url, "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/4")
        self.assertEqual(test_alert.html_url, "https://github.com/octocat/hello-world/code-scanning/4")
        self.assertEqual(test_alert.state, "open")
        self.assertIsNone(test_alert.dismissed_by)
        self.assertIsNone(test_alert.dismissed_at)
        self.assertIsNone(test_alert.dismissed_reason)
        self.assertIsNone(test_alert.dismissed_comment)
        self.assertEqual(test_alert.rule.id, "js/zipslip")
        self.assertEqual(test_alert.rule.severity, "error")
        self.assertEqual(test_alert.rule.description, "Arbitrary file write during zip extraction")
        self.assertEqual(test_alert.rule.name, "js/zipslip")
        self.assertEqual(test_alert.rule.tags[0], "security")
        self.assertEqual(test_alert.rule.tags[1], "external/cwe/cwe-022")
        self.assertEqual(test_alert.tool.name, "CodeQL")
        self.assertIsNone(test_alert.tool.guid)
        self.assertEqual(test_alert.tool.version, "2.4.0")
        self.assertEqual(test_alert.most_recent_instance.ref, "refs/heads/main")
        self.assertEqual(
            test_alert.most_recent_instance.analysis_key, ".github/workflows/codeql-analysis.yml:CodeQL-Build"
        )
        self.assertEqual(test_alert.most_recent_instance.environment, "{}")
        self.assertEqual(test_alert.most_recent_instance.category, ".github/workflows/codeql-analysis.yml:CodeQL-Build")
        self.assertEqual(test_alert.most_recent_instance.state, "open")
        self.assertEqual(test_alert.most_recent_instance.commit_sha, "39406e42cb832f683daa691dd652a8dc36ee8930")
        self.assertEqual(test_alert.most_recent_instance.message["text"], "This path depends on a user-provided value.")
        self.assertEqual(test_alert.most_recent_instance.location.path, "spec-main/api-session-spec.ts")
        self.assertEqual(test_alert.most_recent_instance.location.start_line, 917)
        self.assertEqual(test_alert.most_recent_instance.location.end_line, 917)
        self.assertEqual(test_alert.most_recent_instance.location.start_column, 7)
        self.assertEqual(test_alert.most_recent_instance.location.end_column, 18)
        self.assertEqual(test_alert.most_recent_instance.classifications[0], "test")
        self.assertEqual(
            test_alert.instances_url,
            "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/4/instances",
        )
        self.assertIsNone(test_alert.dismissal_approved_by)
        self.assertIsInstance(test_alert.repository, github.Repository.Repository)
        self.assertEqual(test_alert.repository.name, "Hello-World")
        self.assertEqual(test_alert.repository.full_name, "octocat/Hello-World")

    def testRepr(self):
        multiple_alerts = self.org.get_codescan_alerts()
        alert_list = [alert for alert in multiple_alerts]
        test_alert = alert_list[0]
        self.assertEqual(repr(test_alert), 'OrganizationCodeScanAlert(number=4, id="js/zipslip")')

    def testGetAlertsWithArguments(self):
        alerts = self.org.get_codescan_alerts(
            tool_name="CodeQL", ref="refs/heads/main", sort="created", direction="asc", state="open", severity="error"
        )
        # Note, this doesn't test "tool_guid" or "pr" arguments as they are not found in the test data
        self.assertEqual(len(list(alerts)), 2)  # Update this when more alerts are added
