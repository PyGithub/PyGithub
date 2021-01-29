############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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


class GistComment(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.comment = self.g.get_gist("2729810").get_comment(323629)

    def testAttributes(self):
        self.assertEqual(self.comment.body, "Comment created by PyGithub")
        self.assertEqual(
            self.comment.created_at,
            datetime.datetime(2012, 5, 19, 7, 7, 57, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.comment.id, 323629)
        self.assertEqual(
            self.comment.updated_at,
            datetime.datetime(2012, 5, 19, 7, 7, 57, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.comment.url, "https://api.github.com/gists/2729810/comments/323629"
        )
        self.assertEqual(self.comment.user.login, "jacquev6")
        self.assertEqual(
            repr(self.comment),
            'GistComment(user=NamedUser(login="jacquev6"), id=323629)',
        )

    def testEdit(self):
        self.comment.edit("Comment edited by PyGithub")
        self.assertEqual(self.comment.body, "Comment edited by PyGithub")
        self.assertEqual(
            self.comment.updated_at,
            datetime.datetime(2012, 5, 19, 7, 12, 32, tzinfo=datetime.timezone.utc),
        )

    def testDelete(self):
        self.comment.delete()
