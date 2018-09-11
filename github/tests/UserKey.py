# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
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


class UserKey(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.key = self.g.get_user().get_key(2626650)

    def testAttributes(self):
        self.assertEqual(self.key.id, 2626650)
        self.assertEqual(self.key.key, "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA2Mm0RjTNAYFfSCtUpO54usdseroUSIYg5KX4JoseTpqyiB/hqewjYLAdUq/tNIQzrkoEJWSyZrQt0ma7/YCyMYuNGd3DU6q6ZAyBeY3E9RyCiKjO3aTL2VKQGFvBVVmGdxGVSCITRphAcsKc/PF35/fg9XP9S0anMXcEFtdfMHz41SSw+XtE+Vc+6cX9FuI5qUfLGbkv8L1v3g4uw9VXlzq4GfTA+1S7D6mcoGHopAIXFlVr+2RfDKdSURMcB22z41fljO1MW4+zUS/4FyUTpL991es5fcwKXYoiE+x06VJeJJ1Krwx+DZj45uweV6cHXt2JwJEI9fWB6WyBlDejWw==")
        self.assertEqual(self.key.title, "Key added through PyGithub")
        self.assertEqual(self.key.url, "https://api.github.com/user/keys/2626650")
        self.assertTrue(self.key.verified)

        # test __repr__() based on this attributes
        self.assertEqual(self.key.__repr__(), 'UserKey(title="Key added through PyGithub", id=2626650)')

    def testDelete(self):
        self.key.delete()
