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

import github.CodeScanAlert
import github.PaginatedList

from . import Framework


class CodeScanAlert(Framework.TestCase):
    alert: github.CodeScanAlert.CodeScanAlert

    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("matt-davis27/PyGithub")

    def testAttributes(self):
        alert = self.repo.get_codescan_alert(1)
        self.assertEqual(alert.number, 1)
        self.assertEqual(alert.created_at, datetime(2025, 8, 22, 23, 38, 23, tzinfo=timezone.utc))
        self.assertEqual(alert.updated_at, datetime(2025, 8, 25, 16, 3, 10, tzinfo=timezone.utc))
        self.assertEqual(alert.url, "https://api.github.com/repos/matt-davis27/PyGithub/code-scanning/alerts/1")
        self.assertEqual(alert.html_url, "https://github.com/matt-davis27/PyGithub/security/code-scanning/1")
        self.assertEqual(alert.state, "fixed")
        self.assertEqual(alert.fixed_at, datetime(2025, 8, 25, 16, 3, 9, tzinfo=timezone.utc))
        self.assertIsNone(alert.dismissed_by)
        self.assertIsNone(alert.dismissed_at)
        self.assertIsNone(alert.dismissed_reason)
        self.assertIsNone(alert.dismissed_comment)
        self.assertEqual(alert.rule.id, "actions/missing-workflow-permissions")
        self.assertEqual(alert.rule.severity, "warning")
        self.assertEqual(alert.rule.description, "Workflow does not contain permissions")
        self.assertEqual(alert.rule.name, "actions/missing-workflow-permissions")
        self.assertEqual(alert.rule.tags[0], "actions")
        self.assertEqual(alert.rule.tags[1], "external/cwe/cwe-275")
        self.assertEqual(alert.rule.tags[2], "maintainability")
        self.assertEqual(alert.rule.tags[3], "security")
        self.assertEqual(alert.rule.full_description, "Workflows should contain explicit permissions to restrict the scope of the default GITHUB_TOKEN.")
        self.assertTrue(alert.rule.help.startswith("## Overview"))
        self.assertEqual(alert.rule.security_severity_level, "medium")
        self.assertEqual(alert.tool.name, "CodeQL")
        self.assertIsNone(alert.tool.guid)
        self.assertEqual(alert.tool.version, "2.22.4")
        self.assertEqual(alert.most_recent_instance.ref, "refs/heads/main")
        self.assertEqual(alert.most_recent_instance.analysis_key, ".github/workflows/codeql.yml:analyze")
        self.assertEqual(alert.most_recent_instance.environment, "{\"build-mode\":\"none\",\"language\":\"actions\"}")
        self.assertEqual(alert.most_recent_instance.category, "/language:actions")
        self.assertEqual(alert.most_recent_instance.state, "fixed")
        self.assertEqual(alert.most_recent_instance.commit_sha, "908396804d41cdb1d0c0538b97f25a81383ee61b")
        self.assertEqual(alert.most_recent_instance.message["text"], "Actions job or workflow does not limit the permissions of the GITHUB_TOKEN. Consider setting an explicit permissions block, using the following as a minimal starting point: {{contents: read}}")
        self.assertEqual(alert.most_recent_instance.location.path, ".github/workflows/lint.yml")
        self.assertEqual(alert.most_recent_instance.location.start_line, 12)
        self.assertEqual(alert.most_recent_instance.location.end_line, 29)
        self.assertEqual(alert.most_recent_instance.location.start_column, 5)
        self.assertEqual(alert.most_recent_instance.location.end_column, 3)
        self.assertEqual(len(alert.most_recent_instance.classifications), 0)
        self.assertEqual(alert.instances_url, "https://api.github.com/repos/matt-davis27/PyGithub/code-scanning/alerts/1/instances")
        self.assertIsNone(alert.dismissal_approved_by)

    def testMultipleAlerts(self):
        multiple_alerts = self.repo.get_codescan_alerts()
        self.assertIsInstance(multiple_alerts, github.PaginatedList.PaginatedList)
        self.assertIsInstance(multiple_alerts[0], github.CodeScanAlert.CodeScanAlert)
        alert_list = [alert for alert in multiple_alerts]
        self.assertEqual(len(alert_list), 14)  # Update this when more alerts are added to the PyGithub repo

        test_alert = alert_list[-1]  # Alerts are returned in descending order, so the first alert is the most recent and the last alert is the oldest
        # Everything below is the same as testAttributes. This is just to make sure the list works.
        self.assertEqual(test_alert.number, 1)
        self.assertEqual(test_alert.created_at, datetime(2025, 8, 22, 23, 38, 23, tzinfo=timezone.utc))
        self.assertEqual(test_alert.updated_at, datetime(2025, 8, 25, 16, 3, 10, tzinfo=timezone.utc))
        self.assertEqual(test_alert.url, "https://api.github.com/repos/matt-davis27/PyGithub/code-scanning/alerts/1")
        self.assertEqual(test_alert.html_url, "https://github.com/matt-davis27/PyGithub/security/code-scanning/1")
        self.assertEqual(test_alert.state, "fixed")
        self.assertEqual(test_alert.fixed_at, datetime(2025, 8, 25, 16, 3, 9, tzinfo=timezone.utc))
        self.assertIsNone(test_alert.dismissed_by)
        self.assertIsNone(test_alert.dismissed_at)
        self.assertIsNone(test_alert.dismissed_reason)
        self.assertIsNone(test_alert.dismissed_comment)
        self.assertEqual(test_alert.rule.id, "actions/missing-workflow-permissions")
        self.assertEqual(test_alert.rule.severity, "warning")
        self.assertEqual(test_alert.rule.description, "Workflow does not contain permissions")
        self.assertEqual(test_alert.rule.name, "actions/missing-workflow-permissions")
        self.assertEqual(test_alert.rule.tags[0], "actions")
        self.assertEqual(test_alert.rule.tags[1], "external/cwe/cwe-275")
        self.assertEqual(test_alert.rule.tags[2], "maintainability")
        self.assertEqual(test_alert.rule.tags[3], "security")
        self.assertEqual(test_alert.rule.full_description, "Workflows should contain explicit permissions to restrict the scope of the default GITHUB_TOKEN.")
        self.assertTrue(test_alert.rule.help.startswith("## Overview"))
        self.assertEqual(test_alert.rule.security_severity_level, "medium")
        self.assertEqual(test_alert.tool.name, "CodeQL")
        self.assertIsNone(test_alert.tool.guid)
        self.assertEqual(test_alert.tool.version, "2.22.4")
        self.assertEqual(test_alert.most_recent_instance.ref, "refs/heads/main")
        self.assertEqual(test_alert.most_recent_instance.analysis_key, ".github/workflows/codeql.yml:analyze")
        self.assertEqual(test_alert.most_recent_instance.environment, "{\"build-mode\":\"none\",\"language\":\"actions\"}")
        self.assertEqual(test_alert.most_recent_instance.category, "/language:actions")
        self.assertEqual(test_alert.most_recent_instance.state, "fixed")
        self.assertEqual(test_alert.most_recent_instance.commit_sha, "908396804d41cdb1d0c0538b97f25a81383ee61b")
        self.assertEqual(test_alert.most_recent_instance.message["text"], "Actions job or workflow does not limit the permissions of the GITHUB_TOKEN. Consider setting an explicit permissions block, using the following as a minimal starting point: {{contents: read}}")
        self.assertEqual(test_alert.most_recent_instance.location.path, ".github/workflows/lint.yml")
        self.assertEqual(test_alert.most_recent_instance.location.start_line, 12)
        self.assertEqual(test_alert.most_recent_instance.location.end_line, 29)
        self.assertEqual(test_alert.most_recent_instance.location.start_column, 5)
        self.assertEqual(test_alert.most_recent_instance.location.end_column, 3)
        self.assertEqual(len(test_alert.most_recent_instance.classifications), 0)
        self.assertEqual(test_alert.instances_url, "https://api.github.com/repos/matt-davis27/PyGithub/code-scanning/alerts/1/instances")
        self.assertIsNone(test_alert.dismissal_approved_by)

    def testRepr(self):
        alert = self.repo.get_codescan_alert(1)
        self.assertEqual(repr(alert), 'CodeScanAlert(number=1, id="actions/missing-workflow-permissions")')

    def testGetAlertsWithArguments(self):
        alerts = self.repo.get_codescan_alerts(
            tool_name="CodeQL", ref="refs/heads/main", sort="created", direction="asc", state="fixed", severity="medium"
        )
        # Note, this doesn't test "tool_guid" or "pr" arguments as they are not found in the PyGithub repo test data
        self.assertEqual(len(list(alerts)), 10)  # Update this when more alerts are added to the PyGithub repo and marked as fixed
     