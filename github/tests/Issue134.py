# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
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
################################################################################

import Framework
import github


class Issue134(Framework.BasicTestCase):  # https://github.com/jacquev6/PyGithub/pull/134
    def testGetAuthorizationsFailsWhenAutenticatedThroughOAuth(self):
        g = github.Github(self.oauth_token)
        with self.assertRaises(github.GithubException) as raisedexp:
            list(g.get_user().get_authorizations())
        self.assertEqual(raisedexp.exception.status, 404)

    def testGetAuthorizationsSucceedsWhenAutenticatedThroughLoginPassword(self):
        g = github.Github(self.login, self.password)
        self.assertListKeyEqual(g.get_user().get_authorizations(), lambda a: a.note, [None, None, 'cligh', None, None, 'GitHub Android App'])

    def testGetOAuthScopesFromHeader(self):
        g = github.Github(self.oauth_token)
        self.assertEqual(g.oauth_scopes, None)
        g.get_user().name
        self.assertEqual(g.oauth_scopes, ['repo', 'user', 'gist'])
