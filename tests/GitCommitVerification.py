############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Claire Johns <42869556+johnsc1@users.noreply.github.com>      #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Tim Gates <tim.gates@iress.com>                               #
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

from . import Framework


class GitCommitVerification(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.commit = self.g.get_repo("PyGithub/PyGithub", lazy=True).get_commit(
            "801d64a4c5c0fcb63f695e0f6799117e76e5fe67"
        )

    def testAttributes(self):
        verification = self.commit.commit.verification
        self.assertEqual(
            verification.payload,
            "tree 4f502b4c4e5f0bdc7ee611f914bbdef51aef5efa\nparent 85087354078e426125dbbf88041bbaa6f35d8199\nauthor Tim Gates <tim.gates@iress.com> 1724830907 +1000\ncommitter Tim Gates <tim.gates@iress.com> 1724830915 +1000\n\nCommit verification support\n\nAdd support for verification component of Commit API response to see if\ncommit has been signed and the signature has been checked by Github\n",
        )
        self.assertEqual(verification.reason, "valid")
        self.assertEqual(
            verification.signature,
            "-----BEGIN PGP SIGNATURE-----\n\niMgEAAEKADIWIQRbWfY9TlELdM/5UaauO+DVOCPPBQUCZs7U0RQcdGltLmdhdGVz\nQGlyZXNzLmNvbQAKCRCuO+DVOCPPBQ2tBACAaRNONEWlDDNyYkAnIv8bZ55BuIuy\nTvbxVPjI8KLDqKLzgHO60HhQ3h/hCiug6g5fvVzyIrmayj3eEzaWAfa3+f37f3xK\nflZRMtNFUBYQoLTuyTkKvW85UA2AkUvKp3bHT5W6ZoCKqR5xw6pwKxuYQi7eJG9h\nNPrZTezkL6EDng==\n=Ng9G\n-----END PGP SIGNATURE-----",
        )
        self.assertEqual(verification.verified, True)
        self.assertIsNone(verification.verified_at)
        self.assertEqual(verification.reason, "valid")
        self.assertRegex(verification.signature, ".*PGP.*")
        self.assertRegex(verification.payload, ".*tree.*")
