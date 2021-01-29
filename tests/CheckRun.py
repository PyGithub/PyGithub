############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Dhruv Manilawala <dhruvmanila@gmail.com>                      #
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


class CheckRun(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("PyGithub/PyGithub")
        self.testrepo = self.g.get_repo("dhruvmanila/pygithub-testing")
        self.check_run_id = 1039891953
        self.check_run_ref = "6bc9ecc8c849df4e45e60c1e6a5df8876180a20a"
        self.check_run = self.repo.get_check_run(self.check_run_id)
        self.commit = self.repo.get_commit(self.check_run_ref)

    def testAttributes(self):
        self.assertEqual(self.check_run.app.id, 15368)
        self.assertEqual(self.check_run.app.slug, "github-actions")
        self.assertEqual(self.check_run.check_suite_id, 1110219217)
        self.assertEqual(
            self.check_run.completed_at,
            datetime.datetime(2020, 8, 28, 4, 21, 21, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.check_run.conclusion, "success")
        self.assertEqual(
            self.check_run.details_url,
            "https://github.com/PyGithub/PyGithub/runs/1039891953",
        )
        self.assertEqual(
            self.check_run.external_id, "6b512fe7-587c-5ecc-c4a3-03b7358c152d"
        )
        self.assertEqual(
            self.check_run.head_sha, "6bc9ecc8c849df4e45e60c1e6a5df8876180a20a"
        )
        self.assertEqual(
            self.check_run.html_url,
            "https://github.com/PyGithub/PyGithub/runs/1039891953",
        )
        self.assertEqual(self.check_run.id, 1039891953)
        self.assertEqual(self.check_run.name, "test (Python 3.8)")
        self.assertEqual(self.check_run.node_id, "MDg6Q2hlY2tSdW4xMDM5ODkxOTUz")
        self.assertEqual(self.check_run.output.annotations_count, 0)
        self.assertEqual(len(self.check_run.pull_requests), 0)
        self.assertEqual(
            self.check_run.started_at,
            datetime.datetime(2020, 8, 28, 4, 20, 27, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.check_run.status, "completed")
        self.assertEqual(
            self.check_run.url,
            "https://api.github.com/repos/PyGithub/PyGithub/check-runs/1039891953",
        )
        self.assertEqual(
            repr(self.check_run), 'CheckRun(id=1039891953, conclusion="success")'
        )

    def testCheckRunOutputAttributes(self):
        check_run_output = self.repo.get_check_run(1039891917).output
        self.assertEqual(check_run_output.title, "test (Python 3.6)")
        self.assertEqual(
            check_run_output.summary,
            "There are 1 failures, 0 warnings, and 0 notices.",
        )
        self.assertIsNone(check_run_output.text)
        self.assertEqual(check_run_output.annotations_count, 1)
        self.assertEqual(
            check_run_output.annotations_url,
            "https://api.github.com/repos/PyGithub/PyGithub/check-runs/1039891917/annotations",
        )
        self.assertEqual(
            repr(check_run_output), 'CheckRunOutput(title="test (Python 3.6)")'
        )

    def testGetCheckRunsForRef(self):
        check_runs = self.commit.get_check_runs()
        self.assertEqual(check_runs.totalCount, 4)
        self.assertListEqual(
            [check_run.id for check_run in check_runs],
            [1039891953, 1039891931, 1039891917, 1039891902],
        )

    def testGetCheckRunsForRefFilterByCheckName(self):
        check_runs = self.commit.get_check_runs(check_name="test (Python 3.6)")
        self.assertEqual(check_runs.totalCount, 1)
        self.assertListEqual([check_run.id for check_run in check_runs], [1039891917])

    def testGetCheckRunsForRefFilterByStatus(self):
        completed_check_runs = self.commit.get_check_runs(status="completed")
        self.assertEqual(completed_check_runs.totalCount, 4)
        self.assertListEqual(
            [check_run.id for check_run in completed_check_runs],
            [1039891953, 1039891931, 1039891917, 1039891902],
        )
        queued_check_runs = self.commit.get_check_runs(status="queued")
        self.assertEqual(queued_check_runs.totalCount, 0)
        in_progress_check_runs = self.commit.get_check_runs(status="in_progress")
        self.assertEqual(in_progress_check_runs.totalCount, 0)

    def testGetCheckRunsForRefFilterByFilter(self):
        latest_check_runs = self.commit.get_check_runs(filter="latest")
        all_check_runs = self.commit.get_check_runs(filter="all")
        self.assertEqual(latest_check_runs.totalCount, 4)
        self.assertListEqual(
            [check_run.id for check_run in latest_check_runs],
            [1039891953, 1039891931, 1039891917, 1039891902],
        )
        self.assertEqual(all_check_runs.totalCount, 4)
        self.assertListEqual(
            [check_run.id for check_run in all_check_runs],
            [1039891953, 1039891931, 1039891917, 1039891902],
        )

    def testCreateCheckRunInProgress(self):
        check_run = self.testrepo.create_check_run(
            name="basic_check_run",
            head_sha="0283d46537193f1fed7d46859f15c5304b9836f9",
            status="in_progress",
            external_id="50",
            details_url="https://www.example.com",
            started_at=datetime.datetime(2020, 9, 4, 1, 14, 52),
            output={"title": "PyGithub Check Run Test", "summary": "Test summary"},
        )
        self.assertEqual(check_run.name, "basic_check_run")
        self.assertEqual(check_run.head_sha, "0283d46537193f1fed7d46859f15c5304b9836f9")
        self.assertEqual(check_run.status, "in_progress")
        self.assertEqual(check_run.external_id, "50")
        self.assertEqual(
            check_run.started_at,
            datetime.datetime(2020, 9, 4, 1, 14, 52, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(check_run.output.title, "PyGithub Check Run Test")
        self.assertEqual(check_run.output.summary, "Test summary")
        self.assertIsNone(check_run.output.text)
        self.assertEqual(check_run.output.annotations_count, 0)
        # We don't want to keep this hanging
        check_run.edit(conclusion="success")
        self.assertEqual(check_run.conclusion, "success")
        self.assertEqual(check_run.status, "completed")

    def testCreateCheckRunCompleted(self):
        check_run = self.testrepo.create_check_run(
            name="completed_check_run",
            head_sha="0283d46537193f1fed7d46859f15c5304b9836f9",
            status="completed",
            started_at=datetime.datetime(2020, 10, 20, 10, 30, 29),
            conclusion="success",
            completed_at=datetime.datetime(2020, 10, 20, 11, 30, 50),
            output={
                "title": "Readme report",
                "summary": "There are 0 failures, 2 warnings, and 1 notices.",
                "text": "You may have some misspelled words on lines 2 and 4.",
                "annotations": [
                    {
                        "path": "README.md",
                        "annotation_level": "warning",
                        "title": "Spell Checker",
                        "message": "Check your spelling for 'banaas'.",
                        "raw_details": "Do you mean 'bananas' or 'banana'?",
                        "start_line": 2,
                        "end_line": 2,
                    },
                    {
                        "path": "README.md",
                        "annotation_level": "warning",
                        "title": "Spell Checker",
                        "message": "Check your spelling for 'aples'",
                        "raw_details": "Do you mean 'apples' or 'Naples'",
                        "start_line": 4,
                        "end_line": 4,
                    },
                ],
                "images": [
                    {
                        "alt": "Test Image",
                        "image_url": "http://example.com/images/42",
                    }
                ],
            },
            actions=[
                {
                    "label": "Fix",
                    "identifier": "fix_errors",
                    "description": "Allow us to fix these errors for you",
                }
            ],
        )
        self.assertEqual(check_run.name, "completed_check_run")
        self.assertEqual(check_run.head_sha, "0283d46537193f1fed7d46859f15c5304b9836f9")
        self.assertEqual(check_run.status, "completed")
        self.assertEqual(
            check_run.started_at,
            datetime.datetime(2020, 10, 20, 10, 30, 29, tzinfo=datetime.timezone.utc),
        ),
        self.assertEqual(check_run.conclusion, "success")
        self.assertEqual(
            check_run.completed_at,
            datetime.datetime(2020, 10, 20, 11, 30, 50, tzinfo=datetime.timezone.utc),
        ),
        self.assertEqual(check_run.output.annotations_count, 2)

    def testUpdateCheckRunSuccess(self):
        # This is a different check run created for this test
        check_run = self.testrepo.create_check_run(
            name="edit_check_run",
            head_sha="0283d46537193f1fed7d46859f15c5304b9836f9",
            status="in_progress",
            external_id="100",
            started_at=datetime.datetime(2020, 10, 20, 14, 24, 31),
            output={"title": "Check run for testing edit method", "summary": ""},
        )
        self.assertEqual(check_run.name, "edit_check_run")
        self.assertEqual(check_run.status, "in_progress")
        check_run.edit(
            status="completed",
            conclusion="success",
            output={
                "title": "Check run for testing edit method",
                "summary": "This is the summary of editing check run as completed.",
            },
        )
        self.assertEqual(check_run.name, "edit_check_run")
        self.assertEqual(check_run.status, "completed")
        self.assertEqual(check_run.conclusion, "success")
        self.assertEqual(check_run.output.title, "Check run for testing edit method")
        self.assertEqual(
            check_run.output.summary,
            "This is the summary of editing check run as completed.",
        )
        self.assertEqual(check_run.output.annotations_count, 0)

    def testUpdateCheckRunFailure(self):
        # This is a different check run created for this test
        check_run = self.testrepo.create_check_run(
            name="fail_check_run",
            head_sha="0283d46537193f1fed7d46859f15c5304b9836f9",
            status="in_progress",
            external_id="101",
            started_at=datetime.datetime(2020, 10, 20, 10, 14, 51),
            output={"title": "Check run for testing failure", "summary": ""},
        )
        self.assertEqual(check_run.name, "fail_check_run")
        self.assertEqual(check_run.status, "in_progress")
        check_run.edit(
            status="completed",
            conclusion="failure",
            output={
                "title": "Check run for testing failure",
                "summary": "There is 1 whitespace error.",
                "text": "You may have a whitespace error in the file 'test.py'",
                "annotations": [
                    {
                        "path": "test.py",
                        "annotation_level": "failure",
                        "title": "whitespace checker",
                        "message": "Remove the unnecessary whitespace from the file.",
                        "start_line": 2,
                        "end_line": 2,
                        "start_column": 17,
                        "end_column": 18,
                    }
                ],
            },
            actions=[
                {
                    "label": "Fix",
                    "identifier": "fix_errors",
                    "description": "Allow us to fix these errors for you",
                }
            ],
        )
        self.assertEqual(check_run.status, "completed")
        self.assertEqual(check_run.conclusion, "failure")
        self.assertEqual(check_run.output.annotations_count, 1)

    def testUpdateCheckRunAll(self):
        check_run = self.testrepo.get_check_run(1279259090)
        check_run.edit(
            name="update_all_params",
            head_sha="0283d46537193f1fed7d46859f15c5304b9836f9",
            details_url="https://www.example-url.com",
            external_id="49",
            started_at=datetime.datetime(2020, 10, 20, 1, 10, 20),
            completed_at=datetime.datetime(2020, 10, 20, 2, 20, 30),
            actions=[
                {
                    "label": "Hello World!",
                    "identifier": "identity",
                    "description": "Hey! This is a test",
                }
            ],
        )
        self.assertEqual(check_run.name, "update_all_params")
        self.assertEqual(check_run.head_sha, "0283d46537193f1fed7d46859f15c5304b9836f9")
        self.assertEqual(check_run.details_url, "https://www.example-url.com")
        self.assertEqual(check_run.external_id, "49")
        self.assertEqual(
            check_run.started_at,
            datetime.datetime(2020, 10, 20, 1, 10, 20, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            check_run.completed_at,
            datetime.datetime(2020, 10, 20, 2, 20, 30, tzinfo=datetime.timezone.utc),
        )

    def testCheckRunAnnotationAttributes(self):
        check_run = self.testrepo.get_check_run(1280914700)
        self.assertEqual(check_run.name, "annotations")
        annotation = check_run.get_annotations()[0]
        self.assertEqual(annotation.annotation_level, "warning")
        self.assertIsNone(annotation.end_column)
        self.assertEqual(annotation.end_line, 2)
        self.assertEqual(annotation.message, "Check your spelling for 'banaas'.")
        self.assertEqual(annotation.path, "README.md")
        self.assertEqual(annotation.raw_details, "Do you mean 'bananas' or 'banana'?")
        self.assertIsNone(annotation.start_column)
        self.assertEqual(annotation.start_line, 2)
        self.assertEqual(annotation.title, "Spell Checker")
        self.assertEqual(repr(annotation), 'CheckRunAnnotation(title="Spell Checker")')

    def testListCheckRunAnnotations(self):
        check_run = self.testrepo.get_check_run(1280914700)
        self.assertEqual(check_run.name, "annotations")
        self.assertEqual(check_run.status, "completed")
        annotation_list = check_run.get_annotations()
        self.assertEqual(annotation_list.totalCount, 2)
        self.assertListEqual(
            [annotation.start_line for annotation in annotation_list], [2, 4]
        )
