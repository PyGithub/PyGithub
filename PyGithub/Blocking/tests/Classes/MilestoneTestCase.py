# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.tests.Framework as Framework


class MilestoneTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        milestone = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_milestone(1)
        self.assertEqual(milestone.closed_issues, 0)
        self.assertEqual(milestone.created_at, datetime.datetime(2014, 6, 10, 7, 34, 14))
        self.assertEqual(milestone.creator.login, "jacquev6")
        self.assertEqual(milestone.description, "This is the *first* milestone.")
        self.assertEqual(milestone.due_on, datetime.datetime(2014, 6, 12, 7, 0))
        self.assertEqual(milestone.id, 686540)
        self.assertEqual(milestone.labels_url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/milestones/1/labels")
        self.assertEqual(milestone.number, 1)
        self.assertEqual(milestone.open_issues, 1)
        self.assertEqual(milestone.state, "open")
        self.assertEqual(milestone.title, "First milestone")
        self.assertEqual(milestone.updated_at, datetime.datetime(2014, 6, 10, 7, 34, 29))
        self.assertEqual(milestone.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/milestones/1")
