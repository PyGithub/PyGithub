# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import logging
import unittest
import doctest
import os
import fnmatch

import GithubCredentials


def load_tests(loader, tests, ignore):
    def setUp(test):
        logging.getLogger("PyGithub").setLevel(logging.CRITICAL)

    files = []
    for root, dirNames, fileNames in os.walk("doc"):
        for fileName in fnmatch.filter(fileNames, "*.rst"):
            files.append(os.path.join(root, fileName))
    for root, dirNames, fileNames in os.walk("PyGithub"):
        for fileName in fnmatch.filter(fileNames, "*.py"):
            files.append(os.path.join(root, fileName))

    tests.addTests(doctest.DocFileSuite(*files, module_relative=False, setUp=setUp))
    return tests

if __name__ == "__main__":
    unittest.main()
