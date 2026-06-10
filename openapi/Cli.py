from __future__ import annotations

import os
import shutil
import sys
import unittest
from pathlib import Path
from unittest import SkipTest

from more_itertools import windowed
from parameterized import parameterized
from parameterized.parameterized import param


class Cli(unittest.TestCase):
    keepMode = False
    approveMode = False
    openapi_spec = "api.github.com"
    openapi_version = "2022-11-28"
    openapi_commit = "567046173a5469ed9d537d9d3ac397f51f1c6c77"

    pwd = Path(os.curdir).absolute()
    root_path = Path(__file__).parent.parent
    openapi_spec_path = Path(root_path, f"{openapi_spec}.{openapi_version}.sha-{openapi_commit[:9]}.json")
    tests_path = Path(__file__).parent / "cli-sequence"
    tests = [
        test
        for test in os.listdir(tests_path)
        if test and test.split("-", maxsplit=1)[0].isnumeric() and "-SKIP-" not in test
    ]
    tests = windowed([None] + sorted(tests), n=2)
    fail_fast = False

    @classmethod
    def setUpClass(cls):
        if not cls.openapi_spec_path.exists():
            code = os.system(
                f"{sys.executable} {cls.root_path}/scripts/openapi.py fetch --commit {cls.openapi_commit} {cls.openapi_spec} {cls.openapi_version} {cls.openapi_spec_path}"
            )
            assert code == 0, "Fetching OpenAPI spec failed"

    @staticmethod
    def get_test_name(func, num, p: param):
        return func.__name__ + "_" + p.args[1]

    def run(self, result=None):
        # make subsequent tests fail once a test fails
        Cli.fail_fast = result.session.testsfailed if result is not None else False
        return super().run(result)

    @parameterized.expand(tests, name_func=get_test_name)
    def test(self, prev_test: str | None, test: str):
        if Cli.fail_fast:
            raise SkipTest("Earlier test failed")

        # create the empty run directory
        test_path = Path(self.tests_path, test)
        actual_path = Path(test_path, "actual")
        expected_path = Path(test_path, "expected")
        run_path = Path(test_path, "run")
        if actual_path.exists():
            shutil.rmtree(actual_path)
        if not expected_path.exists():
            os.mkdir(expected_path)
        os.mkdir(actual_path)

        cmd_path = Path(test_path, "commands")
        actual_stdout = Path(actual_path, "stdout")
        actual_diff = Path(actual_path, "run.diff")
        expected_stdout = Path(expected_path, "stdout")
        expected_diff = Path(expected_path, "run.diff")

        prev_test_path = Path(self.tests_path, prev_test) if prev_test is not None else None
        prev_run_path = Path(prev_test_path, "run") if prev_test_path is not None else None

        # copy previous test's run directory
        if run_path.exists():
            shutil.rmtree(run_path)
        if prev_run_path is None:
            os.mkdir(run_path)
            os.symlink(self.openapi_spec_path, Path(run_path, "openapi.spec.json"))
        else:
            shutil.copytree(prev_run_path, run_path, symlinks=True)

        def execute(cmd: str, error_codes: dict[int, str] | None = None):
            code = os.system(cmd)
            if error_codes is not None and code in error_codes:
                self.assertEqual(code, 0, error_codes[code])
            else:
                self.assertEqual(code, 0, f"Executing command failed: {cmd}")

        # run commands
        execute(
            f"cd {run_path}; env ROOT='{self.root_path.relative_to(run_path, walk_up=True)}' LANG=en_US.UTF-8 /bin/bash -e -u -x -o pipefail '{cmd_path}' >'{actual_stdout}' 2>&1"
        )

        # diff stdout
        if self.approveMode:
            shutil.move(actual_stdout, expected_stdout)
        else:
            execute(
                f"cd {self.tests_path}; env LANG=en_US.UTF-8 diff --unified '{expected_stdout.relative_to(self.tests_path)}' '{actual_stdout.relative_to(self.tests_path)}'",
                {
                    256: f"Unexpected changes in STDOUT, approve changes by running: cp '{actual_stdout.relative_to(self.pwd)}' '{expected_stdout.relative_to(self.pwd)}'."
                },
            )

        # diff run dirs
        if prev_test is not None:
            before_path = Path(self.tests_path, "before")
            if before_path.is_symlink():
                os.unlink(before_path)
            os.symlink(Path(prev_test, "run"), before_path, target_is_directory=True)

            after_path = Path(self.tests_path, "after")
            if after_path.is_symlink():
                os.unlink(after_path)
            os.symlink(Path(test, "run"), after_path, target_is_directory=True)

            remove_file_timestamps = (
                "sed -E -e 's/^([-+]{3} .*\\s)[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\\.[0-9]+ \\+0000/\\1YYYY-MM-DD HH:MM:SS +0000/'"
                ""
            )
            execute(
                f"cd {self.tests_path}; env LANG=en_US.UTF-8 TZ=UTC diff --unified --recursive --new-file '{before_path.relative_to(self.tests_path)}' '{after_path.relative_to(self.tests_path)}' | {remove_file_timestamps} >'{actual_diff}' 2>&1 || true"
            )

            os.unlink(before_path)
            os.unlink(after_path)

            if self.approveMode:
                shutil.move(actual_diff, expected_diff)
            else:
                execute(
                    f"cd {self.tests_path}; env LANG=en_US.UTF-8 diff --unified '{expected_diff.relative_to(self.tests_path)}' '{actual_diff.relative_to(self.tests_path)}'",
                    {
                        256: f"Unexpected changes, approve changes by running: cp '{actual_diff.relative_to(self.pwd)}' '{expected_diff.relative_to(self.pwd)}'."
                    },
                )
            if not self.keepMode:
                shutil.rmtree(prev_run_path)

        # cleanup actual
        if not self.keepMode:
            shutil.rmtree(actual_path)


def keepMode():
    Cli.keepMode = True


def approveMode():
    Cli.approveMode = True
