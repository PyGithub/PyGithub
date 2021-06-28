############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Jeppe Fihl-Pearson <jeppe@tenzer.dk>                          #
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


class WorkflowJob(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("PyGithub/PyGithub")
        self.job = self.repo.get_workflow_run(826874646).jobs()[0]

    def testAttributes(self):
        self.assertEqual(self.job.id, 2542493927)
        self.assertEqual(self.job.run_id, 826874646)
        self.assertEqual(
            self.job.run_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/826874646",
        )
        self.assertEqual(self.job.node_id, "MDg6Q2hlY2tSdW4yNTQyNDkzOTI3")
        self.assertEqual(self.job.head_sha, "59d8f95751de5e7cc107a043d8aac99da5445d45")
        self.assertEqual(
            self.job.url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/jobs/2542493927",
        )
        self.assertEqual(
            self.job.html_url,
            "https://github.com/PyGithub/PyGithub/actions/runs/826874646/jobs/791692136",
        )
        self.assertEqual(self.job.status, "completed")
        self.assertEqual(self.job.conclusion, "success")
        started_at = datetime.datetime(2021, 5, 10, 5, 23, 10)
        self.assertEqual(self.job.started_at, started_at)
        completed_at = datetime.datetime(2021, 5, 10, 5, 25, 27)
        self.assertEqual(self.job.completed_at, completed_at)
        self.assertEqual(self.job.name, "test (Python 3.6)")
        self.assertEqual(
            self.job.check_run_url,
            "https://api.github.com/repos/PyGithub/PyGithub/check-runs/2542493927",
        )
        self.assertListKeyEqual(
            self.job.steps,
            lambda s: s.name,
            [
                "Set up job",
                "Run actions/checkout@v2",
                "Set up Python",
                "Install tox",
                "Run tests",
                "Upload coverage to Codecov",
                "Post Run actions/checkout@v2",
                "Complete job",
            ],
        )
