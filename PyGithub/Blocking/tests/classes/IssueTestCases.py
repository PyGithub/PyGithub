# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class IssueAttributes(TestCase):
    @Enterprise("electra")
    def test(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(1)
        self.assertEqual(i.assignee.login, "electra")
        self.assertEqual(i.body, None)
        self.assertEqual(i.body_html, None)
        self.assertEqual(i.body_text, None)
        self.assertEqual(i.closed_at, None)
        self.assertEqual(i.closed_by, None)
        self.assertEqual(i.comments, 0)
        self.assertEqual(i.comments_url, "http://github.home.jacquev6.net/api/v3/repos/electra/issues/issues/1/comments")
        self.assertEqual(i.created_at, datetime.datetime(2014, 8, 3, 23, 19, 5))
        self.assertEqual(i.events_url, "http://github.home.jacquev6.net/api/v3/repos/electra/issues/issues/1/events")
        self.assertEqual(i.html_url, "http://github.home.jacquev6.net/electra/issues/issues/1")
        self.assertEqual(i.id, 15)
        self.assertEqual([l.name for l in i.labels], ["enhancement", "question"])
        self.assertEqual(i.labels_url, "http://github.home.jacquev6.net/api/v3/repos/electra/issues/issues/1/labels{/name}")
        self.assertEqual(i.milestone, None)
        self.assertEqual(i.number, 1)
        self.assertEqual(i.repository, None)
        self.assertEqual(i.state, "open")
        self.assertEqual(i.title, "Immutable issue")
        self.assertEqual(i.updated_at, datetime.datetime(2014, 8, 3, 23, 19, 6))
        self.assertEqual(i.url, "http://github.home.jacquev6.net/api/v3/repos/electra/issues/issues/1")
        self.assertEqual(i.user.login, "penelope")

    @Enterprise("electra")
    def testWithRepository(self):
        u = self.g.get_authenticated_user()
        i = u.get_issues()[0]
        self.assertEqual(i.repository.full_name, "electra/issues")

    @Enterprise("electra")
    def testClosedWithMilestone(self):
        u = self.g.get_authenticated_user()
        i = u.get_issues(state="closed")[0]
        self.assertEqual(i.closed_at, datetime.datetime(2014, 8, 3, 23, 19, 7))
        self.assertEqual(i.closed_by.login, "electra")
        self.assertEqual(i.state, "closed")
        self.assertEqual(i.milestone.number, 1)


class IssueEdit(TestCase):
    @Enterprise("electra")
    def testTitle(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(3)
        self.assertEqual(i.title, "Mutable issue")
        i.edit(title="Mutable issue!")
        self.assertEqual(i.title, "Mutable issue!")
        i.edit(title="Mutable issue")
        self.assertEqual(i.title, "Mutable issue")

    @Enterprise("electra")
    def testBody(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(3)
        self.assertEqual(i.body, None)
        i.edit(body="Body of first issue")
        self.assertEqual(i.body, "Body of first issue")
        i.edit(body=PyGithub.Blocking.Reset)
        self.assertEqual(i.body, None)

    @Enterprise("electra")
    def testAssignee(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(3)
        self.assertEqual(i.assignee, None)
        i.edit(assignee="electra")
        self.assertEqual(i.assignee.login, "electra")
        i.edit(assignee=PyGithub.Blocking.Reset)
        self.assertEqual(i.assignee, None)

    @Enterprise("electra")
    def testState(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(3)
        self.assertEqual(i.state, "open")
        i.edit(state="closed")
        self.assertEqual(i.state, "closed")
        i.edit(state="open")
        self.assertEqual(i.state, "open")

    @Enterprise("electra")
    def testMilestone(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(3)
        self.assertEqual(i.milestone, None)
        i.edit(milestone=3)
        self.assertEqual(i.milestone.number, 3)
        i.edit(milestone=PyGithub.Blocking.Reset)
        self.assertEqual(i.milestone, None)

    @Enterprise("electra")
    def testLabels(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(3)
        self.assertEqual([l.name for l in i.labels], ["enhancement", "question"])
        i.edit(labels=["bug"])
        self.assertEqual([l.name for l in i.labels], ["bug"])
        i.edit(labels=["enhancement", "question"])
        self.assertEqual([l.name for l in i.labels], ["enhancement", "question"])


class IssueLabels(TestCase):
    @Enterprise("electra")
    def testGetLabels(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(1)
        labels = i.get_labels()
        self.assertEqual([l.name for l in labels], ["enhancement", "question"])

    @Enterprise("electra")
    def testAddOneToAndRemoveFromLabels(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(3)
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])
        i.add_to_labels("bug")
        self.assertEqual([l.name for l in i.get_labels()], ["bug", "enhancement", "question"])
        i.remove_from_labels("bug")
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])

    @Enterprise("electra")
    def testAddSeveralToAndRemoveFromLabels(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(3)
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])
        i.add_to_labels("bug", "wontfix")
        self.assertEqual([l.name for l in i.get_labels()], ["bug", "enhancement", "question", "wontfix"])
        i.remove_from_labels("bug")
        i.remove_from_labels("wontfix")
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])

    @Enterprise("electra")
    def testRemoveAllAndSetLabels(self):
        i = self.g.get_repo(("electra", "issues")).get_issue(3)
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])
        i.remove_all_labels()
        self.assertEqual([l.name for l in i.get_labels()], [])
        i.set_labels("enhancement", "question")
        self.assertEqual([l.name for l in i.get_labels()], ["enhancement", "question"])
