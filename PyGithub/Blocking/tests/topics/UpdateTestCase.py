# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking.tests.Framework as Framework


class UpdateTestCase(Framework.SimpleLoginTestCase):
    def testUpdateWasNotNeeded(self):
        user = self.g.get_user("jacquev6")
        self.assertEqual(user.updated_at, datetime.datetime(2013, 12, 20, 6, 32, 34))
        self.assertFalse(user.update())
        self.assertEqual(user.updated_at, datetime.datetime(2013, 12, 20, 6, 32, 34))

    def testUpdateWasNeeded(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle")

        self.g.get_repo("jacquev6/JellyNoSolver").edit(description="Solver for Jelly no Puzzle!")

        self.assertTrue(repo.update())
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle!")

        repo.edit(description="Solver for Jelly no Puzzle")
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle")

    def testUpdateNotNeededAfterEdit(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle")
        repo.edit(description="Solver for Jelly no Puzzle!")
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle!")
        self.assertTrue(repo.update())  # @todoSomeday Consider opening a bug to GitHub: .update() should have been False
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle!")
        repo.edit(description="Solver for Jelly no Puzzle")
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle")

    def testUpdatePreservesIdentityOfClassAttributes(self):
        repo = self.g.get_repo("jacquev6/developer.github.com")
        parent = repo.parent
        self.assertEqual(repo.parent.full_name, "github/developer.github.com")
        self.g.get_repo("jacquev6/developer.github.com").edit(description="GitHub API documentation!")
        self.assertTrue(repo.update())
        self.g.get_repo("jacquev6/developer.github.com").edit(description="GitHub API documentation")
        self.assertEqual(repo.parent.full_name, "github2/developer.github.com")  # Forged in the replay file to prove it was updated
        self.assertIs(repo.parent, parent)

    @Framework.SharesDataWith(testUpdatePreservesIdentityOfClassAttributes)
    def testUpdatePreservesIdentityOfUnionAttributes(self):
        repo = self.g.get_repo("jacquev6/developer.github.com")
        owner = repo.owner
        self.assertEqual(repo.owner.login, "jacquev6")
        self.g.get_repo("jacquev6/developer.github.com").edit(description="GitHub API documentation!")
        self.assertTrue(repo.update())
        self.g.get_repo("jacquev6/developer.github.com").edit(description="GitHub API documentation")
        self.assertEqual(repo.owner.login, "jacquev6_2")  # Forged in the replay file to prove it was updated
        self.assertIs(repo.owner, owner)

    @Framework.SharesDataWith(testUpdatePreservesIdentityOfClassAttributes)
    def testUpdatePreservesIdentityOfStructAttributes(self):
        repo = self.g.get_repo("jacquev6/developer.github.com")
        permissions = repo.permissions
        self.assertTrue(repo.permissions.admin)
        self.g.get_repo("jacquev6/developer.github.com").edit(description="GitHub API documentation!")
        self.assertTrue(repo.update())
        self.g.get_repo("jacquev6/developer.github.com").edit(description="GitHub API documentation")
        self.assertFalse(repo.permissions.admin)  # Forged in the replay file to prove it was updated
        self.assertIs(repo.permissions, permissions)
