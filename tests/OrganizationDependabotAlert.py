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

import github.OrganizationDependabotAlert
import github.PaginatedList
import github.Repository

from . import Framework


class OrganizationDependabotAlert(Framework.TestCase):
    alert: github.OrganizationDependabotAlert.OrganizationDependabotAlert

    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization(
            "github"
        )  # This is a placeholder organization that should always exist, switch this to your own test organization

    def testMultipleAlerts(self):
        multiple_alerts = self.org.get_dependabot_alerts()
        self.assertIsInstance(multiple_alerts, github.PaginatedList.PaginatedList)
        self.assertIsInstance(multiple_alerts[0], github.OrganizationDependabotAlert.OrganizationDependabotAlert)
        alert_list = [alert for alert in multiple_alerts]
        self.assertEqual(len(alert_list), 2)  # Update this when more alerts are added

        test_alert = alert_list[-1]
        self.assertEqual(test_alert.number, 1)
        self.assertEqual(test_alert.state, "open")
        self.assertEqual(test_alert.dependency.package.ecosystem, "pip")
        self.assertEqual(test_alert.dependency.package.name, "ansible")
        self.assertEqual(test_alert.dependency.manifest_path, "path/to/requirements.txt")
        self.assertEqual(test_alert.dependency.scope, "runtime")
        self.assertEqual(test_alert.security_advisory.ghsa_id, "GHSA-8f4m-hccc-8qph")
        self.assertEqual(test_alert.security_advisory.cve_id, "CVE-2021-20191")
        self.assertEqual(
            test_alert.security_advisory.summary,
            "Insertion of Sensitive Information into Log File in ansible",
        )
        self.assertEqual(
            test_alert.security_advisory.description,
            "A flaw was found in ansible. Credentials, such as secrets, are being disclosed in console log by default and not protected by no_log feature when using those modules. An attacker can take advantage of this information to steal those credentials. The highest threat from this vulnerability is to data confidentiality.",
        )
        self.assertEqual(test_alert.security_advisory.severity, "medium")
        self.assertEqual(test_alert.security_advisory.identifiers[0]["value"], "GHSA-8f4m-hccc-8qph")
        self.assertEqual(test_alert.security_advisory.identifiers[0]["type"], "GHSA")
        self.assertEqual(test_alert.security_advisory.identifiers[1]["value"], "CVE-2021-20191")
        self.assertEqual(test_alert.security_advisory.identifiers[1]["type"], "CVE")
        self.assertEqual(
            test_alert.security_advisory.published_at, datetime(2021, 6, 1, 17, 38, 0, tzinfo=timezone.utc)
        )
        self.assertEqual(test_alert.security_advisory.updated_at, datetime(2021, 8, 12, 23, 6, 0, tzinfo=timezone.utc))
        self.assertIsNone(test_alert.security_advisory.withdrawn_at)
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].package.ecosystem, "pip")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].package.name, "ansible")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].vulnerable_version_range, ">= 2.9.0, < 2.9.18")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].severity, "medium")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].first_patched_version["identifier"], "2.9.18")
        self.assertEqual(test_alert.security_vulnerability.package.ecosystem, "pip")
        self.assertEqual(test_alert.security_vulnerability.package.name, "ansible")
        self.assertEqual(test_alert.security_vulnerability.vulnerable_version_range, "< 2.8.19")
        self.assertEqual(test_alert.security_vulnerability.severity, "medium")
        self.assertEqual(test_alert.security_vulnerability.first_patched_version["identifier"], "2.8.19")

        self.assertEqual(test_alert.url, "https://api.github.com/repos/octo-org/hello-world/dependabot/alerts/1")
        self.assertEqual(test_alert.html_url, "https://github.com/octo-org/hello-world/security/dependabot/1")
        self.assertEqual(test_alert.created_at, datetime(2022, 6, 14, 15, 21, 52, tzinfo=timezone.utc))
        self.assertEqual(test_alert.updated_at, datetime(2022, 6, 14, 15, 21, 52, tzinfo=timezone.utc))
        self.assertIsNone(test_alert.dismissed_at)
        self.assertIsNone(test_alert.dismissed_by)
        self.assertIsNone(test_alert.dismissed_reason)
        self.assertIsNone(test_alert.dismissed_comment)
        self.assertIsNone(test_alert.fixed_at)

        self.assertIsInstance(test_alert.repository, github.Repository.Repository)
        self.assertEqual(test_alert.repository.name, "hello-world")
        self.assertEqual(test_alert.repository.full_name, "octo-org/hello-world")

    def testRepr(self):
        multiple_alerts = self.org.get_dependabot_alerts()
        alert_list = [alert for alert in multiple_alerts]
        test_alert = alert_list[-1]
        self.assertEqual(repr(test_alert), 'OrganizationDependabotAlert(number=1, ghsa_id="GHSA-8f4m-hccc-8qph")')

    def testGetAlertsWithAllArguments(self):
        alerts = self.org.get_dependabot_alerts("open", "medium", "pip", "ansible", "runtime", "created", "asc")
        self.assertEqual(len(list(alerts)), 1)  # Update this when more alerts are added
