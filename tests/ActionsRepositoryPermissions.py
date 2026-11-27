############################ Copyrights and license ############################
#                                                                              #
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

from __future__ import annotations

from . import Framework


class ActionsRepositoryPermissions(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.withLazy(True).get_repo("andrewfish0/PyGithub")

    def testAttributes(self):
        permissions = self.repo.get_actions_permissions()
        self.assertEqual(permissions.url, "/repos/andrewfish0/PyGithub/actions/permissions")
        self.assertTrue(permissions.enabled)
        self.assertEqual(permissions.allowed_actions, "all")
        self.assertIsNone(permissions.selected_actions_url)
        self.assertFalse(permissions.sha_pinning_required)
        self.assertEqual(repr(permissions), 'ActionsRepositoryPermissions(enabled=True, allowed_actions="all")')

    def testEdit(self):
        self.repo.get_actions_permissions().edit(enabled=True, allowed_actions="selected", sha_pinning_required=True)
        permissions = self.repo.get_actions_permissions()
        self.assertTrue(permissions.enabled)
        self.assertEqual(permissions.allowed_actions, "selected")
        self.assertEqual(
            permissions.selected_actions_url,
            "https://api.github.com/repositories/1407991155/actions/permissions/selected-actions",
        )
        self.assertTrue(permissions.sha_pinning_required)

        permissions.edit(enabled=False)
        permissions = self.repo.get_actions_permissions()
        self.assertFalse(permissions.enabled)
        self.assertIsNone(permissions.allowed_actions)
        self.assertFalse(permissions.sha_pinning_required)
