############################ Copyrights and license ############################
#                                                                              #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

from __future__ import annotations

from datetime import datetime, timezone

import github

from . import Framework


class ProjectCard(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user().get_repo("PyGithub")
        self.proj = self.g.get_project(1682941)
        self.cols = self.proj.get_columns()
        self.col = self.cols[1]
        cards = self.col.get_cards()
        self.pull_card = cards[0]
        self.issue_card = cards[1]
        self.note_card = cards[2]
        self.edit_col = self.g.get_project(4015343).get_columns()[0]

    # See https://developer.github.com/v3/projects/cards/#get-a-project-card
    def testAttributes(self):
        card = self.pull_card
        self.assertFalse(card.archived)
        self.assertIsNone(card.column_name)
        self.assertEqual(card.column_url, "https://api.github.com/projects/columns/3138831")
        self.assertEqual(card.content_url, "https://api.github.com/repos/bbi-yggy/PyGithub/issues/1")
        self.assertEqual(card.created_at, datetime(2018, 8, 1, 4, 53, 59, tzinfo=timezone.utc))
        self.assertEqual(card.creator, self.repo.owner)
        self.assertEqual(card.created_at.year, 2018)
        self.assertEqual(card.id, 11780055)
        self.assertEqual(card.node_id, "MDExOlByb2plY3RDYXJkMTE3ODAwNTU=")
        self.assertIsNone(card.note, None)
        self.assertIsNone(card.project_id)
        self.assertIsNone(card.project_url)
        self.assertEqual(card.updated_at, datetime(2018, 8, 1, 4, 54, 16, tzinfo=timezone.utc))
        self.assertEqual(card.url, "https://api.github.com/projects/columns/cards/11780055")
        self.assertEqual(repr(card), "ProjectCard(id=11780055)")

    def testGetContent(self):
        pull = self.pull_card.get_content("PullRequest")
        self.assertIsInstance(pull, github.PullRequest.PullRequest)
        self.assertEqual(pull.title, "Work in progress on support for GitHub projects API.")
        self.assertRaises(ValueError, self.pull_card.get_content, "foo")

        issue = self.issue_card.get_content()
        self.assertIsInstance(issue, github.Issue.Issue)
        self.assertEqual(issue.title, "Test issue")

        note_content = self.note_card.get_content()
        self.assertEqual(note_content, None)

    def testMove(self):
        cols = self.cols
        card = self.pull_card
        self.assertTrue(card.move("top", cols[2].id))
        self.assertTrue(card.move("bottom", cols[1]))

    def testDelete(self):
        card = self.pull_card
        self.assertTrue(card.delete())

    def testGetAll(self):
        expectedProjects = ["TestProject"]
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

    def testCreateWithNote(self):
        project = self.repo.create_project("Project created by PyGithub", "Project Body")
        column = project.create_column(
            "Project Column created by PyGithub",
        )
        card1 = column.create_card(note="Project Card")
        self.assertEqual(card1.id, 16039019)

    def testCreateFromIssue(self):
        project = self.repo.create_project("Project created by PyGithub", "Project Body")
        column = project.create_column(
            "Project Column created by PyGithub",
        )
        issue = self.repo.create_issue(title="Issue created by PyGithub")
        card2 = column.create_card(content_id=issue.id, content_type="Issue")
        self.assertEqual(card2.id, 16039106)

    def testEditWithoutParameters(self):
        card = self.edit_col.create_card(note="Project Card")
        card.edit()

    def testEditNote(self):
        card = self.edit_col.create_card(note="Project Card")
        card.edit(note="Edited Card")
        self.assertEqual(card.note, "Edited Card")

    def testEditArchived(self):
        card = self.edit_col.create_card(note="Project Card")
        card.edit(archived=True)
        self.assertEqual(card.archived, True)
