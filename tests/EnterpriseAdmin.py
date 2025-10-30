############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 YugoHino <henom06@gmail.com>                                  #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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


class EnterpriseAdmin(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.enterprise = self.g.get_enterprise("beaver-group")

    def testAttributes(self):
        self.assertEqual(self.enterprise.slug, "beaver-group")
        self.assertEqual(self.enterprise.url, "/enterprises/beaver-group")
        self.assertEqual(repr(self.enterprise), 'Enterprise(slug="beaver-group")')

    def testGetConsumedLicenses(self):
        consumed_licenses = self.enterprise.get_consumed_licenses()
        self.assertEqual(consumed_licenses.total_seats_consumed, 102)
        self.assertEqual(consumed_licenses.total_seats_purchased, 103)

    def testGetEnterpriseUsers(self):
        enterprise_users = self.enterprise.get_consumed_licenses().get_users()
        enterprise_users_list = [
            [
                users.github_com_login,
                users.github_com_name,
                users.enterprise_server_user_ids,
                users.github_com_user,
                users.enterprise_server_user,
                users.visual_studio_subscription_user,
                users.license_type,
                users.github_com_profile,
                users.github_com_member_roles,
                users.github_com_enterprise_roles,
                users.github_com_verified_domain_emails,
                users.github_com_saml_name_id,
                users.github_com_orgs_with_pending_invites,
                users.github_com_two_factor_auth,
                users.enterprise_server_primary_emails,
                users.visual_studio_license_status,
                users.visual_studio_subscription_email,
                users.total_user_accounts,
            ]
            for users in enterprise_users
        ]
        self.assertEqual(len(enterprise_users_list), 102)
        self.assertEqual(enterprise_users_list[42][0], "beaver-user043")
