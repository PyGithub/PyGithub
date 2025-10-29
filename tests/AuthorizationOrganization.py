############################ Copyrights and license ############################
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

from . import Framework


class AuthorizationOrganization(Framework.TestCase):
    def setUp(self):
        super().setUp()

        self.org = self.g.get_organization("BeaverSoftware")
        authorizations = self.org.get_credential_authorizations()
        self.ao = list(authorizations)[0]

    def testAttributes(self):
        ao = self.ao
        self.assertEqual(repr(ao), "AuthorizationOrganization(credential_id=12345)")
        self.assertEqual(ao.authorized_credential_expires_at, datetime(2026, 9, 1, 22, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(ao.authorized_credential_id, 12341234)
        self.assertEqual(ao.authorized_credential_note, "test")
        self.assertEqual(ao.authorized_credential_title, None)
        self.assertEqual(ao.credential_authorized_at, datetime(2025, 9, 1, 9, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(ao.credential_accessed_at, datetime(2025, 10, 14, 6, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(ao.credential_id, 12345)
        self.assertEqual(ao.credential_type, "personal access token")
        self.assertEqual(ao.fingerprint, None)
        self.assertEqual(ao.login, "octocat")
        self.assertEqual(ao.scopes, ["read:org"])
        self.assertEqual(ao.token_last_eight, "ab12cd34")
