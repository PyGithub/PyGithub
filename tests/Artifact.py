############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Yixin Guo <yixin.guo@ni.com>                                  #
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

from . import Framework


class Artifact(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("PyGithub/PyGithub")
        workflow_run = self.repo.get_workflow_run(983901016)
        self.artifact = workflow_run.get_artifacts()[0]

    def testAttributes(self):
        self.assertEqual(
            repr(self.artifact),
            'Artifact(url="https://api.github.com/repos/PyGithub/PyGithub/actions/artifacts/71384263", id=71384263)',
        )
        self.assertEqual(self.artifact.id, 71384263)
        self.assertEqual(self.artifact.name, "fake_artifact")
        self.assertEqual(self.artifact.size_in_bytes, 7501080)
        self.assertEqual(
            self.artifact.url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/artifacts/71384263",
        )
        self.assertEqual(
            self.artifact.archive_download_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/artifacts/71384263/zip",
        )
        self.assertEqual(self.artifact.expired, False)
        created_at = datetime.datetime(2021, 6, 29, 20, 5, 19)
        self.assertEqual(self.artifact.created_at, created_at)
        expires_at = datetime.datetime(2021, 7, 4, 20, 5, 6)
        self.assertEqual(self.artifact.expires_at, expires_at)
        updated_at = datetime.datetime(2021, 6, 29, 20, 5, 20)
        self.assertEqual(self.artifact.updated_at, updated_at)

    def test_get_redirect_url(self):
        redirect_url = self.artifact.__get_download_redirect_url()
        self.assertEqual(
            redirect_url,
            "https://pipelines.actions.githubusercontent.com/vVJrNqNDqm6ysMIhP6YVnHS7J3XmqpVj7W6p4jmwYjdlXCLT8T/_apis/pipelines/1/runs/2597/signedartifactscontent?artifactName=fake_artifact&urlExpires=2021-06-29T22%3A42%3A22.7609983Z&urlSigningMethod=HMACV1&urlSignature=aHKUB4uqBSHptPLIbzTfJNjgPVBP2QIXvayJpUl8GNQ%3D",
        )
