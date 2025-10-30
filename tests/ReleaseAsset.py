############################ Copyrights and license ############################
#                                                                              #
# Copyright 2017 Chris McBride <thehighlander@users.noreply.github.com>        #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Alex Olieman <alex@olieman.net>                               #
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

import hashlib
import tempfile
from datetime import datetime, timezone

from . import Framework


class ReleaseAsset(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.release = self.g.get_user().get_repo("PyGithub").get_releases()[0]
        self.asset = self.release.get_assets()[0]

    def testAttributes(self):
        self.assertEqual(self.release.id, 1210814)
        self.assertEqual(self.asset.id, 16)
        self.assertEqual(
            self.asset.url,
            "https://api.github.com/api/v3/repos/edhollandAL/PyGithub/releases/assets/16",
        )
        self.assertEqual(self.asset.name, "Archive.zip")
        self.assertEqual(self.asset.label, "Installation msi & runbook zipped")
        self.assertEqual(self.asset.content_type, "application/zip")
        self.assertEqual(self.asset.state, "uploaded")
        self.assertEqual(self.asset.size, 3783)
        self.assertEqual(self.asset.download_count, 2)
        self.assertEqual(
            self.asset.created_at,
            datetime(2017, 2, 1, 22, 40, 58, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.asset.updated_at,
            datetime(2017, 2, 1, 22, 44, 58, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.asset.browser_download_url,
            "https://github.com/edhollandAL/PyGithub/releases/download/v1.25.2/Asset.zip",
        )
        self.assertEqual(self.asset.uploader.login, "PyGithub")
        self.assertEqual(
            repr(self.asset),
            'GitReleaseAsset(url="https://api.github.com/api/v3/repos/edhollandAL/PyGithub/releases/assets/16")',
        )

    def testDelete(self):
        self.assertTrue(self.asset.delete_asset())

    def testUpdate(self):
        new_name = "updated-name.zip"
        new_label = "Updated label"
        updated_asset = self.asset.update_asset(new_name, new_label)
        self.assertEqual(updated_asset.name, new_name)
        self.assertNotEqual(self.asset.name, updated_asset.name)
        self.assertEqual(updated_asset.label, new_label)
        self.assertNotEqual(self.asset.label, updated_asset.label)


class PublicReleaseAsset(Framework.TestCase):
    def setUp(self):
        self.authMode = "none"
        super().setUp()
        public_repo = self.g.get_repo("stellarcarbon/sorocarbon")
        self.release = public_repo.get_release(223668595)
        self.asset = self.release.assets[0]

    def testAttributes(self):
        self.assertEqual(self.release.id, 223668595)
        self.assertEqual(self.asset.id, 261582854)
        self.assertEqual(
            self.asset.url,
            "https://api.github.com/repos/stellarcarbon/sorocarbon/releases/assets/261582854",
        )
        self.assertEqual(self.asset.name, "sink-carbon_v0.3.0.wasm")
        self.assertEqual(self.asset.label, "")
        self.assertEqual(self.asset.content_type, "application/wasm")
        self.assertEqual(self.asset.state, "uploaded")
        self.assertEqual(self.asset.size, 4945)
        self.assertEqual(self.asset.digest, "sha256:2e4ca075988921c6c8bf01cc9e7bd4530830898f47346f1945cad930b7dfdf4d")
        self.assertEqual(
            self.asset.created_at,
            datetime(2025, 6, 6, 14, 43, 29, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.asset.updated_at,
            datetime(2025, 6, 6, 14, 43, 29, tzinfo=timezone.utc),
        )
        self.assertEqual(
            self.asset.browser_download_url,
            "https://github.com/stellarcarbon/sorocarbon/releases/download/v0.3.0__src_sink_carbon__sink-carbon_cli22.0.1/sink-carbon_v0.3.0.wasm",
        )
        self.assertEqual(self.asset.uploader.login, "github-actions[bot]")
        self.assertEqual(
            repr(self.asset),
            'GitReleaseAsset(url="https://api.github.com/repos/stellarcarbon/sorocarbon/releases/assets/261582854")',
        )

    def testDownload(self):
        with tempfile.TemporaryDirectory() as path:
            tmpf_path = path + "/asset"
            self.asset.download_asset(tmpf_path)
            with open(tmpf_path, "rb") as tmpf:
                tmpf.seek(0)
                hash = hashlib.sha256(tmpf.read())
                size = tmpf.tell()

        assert self.asset.digest
        digest = self.asset.digest.split(":")[1]
        self.assertEqual(hash.hexdigest(), digest)
        self.assertEqual(size, self.asset.size)
