#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from __future__ import print_function

import coverage
import glob
import os
import shutil
import sys
import types
import unittest
sys.path.append(".")


class TestFamily(object):
    def __init__(self, module, description, include, omit=None):
        self.module = module
        self.description = description
        self.include = include
        self.omit = omit

    def run(self):
        print("==== Runing", self.description, "====")
        shutil.copy("coverage/data.imports", "coverage/data." + self.module)
        cov = coverage.coverage(branch=True, data_file="coverage/data." + self.module)
        cov.load()
        try:
            cov.start()
            return unittest.main(exit=False, module=self.module, argv=["test"]).result.wasSuccessful()
        finally:
            print()
            cov.stop()
            cov.save()

    def report(self):
        if self.include is not None:
            cov = coverage.coverage(branch=True, data_file="coverage/data." + self.module)
            cov.load()
            if cov.html_report(directory=os.path.join("coverage", self.module), include=self.include, omit=self.omit) != 100.:
                print("==== Partial coverage of", self.description, "====")
                cov.report(include=self.include, omit=self.omit) == 100.
                print()


def main():
    cov = coverage.coverage(branch=True, data_file="coverage/data.imports")
    cov.start()
    import PyGithub.Blocking.AuthenticatedUser
    import PyGithub.Blocking.Commit
    import PyGithub.Blocking.Contributor
    import PyGithub.Blocking.Dir
    import PyGithub.Blocking.File
    import PyGithub.Blocking.Gist
    import PyGithub.Blocking.GitBlob
    import PyGithub.Blocking.GitCommit
    import PyGithub.Blocking.Github
    import PyGithub.Blocking.GitRef
    import PyGithub.Blocking.GitTag
    import PyGithub.Blocking.GitTree
    import PyGithub.Blocking.Issue
    import PyGithub.Blocking.Label
    import PyGithub.Blocking.Milestone
    import PyGithub.Blocking.Organization
    import PyGithub.Blocking.PublicKey
    import PyGithub.Blocking.PullRequest
    import PyGithub.Blocking.Repository
    import PyGithub.Blocking.Submodule
    import PyGithub.Blocking.Subscription
    import PyGithub.Blocking.SymLink
    import PyGithub.Blocking.Team
    import PyGithub.Blocking.User
    cov.stop()
    cov.save()

    families = []

    if len(sys.argv) == 1 or "--unit" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily("PyGithub.Blocking.tests.unit.all", "Unit tests", ["PyGithub/Blocking/_*.py", "PyGithub/Blocking/tests/unit/*.py"]))

    if len(sys.argv) == 1 or "--topics" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily("PyGithub.Blocking.tests.topics.all", "Topics tests", None))

    if len(sys.argv) == 1 or "--old-classes" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily("PyGithub.Blocking.tests.old_classes.all", "Old classes tests", ["PyGithub/Blocking/*.py", "PyGithub/Blocking/tests/old_classes/*.py"], ["PyGithub/Blocking/tests/Framework.py", "PyGithub/Blocking/tests/__init__.py", "PyGithub/Blocking/_*.py"]))

    for f in glob.glob("PyGithub/Blocking/tests/classes/*TestCases.py"):
        n = f[32:-12]
        if len(sys.argv) == 1 or "--classes" in sys.argv or "--all" in sys.argv or "--class={}".format(n) in sys.argv:
            families.append(TestFamily("PyGithub.Blocking.tests.classes.{}TestCases".format(n), "{} test cases".format(n), ["PyGithub/Blocking/{}.py".format(n), "PyGithub/Blocking/tests/classes/{}TestCases.py".format(n)]))

    if "--doc" in sys.argv or "--all" in sys.argv:
        families.append(TestFamily("PyGithub.Blocking.tests.doc", "Doc tests", None))

    for f in families:
        if not f.run():
            exit(1)

    for f in families:
        # @todoAlpha Once we reach 100% coverage on all families, detect coverage < 100%. Maybe report only if coverage < 100% ?
        f.report()

    if len([f for f in families if f.include is not None]) > 1:
        print()
        print("==== Global coverage ====")
        cov = coverage.coverage(branch=True, data_file="coverage/data")
        cov.combine()
        cov.report(show_missing=False, include="PyGithub/Blocking/*", omit="PyGithub/Blocking/tests/*")
        cov.html_report(directory=os.path.join("coverage", "global"), include="PyGithub/Blocking/*", omit="PyGithub/Blocking/tests/*")

main()
