############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Joseph Henrich <crimsonknave@gmail.com>                       #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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
from decimal import Decimal

import github.GlobalAdvisory

from . import Framework


class GlobalAdvisory(Framework.TestCase):
    advisory: github.GlobalAdvisory.GlobalAdvisory

    def setUp(self):
        super().setUp()

    def testAttributes(self):
        self.advisory = self.g.get_global_advisory("GHSA-wqc8-x2pr-7jqh")
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
        self.assertEqual(self.advisory.cvss.version, Decimal("3.1"))
        self.assertEqual(self.advisory.cvss.score, Decimal("8.4"))
        self.assertEqual(self.advisory.cvss.vector_string, "CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:L")
        self.assertEqual(
            self.advisory.cvss_severities,
            {
                "cvss_v3": {"vector_string": "CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:L", "score": 8.4},
                "cvss_v4": {"vector_string": None, "score": 0.0},
            },
        )
        self.assertListKeyEqual(
            self.advisory.cwes,
            lambda e: (e.cwe_id, e.name),
            [
                ("CWE-913", "Improper Control of Dynamically-Managed Code Resources"),
            ],
        )
        self.assertEqual(
            self.advisory.description[:100],
            "### Impact\n\nRestrictedPython does not check access to stack frames and their attributes. Stack frame",
        )
        self.assertEqual(self.advisory.epss, {"percentage": 0.00156, "percentile": 0.52841})
        self.assertEqual(self.advisory.ghsa_id, "GHSA-wqc8-x2pr-7jqh")
        self.assertEqual(self.advisory.github_reviewed_at, datetime(2023, 7, 10, 21, 53, 22, tzinfo=timezone.utc))
        self.assertEqual(
            self.advisory.html_url,
            "https://github.com/advisories/GHSA-wqc8-x2pr-7jqh",
        )
        self.assertListEqual(
            self.advisory.identifiers,
            [{"type": "GHSA", "value": "GHSA-wqc8-x2pr-7jqh"}, {"type": "CVE", "value": "CVE-2023-37271"}],
        )
        self.assertEqual(self.advisory.nvd_published_at, datetime(2023, 7, 11, 18, 15, 20, tzinfo=timezone.utc))
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
        self.assertEqual(self.advisory.updated_at, datetime(2023, 11, 7, 5, 5, 13, tzinfo=timezone.utc))
        self.assertEqual(self.advisory.url, "https://api.github.com/advisories/GHSA-wqc8-x2pr-7jqh")
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

    def testNewlyReleased(self):
        """
        Test an advisory that was freshly released and does not have values for all fields.
        """
        self.advisory = self.g.get_global_advisory("GHSA-cx3j-qqxj-9597")
        self.assertListKeyEqual(
            self.advisory.credits,
            lambda e: (e.user.login, e.type),
            [],
        )
        self.assertEqual(self.advisory.cve_id, "CVE-2023-3481")
        self.assertEqual(self.advisory.cvss.version, None)
        self.assertEqual(self.advisory.cvss.score, None)
        self.assertEqual(self.advisory.cvss.vector_string, None)
        self.assertListKeyEqual(
            self.advisory.cwes,
            lambda e: (e.cwe_id, e.name),
            [
                ("CWE-80", "Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)"),
                ("CWE-116", "Improper Encoding or Escaping of Output"),
            ],
        )
        self.assertEqual(
            self.advisory.description, "### Impact\nCritters version 0.0.17-0.0.19 have an issue when parsing..."
        )
        self.assertEqual(self.advisory.ghsa_id, "GHSA-cx3j-qqxj-9597")
        self.assertEqual(
            self.advisory.github_reviewed_at,
            datetime(2023, 8, 11, 18, 57, 53, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.advisory.html_url,
            "https://github.com/advisories/GHSA-cx3j-qqxj-9597",
        )
        self.assertListEqual(
            self.advisory.identifiers,
            [{"type": "GHSA", "value": "GHSA-cx3j-qqxj-9597"}, {"type": "CVE", "value": "CVE-2023-3481"}],
        )
        self.assertEqual(self.advisory.nvd_published_at, None)
        self.assertEqual(
            self.advisory.published_at,
            datetime(2023, 8, 11, 18, 57, 53, tzinfo=timezone.utc),
        )
        self.assertListEqual(
            self.advisory.references,
            [
                "https://github.com/GoogleChromeLabs/critters/security/advisories/GHSA-cx3j-qqxj-9597",
                "https://github.com/GoogleChromeLabs/critters/pull/133",
                "https://github.com/GoogleChromeLabs/critters/commit/7757902c9e0b3285d516359b3cb602cd9d50d80e",
                "https://github.com/advisories/GHSA-cx3j-qqxj-9597",
            ],
        )
        self.assertEqual(
            self.advisory.repository_advisory_url,
            "https://api.github.com/repos/GoogleChromeLabs/critters/security-advisories/GHSA-cx3j-qqxj-9597",
        )
        self.assertEqual(self.advisory.severity, "high")
        self.assertEqual(
            self.advisory.source_code_location,
            "https://github.com/GoogleChromeLabs/critters",
        )
        self.assertEqual(
            self.advisory.summary,
            "Critters Cross-site Scripting Vulnerability",
        )
        self.assertEqual(
            self.advisory.type,
            "reviewed",
        )
        self.assertEqual(
            self.advisory.updated_at,
            datetime(2023, 8, 11, 18, 57, 54, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.advisory.url,
            "https://api.github.com/advisories/GHSA-cx3j-qqxj-9597",
        )
        self.assertListKeyEqual(
            self.advisory.vulnerabilities,
            lambda e: (
                (e.package.ecosystem, e.package.name),
                e.patched_versions,
                e.vulnerable_functions,
                e.vulnerable_version_range,
            ),
            [(("npm", "critters"), None, [], ">= 0.0.17, <= 0.0.19")],
        )
        self.assertEqual(self.advisory.withdrawn_at, None)
