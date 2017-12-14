# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
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

import datetime


class CommitComment(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.comment = self.g.get_user().get_repo("PyGithub").get_comment(1361949)

    def testAttributes(self):
        self.assertEqual(self.comment.body, "Comment created by PyGithub")
        self.assertEqual(self.comment.commit_id, "6945921c529be14c3a8f566dd1e483674516d46d")
        self.assertEqual(self.comment.created_at, datetime.datetime(2012, 5, 22, 18, 40, 18))
        self.assertEqual(self.comment.html_url, "https://github.com/jacquev6/PyGithub/commit/6945921c529be14c3a8f566dd1e483674516d46d#commitcomment-1361949")
        self.assertEqual(self.comment.id, 1361949)
        self.assertEqual(self.comment.line, None)
        self.assertEqual(self.comment.path, None)
        self.assertEqual(self.comment.position, None)
        self.assertEqual(self.comment.updated_at, datetime.datetime(2012, 5, 22, 18, 40, 18))
        self.assertEqual(self.comment.url, "https://api.github.com/repos/jacquev6/PyGithub/comments/1361949")
        self.assertEqual(self.comment.user.login, "jacquev6")

        # test __repr__() based on this attributes
        self.assertEqual(self.comment.__repr__(),
                         'CommitComment(user=NamedUser(login="jacquev6"), id=1361949)')

    def testEdit(self):
        self.comment.edit("Comment edited by PyGithub")

    def testDelete(self):
        self.comment.delete()

    def testGetReactions(self):
        reactions = self.comment.get_reactions()
        self.assertEqual(reactions[0].content, "+1")

    def testCreateReaction(self):
        reaction = self.comment.create_reaction("hooray")

        self.assertEqual(reaction.id, 17283092)
        self.assertEqual(reaction.content, "hooray")
