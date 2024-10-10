############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jeppe Fihl-Pearson <tenzer@tenzer.dk>                         #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Xavi Vega <xabi1309@gmail.com>                                #
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

from datetime import datetime, timezone

from . import Framework


class WorkflowJob(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("PyGithub/PyGithub")
        self.job = self.repo.get_workflow_run(4205440316).jobs()[0]

    def testAttributes(self):
        self.assertEqual(self.job.id, 11421878319)
        self.assertEqual(self.job.run_id, 4205440316)
        self.assertEqual(
            self.job.run_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/4205440316",
        )
        self.assertEqual(self.job.node_id, "CR_kwDOGpsAJ88AAAACqMwILw")
        self.assertEqual(self.job.head_sha, "06ec040b2eeef6c0316dd5abcda0608525a3f205")
        self.assertEqual(
            self.job.url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/jobs/11421878319",
        )
        self.assertEqual(
            self.job.html_url,
            "https://github.com/PyGithub/PyGithub/actions/runs/4205440316/jobs/7297536068",
        )
        self.assertEqual(self.job.status, "completed")
        self.assertEqual(self.job.conclusion, "success")
        started_at = datetime(2023, 2, 17, 16, 3, 46, tzinfo=timezone.utc)
        self.assertEqual(self.job.started_at, started_at)
        completed_at = datetime(2023, 2, 17, 16, 4, 52, tzinfo=timezone.utc)
        self.assertEqual(self.job.completed_at, completed_at)
        self.assertEqual(self.job.name, "test (Python 3.7)")
        self.assertEqual(
            self.job.check_run_url,
            "https://api.github.com/repos/PyGithub/PyGithub/check-runs/11421878319",
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
                "Post Set up Python",
                "Post Run actions/checkout@v2",
                "Complete job",
            ],
        )
        self.assertEqual(
            self.job.logs_url(),
            "https://pipelines.actions.githubusercontent.com/serviceHosts/d560a817-28d4-4544-a539-eb35c2a56899/_apis/pipelines/1/runs/5/signedlogcontent/5?urlExpires=2023-03-15T17%3A02%3A58.1305046Z&urlSigningMethod=HMACV1&urlSignature=abcdefghijklmn",
        )
        self.assertEqual(self.job.runner_id, 2)
        self.assertEqual(self.job.runner_name, "GitHub Actions 2")
        self.assertEqual(self.job.runner_group_id, 2)
        self.assertEqual(self.job.runner_group_name, "GitHub Actions")
        created_at = datetime(2023, 2, 17, 16, 3, 38, tzinfo=timezone.utc)
        self.assertEqual(self.job.created_at, created_at)
        self.assertEqual(self.job.head_branch, "tz-aware-2")
        self.assertEqual(self.job.labels, ["ubuntu-latest"])
        self.assertEqual(self.job.run_attempt, 1)
        self.assertEqual(self.job.workflow_name, "CI")
