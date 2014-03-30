#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from __future__ import print_function

import sys
import coverage
import os
import types
import unittest
sys.path.append(".")


baseDirectory = "PyGithub"


def main():
    cov = coverage.coverage(
        branch=True,
        omit=[os.path.join(baseDirectory, "Blocking", "tests", "*"), os.path.join(baseDirectory, "tests.py"), os.path.join(baseDirectory, "unit_tests.py")]
    )
    cov.start()

    unitTestsResult = unittest.main(exit=False, module="PyGithub.unit_tests", argv=["test"]).result.wasSuccessful()

    cov.stop()
    incForUnitTests = [os.path.join(baseDirectory, "*", "_*"), os.path.join(baseDirectory, "Blocking", "PaginatedList.py")]
    cov.html_report(directory="unit_tests_coverage", include=incForUnitTests)
    unitTestsCoverage = cov.report(include=incForUnitTests) == 100.
    cov.start()

    if len(sys.argv) == 1:
        allTestsResult = unittest.main(exit=False, module="PyGithub.tests", argv=["test"]).result.wasSuccessful()

        cov.stop()
        incForAllTests = [os.path.join(baseDirectory, "*")]
        cov.html_report(directory="all_tests_coverage", include=incForAllTests)
        allTestsCoverage = cov.report(include=incForAllTests) == 100.

    print()
    print("====================================")
    print("= Unit tests:", "OK" if unitTestsResult else "FAIL")
    print("= Unit tests coverage:", "OK" if unitTestsCoverage else "FAIL")
    if len(sys.argv) == 1:
        print("= All tests:", "OK" if allTestsResult else "FAIL")
        print("= All tests coverage:", "OK" if allTestsCoverage else "FAIL")
    print("====================================")
    sys.exit(0 if unitTestsResult and unitTestsCoverage and allTestsResult else 1)  # @todoAlpha add "and allTestsCoverage"

main()
