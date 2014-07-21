# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import time

import PyGithub.Blocking

import PyGithub.Blocking.tests.Framework as Framework


class TeamTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        t = self.g.get_team(141487)
        self.assertEqual(t.id, 141487)
        self.assertEqual(t.members_count, 1)
        self.assertEqual(t.members_url, "https://api.github.com/teams/141487/members{/member}")
        self.assertEqual(t.name, "Owners")
        self.assertEqual(t.organization.login, "BeaverSoftware")
        self.assertEqual(t.permission, "admin")
        self.assertEqual(t.repos_count, 1)
        self.assertEqual(t.repositories_url, "https://api.github.com/teams/141487/repos")
        self.assertEqual(t.slug, "owners")
        self.assertEqual(t.url, "https://api.github.com/teams/141487")

    def testImpossibleToEditNameOfOwnersTeam(self):
        team = self.g.get_team(141487)
        self.assertEqual(team.name, "Owners")
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            team.edit(name="Owners FTW")

    def testEditName(self):
        # @todoAlpha Can it be Reset? Globaly we need to review all .edit parameters for Reset
        # @todoAlpha Review all string parameters that should be enums
        team = self.g.get_team(141496)
        self.assertEqual(team.name, "Members")
        team.edit(name="Members FTW")
        self.assertEqual(team.name, "Members FTW")
        team.edit(name="Members")
        self.assertEqual(team.name, "Members")
        with self.assertRaises(TypeError):
            team.edit(name=PyGithub.Blocking.Reset)

    def testEditPermission(self):
        team = self.g.get_team(141496)
        self.assertEqual(team.permission, "push")
        team.edit(permission="pull")
        self.assertEqual(team.permission, "pull")
        team.edit(permission="push")
        self.assertEqual(team.permission, "push")
        with self.assertRaises(TypeError):
            team.edit(permission=PyGithub.Blocking.Reset)

    def testGetMembers(self):
        members = self.g.get_team(141487).get_members()
        self.assertEqual(members[0].login, "jacquev6")

    def testGetMembers_allParameters(self):
        members = self.g.get_team(141487).get_members(per_page=3)
        self.assertEqual(members[0].login, "jacquev6")

    def testHasInMembers(self):
        team = self.g.get_team(141487)
        self.assertTrue(team.has_in_members("jacquev6"))
        self.assertFalse(team.has_in_members("nvie"))

    def testAddRemoveMember(self):
        team = self.g.get_team(141487)
        self.assertFalse(team.has_in_members("Lyloa"))
        self.assertFalse(team.organization.has_in_members("Lyloa"))
        team.add_to_members("Lyloa")
        self.assertTrue(team.has_in_members("Lyloa"))
        self.assertTrue(team.organization.has_in_members("Lyloa"))
        team.remove_from_members("Lyloa")
        self.assertFalse(team.has_in_members("Lyloa"))
        self.assertFalse(team.organization.has_in_members("Lyloa"))

    def testGetRepos(self):
        repos = self.g.get_team(141487).get_repos()
        self.assertEqual(repos[0].full_name, "BeaverSoftware/FatherBeaver")

    def testGetRepos_allParameters(self):
        repos = self.g.get_team(141487).get_repos(per_page=1)
        self.assertEqual(repos[0].full_name, "BeaverSoftware/FatherBeaver")

    def testAddRemoveRepo(self):
        team = self.g.get_team(141496)
        self.assertTrue(team.has_in_repos("BeaverSoftware/FatherBeaver"))
        team.remove_from_repos("BeaverSoftware/FatherBeaver")
        self.assertFalse(team.has_in_repos("BeaverSoftware/FatherBeaver"))
        team.add_to_repos("BeaverSoftware/FatherBeaver")
        self.assertTrue(team.has_in_repos("BeaverSoftware/FatherBeaver"))

    def testImpossibleToRemoveRepoFromOwnersTeam(self):
        team = self.g.get_team(141487)
        # Currently a 500 from GitHub. Contacted support.
        with self.assertRaises(PyGithub.Blocking.ServerErrorException):
            team.remove_from_repos("BeaverSoftware/FatherBeaver")

    # @todoSomeday: test if it is possible to remove_from_members the last member of the Owners team.
