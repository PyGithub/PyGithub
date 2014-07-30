# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class MilestoneAttributes(TestCase):
    @Enterprise.User(1)
    def test(self):
        m = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_milestone(1)
        self.assertEqual(m.closed_issues, 0)
        self.assertEqual(m.created_at, datetime.datetime(2014, 7, 20, 6, 43, 19))
        self.assertEqual(m.creator.login, "ghe-user-1")
        self.assertEqual(m.description, "Body of first milestone")
        self.assertEqual(m.due_on, datetime.datetime(2014, 7, 26, 0, 0))
        self.assertEqual(m.id, 1)
        self.assertEqual(m.labels_url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/milestones/1/labels")
        self.assertEqual(m.number, 1)
        self.assertEqual(m.open_issues, 3)
        self.assertEqual(m.state, "open")
        self.assertEqual(m.title, "First milestone")
        self.assertEqual(m.updated_at, datetime.datetime(2014, 7, 23, 4, 47, 58))
        self.assertEqual(m.url, "http://github.home.jacquev6.net/api/v3/repos/ghe-user-1/repo-user-1-1/milestones/1")


class MilestoneEdit(TestCase):
    @Enterprise.User(1)
    def testTitle(self):
        m = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_milestone(1)
        self.assertEqual(m.title, "First milestone")
        m.edit(title="First milestone!")
        self.assertEqual(m.title, "First milestone!")
        m.edit(title="First milestone")
        self.assertEqual(m.title, "First milestone")

    @Enterprise.User(1)
    def testState(self):
        m = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_milestone(1)
        self.assertEqual(m.state, "open")
        m.edit(state="closed")
        self.assertEqual(m.state, "closed")
        m.edit(state="open")
        self.assertEqual(m.state, "open")

    @Enterprise.User(1)
    def testDescription(self):
        m = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_milestone(1)
        self.assertEqual(m.description, "Body of first milestone")
        m.edit(description=PyGithub.Blocking.Reset)
        self.assertIsNone(m.description)
        m.edit(description="Body of first milestone")
        self.assertEqual(m.description, "Body of first milestone")

    @Enterprise.User(1)
    def testDueOn(self):
        m = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_milestone(1)
        self.assertEqual(m.due_on, datetime.datetime(2014, 7, 26, 0, 0))
        m.edit(due_on=PyGithub.Blocking.Reset)
        self.assertIsNone(m.due_on)
        m.edit(due_on="2014-07-26T00:00:00Z")
        self.assertEqual(m.due_on, datetime.datetime(2014, 7, 26, 0, 0))


class MilestoneLabels(TestCase):
    @Enterprise.User(1)
    def testGetLabels(self):
        m = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).get_milestone(1)
        labels = m.get_labels()
        self.assertEqual([l.name for l in labels], ["enhancement", "question"])


class MilestoneDelete(TestCase):
    @Enterprise.User(1)
    def test(self):
        m = self.g.get_repo(("ghe-user-1", "repo-user-1-1")).create_milestone("Created by PyGithub")
        self.assertIsNone(m.description)
        m.delete()
