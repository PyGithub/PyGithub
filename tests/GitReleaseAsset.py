############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

import os
from datetime import datetime, timezone
from tempfile import NamedTemporaryFile
from unittest import skipIf

from . import Framework


class GitReleaseAsset(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.release = self.g.get_repo("EnricoMi/PyGithub", lazy=True).get_release(197548596)
        self.asset = self.release.assets[0]

    def testAttributes(self):
        self.assertEqual(
            self.asset.browser_download_url, "https://github.com/EnricoMi/PyGithub/releases/download/v1.55/asset1.md"
        )
        self.assertEqual(self.asset.content_type, "text/markdown")
        self.assertEqual(self.asset.created_at, datetime(2025, 1, 30, 11, 11, 32, tzinfo=timezone.utc))
        self.assertEqual(self.asset.digest, "sha256:abc123")
        self.assertEqual(self.asset.download_count, 0)
        self.assertEqual(self.asset.id, 224868540)
        self.assertIsNone(self.asset.label)
        self.assertEqual(self.asset.name, "asset1.md")
        self.assertEqual(self.asset.node_id, "RA_kwDOGpsAJ84NZzi8")
        self.assertEqual(self.asset.size, 2524)
        self.assertEqual(self.asset.state, "uploaded")
        self.assertEqual(self.asset.updated_at, datetime(2025, 1, 30, 11, 12, tzinfo=timezone.utc))
        self.assertEqual(self.asset.uploader.login, "EnricoMi")
        self.assertEqual(self.asset.url, "https://api.github.com/repos/EnricoMi/PyGithub/releases/assets/224868540")

    @skipIf(os.name == "nt", "not working on Windows")
    def testDownloadAssetFile(self):
        with NamedTemporaryFile(mode="rb") as file:
            self.asset.download_asset(file.name)
            content = file.read()
        self.assertEqual(len(content), 2524)
        self.assertEqual(
            content[:172],
            b"# PyGitHub\n\n"
            b"[![PyPI](https://img.shields.io/pypi/v/PyGithub.svg)](https://pypi.python.org/pypi/PyGithub)\n"
            b"![CI](https://github.com/PyGithub/PyGithub/workflows/CI/badge.svg)\n",
        )
        self.assertEqual(content[-50:], b"send an email to someone in the MAINTAINERS file.\n")

        source_asset = self.release.assets[1]
        with NamedTemporaryFile(mode="rb") as file:
            source_asset.download_asset(file.name)
            content = file.read()
        self.assertEqual(len(content), 1199)
        self.assertEqual(content[:19], b"\x1f\x8b\x08\x08\xf5\x9aag\x00\x03README.md")

    def testDownloadAssetStream(self):
        (_, _, chunks) = self.asset.download_asset()
        content = b"".join([chunk for chunk in chunks if chunk])
        self.assertEqual(len(content), 2524)
        self.assertEqual(
            content[:172],
            b"# PyGitHub\n\n"
            b"[![PyPI](https://img.shields.io/pypi/v/PyGithub.svg)](https://pypi.python.org/pypi/PyGithub)\n"
            b"![CI](https://github.com/PyGithub/PyGithub/workflows/CI/badge.svg)\n",
        )
        self.assertEqual(content[-50:], b"send an email to someone in the MAINTAINERS file.\n")

        source_asset = self.release.assets[1]
        (_, _, chunks) = source_asset.download_asset()
        content = b"".join([chunk for chunk in chunks if chunk])
        self.assertEqual(len(content), 1199)
        self.assertEqual(content[:19], b"\x1f\x8b\x08\x08\xf5\x9aag\x00\x03README.md")
