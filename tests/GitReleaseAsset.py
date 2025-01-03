############################ Copyrights and license ############################
#                                                                              #
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

from . import Framework

repo_name = "RepoTest"
user = "rickrickston123"
release_id = 28524234


class GitReleaseAsset(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user(user).get_repo(repo_name)
        self.release = self.repo.get_release(release_id)
        self.asset = self.release.assets[0]

    def testAttributes(self):
        self.assertEqual(
            self.asset.browser_download_url, "https://github.com/rickrickston123/RepoTest/releases/download/v1.0/fact"
        )
        self.assertEqual(self.asset.content_type, "application/octet-stream")
        self.assertEqual(self.asset.created_at, datetime(2020, 7, 14, 0, 58, 17, tzinfo=timezone.utc))
        self.assertEqual(self.asset.download_count, 0)
        self.assertEqual(self.asset.id, 22848494)
        self.assertIsNone(self.asset.label)
        self.assertEqual(self.asset.name, "fact")
        self.assertEqual(self.asset.node_id, "MDEyOlJlbGVhc2VBc3NldDIyODQ4NDk0")
        self.assertEqual(self.asset.size, 40)
        self.assertEqual(self.asset.state, "uploaded")
        self.assertEqual(self.asset.updated_at, datetime(2020, 7, 14, 0, 58, 18, tzinfo=timezone.utc))
        self.assertEqual(self.asset.uploader.login, "rickrickston123")
        self.assertEqual(
            self.asset.url, "https://api.github.com/repos/rickrickston123/RepoTest/releases/assets/22848494"
        )
