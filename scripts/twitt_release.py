#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
# ##############################################################################

import sys
import twitter  # pip install python-twitter

import TwitterCredentials as cred
# Must contain:
# consumer_key = ""
# consumer_secret = ""
# access_token_key = ""
# access_token_secret = ""
# from https://dev.twitter.com/apps/5252388/show

api = twitter.Api(consumer_key=cred.consumer_key, consumer_secret=cred.consumer_secret, access_token_key=cred.access_token_key, access_token_secret=cred.access_token_secret)
message = "I've just published version " + sys.argv[1] + " of PyGithub http://github.com/jacquev6/PyGithub"
api.PostUpdate(message)
