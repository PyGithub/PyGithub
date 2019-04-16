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
# Copyright 2018 Laurent Raufaste <analogue@glop.org>                          #
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

import datetime


class RepositoryKey(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        # When recording test, be sure to create a deploy key for yourself on
        # Github and update it here.
        self.key = self.g.get_user("lra").get_repo("mackup").get_key(21870881)

    def testAttributes(self):
        self.assertEqual(self.key.id, 21870881)
        self.assertEqual(self.key.key, "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLOoLSVPwG1OSgVSeEXNbfIofYdxR5zs3u4PryhnamfFPYwi2vZW3ZxeI1oRcDh2VEdwGvlN5VUduKJNoOWMVzV2jSyR8CeDHH+I0soQCC7kfJVodU96HcPMzZ6MuVwSfD4BFGvKMXyCnBUqzo28BGHFwVQG8Ya9gL6/cTbuWywgM4xaJgMHv1OVcESXBtBkrqOneTJuOgeEmP0RfUnIAK/3/wbg9mfiBq7JV4cmWAg1xNE8GJoAbci59Tdx1dQgVuuqdQGk5jzNusOVneyMtGEB+p7UpPLJsGBW29rsMt7ITUbXM/kl9v11vPtWb+oOUThoFsDYmsWy7fGGP9YAFB")
        self.assertEqual(self.key.title, "PyGithub Test Key")
        self.assertEqual(self.key.url, "https://api.github.com/repos/lra/mackup/keys/21870881")
        self.assertEqual(self.key.created_at, datetime.datetime(2017, 2, 22, 8, 16, 23))
        self.assertTrue(self.key.verified)

        # test __repr__() based on this attributes
        self.assertEqual(self.key.__repr__(), 'RepositoryKey(title="PyGithub Test Key", id=21870881)')

    def testDelete(self):
        self.key.delete()
