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
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_user().get_repo('PyGithub')

    def testGetProject(self):
        pid = 1682941
        proj = self.g.get_project(pid)
        self.assertEqual(proj.id, pid)
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
        pid = 1682941
        proj = self.g.get_project(pid)
        self.assertEqual(proj.owner_url, "https://api.github.com/repos/bbi-yggy/PyGithub")
        self.assertEqual(proj.url, "https://api.github.com/projects/1682941")
        self.assertEqual(proj.html_url, "https://github.com/bbi-yggy/PyGithub/projects/1")
        self.assertEqual(proj.columns_url, "https://api.github.com/projects/1682941/columns")
        self.assertEqual(proj.id, pid)
        self.assertEqual(proj.node_id, "MDc6UHJvamVjdDE2ODI5NDE=")
        self.assertEqual(proj.name, 'TestProject')
        self.assertEqual(proj.body, "To be used for testing project access API for PyGithub.")
        self.assertEqual(proj.number, 1)
        self.assertEqual(proj.state, "open")
        self.assertEqual(proj.creator, self.repo.owner)
        self.assertEqual(proj.created_at.year, 2018)
        self.assertTrue(proj.updated_at > proj.created_at)

    # See https://developer.github.com/v3/projects/columns/#get-a-project-column
    def testProjectColumnAttributes(self):
        proj = self.g.get_project(1682941)
        col = proj.get_columns()[0]
        self.assertEqual(col.id, 3138830)
        self.assertEqual(col.node_id, "MDEzOlByb2plY3RDb2x1bW4zMTM4ODMw")
        self.assertEqual(col.name, "To Do")
        self.assertEqual(col.url, "https://api.github.com/projects/columns/3138830")
        self.assertEqual(col.project_url, "https://api.github.com/projects/1682941")
        self.assertEqual(col.cards_url, "https://api.github.com/projects/columns/3138830/cards")
        self.assertEqual(col.created_at.year, 2018)
        self.assertTrue(col.updated_at >= col.created_at)

    # See https://developer.github.com/v3/projects/cards/#get-a-project-card
    def testProjectCardAttributes(self):
        proj = self.g.get_project(1682941)
        col = proj.get_columns()[1]
        card = col.get_cards()[0]
        self.assertEqual(card.url, "https://api.github.com/projects/columns/cards/11780055")
        self.assertEqual(card.column_url, "https://api.github.com/projects/columns/3138831")
        self.assertEqual(card.content_url, "https://api.github.com/repos/bbi-yggy/PyGithub/issues/1")
        self.assertEqual(card.id, 11780055)
        self.assertEqual(card.node_id, "MDExOlByb2plY3RDYXJkMTE3ODAwNTU=")
        self.assertEqual(card.note, None)   # No notes for cards with content.
        self.assertEqual(card.creator, self.repo.owner)
        self.assertEqual(card.created_at.year, 2018)
        self.assertTrue(card.updated_at >= card.created_at)
        self.assertFalse(card.archived)

    def testGetProjectCardContent(self):
        proj = self.g.get_project(1682941)
        col = proj.get_columns()[1]
        cards = col.get_cards()

        pull_card = cards[0]
        pull = pull_card.get_content("PullRequest")
        self.assertIsInstance(pull, github.PullRequest.PullRequest)
        self.assertEqual(pull.title, "Work in progress on support for GitHub projects API.")

        issue_card = cards[1]
        issue = issue_card.get_content()
        self.assertIsInstance(issue, github.Issue.Issue)
        self.assertEqual(issue.title, "Test issue")

        note_card = cards[2]
        note_content = note_card.get_content()
        self.assertEqual(note_content, None)

    def testGetAllProjectCards(self):
        expectedProjects = ['TestProject']
        expectedCards = 5
        projects = []
        cards = 0
        for proj in self.repo.get_projects():
            projects.append(proj.name)
            for col in proj.get_columns():
                for card in col.get_cards("all"):
                    cards += 1
        self.assertEqual(projects, expectedProjects)
        self.assertEqual(cards, expectedCards)

    def testCreateColumn(self):
        project = self.repo.create_project("Project created by PyGithub", "Project Body")
        column = project.create_column("Project Column created by PyGithub",)
        self.assertEqual(column.id, 3999333)

    def testCreateCardWithNote(self):
        project = self.repo.create_project("Project created by PyGithub",
                                           "Project Body")
        column = project.create_column("Project Column created by PyGithub",)
        card1 = column.create_card(note="Project Card")
        self.assertEqual(card1.id, 16039019)

    def testCreateCardFromIssue(self):
        project = self.repo.create_project("Project created by PyGithub",
                                           "Project Body")
        column = project.create_column("Project Column created by PyGithub",)
        issue = self.repo.create_issue(title="Issue created by PyGithub")
        card2 = column.create_card(content_id=issue.id,
                                   content_type="Issue")
        self.assertEqual(card2.id, 16039106)
