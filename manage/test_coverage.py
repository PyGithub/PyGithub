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
        self.isResultOk = unittest.main(exit=False, module="PyGithub.Blocking.tests." + self.module, argv=["test"]).result.wasSuccessful()
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
        families.append(TestFamily(cov, "unit.all", "Unit tests", [os.path.join(baseDirectory, "*", "_*")]))
    if len(sys.argv) == 1 or "--topics" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily(cov, "topics.all", "Topics tests", [os.path.join(baseDirectory, "*")]))
    if len(sys.argv) == 1 or "--old-classes" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily(cov, "old_classes.all", "Old classes tests", [os.path.join(baseDirectory, "*")]))
    if len(sys.argv) == 1 or "--classes" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily(cov, "classes.all", "Classes tests", [os.path.join(baseDirectory, "*")]))
    if "--doc" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily(cov, "doc", "Doc tests", [os.path.join(baseDirectory, "*")]))

    for f in families:
        f.run()

    print("====================================")
    for f in families:
        f.report()
    print("====================================")

main()


# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# from __future__ import print_function

# import unittest
# import os
# import shutil

# import coverage

# importsCoverage = coverage.coverage(branch=True, data_file="coverage.imports")
# importsCoverage.start()
# import PyGithub.Blocking.new_tests.All
# importsCoverage.stop()
# importsCoverage.save()

# isGlobalTestOk = True
# for module in PyGithub.Blocking.new_tests.All.all:
#     shutil.copy("coverage.imports", "coverage." + module)
#     cov = coverage.coverage(branch=True, data_file="coverage." + module)
#     cov.load()
#     cov.start()
#     isTestOk = unittest.main(exit=False, module="PyGithub.Blocking.new_tests." + module + "TestCases", argv=["test"]).result.wasSuccessful()
#     cov.stop()
#     cov.save()
#     isGlobalTestOk = isGlobalTestOk and isTestOk

# if not isGlobalTestOk:
#     exit(1)

# globalInclude = []
# for module in PyGithub.Blocking.new_tests.All.all:
#     cov = coverage.coverage(branch=True, data_file="coverage." + module)
#     cov.load()
#     include = ["PyGithub/Blocking/" + module + ".py", "PyGithub/Blocking/new_tests/" + module + "TestCases.py"]
#     isCoverageOk = cov.report(include=include) == 100.
#     globalInclude += include

# globalCoverage = coverage.coverage(branch=True, data_file="coverage")
# globalCoverage.combine()
# isGlobalCoverageOk = globalCoverage.report(include=globalInclude) == 100.

# if not isGlobalCoverageOk:
#     exit(1)
