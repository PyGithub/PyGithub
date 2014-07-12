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


class TestFamily(object):
    def __init__(self, cov, module, description, include):
        self.cov = cov
        self.module = module
        self.description = description
        self.include = include

    def run(self):
        print("==== Runing", self.description, "====")
        self.cov.start()
        self.isResultOk = unittest.main(exit=False, module=self.module, argv=["test"]).result.wasSuccessful()
        self.cov.stop()
        self.cov.html_report(directory="unit_tests_coverage", include=self.include)
        self.isCoverageOk = self.cov.report(include=self.include) == 100.
        print()

    def report(self):
        print("= {}: {}".format(self.description, "OK" if self.isResultOk else "FAIL"))
        print("= {} coverage: {}".format(self.description, "OK" if self.isCoverageOk else "FAIL"))


def main():
    cov = coverage.coverage(
        branch=True,
        omit=[os.path.join(baseDirectory, "Blocking", "tests", "*"), os.path.join(baseDirectory, "*_tests.py")]
    )
    cov.start()

    families = []
    families.append(TestFamily(cov, "PyGithub.unit_tests", "Unit tests", [os.path.join(baseDirectory, "*", "_*"), os.path.join(baseDirectory, "Blocking", "PaginatedList.py")]))
    if "--unit" not in sys.argv:
        families.append(TestFamily(cov, "PyGithub.integ_tests", "Integration tests", [os.path.join(baseDirectory, "*")]))
    if "--all" in sys.argv:
        families.append(TestFamily(cov, "PyGithub.doc_tests", "Doc tests", [os.path.join(baseDirectory, "*")]))

    for f in families:
        f.run()

    print("====================================")
    for f in families:
        f.report()
    print("====================================")

main()
