# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2018 bbi-yggy <yossarian@blackbirdinteractive.com>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.github.io/PyGithub/v1/index.html                             #
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

import Framework

import github

# TODO: test for retrieving organization projects
# TODO: test for getting issue / pull request content from card

# https://github.com/PyGithub/PyGithub/issues/606
# https://github.com/PyGithub/PyGithub/pull/854
class Issue606(Framework.BasicTestCase):
    def setUp(self):
        Framework.BasicTestCase.setUp(self)
        self.g = github.Github(self.oauth_token)
        self.repo = self.g.get_user().get_repo("PyGithub")

    def testProjectList(self):
        for proj in self.repo.get_projects():
            print "project: %s" % (proj.name)
            for col in proj.get_columns():
                print "  column: %d: %s" % (col.id, col.name)
                for card in col.get_cards("all"):
                    print "    card: %d: %s" % (card.id, card.note)
                    print "      content type: %s" % (card.content_type)
                    print "      content url: %s" % (card.content_url)
