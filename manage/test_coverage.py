#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from __future__ import print_function

import sys
import coverage
import os
import unittest
sys.path.append(".")


baseDirectory = "PyGithub"


def main():
    cov = coverage.coverage(
        branch=True,
        include=[os.path.join(baseDirectory, "*")],
        omit=[os.path.join(baseDirectory, "tests.py"), os.path.join(baseDirectory, "Blocking", "tests", "*")]
    )
    cov.start()
    import PyGithub.tests
    unitTests = unittest.main(exit=False, module=PyGithub.tests)
    cov.stop()
    # cov.html_report(directory="test_coverage")
    coverageResult = cov.report() == 100.
    testsResult = unitTests.result.wasSuccessful()
    print()
    print("====================================")
    print("Functionalities:", "OK" if testsResult else "FAIL")
    print("Test coverage:", "OK" if coverageResult else "FAIL")
    print("====================================")
    sys.exit(0 if testsResult and coverageResult else 1)

main()
