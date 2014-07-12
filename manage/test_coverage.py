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
        self.isResultOk = unittest.main(exit=False, module="PyGithub." + self.module, argv=["test"]).result.wasSuccessful()
        self.cov.stop()
        self.cov.html_report(directory=os.path.join("coverage", self.module), include=self.include)
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
    if len(sys.argv) == 1 or "--unit" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily(cov, "unit_tests", "Unit tests", [os.path.join(baseDirectory, "*", "_*")]))
    if len(sys.argv) == 1 or "--integ" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily(cov, "integ_tests", "Integration tests", [os.path.join(baseDirectory, "*")]))
    if "--doc" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily(cov, "doc_tests", "Doc tests", [os.path.join(baseDirectory, "*")]))

    for f in families:
        f.run()

    print("====================================")
    for f in families:
        f.report()
    print("====================================")

main()
