# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class IssueAttributes(TestCase):
    @Enterprise.User(1)
    def test(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        self.assertEqual(i.assignee.login, "ghe-user-1")
        self.assertEqual(i.body, "Body of first issue")
        self.assertEqual(i.body_html, "<p>Body of first issue</p>")
        self.assertEqual(i.body_text, "Body of first issue")
        self.assertEqual(i.closed_at, None)
        self.assertEqual(i.closed_by.login, "ghe-user-1")
        self.assertEqual(i.comments, 0)
        self.assertEqual(i.comments_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/issues/1/comments")
        self.assertEqual(i.created_at, datetime.datetime(2014, 7, 20, 6, 42, 48))
        self.assertEqual(i.events_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/issues/1/events")
        self.assertEqual(i.html_url, "http://github.home.jacquev6.net/ghe-user-1/repo-user-1-1/issues/1")
        self.assertEqual(i.id, 1)
        self.assertEqual([l.name for l in i.labels], ["enhancement", "question"])
        self.assertEqual(i.labels_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/issues/1/labels{/name}")
        self.assertEqual(i.milestone.number, 1)
        self.assertEqual(i.number, 1)
        self.assertIsNone(i.repository)
        self.assertEqual(i.state, "open")
        self.assertEqual(i.title, "First issue")
        self.assertEqual(i.updated_at, datetime.datetime(2014, 7, 20, 7, 24, 39))
        self.assertEqual(i.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/issues/1")
        self.assertEqual(i.user.login, "ghe-user-1")

    @Enterprise.User(1)
    def testWithRepository(self):
        u = self.g.get_authenticated_user()
        i = u.get_issues()[0]
        self.assertEqual(i.repository.full_name, "ghe-user-1/repo-user-1-1")


class IssueEdit(TestCase):
    @Enterprise.User(1)
    def testTitle(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        self.assertEqual(i.title, "First issue")
        i.edit(title="First issue!")
        self.assertEqual(i.title, "First issue!")
        i.edit(title="First issue")
        self.assertEqual(i.title, "First issue")

    @Enterprise.User(1)
    def testBody(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        self.assertEqual(i.body, "Body of first issue")
        i.edit(body=PyGithub.Blocking.Reset)
        self.assertIsNone(i.body)
        i.edit(body="Body of first issue")
        self.assertEqual(i.body, "Body of first issue")

    @Enterprise.User(1)
    def testAssignee(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        self.assertEqual(i.assignee.login, "ghe-user-1")
        i.edit(assignee=PyGithub.Blocking.Reset)
        self.assertIsNone(i.assignee)
        i.edit(assignee="ghe-user-1")
        self.assertEqual(i.assignee.login, "ghe-user-1")

    @Enterprise.User(1)
    def testState(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        self.assertEqual(i.state, "open")
        i.edit(state="closed")
        self.assertEqual(i.state, "closed")
        i.edit(state="open")
        self.assertEqual(i.state, "open")

    @Enterprise.User(1)
    def testMilestone(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        self.assertEqual(i.milestone.number, 1)
        i.edit(milestone=PyGithub.Blocking.Reset)
        self.assertIsNone(i.milestone)
        i.edit(milestone=1)
        self.assertEqual(i.milestone.number, 1)

    @Enterprise.User(1)
    def testLabels(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        self.assertEqual([l.name for l in i.labels], ["enhancement", "question"])
        i.edit(labels=["bug"])
        self.assertEqual([l.name for l in i.labels], ["bug"])
        i.edit(labels=["enhancement", "question"])
        self.assertEqual([l.name for l in i.labels], ["enhancement", "question"])


class IssueLabels(TestCase):
    @Enterprise.User(1)
    def testGetLabels(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        labels = i.get_labels()
        self.assertEqual([l.name for l in labels], ["enhancement", "question"])

    @Enterprise.User(1)
    def testAddOneToAndRemoveFromLabels(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])
        i.add_to_labels("bug")
        self.assertEqual([l.name for l in i.get_labels()], ["bug", "enhancement", "question"])
        i.remove_from_labels("bug")
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])

    @Enterprise.User(1)
    def testAddSeveralToAndRemoveFromLabels(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])
        i.add_to_labels("bug", "wontfix")
        self.assertEqual([l.name for l in i.get_labels()], ["bug", "enhancement", "question", "wontfix"])
        i.remove_from_labels("bug")
        i.remove_from_labels("wontfix")
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])

    @Enterprise.User(1)
    def testRemoveAllAndSetLabels(self):
        i = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_issue(1)
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])
        i.remove_all_labels()
        self.assertEqual([l.name for l in i.get_labels()], [])
        i.set_labels("enhancement", "question")
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])
