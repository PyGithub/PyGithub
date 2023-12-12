############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Yannick Jadoul <yannick.jadoul@belgacom.net>                  #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jeppe Fihl-Pearson <tenzer@tenzer.dk>                         #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Sasha Chung <50770626+nuang-ee@users.noreply.github.com>      #
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


class WorkflowRun(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("PyGithub/PyGithub")
        self.workflow_run = self.repo.get_workflow_run(3881497935)

    def testAttributes(self):
        self.assertEqual(
            repr(self.workflow_run),
            'WorkflowRun(url="https://api.github.com/repos/PyGithub/PyGithub/actions/runs/3881497935", id=3881497935)',
        )
        self.assertEqual(self.workflow_run.id, 3881497935)
        self.assertEqual(self.workflow_run.name, "CI")
        self.assertEqual(self.workflow_run.head_branch, "feat/workflow-run")
        self.assertEqual(self.workflow_run.head_sha, "c6e5cac67a58a4eb11f1f28567a77a6e2cc8ee98")
        self.assertEqual(self.workflow_run.path, ".github/workflows/ci.yml")
        self.assertEqual(self.workflow_run.display_title, "TEST PR")
        self.assertEqual(self.workflow_run.run_number, 930)
        self.assertEqual(self.workflow_run.run_attempt, 1)
        self.assertEqual(
            self.workflow_run.run_started_at,
            datetime(2023, 1, 10, 8, 24, 19, tzinfo=timezone.utc),
        )
        self.assertEqual(self.workflow_run.event, "pull_request")
        self.assertEqual(self.workflow_run.status, "completed")
        self.assertEqual(self.workflow_run.conclusion, "success")
        self.assertEqual(self.workflow_run.workflow_id, 1903133)
        self.assertEqual(
            self.workflow_run.url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/3881497935",
        )
        self.assertEqual(
            self.workflow_run.html_url,
            "https://github.com/PyGithub/PyGithub/actions/runs/3881497935",
        )
        self.assertEqual(self.workflow_run.pull_requests, [])
        created_at = datetime(2023, 1, 10, 8, 24, 19, tzinfo=timezone.utc)
        self.assertEqual(self.workflow_run.created_at, created_at)
        updated_at = datetime(2023, 1, 10, 8, 28, 20, tzinfo=timezone.utc)
        self.assertEqual(self.workflow_run.updated_at, updated_at)
        self.assertEqual(
            self.workflow_run.jobs_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/3881497935/jobs",
        )
        self.assertEqual(
            self.workflow_run.logs_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/3881497935/logs",
        )
        self.assertEqual(
            self.workflow_run.check_suite_url,
            "https://api.github.com/repos/PyGithub/PyGithub/check-suites/10279069747",
        )
        self.assertEqual(
            self.workflow_run.artifacts_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/3881497935/artifacts",
        )
        self.assertEqual(
            self.workflow_run.cancel_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/3881497935/cancel",
        )
        self.assertEqual(
            self.workflow_run.rerun_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/runs/3881497935/rerun",
        )
        self.assertEqual(
            self.workflow_run.workflow_url,
            "https://api.github.com/repos/PyGithub/PyGithub/actions/workflows/1903133",
        )
        self.assertEqual(self.workflow_run.head_commit.message, "add attribute 'name' on WorkflowRun")
        self.assertEqual(self.workflow_run.repository.name, "PyGithub")
        self.assertEqual(self.workflow_run.head_repository.name, "PyGithub")

    def test_timing(self):
        timing = self.workflow_run.timing()
        self.assertEqual(
            timing.billable,
            {
                "UBUNTU": {
                    "job_runs": [
                        {"duration_ms": 0, "job_id": 10545727758},
                        {"duration_ms": 0, "job_id": 10545727888},
                        {"duration_ms": 0, "job_id": 10545728039},
                        {"duration_ms": 0, "job_id": 10545728190},
                        {"duration_ms": 0, "job_id": 10545728356},
                    ],
                    "jobs": 5,
                    "total_ms": 0,
                }
            },
        )
        self.assertEqual(timing.run_duration_ms, 241000)

    def test_rerun(self):
        wr = self.repo.get_workflow_run(3910280793)
        self.assertFalse(wr.rerun())

    def test_rerun_with_successful_run(self):
        wr = self.repo.get_workflow_run(3881497935)
        self.assertFalse(wr.rerun())

    def test_cancel(self):
        wr = self.repo.get_workflow_run(3911660493)
        self.assertFalse(wr.cancel())

    def test_delete(self):
        wr = self.repo.get_workflow_run(3881497935)
        self.assertFalse(wr.delete())

    def test_jobs(self):
        self.assertListKeyEqual(
            self.workflow_run.jobs(),
            lambda j: j.id,
            [10545727758, 10545727888, 10545728039, 10545728190, 10545728356],
        )
