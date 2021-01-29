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
# Copyright 2020 Huan-Cheng Chang <changhc84@gmail.com>                        #
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

import datetime

from . import Framework


class PullRequestComment(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.comment = (
            self.g.get_user().get_repo("PyGithub").get_pull(31).get_comment(886298)
        )

    def testAttributes(self):
        self.assertEqual(self.comment.body, "Comment created by PyGithub")
        self.assertEqual(
            self.comment.commit_id, "8a4f306d4b223682dd19410d4a9150636ebe4206"
        )
        self.assertEqual(
            self.comment.created_at,
            datetime.datetime(2012, 5, 27, 9, 40, 12, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.comment.id, 886298)
        self.assertEqual(
            self.comment.original_commit_id, "8a4f306d4b223682dd19410d4a9150636ebe4206"
        )
        self.assertEqual(self.comment.original_position, 5)
        self.assertEqual(self.comment.path, "src/github/Issue.py")
        self.assertEqual(self.comment.position, 5)
        self.assertEqual(
            self.comment.updated_at,
            datetime.datetime(2012, 5, 27, 9, 40, 12, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.comment.url,
            "https://api.github.com/repos/jacquev6/PyGithub/pulls/comments/886298",
        )
        self.assertEqual(self.comment.user.login, "jacquev6")
        self.assertEqual(
            self.comment.html_url,
            "https://github.com/jacquev6/PyGithub/pull/170#issuecomment-18637907",
        )
        self.assertEqual(
            repr(self.comment),
            'PullRequestComment(user=NamedUser(login="jacquev6"), id=886298)',
        )

    def testEdit(self):
        self.comment.edit("Comment edited by PyGithub")
        self.assertEqual(self.comment.body, "Comment edited by PyGithub")

    def testDelete(self):
        self.comment.delete()

    def testGetReactions(self):
        reactions = self.comment.get_reactions()
        self.assertEqual(reactions[0].content, "+1")

    def testCreateReaction(self):
        reaction = self.comment.create_reaction("hooray")

        self.assertEqual(reaction.id, 17283822)
        self.assertEqual(reaction.content, "hooray")

    def testDeleteReaction(self):
        self.assertTrue(self.comment.delete_reaction(85750463))
