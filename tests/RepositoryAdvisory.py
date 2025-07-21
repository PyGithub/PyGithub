############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Jonathan Leitschuh <jonathan.leitschuh@gmail.com>             #
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

import github.RepositoryAdvisory

from . import Framework


class RepositoryAdvisory(Framework.TestCase):
    advisory: github.RepositoryAdvisory.RepositoryAdvisory

    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user().get_repo("security-research")
        self.advisory = self.repo.get_repository_advisory("GHSA-wmmh-r9w4-hpxx")
        self.advisory.clear_credits()
        self.advisory.offer_credit("octocat", "analyst")

    def testAttributes(self):
        self.assertEqual(self.advisory.author.login, "JLLeitschuh")
        self.assertEqual(self.advisory.closed_at, None)
        self.assertIsNone(self.advisory.collaborating_teams)
        self.assertIsNone(self.advisory.collaborating_users)
        self.assertEqual(
            self.advisory.created_at,
            datetime(2023, 3, 28, 21, 41, 40, tzinfo=timezone.utc),
        )
        self.assertListKeyEqual(self.advisory.credits, lambda e: (e.login, e.type), [("octocat", "analyst")])
        self.assertListKeyEqual(
            self.advisory.credits_detailed,
            lambda e: (e.user.login, e.type),
            [("octocat", "analyst")],
        )
        self.assertEqual(self.advisory.cve_id, "CVE-2023-00000")
        self.assertEqual(self.advisory.cvss.vector_string, "CVSS:3.1/AV:N/AC:H/PR:H/UI:R/S:C/C:H/I:H/A:H")
        self.assertIsNone(self.advisory.cvss_severities)
        self.assertListEqual(self.advisory.cwe_ids, ["CWE-400", "CWE-501"])
        self.assertListKeyEqual(
            self.advisory.cwes,
            lambda e: (e.cwe_id, e.name),
            [
                ("CWE-400", "Uncontrolled Resource Consumption"),
                ("CWE-501", "Trust Boundary Violation"),
            ],
        )
        self.assertEqual(
            self.advisory.description,
            "This is a detailed description of this advisories impact and patches.",
        )
        self.assertEqual(self.advisory.ghsa_id, "GHSA-wmmh-r9w4-hpxx")
        self.assertEqual(
            self.advisory.html_url,
            "https://github.com/JLLeitschuh/security-research/security/advisories/GHSA-wmmh-r9w4-hpxx",
        )
        self.assertEqual(
            self.advisory.identifiers,
            [{"value": "GHSA-wmmh-r9w4-hpxx", "type": "GHSA"}, {"value": "CVE-2023-00000", "type": "CVE"}],
        )
        self.assertIsNone(self.advisory.private_fork)
        self.assertEqual(self.advisory.published_at, None)
        self.assertIsNone(self.advisory.publisher)
        self.assertEqual(self.advisory.severity, "high")
        self.assertEqual(self.advisory.state, "draft")
        self.assertIsNone(self.advisory.submission)
        self.assertEqual(self.advisory.summary, "A test creating a GHSA via the API")
        self.assertEqual(
            self.advisory.updated_at,
            datetime(2023, 3, 30, 19, 31, 33, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.advisory.url,
            "https://api.github.com/repos/JLLeitschuh/security-research/security-advisories/GHSA-wmmh-r9w4-hpxx",
        )
        self.assertListKeyEqual(
            self.advisory.vulnerabilities,
            lambda e: (
                (e.package.ecosystem, e.package.name),
                e.patched_versions,
                e.vulnerable_functions,
                e.vulnerable_version_range,
            ),
            [(("npm", "a-package"), "1.0.5", ["function-name"], ">= 1.0.2")],
        )
        self.assertEqual(self.advisory.withdrawn_at, None)

    def testRemoveCredit(self):
        self.advisory.revoke_credit("octocat")
        self.assertListKeyEqual(
            self.advisory.credits,
            lambda e: e.login,
            [],
        )
        self.assertListKeyEqual(
            self.advisory.credits_detailed,
            lambda e: e.user.login,
            [],
        )

    def testOfferCredit(self):
        self.advisory.offer_credit("JLLeitschuh", "reporter")
        self.assertListKeyEqual(
            self.advisory.credits,
            lambda e: e.login,
            ["octocat", "JLLeitschuh"],
        )
        self.assertListKeyEqual(
            self.advisory.credits_detailed,
            lambda e: e.user.login,
            ["octocat", "JLLeitschuh"],
        )

    def testOfferCredits(self):
        self.advisory.clear_credits()
        self.advisory.offer_credits(
            [
                {"login": "octocat", "type": "sponsor"},
                {"login": "JLLeitschuh", "type": "reporter"},
            ]
        )
        self.assertListKeyEqual(
            self.advisory.credits_detailed,
            lambda e: (e.user.login, e.type),
            [("octocat", "sponsor"), ("JLLeitschuh", "reporter")],
        )

    def testRepositoryWithNoAdvisories(self):
        repo = self.g.get_user().get_repo("PyGithub")
        self.assertListKeyEqual(
            repo.get_repository_advisories(),
            lambda e: e.ghsa_id,
            [],
        )

    def testGetAdvisories(self):
        self.assertListKeyEqual(
            self.repo.get_repository_advisories(),
            lambda e: e.ghsa_id,
            [
                "GHSA-wmmh-r9w4-hpxx",
                "GHSA-wvgm-59wj-rh8h",
                "GHSA-22cq-8f5q-p5g2",
                "GHSA-7hfp-mpq6-2jhf",
                "GHSA-hfmw-fx2m-jj4c",
                "GHSA-rvp4-r3g6-8hxq",
                "GHSA-cm59-pr5q-cw85",
                "GHSA-vpcc-9rh2-8jfp",
                "GHSA-7fjx-657r-9r5h",
                "GHSA-22c6-wcjm-qfjg",
                "GHSA-5w9v-8x7x-rfqm",
                "GHSA-2r85-x9cf-8fcg",
                "GHSA-6m9h-r5m3-9r7f",
                "GHSA-f4jh-ww96-9h9j",
                "GHSA-j83w-7qr9-wv86",
                "GHSA-7gf3-89f6-823j",
                "GHSA-jpcm-4485-69p7",
            ],
        )

    def testCreateRepositoryAdvisory(self):
        repo = self.g.get_repo("JLLeitschuh/code-sandbox")
        advisory = repo.create_repository_advisory(
            "A test creating a GHSA via the API",
            "This is a detailed description of this advisories impact and patches.",
            "high",
            "CVE-2000-00000",
            vulnerabilities=[
                {
                    "package": {"ecosystem": "npm", "name": "b-package"},
                    "vulnerable_version_range": "<=4.0.4",
                    "patched_versions": "4.0.5",
                    "vulnerable_functions": ["function-name"],
                }
            ],
            cwe_ids=["CWE-401", "CWE-502"],
            credits=[
                {"login": "octocat", "type": "analyst"},
                {"login": "JLLeitschuh", "type": "reporter"},
            ],
        )
        self.assertEqual(advisory.ghsa_id, "GHSA-g45c-2crh-4xmp")
        self.assertEqual(advisory.summary, "A test creating a GHSA via the API")
        self.assertEqual(
            advisory.description,
            "This is a detailed description of this advisories impact and patches.",
        )
        self.assertEqual(advisory.severity, "high")
        self.assertEqual(advisory.cve_id, "CVE-2000-00000")
        self.assertListKeyEqual(
            advisory.vulnerabilities,
            lambda e: (
                (e.package.ecosystem, e.package.name),
                e.patched_versions,
                e.vulnerable_functions,
                e.vulnerable_version_range,
            ),
            [(("npm", "b-package"), "4.0.5", ["function-name"], "<=4.0.4")],
        )
        self.assertListKeyEqual(
            advisory.cwe_ids,
            lambda e: e,
            ["CWE-401", "CWE-502"],
        )
        self.assertListKeyEqual(
            advisory.credits_detailed,
            lambda e: (e.user.login, e.type),
            [("octocat", "analyst"), ("JLLeitschuh", "reporter")],
        )

    def testUpdateRepositoryAdvisory(self):
        repo = self.g.get_repo("JLLeitschuh/code-sandbox")
        advisory = repo.get_repository_advisory("GHSA-g45c-2crh-4xmp")
        advisory.edit(
            summary="A test updating a GHSA via the API",
            description="This is an updated detailed description of this advisories impact and patches.",
            severity_or_cvss_vector_string="low",
            cve_id="CVE-2000-00001",
            vulnerabilities=[
                {
                    "package": {"ecosystem": "npm", "name": "c-package"},
                    "vulnerable_version_range": "<=4.0.6",
                    "patched_versions": "4.0.7",
                    "vulnerable_functions": ["function-name-a"],
                }
            ],
            cwe_ids=["CWE-402", "CWE-500"],
            credits=[
                {"login": "octocat", "type": "sponsor"},
                {"login": "JLLeitschuh", "type": "reporter"},
            ],
        )
        self.assertEqual(advisory.ghsa_id, "GHSA-g45c-2crh-4xmp")
        self.assertEqual(advisory.summary, "A test updating a GHSA via the API")
        self.assertEqual(
            advisory.description,
            "This is an updated detailed description of this advisories impact and patches.",
        )
        self.assertEqual(advisory.severity, "low")
        self.assertEqual(advisory.cve_id, "CVE-2000-00001")
        self.assertListKeyEqual(
            advisory.vulnerabilities,
            lambda e: (
                (e.package.ecosystem, e.package.name),
                e.patched_versions,
                e.vulnerable_functions,
                e.vulnerable_version_range,
            ),
            [(("npm", "c-package"), "4.0.7", ["function-name-a"], "<=4.0.6")],
        )
        self.assertListKeyEqual(
            advisory.cwe_ids,
            lambda e: e,
            ["CWE-402", "CWE-500"],
        )
        self.assertListKeyEqual(
            advisory.credits_detailed,
            lambda e: (e.user.login, e.type),
            [("octocat", "sponsor"), ("JLLeitschuh", "reporter")],
        )

    def testUpdateSingleFieldDoesNotRemoveOtherFields(self):
        repo = self.g.get_repo("JLLeitschuh/code-sandbox")
        advisory = repo.create_repository_advisory(
            "A test editing a GHSA via the API with only a single manipulation",
            "This is a detailed description of this advisories impact and patches.",
            "high",
            "CVE-2000-00000",
            vulnerabilities=[
                {
                    "package": {"ecosystem": "npm", "name": "b-package"},
                    "vulnerable_version_range": "<=4.0.4",
                    "patched_versions": "4.0.5",
                    "vulnerable_functions": ["function-name"],
                }
            ],
            cwe_ids=["CWE-401", "CWE-502"],
            credits=[
                {"login": "octocat", "type": "analyst"},
                {"login": "JLLeitschuh", "type": "reporter"},
            ],
        )
        advisory.edit(description="A modified description")
        self.assertEqual(advisory.ghsa_id, "GHSA-4wwp-8jp9-9233")
        self.assertEqual(
            advisory.summary,
            "A test editing a GHSA via the API with only a single manipulation",
        )
        self.assertEqual(advisory.description, "A modified description")
        self.assertEqual(advisory.severity, "high")
        self.assertEqual(advisory.cve_id, "CVE-2000-00000")
        self.assertListKeyEqual(
            advisory.vulnerabilities,
            lambda e: (
                (e.package.ecosystem, e.package.name),
                e.patched_versions,
                e.vulnerable_functions,
                e.vulnerable_version_range,
            ),
            [(("npm", "b-package"), "4.0.5", ["function-name"], "<=4.0.4")],
        )
        self.assertListKeyEqual(
            advisory.cwe_ids,
            lambda e: e,
            ["CWE-401", "CWE-502"],
        )
        self.assertListKeyEqual(
            advisory.credits_detailed,
            lambda e: (e.user.login, e.type),
            [("octocat", "analyst"), ("JLLeitschuh", "reporter")],
        )

    def testAddVulnerability(self):
        repo = self.g.get_repo("JLLeitschuh/code-sandbox")
        advisory = repo.create_repository_advisory(
            summary="A test creating a GHSA via the API adding and removing vulnerabilities",
            description="Simple description",
            severity_or_cvss_vector_string="low",
        )
        advisory.add_vulnerability(ecosystem="maven")
        self.assertListKeyEqual(
            advisory.vulnerabilities,
            lambda e: (
                (e.package.ecosystem, e.package.name),
                e.patched_versions,
                e.vulnerable_functions,
                e.vulnerable_version_range,
            ),
            [(("maven", None), None, [], None)],
        )
        advisory.add_vulnerability(
            ecosystem="npm",
            package_name="b-package",
            vulnerable_version_range="<=4.0.9",
            patched_versions="4.0.10",
            vulnerable_functions=["function-name-c"],
        )
        self.assertListKeyEqual(
            advisory.vulnerabilities,
            lambda e: (
                (e.package.ecosystem, e.package.name),
                e.patched_versions,
                e.vulnerable_functions,
                e.vulnerable_version_range,
            ),
            [
                (("maven", None), None, [], None),
                (("npm", "b-package"), "4.0.10", ["function-name-c"], "<=4.0.9"),
            ],
        )
