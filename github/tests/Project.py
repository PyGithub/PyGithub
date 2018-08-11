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

def dump(obj, name="obj"):
    print
    for attr in dir(obj):
        if not attr.startswith("_") and not attr.startswith("raw"):
            print "%s.%s =" % (name, attr),
            print getattr(obj, attr)
    
class Project(Framework.TestCase):
    def setUp(self):
        # Force token authenticaton mode, since that's how the replay data was recorded.
        self.tokenAuthMode = True
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_user().get_repo('PyGithub')

    def testGetProject(self):
        id = 1682941
        proj = self.g.get_project(id)
        self.assertEqual(proj.id, id)
        self.assertEqual(proj.name, 'TestProject')
        
    def testGetOrganizationProjects(self):
        expectedProjects = ['Project1', 'Project2', 'Project3']
        org = self.g.get_organization('PyGithubTestOrg')
        projects = []
        for proj in org.get_projects("open"):
            projects.append(proj.name)
        self.assertEqual(projects, expectedProjects)
        
    def testGetRepositoryProjects(self):
        expectedProjects = ['TestProject', 'TestProjectClosed']
        projects = []
        for proj in self.repo.get_projects("all"):
            projects.append(proj.name)
        self.assertEqual(projects, expectedProjects)
        
    # See https://developer.github.com/v3/projects/#get-a-project
    def testProjectAttributes(self):
        id = 1682941
        proj = self.g.get_project(id)
        self.assertEqual(proj.owner_url, "https://api.github.com/repos/bbi-yggy/PyGithub")
        self.assertEqual(proj.url, "https://api.github.com/projects/1682941")
        self.assertEqual(proj.html_url, "https://github.com/bbi-yggy/PyGithub/projects/1")
        self.assertEqual(proj.columns_url, "https://api.github.com/projects/1682941/columns")
        self.assertEqual(proj.id, id)
        self.assertEqual(proj.node_id, "MDc6UHJvamVjdDE2ODI5NDE=")
        self.assertEqual(proj.name, 'TestProject')
        self.assertEqual(proj.body, "To be used for testing project access API for PyGithub.")
        self.assertEqual(proj.number, 1)
        self.assertEqual(proj.state, "open")
        self.assertEqual(proj.creator, self.repo.owner)
        self.assertEqual(proj.created_at.year, 2018)
        self.assertTrue(proj.updated_at > proj.created_at)
        
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
