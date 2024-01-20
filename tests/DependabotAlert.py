from datetime import datetime, timezone

import github.DependabotAlert

from . import Framework


class DependabotAlert(Framework.TestCase):
    alert: github.DependabotAlert.DependabotAlert

    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("coopernetes/PyGithub")
        self.alert = self.repo.get_dependabot_alert(1)

    def testAttributes(self):
        self.assertEqual(self.alert.number, 1)
        self.assertEqual(self.alert.state, "dismissed")
        self.assertEqual(self.alert.dependency.package.ecosystem, "pip")
        self.assertEqual(self.alert.dependency.package.name, "jinja2")
        self.assertEqual(self.alert.dependency.manifest_path, "requirements/docs.txt")
        self.assertEqual(self.alert.dependency.scope, "runtime")
        self.assertEqual(self.alert.security_advisory.ghsa_id, "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(self.alert.security_advisory.cve_id, "CVE-2024-22195")
        self.assertEqual(
            self.alert.security_advisory.summary,
            "Jinja vulnerable to HTML attribute injection when passing user input as keys to xmlattr filter",
        )
        self.assertEqual(
            self.alert.security_advisory.description,
            "The `xmlattr` filter in affected versions of Jinja accepts keys containing spaces. XML/HTML attributes cannot contain spaces, as each would then be interpreted as a separate attribute. If an application accepts keys (as opposed to only values) as user input, and renders these in pages that other users see as well, an attacker could use this to inject other attributes and perform XSS. Note that accepting keys as user input is not common or a particularly intended use case of the `xmlattr` filter, and an application doing so should already be verifying what keys are provided regardless of this fix.",
        )
        self.assertEqual(self.alert.security_advisory.severity, "medium")
        self.assertEqual(self.alert.security_advisory.identifiers[0]["value"], "GHSA-h5c8-rqwp-cp95")
        self.assertEqual(self.alert.security_advisory.identifiers[0]["type"], "GHSA")
        self.assertEqual(self.alert.security_advisory.identifiers[1]["value"], "CVE-2024-22195")
        self.assertEqual(self.alert.security_advisory.identifiers[1]["type"], "CVE")
        self.assertEqual(
            self.alert.security_advisory.published_at, datetime(2024, 1, 11, 15, 20, 48, tzinfo=timezone.utc)
        )
        self.assertEqual(
            self.alert.security_advisory.updated_at, datetime(2024, 1, 11, 15, 20, 50, tzinfo=timezone.utc)
        )
        self.assertEqual(self.alert.security_advisory.withdrawn_at, None)
        self.assertEqual(self.alert.security_advisory.vulnerabilities[0].package["ecosystem"], "pip")
        self.assertEqual(self.alert.security_advisory.vulnerabilities[0].package["name"], "jinja2")
        self.assertEqual(self.alert.security_advisory.vulnerabilities[0].vulnerable_version_range, "< 3.1.3")
        self.assertEqual(self.alert.security_advisory.vulnerabilities[0].severity, "medium")
        self.assertEqual(self.alert.security_advisory.vulnerabilities[0].first_patched_version["identifier"], "3.1.3")
        self.assertEqual(self.alert.url, "https://api.github.com/repos/coopernetes/PyGithub/dependabot/alerts/1")
        self.assertEqual(self.alert.html_url, "https://github.com/coopernetes/PyGithub/security/dependabot/1")
        self.assertEqual(self.alert.created_at, datetime(2024, 1, 20, 17, 12, 38, tzinfo=timezone.utc))
        self.assertEqual(self.alert.updated_at, datetime(2024, 1, 20, 19, 4, 13, tzinfo=timezone.utc))
        self.assertEqual(self.alert.dismissed_at, datetime(2024, 1, 20, 19, 4, 13, tzinfo=timezone.utc))
        self.assertEqual(self.alert.dismissed_by.login, "coopernetes")
        self.assertEqual(self.alert.dismissed_reason, "tolerable_risk")
        self.assertEqual(self.alert.dismissed_comment, "Example comment")
        self.assertEqual(self.alert.fixed_at, None)
