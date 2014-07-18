# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import unittest

from PyGithub.unit_tests import *

from PyGithub.Blocking.tests.Classes.AuthenticatedUserTestCase import *
from PyGithub.Blocking.tests.Classes.CommitTestCase import *
from PyGithub.Blocking.tests.Classes.DirTestCase import *
from PyGithub.Blocking.tests.Classes.FileTestCase import *
from PyGithub.Blocking.tests.Classes.GistTestCase import *
from PyGithub.Blocking.tests.Classes.GitBlobTestCase import *
from PyGithub.Blocking.tests.Classes.GitCommitTestCase import *
from PyGithub.Blocking.tests.Classes.GithubTestCase import *
from PyGithub.Blocking.tests.Classes.GitRefTestCase import *
from PyGithub.Blocking.tests.Classes.GitTagTestCase import *
from PyGithub.Blocking.tests.Classes.GitTreeTestCase import *
from PyGithub.Blocking.tests.Classes.IssueTestCase import *
from PyGithub.Blocking.tests.Classes.LabelTestCase import *
from PyGithub.Blocking.tests.Classes.MilestoneTestCase import *
from PyGithub.Blocking.tests.Classes.OrganizationTestCase import *
from PyGithub.Blocking.tests.Classes.PublicKeyTestCase import *
from PyGithub.Blocking.tests.Classes.RepositoryTestCase import *
from PyGithub.Blocking.tests.Classes.SubmoduleTestCase import *
from PyGithub.Blocking.tests.Classes.SubscriptionTestCase import *
from PyGithub.Blocking.tests.Classes.SymLinkTestCase import *
from PyGithub.Blocking.tests.Classes.TagTestCase import *
from PyGithub.Blocking.tests.Classes.TeamTestCase import *
from PyGithub.Blocking.tests.Classes.UserTestCase import *

from PyGithub.Blocking.tests.Topics.AuthenticationTestCase import *
from PyGithub.Blocking.tests.Topics.DebugMessagesTestCases import *
from PyGithub.Blocking.tests.Topics.LazyCompletionTestCase import *
from PyGithub.Blocking.tests.Topics.PaginationTestCases import *
from PyGithub.Blocking.tests.Topics.ParameterTypingTestCase import *
from PyGithub.Blocking.tests.Topics.RateLimitingTestCase import *
from PyGithub.Blocking.tests.Topics.UnexpectedAttributeTestCase import *
from PyGithub.Blocking.tests.Topics.UnusualErrorsTestCase import *
from PyGithub.Blocking.tests.Topics.UpdateTestCase import *


if __name__ == "__main__":
    unittest.main()
