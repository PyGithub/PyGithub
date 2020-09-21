# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Alexandre Delisle <alexodelisle@gmail.com>                    #
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


class OrganizationAuthorization(Framework.TestCase):
    subset = {
        "login": "AlexandreODelisle",
        "credential_id": 5016093,
        "credential_type": "personal access token",
        "token_last_eight": "72e2297c",
        "scopes": ["repo"],
        "credential_authorized_at": "2020-09-20T23:48:42Z",  # Will need to be updated if test re-ran ( delete )
        "credential_accessed_at": "2020-09-20T23:57:07Z",  # Will need to be updated if test re-ran ( delete )
    }

    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("Learn-Think-Do")

    def testGetCredentialsAuth(self):
        credentials_list = self.org.get_credential_authorizations()
        self.assertTrue(
            any([self.subset.items() <= x._rawData.items() for x in credentials_list])
        )

    def testRemoveCredentialAuth(self):
        credentials_list = self.org.get_credential_authorizations()
        self.assertTrue(
            any([self.subset.items() <= x._rawData.items() for x in credentials_list])
        )
        self.assertTrue(
            self.org.remove_credential_authorization(
                credential_id=self.subset["credential_id"]
            )
        )
        credentials_list = self.org.get_credential_authorizations()
        self.assertFalse(
            any([self.subset.items() <= x._rawData.items() for x in credentials_list])
        )
