############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Nicolas Agustín Torres <nicolastrres@gmail.com>               #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Huan-Cheng Chang <changhc84@gmail.com>                        #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2023 Malik Shahzad Muzaffar <shahzad.malik.muzaffar@cern.ch>       #
# Copyright 2024 Arash Kadkhodaei <arash77.kad@gmail.com>                      #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

from . import Framework


class IssueComment(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.comment = self.g.get_repo("PyGithub/PyGithub").get_issue(28).get_comment(20227753)

    def testAttributes(self):
        self.assertEqual(self.comment.author_association, "CONTRIBUTOR")
        self.assertEqual(self.comment.body, "Comment created by PyGithub\n")
        self.assertIsNone(self.comment.body_html)
        self.assertIsNone(self.comment.body_text)
        self.assertEqual(self.comment.created_at, datetime(2013, 6, 29, 10, 31, 38, tzinfo=timezone.utc))
        self.assertEqual(self.comment.html_url, "https://github.com/PyGithub/PyGithub/issues/28#issuecomment-20227753")
        self.assertEqual(self.comment.id, 20227753)
        self.assertEqual(self.comment.issue_url, "https://api.github.com/repos/PyGithub/PyGithub/issues/28")
        self.assertEqual(self.comment.node_id, "MDEyOklzc3VlQ29tbWVudDIwMjI3NzUz")
        self.assertEqual(self.comment.body, "Comment created by PyGithub\n")
        self.assertEqual(self.comment.created_at, datetime(2013, 6, 29, 10, 31, 38, tzinfo=timezone.utc))
        self.assertEqual(self.comment.id, 20227753)
        self.assertIsNone(self.comment.performed_via_github_app)
        self.assertEqual(
            self.comment.reactions,
            {
                "url": "https://api.github.com/repos/PyGithub/PyGithub/issues/comments/20227753/reactions",
                "total_count": 2,
                "+1": 1,
                "-1": 0,
                "laugh": 0,
                "hooray": 1,
                "confused": 0,
                "heart": 0,
                "rocket": 0,
                "eyes": 0,
            },
        )
        self.assertEqual(self.comment.updated_at, datetime(2013, 6, 29, 10, 31, 38, tzinfo=timezone.utc))
        self.assertEqual(self.comment.url, "https://api.github.com/repos/PyGithub/PyGithub/issues/comments/20227753")
        self.assertEqual(self.comment.user.login, "stuglaser")
        self.assertEqual(self.comment.html_url, "https://github.com/PyGithub/PyGithub/issues/28#issuecomment-20227753")
        self.assertEqual(repr(self.comment), 'IssueComment(user=NamedUser(login="stuglaser"), id=20227753)')
        self.assertEqual(
            self.comment.reactions,
            {
                "url": "https://api.github.com/repos/PyGithub/PyGithub/issues/comments/20227753/reactions",
                "total_count": 2,
                "+1": 1,
                "-1": 0,
                "laugh": 0,
                "hooray": 1,
                "confused": 0,
                "heart": 0,
                "rocket": 0,
                "eyes": 0,
            },
        )

    def testEdit(self):
        self.comment.edit("Comment edited by PyGithub")
        self.assertEqual(self.comment.body, "Comment edited by PyGithub")
        self.assertEqual(
            self.comment.updated_at,
            datetime(2012, 5, 20, 11, 53, 59, tzinfo=timezone.utc),
        )

    def testMinimize(self):
        self.assertTrue(self.comment.minimize())

    def testUnminimize(self):
        self.assertTrue(self.comment.unminimize())

    def testGetReactions(self):
        reactions = self.comment.get_reactions()
        self.assertEqual(reactions[0].content, "+1")

    def testCreateReaction(self):
        reaction = self.comment.create_reaction("hooray")

        self.assertEqual(reaction.id, 17282654)
        self.assertEqual(reaction.content, "hooray")

    def testDeleteReaction(self):
        self.assertTrue(self.comment.delete_reaction(85743754))

    # this should be the last test as this deletes the comment used above.
    def testDelete(self):
        self.comment.delete()
