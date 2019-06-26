# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
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

import Framework


class ContentFile(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.file = self.g.get_user().get_repo("PyGithub").get_readme()

    def testAttributes(self):
        self.assertEqual(self.file.type, "file")
        self.assertEqual(self.file.encoding, "base64")
        self.assertEqual(self.file.size, 7531)
        self.assertEqual(self.file.name, "ReadMe.md")
        self.assertEqual(self.file.path, "ReadMe.md")
        self.assertEqual(len(self.file.content), 10212)
        self.assertEqual(len(self.file.decoded_content), 7531)
        self.assertEqual(self.file.sha, "5628799a7d517a4aaa0c1a7004d07569cd154df0")
        self.assertEqual(self.file.download_url, "https://raw.githubusercontent.com/jacquev6/PyGithub/master/README.md")

        # test __repr__() based on this attributes
        self.assertEqual(self.file.__repr__(), 'ContentFile(path="ReadMe.md")')
