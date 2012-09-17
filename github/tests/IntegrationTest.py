#!/bin/env python

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import Framework


from AuthenticatedUser import *
from Authentication import *
from Authorization import *
from Branch import *
from Commit import *
from CommitComment import *
from CommitStatus import *
from ContentFile import *
from Download import *
from Event import *
from Gist import *
from GistComment import *
from GitBlob import *
from GitCommit import *
from Github import *
from GitRef import *
from GitTag import *
from GitTree import *
from Hook import *
from Issue import *
from IssueComment import *
from IssueEvent import *
from Label import *
from Milestone import *
from NamedUser import *
from Organization import *
from PullRequest import *
from PullRequestComment import *
from PullRequestFile import *
from RateLimiting import *
from Repository import *
from RepositoryKey import *
from Tag import *
from Team import *
from UserKey import *
from Markdown import *

from PaginatedList import *
from Issue33 import *
from Issue50 import *
from Issue54 import *
from Exceptions import *
from Enterprise import *
from Issue80 import *

Framework.main()
