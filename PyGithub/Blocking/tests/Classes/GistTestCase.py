# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.tests.Framework as Framework


class GistTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        g = self.g.get_gist("5339374")
        self.assertEqual(g.comments, 0)
        self.assertEqual(g.comments_url, "https://api.github.com/gists/5339374/comments")
        self.assertEqual(g.commits_url, "https://api.github.com/gists/5339374/commits")
        self.assertEqual(g.created_at, datetime.datetime(2013, 4, 8, 18, 46, 14))
        self.assertEqual(g.description, "Test gist for PyGithub")
        self.assertEqual(len(g.files), 1)
        self.assertEqual(g.files["baz.txt"].content, "Bar -> baz")
        self.assertEqual(g.files["baz.txt"].filename, "baz.txt")
        self.assertIsNone(g.files["baz.txt"].language)
        self.assertEqual(g.files["baz.txt"].raw_url, "https://gist.githubusercontent.com/jacquev6/5339374/raw/4821236b6b52e23dfbf8e39157d250f3461aa9c5/baz.txt")
        self.assertEqual(g.files["baz.txt"].size, 10)
        self.assertEqual(g.files["baz.txt"].truncated, False)
        self.assertEqual(g.files["baz.txt"].type, "text/plain")
        self.assertEqual(g.forks_url, "https://api.github.com/gists/5339374/forks")
        self.assertEqual(g.git_pull_url, "https://gist.github.com/5339374.git")
        self.assertEqual(g.git_push_url, "https://gist.github.com/5339374.git")
        self.assertEqual(len(g.history), 5)
        # @todoAlpha HistoryElement has a url, should it be updatable?
        self.assertEqual(g.history[0].change_status.additions, 1)
        self.assertEqual(g.history[0].change_status.deletions, 1)
        self.assertEqual(g.history[0].change_status.total, 2)
        self.assertEqual(g.history[0].committed_at, datetime.datetime(2013, 4, 8, 19, 4, 7))
        self.assertEqual(g.history[0].url, "https://api.github.com/gists/5339374/c670d47c5ffee49794a9793a513603fab578bc56")
        self.assertEqual(g.history[0].user.login, "jacquev6")
        self.assertEqual(g.history[0].version, "c670d47c5ffee49794a9793a513603fab578bc56")
        self.assertEqual(g.html_url, "https://gist.github.com/5339374")
        self.assertEqual(g.id, "5339374")
        self.assertEqual(g.owner.login, "jacquev6")
        self.assertEqual(g.public, True)
        self.assertEqual(g.updated_at, datetime.datetime(2013, 4, 8, 19, 4, 7))
        self.assertEqual(g.url, "https://api.github.com/gists/5339374")
        self.assertIsNone(g.user)

    # @todoAlpha Test update on all classes?
    # def testUpdate(self):
    #     pass

    def testForksAttributes(self):
        g = self.g.get_gist("6296732")
        self.assertEqual(g.fork_of.owner.login, "HyroVitalyProtago")

    def testStarring(self):
        g = self.g.get_gist("1942384")
        self.assertTrue(g.is_starred())
        g.reset_starred()
        self.assertFalse(g.is_starred())
        g.set_starred()
        self.assertTrue(g.is_starred())

    def testGetForks(self):
        g = self.g.get_gist("6296553")
        # Inline forks, not very consistent with...
        self.assertEqual(len(g.forks), 2)
        self.assertEqual(g.forks[0].user.login, "jacquev6")
        # ... subresource forks (owner <-> user).
        forks = list(g.get_forks())
        self.assertEqual(len(forks), 2)
        self.assertEqual(forks[0].owner.login, "jacquev6")

    def testGetForks_allParameters(self):
        g = self.g.get_gist("6296553")
        forks = list(g.get_forks(per_page=1))
        self.assertEqual(forks[0].owner.login, "jacquev6")

    def testCreateFork(self):
        g = self.g.get_gist("4059305")
        self.assertEqual(g.owner.login, "jsvnm")
        f = g.create_fork()
        self.assertEqual(f.owner.login, "jacquev6")
        f.delete()

    def testEditAndUpdate(self):
        g1 = self.g.get_gist("5339374")
        self.assertEqual(g1.description, "Test gist for PyGithub")
        g2 = self.g.get_gist("5339374")
        self.assertFalse(g2.update())
        g1.edit(description="Test gist for PyGithub - edited")
        self.assertEqual(g1.description, "Test gist for PyGithub - edited")
        self.assertFalse(g1.update())
        self.assertTrue(g2.update())
        self.assertEqual(g2.description, "Test gist for PyGithub - edited")
        g1.edit(description="Test gist for PyGithub")

    def testAddAndRemoveFile(self):
        g = self.g.get_gist("5339374")
        self.assertFalse("new.txt" in g.files)
        g.edit(files={"new.txt": {"content": "Added"}})
        self.assertTrue("new.txt" in g.files)
        g.edit(files={"new.txt": None})
        # @todoSomeday Consider opening an issue with GitHub because deleted files are still present in PATCH's response
        self.assertTrue("new.txt" in g.files)
        # But they disappear after an update
        self.assertTrue(g.update())
        self.assertFalse("new.txt" in g.files)

    def testRenameFile(self):
        g = self.g.get_gist("5339374")
        self.assertTrue("baz.txt" in g.files)
        content = g.files["baz.txt"].content
        g.edit(files={"baz.txt": {"filename": "toto.txt", "content": content}})
        # self.assertFalse("baz.txt" in g.files)
        # self.assertTrue("toto.txt" in g.files)
        g.edit(files={"toto.txt": {"filename": "baz.txt", "content": content}})
