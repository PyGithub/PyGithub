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
            self.org.create_secret("test_secret", "does not matter", "all")
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

        gotten_secret = self.org.create_secret(new_secret_name, new_secret_value, visibility)
        self.assertEqual(new_secret_name, gotten_secret.name)
        self.assertEqual(visibility, gotten_secret.visibility)

        gotten_secret.delete()

        def no_repos_if_visibility_private():
            # Cannot have selected_repository_ids with visibility "private"
            self.org.create_secret(
                "not_important",
                "not important either",
                visibility="private",
                selected_repositories=[self.repo, self.repo2],
            )

        self.assertRaises(AssertionError, no_repos_if_visibility_private)

        def no_repos_if_visibility_all():
            # Cannot have selected_repository_ids with visibility "all"
            self.org.create_secret(
                "not_important",
                "not important either",
                visibility="all",
                selected_repositories=[self.repo, self.repo2],
            )

        self.assertRaises(AssertionError, no_repos_if_visibility_all)

        def repos_must_be_a_list():
            self.org.create_secret(
                "not_important",
                "not important either",
                visibility="selected",
                selected_repositories=self.repo,
            )

        self.assertRaises(AssertionError, repos_must_be_a_list)

        def bad_repo_type():
            self.org.create_secret(
                "not_important",
                "not important either",
                visibility="selected",
                selected_repositories=["not", "integers"],
            )

        self.assertRaises(AssertionError, bad_repo_type)

        self.org.create_secret(
            "not_important",
            "not important either",
            visibility="selected",
            selected_repositories=[self.repo, self.repo2],
        )

        secret = self.org.create_secret(
            "not_important",
            "not important either",
            visibility="selected",
            selected_repositories=[self.repo],
        )

        secret.delete()

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
        exclusive_secret = self.org.create_secret("exclusive_secret", "nothing", "selected", [])

        self.assertEqual(0, exclusive_secret.selected_repositories.totalCount)

        exclusive_secret.set_repos([self.repo.id, self.repo2.id])
        secret_selected_repositories = exclusive_secret.selected_repositories
        self.assertEqual(2, secret_selected_repositories.totalCount)
        self.assertListKeyEqual(
            secret_selected_repositories,
            lambda s: s.id,
            [self.repo.id, self.repo2.id],
        )

        exclusive_secret.remove_repo(self.repo)
        secret_selected_repositories = exclusive_secret.selected_repositories
        self.assertEqual(1, secret_selected_repositories.totalCount)
        self.assertEqual(self.repo2.id, secret_selected_repositories[0].id)

        exclusive_secret.remove_repo(self.repo2)
        exclusive_secret.add_repo(self.repo)
        secret_selected_repositories = exclusive_secret.selected_repositories
        self.assertEqual(1, secret_selected_repositories.totalCount)
        self.assertEqual(self.repo.id, secret_selected_repositories[0].id)
