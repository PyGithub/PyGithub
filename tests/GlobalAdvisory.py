from datetime import datetime, timezone

import github.GlobalAdvisory

from . import Framework


class GlobalAdvisory(Framework.TestCase):
    advisory: github.GlobalAdvisory.GlobalAdvisory

    def setUp(self):
        super().setUp()
        self.advisory = self.g.get_global_advisory("GHSA-wqc8-x2pr-7jqh")

    def testAttributes(self):
        self.assertListKeyEqual(
            self.advisory.credits,
            lambda e: (e.user.login, e.type),
            [
                ("loechel", "remediation_developer"),
                ("Quasar0147", "reporter"),
                ("despawningbone", "reporter"),
                ("dataflake", "coordinator"),
                ("nneonneo", "other"),
            ],
        )
        self.assertEqual(self.advisory.cve_id, "CVE-2023-37271")
        self.assertListKeyEqual(
            self.advisory.cwes,
            lambda e: (e.cwe_id, e.name),
            [
                ("CWE-913", "Improper Control of Dynamically-Managed Code Resources"),
            ],
        )
        self.assertEqual(
            self.advisory.description,
            "### Impact\n\nRestrictedPython does not check access to stack frames...",
        )
        self.assertEqual(self.advisory.ghsa_id, "GHSA-wqc8-x2pr-7jqh")
        self.assertEqual(
            self.advisory.github_reviewed_at,
            datetime(2023, 7, 10, 21, 53, 22, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.advisory.html_url,
            "https://github.com/advisories/GHSA-wqc8-x2pr-7jqh",
        )
        self.assertListEqual(
            self.advisory.identifiers,
            [{"type": "GHSA", "value": "GHSA-wqc8-x2pr-7jqh"}, {"type": "CVE", "value": "CVE-2023-37271"}],
        )
        self.assertEqual(self.advisory.nvd_published_at, None)
        self.assertEqual(
            self.advisory.published_at,
            datetime(2023, 7, 10, 21, 53, 22, tzinfo=timezone.utc),
        )
        self.assertListEqual(
            self.advisory.references,
            [
                "https://github.com/zopefoundation/RestrictedPython/security/advisories/GHSA-wqc8-x2pr-7jqh",
                "https://github.com/zopefoundation/RestrictedPython/commit/c8eca66ae49081f0016d2e1f094c3d72095ef531",
                "https://nvd.nist.gov/vuln/detail/CVE-2023-37271",
                "https://github.com/pypa/advisory-database/tree/main/vulns/restrictedpython/PYSEC-2023-118.yaml",
                "https://github.com/advisories/GHSA-wqc8-x2pr-7jqh",
            ],
        )
        self.assertEqual(
            self.advisory.repository_advisory_url,
            "https://api.github.com/repos/zopefoundation/RestrictedPython/security-advisories/GHSA-wqc8-x2pr-7jqh",
        )
        self.assertEqual(self.advisory.severity, "high")
        self.assertEqual(
            self.advisory.source_code_location,
            "https://github.com/zopefoundation/RestrictedPython",
        )
        self.assertEqual(
            self.advisory.summary,
            "RestrictedPython vulnerable to arbitrary code execution via stack frame sandbox escape",
        )
        self.assertEqual(
            self.advisory.type,
            "reviewed",
        )
        self.assertEqual(
            self.advisory.updated_at,
            datetime(2023, 7, 20, 18, 59, 27, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.advisory.url,
            "https://api.github.com/advisories/GHSA-wqc8-x2pr-7jqh",
        )
        self.assertListKeyEqual(
            self.advisory.vulnerabilities,
            lambda e: (
                (e.package.ecosystem, e.package.name),
                e.patched_versions,
                e.vulnerable_functions,
                e.vulnerable_version_range,
            ),
            [
                (("pip", "RestrictedPython"), None, [], "< 5.3"),
                (("pip", "RestrictedPython"), None, [], ">= 6.0a1.dev0, < 6.1"),
                (("pip", "restrictedpython"), None, [], ">= 0, < 5.3"),
            ],
        )
        self.assertEqual(self.advisory.withdrawn_at, None)
