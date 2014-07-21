# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import PyGithub.Blocking.tests.Framework as Framework


class ParameterTypingTestCase(Framework.SimpleLoginTestCase):
    def testAcceptStringAsRepo(self):
        self.assertTrue(self.g.get_authenticated_user().has_in_starred("nvie/gitflow"))

    @Framework.SharesDataWith(testAcceptStringAsRepo)
    def testAcceptTwoStringsAsRepo(self):
        self.assertTrue(self.g.get_authenticated_user().has_in_starred(("nvie", "gitflow")))

    def testAcceptRepoAsRepo(self):
        repo = self.g.get_repo("nvie/gitflow")
        self.assertTrue(self.g.get_authenticated_user().has_in_starred(repo))

    def testDontAcceptNoneAsRepo(self):
        u = self.g.get_authenticated_user()
        with self.assertRaises(TypeError):
            u.has_in_starred(None)

    def testAcceptStringAsUser(self):
        self.assertFalse(self.g.get_authenticated_user().has_in_following("defunkt"))

    def testAcceptUserAsUser(self):
        user = self.g.get_user("defunkt")
        self.assertFalse(self.g.get_authenticated_user().has_in_following(user))

    def testAcceptAuthenticatedUserAsUser(self):
        user = self.g.get_authenticated_user()
        repo = user.get_repo("PyGithub")
        self.assertTrue(repo.has_in_assignees(user))

    @Framework.SharesDataWith(testDontAcceptNoneAsRepo)
    def testDontAcceptNoneAsUser(self):
        u = self.g.get_authenticated_user()
        with self.assertRaises(TypeError):
            u.has_in_following(None)

    def testDontAcceptStringAsBool(self):
        o = self.g.get_org("BeaverSoftware")
        with self.assertRaises(TypeError):
            o.create_repo("Whatever", has_issues="foobar")

    @Framework.SharesDataWith(testDontAcceptStringAsBool)
    def testDontAcceptBoolAsStringReset(self):
        o = self.g.get_org("BeaverSoftware")
        with self.assertRaises(TypeError):
            o.edit(company=True)

    @Framework.SharesDataWith(testDontAcceptNoneAsRepo)
    def testDontAcceptStringAsBoolReset(self):
        u = self.g.get_authenticated_user()
        with self.assertRaises(TypeError):
            u.edit(hireable="foobar")

    def testAcceptTwoStringsAsRepoFullName(self):
        self.assertEqual(self.g.get_repo(("jacquev6", "PyGithub")).full_name, "jacquev6/PyGithub")

    def testDontAcceptNoneAsRepoFullName(self):
        with self.assertRaises(TypeError):
            self.g.get_repo(None)

    @Framework.SharesDataWith(testDontAcceptStringAsBool)
    def testDontAcceptStringAsInt(self):
        o = self.g.get_org("BeaverSoftware")
        with self.assertRaises(TypeError):
            o.get_repos(per_page="42")

    @Framework.SharesDataWith(testDontAcceptStringAsBool)
    def testDontAcceptArbitraryStringAsEnum(self):
        o = self.g.get_org("BeaverSoftware")
        with self.assertRaises(TypeError):
            o.get_members(filter="foobar")

    @Framework.SharesDataWith(testDontAcceptStringAsBool)
    def testDontAcceptIntAsEnum(self):
        o = self.g.get_org("BeaverSoftware")
        with self.assertRaises(TypeError):
            o.get_members(filter=42)

    def testDontAcceptStringAsTeam(self):
        org = self.g.get_org("BeaverSoftware")
        with self.assertRaises(TypeError):
            org.create_repo("potential-octo-lana", team_id="foobar")

    def testAcceptTeamAsTeam(self):
        org = self.g.get_org("BeaverSoftware")
        team = org.get_teams()[0]
        org.create_repo("potential-octo-lana", team_id=team)

    def testDontAcceptStringAsRepoId(self):
        with self.assertRaises(TypeError):
            self.g.get_repos(since="foobar")

    def testDontAcceptStringAsUserId(self):
        with self.assertRaises(TypeError):
            self.g.get_users(since="foobar")

    def testAcceptGitIgnoreTemplateAsGitIgnoreTemplate(self):
        org = self.g.get_org("BeaverSoftware")
        tmpl = self.g.get_gitignore_template("Python")
        org.create_repo("potential-octo-lana", auto_init=True, gitignore_template=tmpl)

    @Framework.SharesDataWith(testDontAcceptStringAsBool)
    def testDontAcceptIntAsGitIgnoreTemplate(self):
        org = self.g.get_org("BeaverSoftware")
        with self.assertRaises(TypeError):
            org.create_repo("potential-octo-lana", auto_init=True, gitignore_template=42)

    @Framework.SharesDataWith(testAcceptTwoStringsAsRepoFullName)
    def testDontAcceptIntAsGitAuthor(self):
        repo = self.g.get_repo(("jacquev6", "PyGithub"))
        with self.assertRaises(TypeError):
            repo.create_file("path/to/file", "Comment", "content", author=42)

    def testDontAcceptIntAsDatetime(self):
        with self.assertRaises(TypeError):
            self.g.get_public_gists(since=10)
