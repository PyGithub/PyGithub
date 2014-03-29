# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

"""
"""

from PyGithub.Blocking.Exceptions import *
from PyGithub.Blocking._send import Reset

# @todoSomeday Low-level API to access headers of last request?
# @todoSomeday Open bug report to Github: master_branch is present in parent and source on GET /repo even with "Accept: v3"
# @todoSomeday Open feature request to Github to fork to org with team_id
# @todoSomeday Pull request to add blog in input array http://developer.github.com/v3/orgs/#edit-an-organization
# @todoBeta Should we have a Subscription.repository attribute encapsulating repository_url? Probably more a get_repository method?
# @todoSomeday Check that forks and sources are allowed in User.get_repos, and submit merge request to fix doc in developer.github.com
