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

class Project(Framework.TestCase):
    def setUp(self):
        # Force token authenticaton mode, since that's how the replay data was recorded.
        self.tokenAuthMode = True
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_user().get_repo("PyGithub")

    def testGetProject(self):
        proj = self.g.get_project(1085833)
        #print "Project: %s (id=%s)" % (proj.name, proj.id)
        
    def testGetOrganizationProjects(self):
        org = self.g.get_organization("blackbirdinteractive")
        #print "Organization: " + org.name
        for proj in org.get_projects():
            #print "  Project: %s (id=%s)" % (proj.name, proj.id)
            pass
        
    def testGetRepositoryProjects(self):
        pass
        
    def testProjectAttributes(self):
        pass
        
    def testProjectColumnAttributes(self):
        pass
        
    def testProjectCardAttributes(self):
        pass

    def testGetProjectCardContent(self):
        pass
        
    def testGetAllProjectCards(self):
        expectedProjects = ['TestProject']
        expectedCards = 3
        projects = []
        cards = 0
        for proj in self.repo.get_projects():
            projects.append(proj.name)
            for col in proj.get_columns():
                for card in col.get_cards("all"):
                    cards += 1
        self.assertEqual(projects, expectedProjects)
        self.assertEqual(cards, expectedCards)
