# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.tests.Framework as Framework


class GistTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        g = self.g.get_gist("5339374")
        # @todoAlpha files
        # @todoAlpha forks
        # @todoAlpha fork_of (seems to be present only on forks => testForksAttributes)
        self.assertEqual(g.comments, 0)
        self.assertEqual(g.comments_url, "https://api.github.com/gists/5339374/comments")
        self.assertEqual(g.commits_url, "https://api.github.com/gists/5339374/commits")
        self.assertEqual(g.created_at, datetime.datetime(2013, 4, 8, 18, 46, 14))
        self.assertEqual(g.description, "Test gist for PyGithub")
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
