############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
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


class WorkflowRun(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("PyGithub/PyGithub")
        self.workflow_run = self.repo.get_workflow_run(148274629)

    def testAttributes(self):
        self.assertEqual(
            repr(self.workflow_run),
            'WorkflowRun(url="https://api.github.com/repos/PyGithub/PyGithub/actions/runs/148274629", id=148274629)',
        )
        self.assertEqual(self.workflow_run.id, 148274629)
        self.assertEqual(self.workflow_run.head_branch, "more-precise-typing")
        self.assertEqual(
            self.workflow_run.head_sha, "f91c729d786efcc93db47dd755313a26172c105e"
        )
        self.assertEqual(self.workflow_run.run_number, 162)
        self.assertEqual(self.workflow_run.event, "pull_request")
        self.assertEqual(self.workflow_run.status, "completed")
        self.assertEqual(self.workflow_run.conclusion, "failure")
        self.assertEqual(self.workflow_run.workflow_id, 1026390)
        self.assertEqual(
            self.workflow_run.url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/148274629",
        )
        self.assertEqual(
            self.workflow_run.html_url,
            "https://github.com/PyGithub/PyGithub/actions/runs/148274629",
        )
        self.assertEqual(self.workflow_run.pull_requests, [])
        created_at = datetime.datetime(2020, 6, 26, 4, 51, 26)
        self.assertEqual(self.workflow_run.created_at, created_at)
        updated_at = datetime.datetime(2020, 6, 26, 4, 52, 59)
        self.assertEqual(self.workflow_run.updated_at, updated_at)
        self.assertEqual(
            self.workflow_run.jobs_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/148274629/jobs",
        )
        self.assertEqual(
            self.workflow_run.logs_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/148274629/logs",
        )
        self.assertEqual(
            self.workflow_run.check_suite_url,
            "https://api.github.com/repos/PyGithub/PyGithub/check-suites/843925976",
        )
        self.assertEqual(
            self.workflow_run.artifacts_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/148274629/artifacts",
        )
        self.assertEqual(
            self.workflow_run.cancel_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/148274629/cancel",
        )
        self.assertEqual(
            self.workflow_run.rerun_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/148274629/rerun",
        )
        self.assertEqual(
            self.workflow_run.workflow_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/workflows/1026390",
        )
        self.assertEqual(self.workflow_run.head_commit.message, "More precise typing")
        self.assertEqual(self.workflow_run.repository.name, "PyGithub")
        self.assertEqual(self.workflow_run.head_repository.name, "PyGithub")

    def test_timing(self):
        timing = self.workflow_run.timing()
        self.assertEqual(timing.billable, {})
        self.assertEqual(timing.run_duration_ms, 105000)

    def test_rerun(self):
        self.assertTrue(self.workflow_run.rerun())

    def test_rerun_with_successful_run(self):
        wr = self.repo.get_workflow_run(145732882)
        self.assertFalse(wr.rerun())

    def test_cancel(self):
        self.assertTrue(self.workflow_run.cancel())
