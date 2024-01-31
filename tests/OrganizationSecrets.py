############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Denis Blanchette <dblanchette@coveo.com>                      #
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
from unittest import mock

from . import Framework


class OrganizationSecrets(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("coveooss")
        with mock.patch("github.PublicKey.encrypt") as encrypt:
            encrypt.return_value = "MOCK_ENCRYPTED_VALUE"
            self.org.create_or_update_secret("test_secret", "does not matter", "all")
        self.secret = self.org.get_secret("test_secret")
        self.repo = self.org.get_repo("github-app-playground")
        self.repo2 = self.org.get_repo("github-app-playground2")

    @mock.patch("github.PublicKey.encrypt", return_value="MOCK_ENCRYPTED_VALUE")
    def testGetPublicKey(self, _encrypt):
        org_public_key = self.org.get_public_key()
        self.assertEqual("aAAAaAAAA11A1Aa1aaaAAA1AAAaAAAAaAAa1/AAaA11=", org_public_key.key)
        self.assertEqual("123456789012345678", org_public_key.key_id)

    @mock.patch("github.PublicKey.encrypt", return_value="MOCK_ENCRYPTED_VALUE")
    def testCreateOrUpdateSecret(self, _encrypt):
        new_secret_name = "TEST_FUN_SECRET"
        new_secret_value = "new secret value"
        visibility = "all"

        created = self.org.create_or_update_secret(new_secret_name, new_secret_value, visibility)
        self.assertTrue(created)
        created_again = self.org.create_or_update_secret(new_secret_name, new_secret_value, visibility)
        self.assertFalse(created_again)

        gotten_secret = self.org.get_secret(new_secret_name)
        self.assertEqual(new_secret_name, gotten_secret.name)
        self.assertEqual(visibility, gotten_secret.visibility)

        self.org.delete_secret(gotten_secret.name)

        def will_raise():
            # Cannot have selected_repository_ids with visibility "private"
            self.org.create_or_update_secret(
                "not_important",
                "not important either",
                visibility="private",
                selected_repository_ids=[self.repo.id, self.repo2.id],
            )

        self.assertRaisesRegex(
            ValueError,
            "selected_repository_ids can only be used with visibility `selected`",
            will_raise,
        )

        def will_also_raise():
            # Cannot have selected_repository_ids with visibility "all"
            self.org.create_or_update_secret(
                "not_important",
                "not important either",
                visibility="all",
                selected_repository_ids=[self.repo.id, self.repo2.id],
            )

        self.assertRaisesRegex(
            ValueError,
            "selected_repository_ids can only be used with visibility `selected`",
            will_also_raise,
        )

        def will_raise_again():
            self.org.create_or_update_secret(
                "not_important",
                "not important either",
                visibility="selected",
                selected_repository_ids=self.repo.id,
            )

        self.assertRaisesRegex(ValueError, "selected_repository_ids should be a list", will_raise_again)

        def will_raise_a_final_time():
            self.org.create_or_update_secret(
                "not_important",
                "not important either",
                visibility="selected",
                selected_repository_ids=["not", "integers"],
            )

        self.assertRaisesRegex(
            ValueError,
            "selected_repository_ids elements should all be int",
            will_raise_a_final_time,
        )

        created_the_third = self.org.create_or_update_secret(
            "not_important",
            "not important either",
            visibility="selected",
            selected_repository_ids=[self.repo.id, self.repo2.id],
        )

        self.assertTrue(created_the_third)

        created4 = self.org.create_or_update_secret(
            "not_important",
            "not important either",
            visibility="selected",
            selected_repository_ids=[self.repo.id],
        )

        self.assertFalse(created4)

        self.org.delete_secret("not_important")

    def testGetSecret(self):
        secret = self.org.get_secret(self.secret.name)

        self.assertEqual(self.secret.name, secret.name)
        self.assertEqual(self.secret.visibility, secret.visibility)
        self.assertEqual(self.secret.created_at, secret.created_at)
        self.assertEqual(self.secret.updated_at, secret.updated_at)

    def testGetSecrets(self):
        secrets = self.org.get_secrets()

        first_secret = secrets[0]
        self.assertEqual(self.secret.name, first_secret.name)
        self.assertEqual(self.secret.visibility, first_secret.visibility)
        self.assertEqual(self.secret.created_at, first_secret.created_at)
        self.assertEqual(self.secret.updated_at, first_secret.updated_at)

    @mock.patch("github.PublicKey.encrypt", return_value="MOCK_ENCRYPTED_VALUE")
    def testSecretSelectedRepositories(self, _encrypt):
        self.org.create_or_update_secret("exclusive_secret", "nothing", "selected")
        exclusive_secret = self.org.get_secret("exclusive_secret")

        secret_selected_repositories = self.org.list_secret_selected_repositories(exclusive_secret.name)
        self.assertEqual(0, secret_selected_repositories.totalCount)

        self.org.set_secret_selected_repositories(exclusive_secret.name, [self.repo.id, self.repo2.id])
        secret_selected_repositories_again = self.org.list_secret_selected_repositories(exclusive_secret.name)
        self.assertEqual(2, secret_selected_repositories.totalCount)
        self.assertListKeyEqual(
            secret_selected_repositories_again,
            lambda s: s.id,
            [self.repo.id, self.repo2.id],
        )

        self.org.remove_secret_selected_repository(exclusive_secret.name, self.repo.id)
        secret_selected_repositories3 = self.org.list_secret_selected_repositories(exclusive_secret.name)
        self.assertEqual(1, secret_selected_repositories3.totalCount)
        self.assertEqual(self.repo2.id, secret_selected_repositories3[0].id)

        self.org.remove_secret_selected_repository(exclusive_secret.name, self.repo2.id)
        self.org.add_secret_selected_repository(exclusive_secret.name, self.repo.id)
        secret_selected_repositories4 = self.org.list_secret_selected_repositories(exclusive_secret.name)
        self.assertEqual(1, secret_selected_repositories4.totalCount)
        self.assertEqual(self.repo.id, secret_selected_repositories4[0].id)
