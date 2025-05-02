############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
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

from datetime import datetime, timezone

import pytest

import github.DependabotAlert
import github.PaginatedList

from . import Framework


class DependabotAlert(Framework.TestCase):
    alert: github.DependabotAlert.DependabotAlert

    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("coopernetes/PyGithub")

    def testAttributes(self):
        alert = self.repo.get_dependabot_alert(1)
        self.assertIsNone(alert.auto_dismissed_at)
        self.assertEqual(alert.created_at, datetime(2024, 1, 20, 17, 12, 38, tzinfo=timezone.utc))
        self.assertEqual(alert.dependency.package.name, "jinja2")
        self.assertEqual(alert.dismissed_at, datetime(2024, 1, 21, 3, 35, 38, tzinfo=timezone.utc))
        self.assertEqual(alert.dismissed_by.login, "coopernetes")
        self.assertEqual(alert.dismissed_reason, "tolerable_risk")
        self.assertEqual(alert.dismissed_comment, "Example comment")
        self.assertIsNone(alert.fixed_at)
        self.assertEqual(alert.html_url, "https://github.com/coopernetes/PyGithub/security/dependabot/1")
        self.assertEqual(alert.number, 1)
        self.assertEqual(alert.security_advisory.ghsa_id, "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(alert.security_vulnerability.package.name, "jinja2")
        self.assertEqual(alert.state, "dismissed")
        self.assertEqual(alert.dependency.package.ecosystem, "pip")
        self.assertEqual(alert.dependency.package.name, "jinja2")
        self.assertEqual(alert.dependency.manifest_path, "requirements/docs.txt")
        self.assertEqual(alert.dependency.scope, "runtime")
        self.assertEqual(alert.security_advisory.ghsa_id, "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(alert.security_advisory.cve_id, "CVE-2024-22195")
        self.assertEqual(
            alert.security_advisory.summary,
            "Jinja vulnerable to HTML attribute injection when passing user input as keys to xmlattr filter",
        )
        self.assertEqual(
            alert.security_advisory.description,
            "The `xmlattr` filter in affected versions of Jinja accepts keys containing spaces. XML/HTML attributes cannot contain spaces, as each would then be interpreted as a separate attribute. If an application accepts keys (as opposed to only values) as user input, and renders these in pages that other users see as well, an attacker could use this to inject other attributes and perform XSS. Note that accepting keys as user input is not common or a particularly intended use case of the `xmlattr` filter, and an application doing so should already be verifying what keys are provided regardless of this fix.",
        )
        self.assertEqual(alert.security_advisory.severity, "medium")
        self.assertEqual(alert.security_advisory.identifiers[0]["value"], "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(alert.security_advisory.identifiers[0]["type"], "GHSA")
        self.assertEqual(alert.security_advisory.identifiers[1]["value"], "CVE-2024-22195")
        self.assertEqual(alert.security_advisory.identifiers[1]["type"], "CVE")
        self.assertEqual(
            alert.security_advisory.references[0]["url"],
            "https://github.com/pallets/jinja/security/advisories/GHSA-h5c8-rqwp-cp95",
        )
        self.assertEqual(
            alert.security_advisory.references[1]["url"], "https://nvd.nist.gov/vuln/detail/CVE-2024-22195"
        )
        self.assertEqual(
            alert.security_advisory.references[2]["url"],
            "https://github.com/pallets/jinja/commit/716795349a41d4983a9a4771f7d883c96ea17be7",
        )
        self.assertEqual(
            alert.security_advisory.references[3]["url"], "https://github.com/pallets/jinja/releases/tag/3.1.3"
        )
        self.assertEqual(
            alert.security_advisory.references[4]["url"], "https://github.com/advisories/GHSA-h5c8-rqwp-cp95"
        )
        self.assertEqual(alert.security_advisory.published_at, datetime(2024, 1, 11, 15, 20, 48, tzinfo=timezone.utc))
        self.assertEqual(alert.security_advisory.updated_at, datetime(2024, 1, 11, 15, 20, 50, tzinfo=timezone.utc))
        self.assertEqual(alert.security_advisory.withdrawn_at, None)
        self.assertEqual(alert.security_advisory.vulnerabilities[0].package.ecosystem, "pip")
        self.assertEqual(alert.security_advisory.vulnerabilities[0].package.name, "jinja2")
        self.assertEqual(alert.security_advisory.vulnerabilities[0].vulnerable_version_range, "< 3.1.3")
        self.assertEqual(alert.security_advisory.vulnerabilities[0].severity, "medium")
        self.assertEqual(alert.security_advisory.vulnerabilities[0].first_patched_version["identifier"], "3.1.3")
        self.assertEqual(alert.security_vulnerability.package.ecosystem, "pip")
        self.assertEqual(alert.security_vulnerability.package.name, "jinja2")
        self.assertEqual(alert.security_vulnerability.vulnerable_version_range, "< 3.1.3")
        self.assertEqual(alert.security_vulnerability.severity, "medium")
        self.assertEqual(alert.security_vulnerability.first_patched_version["identifier"], "3.1.3")
        self.assertEqual(alert.updated_at, datetime(2024, 1, 21, 3, 35, 38, tzinfo=timezone.utc))
        self.assertEqual(alert.url, "https://api.github.com/repos/coopernetes/PyGithub/dependabot/alerts/1")
        self.assertEqual(alert.html_url, "https://github.com/coopernetes/PyGithub/security/dependabot/1")

    def testMultipleAlerts(self):
        multiple_alerts = self.repo.get_dependabot_alerts()
        self.assertIsInstance(multiple_alerts, github.PaginatedList.PaginatedList)
        self.assertIsInstance(multiple_alerts[0], github.DependabotAlert.DependabotAlert)
        alert_list = [alert for alert in multiple_alerts]
        test_alert = alert_list[0]

        self.assertEqual(len(alert_list), 1)
        # Everything below is the same as testAttributes. This is just to make sure the list works.
        self.assertEqual(test_alert.number, 1)
        self.assertEqual(test_alert.state, "dismissed")
        self.assertEqual(test_alert.dependency.package.ecosystem, "pip")
        self.assertEqual(test_alert.dependency.package.name, "jinja2")
        self.assertEqual(test_alert.dependency.manifest_path, "requirements/docs.txt")
        self.assertEqual(test_alert.dependency.scope, "runtime")
        self.assertEqual(test_alert.security_advisory.ghsa_id, "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(test_alert.security_advisory.cve_id, "CVE-2024-22195")
        self.assertEqual(
            test_alert.security_advisory.summary,
            "Jinja vulnerable to HTML attribute injection when passing user input as keys to xmlattr filter",
        )
        self.assertEqual(
            test_alert.security_advisory.description,
            "The `xmlattr` filter in affected versions of Jinja accepts keys containing spaces. XML/HTML attributes cannot contain spaces, as each would then be interpreted as a separate attribute. If an application accepts keys (as opposed to only values) as user input, and renders these in pages that other users see as well, an attacker could use this to inject other attributes and perform XSS. Note that accepting keys as user input is not common or a particularly intended use case of the `xmlattr` filter, and an application doing so should already be verifying what keys are provided regardless of this fix.",
        )
        self.assertEqual(test_alert.security_advisory.severity, "medium")
        self.assertEqual(test_alert.security_advisory.identifiers[0]["value"], "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(test_alert.security_advisory.identifiers[0]["type"], "GHSA")
        self.assertEqual(test_alert.security_advisory.identifiers[1]["value"], "CVE-2024-22195")
        self.assertEqual(test_alert.security_advisory.identifiers[1]["type"], "CVE")
        self.assertEqual(
            test_alert.security_advisory.published_at, datetime(2024, 1, 11, 15, 20, 48, tzinfo=timezone.utc)
        )
        self.assertEqual(
            test_alert.security_advisory.updated_at, datetime(2024, 1, 11, 15, 20, 50, tzinfo=timezone.utc)
        )
        self.assertEqual(test_alert.security_advisory.withdrawn_at, None)
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].package.ecosystem, "pip")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].package.name, "jinja2")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].vulnerable_version_range, "< 3.1.3")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].severity, "medium")
        self.assertEqual(test_alert.security_advisory.vulnerabilities[0].first_patched_version["identifier"], "3.1.3")
        self.assertEqual(test_alert.security_vulnerability.package.ecosystem, "pip")
        self.assertEqual(test_alert.security_vulnerability.package.name, "jinja2")
        self.assertEqual(test_alert.security_vulnerability.vulnerable_version_range, "< 3.1.3")
        self.assertEqual(test_alert.security_vulnerability.severity, "medium")
        self.assertEqual(test_alert.security_vulnerability.first_patched_version["identifier"], "3.1.3")

        self.assertEqual(test_alert.url, "https://api.github.com/repos/coopernetes/PyGithub/dependabot/alerts/1")
        self.assertEqual(test_alert.html_url, "https://github.com/coopernetes/PyGithub/security/dependabot/1")
        self.assertEqual(test_alert.created_at, datetime(2024, 1, 20, 17, 12, 38, tzinfo=timezone.utc))
        self.assertEqual(test_alert.updated_at, datetime(2024, 1, 20, 22, 4, tzinfo=timezone.utc))
        self.assertEqual(test_alert.dismissed_at, datetime(2024, 1, 20, 22, 4, tzinfo=timezone.utc))
        self.assertEqual(test_alert.dismissed_by.login, "coopernetes")
        self.assertEqual(test_alert.dismissed_reason, "tolerable_risk")
        self.assertEqual(test_alert.dismissed_comment, "Example comment")
        self.assertEqual(test_alert.fixed_at, None)

    def testRepr(self):
        alert = self.repo.get_dependabot_alert(1)
        self.assertEqual(repr(alert), 'DependabotAlert(number=1, ghsa_id="GHSA-h5c8-rqwp-cp95")')

    def testGetAlertsWithAllArguments(self):
        alerts = self.repo.get_dependabot_alerts(
            "open", "medium", "pip", "foo,jinja2", "bar/package.json,requirements/docs.txt", "runtime", "created", "asc"
        )
        self.assertEqual(len(list(alerts)), 1)

    def testUpdateAlertDismissedWithoutReason(self):
        with pytest.raises(AssertionError):
            self.repo.update_dependabot_alert(1, "dismissed")

    def testUpdateAlertOpen(self):
        alert = self.repo.update_dependabot_alert(1, "open")
        self.assertEqual(alert.state, "open")
        self.assertEqual(alert.dismissed_reason, None)
        self.assertEqual(alert.dismissed_comment, None)

    def testUpdateAlertDismissed(self):
        alert = self.repo.update_dependabot_alert(1, "dismissed", "tolerable_risk", "Example comment")
        self.assertEqual(alert.state, "dismissed")
        self.assertEqual(alert.dismissed_reason, "tolerable_risk")
        self.assertEqual(alert.dismissed_comment, "Example comment")
