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

import datetime

from . import Framework


class OrganizationAuthorization(Framework.TestCase):
    subset = {
        "login": "AlexandreODelisle",
        "credential_id": 5077647,
        "credential_type": "personal access token",
        "token_last_eight": "4c4c6b2c",
        "scopes": ["repo"],
        "credential_authorized_at": datetime.datetime.strptime(
            "2020-09-23 00:22:07", "%Y-%m-%d %H:%M:%S"
        ),  # Will need to be updated if test re-ran ( delete )
        "credential_accessed_at": None,  # Will need to be updated if test re-ran ( delete )
    }

    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("Learn-Think-Do")

    def testAttributes(self):
        credentials_list = self.org.get_credential_authorizations()
        filtered_credentials_list = list(
            filter(
                lambda x: x.login == self.subset["login"]
                and x.credential_id == self.subset["credential_id"],
                credentials_list,
            )
        )

        AuthCred = filtered_credentials_list[0]
        self.assertEqual(AuthCred.login, self.subset["login"])
        self.assertEqual(AuthCred.credential_type, self.subset["credential_type"])
        self.assertEqual(AuthCred.credential_id, self.subset["credential_id"])
        self.assertEqual(AuthCred.token_last_eight, self.subset["token_last_eight"])
        self.assertEqual(AuthCred.scopes, self.subset["scopes"])
        self.assertEqual(
            AuthCred.credential_authorized_at, self.subset["credential_authorized_at"]
        )
        self.assertEqual(
            AuthCred.credential_accessed_at, self.subset["credential_accessed_at"]
        )

    def testGetCredentialsAuth(self):
        credentials_list = self.org.get_credential_authorizations()
        if "credential_authorized_at" in self.subset.keys():
            self.subset.pop(
                "credential_authorized_at"
            )  # because _rawData return a Str for datetime

        self.assertTrue(
            any([self.subset.items() <= x._rawData.items() for x in credentials_list])
        )

    def testRemoveCredentialAuth(self):
        credentials_list = self.org.get_credential_authorizations()
        if "credential_authorized_at" in self.subset.keys():
            self.subset.pop(
                "credential_authorized_at"
            )  # because _rawData return a Str for datetime

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
