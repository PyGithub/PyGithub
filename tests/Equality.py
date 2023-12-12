############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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


class Equality(Framework.TestCase):
    def testUserEquality(self):
        u1 = self.g.get_user("jacquev6")
        u2 = self.g.get_user("jacquev6")
        self.assertEqual(u1, u2)
        self.assertEqual(hash(u1), hash(u2))

    def testUserDifference(self):
        u1 = self.g.get_user("jacquev6")
        u2 = self.g.get_user("OddBloke")
        self.assertNotEqual(u1, u2)
        self.assertNotEqual(hash(u1), hash(u2))

    def testBranchEquality(self):
        # Erf, equality of NonCompletableGithubObjects will be difficult to implement
        # because even their _rawData can differ. (Here, the avatar_url is not equal)
        # (CompletableGithubObjects are compared by their API url, which is a good key)
        r = self.g.get_user().get_repo("PyGithub")
        b1 = r.get_branch("develop")
        b2 = r.get_branch("develop")
        self.assertNotEqual(b1._rawData, b2._rawData)
