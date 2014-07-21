# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.tests.Framework as Framework
from PyGithub.Blocking.tests.Framework import *


class IssueTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        issue = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_issue(1)
        self.assertEqual(issue.assignee.login, "jacquev6")
        self.assertEqual(issue.body, "This is the *first* issue.")
        self.assertEqual(issue.body_html, "<p>This is the <em>first</em> issue.</p>")
        self.assertEqual(issue.body_text, "This is the first issue.")
        self.assertEqual(issue.closed_at, None)
        self.assertEqual(issue.closed_by, None)
        self.assertEqual(issue.comments, 1)
        self.assertEqual(issue.comments_url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/issues/1/comments")
        self.assertEqual(issue.created_at, datetime.datetime(2014, 6, 10, 7, 16, 15))
        self.assertEqual(issue.events_url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/issues/1/events")
        self.assertEqual(issue.html_url, "https://github.com/jacquev6/PyGithubIntegrationTests/issues/1")
        self.assertEqual(issue.id, 35356603)
        self.assertEqual(len(issue.labels), 2)
        self.assertEqual(issue.labels[0].name, "enhancement")
        self.assertEqual(issue.labels[1].name, "question")
        self.assertEqual(issue.labels_url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/issues/1/labels{/name}")
        self.assertEqual(issue.milestone.title, "First milestone")
        self.assertEqual(issue.number, 1)
        self.assertEqual(issue.state, "open")
        self.assertEqual(issue.title, "First issue")
        self.assertEqual(issue.updated_at, datetime.datetime(2014, 6, 10, 7, 34, 29))
        self.assertEqual(issue.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/issues/1")
        self.assertEqual(issue.user.login, "jacquev6")


class IssueEdit(TestCase):
    @Enterprise.User(1)
    def testEditTitle(self):
        # Verified Reset doesn't work
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        issue = r.get_issue(1)
        self.assertEqual(issue.title, "First issue")
        issue.edit(title="First issue!")
        self.assertEqual(issue.title, "First issue!")
        issue.edit(title="First issue")
        self.assertEqual(issue.title, "First issue")

    @Enterprise.User(1)
    def testEditBody(self):
        # Verified Reset doesn't work
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        issue = r.get_issue(1)
        self.assertEqual(issue.body, "Body of first issue")
        issue.edit(body="Body of first issue!")
        self.assertEqual(issue.body, "Body of first issue!")
        issue.edit(body="Body of first issue")
        self.assertEqual(issue.body, "Body of first issue")

    @Enterprise.User(1)
    def testEditAssignee(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        issue = r.get_issue(1)
        self.assertEqual(issue.assignee.login, "ghe-user-1")
        issue.edit(assignee=PyGithub.Blocking.Reset)
        self.assertIsNone(issue.assignee)
        issue.edit(assignee="ghe-user-1")
        self.assertEqual(issue.assignee.login, "ghe-user-1")

    @Enterprise.User(1)
    def testEditState(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        issue = r.get_issue(1)
        self.assertEqual(issue.state, "open")
        issue.edit(state="closed")
        self.assertEqual(issue.state, "closed")
        issue.edit(state="open")
        self.assertEqual(issue.state, "open")

    @Enterprise.User(1)
    def testEditMilestone(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        issue = r.get_issue(1)
        self.assertEqual(issue.milestone.number, 1)
        issue.edit(milestone=PyGithub.Blocking.Reset)
        self.assertIsNone(issue.milestone)
        issue.edit(milestone=1)
        self.assertEqual(issue.milestone.number, 1)

    @Enterprise.User(1)
    def testEditLabels(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        issue = r.get_issue(1)
        self.assertEqual(len(issue.labels), 2)
        self.assertEqual(issue.labels[0].name, "enhancement")
        self.assertEqual(issue.labels[1].name, "question")
        issue.edit(labels=["bug"])
        self.assertEqual(len(issue.labels), 1)
        self.assertEqual(issue.labels[0].name, "bug")
        issue.edit(labels=["enhancement", "question"])
        self.assertEqual(len(issue.labels), 2)
        self.assertEqual(issue.labels[0].name, "enhancement")
        self.assertEqual(issue.labels[1].name, "question")
