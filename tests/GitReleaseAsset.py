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

import os
import zipfile
from datetime import datetime, timezone

from github import GithubException

from . import Framework

repo_name = "RepoTest"
user = "rickrickston123"
release_id = 28524234


class GitRelease(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user(user).get_repo(repo_name)
        self.release = self.repo.get_release(release_id)
        self.asset = self.release.assets[0]

    def testAttributes(self):
        self.assertEqual(self.asset.browser_download_url, "")
        self.assertEqual(self.asset.content_type, "")
        self.assertEqual(self.asset.created_at, datetime(2020, 1, 2, 12, 34, 56, tzinfo=timezone.utc))
        self.assertEqual(self.asset.download_count, 0)
        self.assertEqual(self.asset.id, "")
        self.assertEqual(self.asset.label, "")
        self.assertEqual(self.asset.name, "")
        self.assertEqual(self.asset.node_id, "")
        self.assertEqual(self.asset.size, 0)
        self.assertEqual(self.asset.state, "")
        self.assertEqual(self.asset.updated_at, datetime(2020, 1, 2, 12, 34, 56, tzinfo=timezone.utc))
        self.assertEqual(self.asset.uploader.login, "")
        self.assertEqual(self.asset.url, "")
