############################ Copyrights and license ############################
#                                                                              #
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

from datetime import datetime

from . import Framework


class Pages(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("PyGithub/PyGithub")
        self.pages = self.repo.get_pages()

    def testAttributes(self):
        pages = self.pages
        self.assertEqual(repr(pages), 'Pages(html_url="https://pygithub.example.com/", build_type="legacy")')
        self.assertEqual(pages.url, "https://api.github.com/repos/PyGithub/PyGithub/pages")
        self.assertEqual(pages.status, "built")
        self.assertEqual(pages.cname, "pygithub.example.com")
        self.assertEqual(pages.protected_domain_state, "verified")
        self.assertIsNone(pages.pending_domain_unverified_at)
        self.assertFalse(pages.custom_404)
        self.assertEqual(pages.html_url, "https://pygithub.example.com/")
        self.assertEqual(pages.build_type, "legacy")
        self.assertTrue(pages.public)
        self.assertTrue(pages.https_enforced)
        self.assertEqual(repr(pages.source), 'PagesSource(path="/docs", branch="main")')
        self.assertEqual(pages.source.branch, "main")
        self.assertEqual(pages.source.path, "/docs")
        certificate = pages.https_certificate
        self.assertEqual(repr(certificate), 'PagesHttpsCertificate(state="approved")')
        self.assertEqual(certificate.state, "approved")
        self.assertEqual(certificate.description, "Certificate is approved")
        self.assertEqual(certificate.domains, ["pygithub.example.com"])
        self.assertEqual(certificate.expires_at, datetime(2027, 2, 14))

    def testEdit(self):
        self.pages.edit(cname="pygithub.example.com", https_enforced=True, source_branch="main", source_path="/")

    def testEditRemoveCname(self):
        self.pages.edit(cname=None)

    def testEditSource(self):
        self.pages.edit(source="master /docs")

    def testEditWorkflow(self):
        self.pages.edit(build_type="workflow")

    def testEditIncompleteSource(self):
        with self.assertRaises(AssertionError):
            self.pages.edit(source_branch="main")

    def testEditSourceAndSourceBranch(self):
        with self.assertRaises(AssertionError):
            self.pages.edit(source="gh-pages", source_branch="main", source_path="/")

    def testDelete(self):
        self.pages.delete()
