# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Jesse Li (https://github.com/jesseli2002)                     #
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

import datetime
import os

from . import Framework


class Release1140(Framework.TestCase):
    # https://github.com/PyGithub/PyGithub/issues/1140
    def setUp(self):
        super().setUp()
        self.content_path = "content.txt"
        with open(self.content_path, "w") as content:
            content.write("Files are my favorite!")

    def testUploadAssetFromMemory(self):
        release = self.g.get_user().get_repo("RepoTest").get_releases()[0]

        content_size = os.path.getsize(self.content_path)
        with open(self.content_path, "rb") as f:
            release.upload_asset_from_memory(
                f,
                content_size,
                name="file_name",
                content_type="text/plain",
                label="unit test artifact",
            )

