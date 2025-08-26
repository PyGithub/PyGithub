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

import github.SecretScanAlert
import github.PaginatedList

from . import Framework


class SecretScanAlert(Framework.TestCase):
    alert: github.SecretScanAlert.SecretScanAlert

    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("matt-davis27/PyGithub")

    def testAttributes(self):
        alert = self.repo.get_secret_scanning_alert(1)
        self.assertEqual(alert.number, 1)
        self.assertEqual(alert.created_at, datetime(2020, 11, 6, 18, 18, 30, tzinfo=timezone.utc))
        self.assertEqual(alert.url, "https://api.github.com/repos/matt-davis27/PyGithub/secret-scanning/alerts/1")
        self.assertEqual(alert.html_url, "https://github.com/matt-davis27/PyGithub/security/secret-scanning/1")
        self.assertEqual(alert.locations_url, "https://api.github.com/repos/matt-davis27/PyGithub/secret-scanning/alerts/1/locations")
        self.assertEqual(alert.state, "open")
        self.assertIsNone(alert.resolution)
        self.assertIsNone(alert.resolved_at)
        self.assertIsNone(alert.resolved_by)
        self.assertEqual(alert.secret_type, "mailchimp_api_key")
        self.assertEqual(alert.secret, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-us2")
        self.assertIsNone(alert.push_protection_bypassed_by)
        self.assertFalse(alert.push_protection_bypassed)
        self.assertIsNone(alert.push_protection_bypassed_at)
        self.assertIsNone(alert.push_protection_bypass_request_reviewer)
        self.assertIsNone(alert.push_protection_bypass_request_reviewer_comment)
        self.assertIsNone(alert.push_protection_bypass_request_comment)
        self.assertIsNone(alert.push_protection_bypass_request_html_url)
        self.assertIsNone(alert.resolution_comment)
        self.assertEqual(alert.validity, "unknown")
        self.assertFalse(alert.publicly_leaked)
        self.assertFalse(alert.multi_repo)
        self.assertFalse(alert.is_base64_encoded)
        self.assertEqual(alert.first_location_detected.path, "/example/secrets.txt")
        self.assertEqual(alert.first_location_detected.start_line, 1)
        self.assertEqual(alert.first_location_detected.end_line, 2)
        self.assertEqual(alert.first_location_detected.start_column, 3)
        self.assertEqual(alert.first_location_detected.end_column, 4)
        self.assertFalse(alert.has_more_locations)

    def testMultipleAlerts(self):
        multiple_alerts = self.repo.get_secret_scanning_alerts()
        self.assertIsInstance(multiple_alerts, github.PaginatedList.PaginatedList)
        self.assertIsInstance(multiple_alerts[0], github.SecretScanAlert.SecretScanAlert)
        alert_list = [alert for alert in multiple_alerts]
        self.assertEqual(len(alert_list), 2)

        test_alert = alert_list[-1]  # Alerts are returned in descending order, so the first alert is the most recent and the last alert is the oldest
        # Everything below is the same as testAttributes. This is just to make sure the list works.
        self.assertEqual(test_alert.number, 1)
        self.assertEqual(test_alert.created_at, datetime(2020, 11, 6, 18, 18, 30, tzinfo=timezone.utc))
        self.assertEqual(test_alert.url, "https://api.github.com/repos/matt-davis27/PyGithub/secret-scanning/alerts/1")
        self.assertEqual(test_alert.html_url, "https://github.com/matt-davis27/PyGithub/security/secret-scanning/1")
        self.assertEqual(test_alert.locations_url, "https://api.github.com/repos/matt-davis27/PyGithub/secret-scanning/alerts/1/locations")
        self.assertEqual(test_alert.state, "open")
        self.assertIsNone(test_alert.resolution)
        self.assertIsNone(test_alert.resolved_at)
        self.assertIsNone(test_alert.resolved_by)
        self.assertEqual(test_alert.secret_type, "mailchimp_api_key")
        self.assertEqual(test_alert.secret, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-us2")
        self.assertIsNone(test_alert.push_protection_bypassed_by)
        self.assertFalse(test_alert.push_protection_bypassed)
        self.assertIsNone(test_alert.push_protection_bypassed_at)
        self.assertIsNone(test_alert.push_protection_bypass_request_reviewer)
        self.assertIsNone(test_alert.push_protection_bypass_request_reviewer_comment)
        self.assertIsNone(test_alert.push_protection_bypass_request_comment)
        self.assertIsNone(test_alert.push_protection_bypass_request_html_url)
        self.assertIsNone(test_alert.resolution_comment)
        self.assertEqual(test_alert.validity, "unknown")
        self.assertFalse(test_alert.publicly_leaked)
        self.assertFalse(test_alert.multi_repo)
        self.assertFalse(test_alert.is_base64_encoded)
        self.assertEqual(test_alert.first_location_detected.path, "/example/secrets.txt")
        self.assertEqual(test_alert.first_location_detected.start_line, 1)
        self.assertEqual(test_alert.first_location_detected.end_line, 2)
        self.assertEqual(test_alert.first_location_detected.start_column, 3)
        self.assertEqual(test_alert.first_location_detected.end_column, 4)
        self.assertFalse(test_alert.has_more_locations)

    def testRepr(self):
        alert = self.repo.get_secret_scanning_alert(1)
        self.assertEqual(repr(alert), 'SecretScanAlert(number=1)')

    def testGetAlertsWithAllArguments(self):
        multiple_alerts = self.repo.get_secret_scanning_alerts(
            state="resolved", secret_type="adafruit_io_key", resolution="false_positive", sort="created", direction="asc", validity="inactive", is_publicly_leaked=False, is_multi_repo=False, hide_secret=True
        )
        alert_list = [alert for alert in multiple_alerts]
        self.assertEqual(len(alert_list), 1)

        test_alert = alert_list[-1]
        self.assertIsNone(test_alert.secret)  # Because hide_secret is True
