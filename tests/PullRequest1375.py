############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Olof-Joachim Frahm <olof@macrolet.net>                        #
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

from . import Framework


class PullRequest1375(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.pr = self.g.get_repo("rsn491/PyGithub").get_pulls()[0]

    def testCreateReviewCommentReply(self):
        comment_id = 373866377  # id of pull request comment without replies
        first_reply_body = "Comment reply created by PyGithub"
        second_reply_body = "Second comment reply created by PyGithub"

        first_reply = self.pr.create_review_comment_reply(comment_id, first_reply_body)
        second_reply = self.pr.create_review_comment_reply(
            first_reply.id, second_reply_body
        )

        # ensure both first and second reply have `in_reply_to_id` attr set to top comment
        self.assertEqual(first_reply.in_reply_to_id, comment_id)
        self.assertEqual(second_reply.in_reply_to_id, comment_id)

        self.assertEqual(first_reply.body, first_reply_body)
        self.assertEqual(second_reply.body, second_reply_body)
