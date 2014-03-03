# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import logging
import unittest
import sys
import doctest
import os
import fnmatch

from PyGithub.Blocking.tests.Classes.AuthenticatedUserTestCase import *
from PyGithub.Blocking.tests.Classes.GithubTestCase import *
from PyGithub.Blocking.tests.Classes.OrganizationTestCase import *
from PyGithub.Blocking.tests.Classes.RepositoryTestCase import *
from PyGithub.Blocking.tests.Classes.SubscriptionTestCase import *
from PyGithub.Blocking.tests.Classes.TeamTestCase import *
from PyGithub.Blocking.tests.Classes.UserTestCase import *

from PyGithub.Blocking.tests.Topics.AuthenticationTestCase import *
from PyGithub.Blocking.tests.Topics.BadAttributeExceptionTestCase import *
from PyGithub.Blocking.tests.Topics.DebugMessagesTestCases import *
from PyGithub.Blocking.tests.Topics.LazyCompletionTestCase import *
from PyGithub.Blocking.tests.Topics.PaginationTestCases import *
from PyGithub.Blocking.tests.Topics.ParameterTypingTestCase import *
from PyGithub.Blocking.tests.Topics.RateLimitingTestCase import *
from PyGithub.Blocking.tests.Topics.UnexpectedAttributeTestCase import *
from PyGithub.Blocking.tests.Topics.UnusualErrorsTestCase import *
from PyGithub.Blocking.tests.Topics.UpdateTestCase import *


try:
    import GithubCredentials
    hasGithubCredentials = True
except ImportError:
    hasGithubCredentials = False


shouldRunDocTests = hasGithubCredentials and sys.hexversion < 0x03000000


def load_tests(loader, tests, ignore):
    if shouldRunDocTests:
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
