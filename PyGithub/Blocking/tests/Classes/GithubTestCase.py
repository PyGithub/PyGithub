# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import textwrap

import PyGithub.Blocking.tests.Framework as Framework


class GithubTestCase(Framework.SimpleLoginTestCase):
    def testGetAuthenticatedUser(self):
        u = self.g.get_authenticated_user()
        self.assertEqual(u.login, "jacquev6")

    def testGetUser(self):
        u = self.g.get_user("nvie")
        self.assertEqual(u.name, "Vincent Driessen")

    def testGetUsers(self):
        users = self.g.get_users()
        self.assertEqual(users[0].login, "mojombo")
        self.assertEqual(users[1].login, "defunkt")

    def testGetUsersSinceId(self):
        users = self.g.get_users(since=327146)
        self.assertEqual(users[0].login, "FRINOS")
        self.assertEqual(users[1].login, "vangu90")

    def testGetUsersSinceUser(self):
        jacquev6 = self.g.get_user("jacquev6")
        users = self.g.get_users(since=jacquev6)
        self.assertEqual(users[0].login, "FRINOS")
        self.assertEqual(users[1].login, "vangu90")

    def testGetOrg(self):
        u = self.g.get_org("github")
        self.assertEqual(u.name, "GitHub")

    def testGetRepo(self):
        r = self.g.get_repo("nvie/gitflow")
        self.assertEqual(r.full_name, "nvie/gitflow")

    def testGetRepos(self):
        repos = self.g.get_repos()
        self.assertEqual(repos[0].full_name, "mojombo/grit")
        self.assertEqual(repos[1].full_name, "wycats/merb-core")

    def testGetReposSinceId(self):
        repos = self.g.get_repos(since=3544490)
        self.assertEqual(repos[0].full_name, "dereuromark/setup")
        self.assertEqual(repos[1].full_name, "hwatcha/ror")

    def testGetReposSinceRepo(self):
        pygithub = self.g.get_repo("jacquev6/PyGithub")
        repos = self.g.get_repos(since=pygithub)
        self.assertEqual(repos[0].full_name, "dereuromark/setup")
        self.assertEqual(repos[1].full_name, "hwatcha/ror")

    def testPaginationOfGetReposSince(self):
        repos = self.g.get_repos(since=3544490)
        self.assertEqual(repos[150].full_name, "swoosh/Hello-World")

    def testGetGitIgnoreTemplate(self):
        template = self.g.get_gitignore_template("C")
        self.assertEqual(template.name, "C")
        expectedSource = textwrap.dedent("""\
        # Object files
        *.o
        *.ko

        # Libraries
        *.lib
        *.a

        # Shared objects (inc. Windows DLLs)
        *.dll
        *.so
        *.so.*
        *.dylib

        # Executables
        *.exe
        *.out
        *.app
        """)
        self.assertEqual(template.source, expectedSource)

    def testGetGitIgnoreTemplates(self):
        templates = self.g.get_gitignore_templates()
        self.assertEqual(
            templates,
            [
                "Actionscript",
                "Android",
                "AppceleratorTitanium",
                "Autotools",
                "Bancha",
                "C",
                "C++",
                "CFWheels",
                "CMake",
                "CSharp",
                "CakePHP",
                "Clojure",
                "CodeIgniter",
                "Compass",
                "Concrete5",
                "Coq",
                "Dart",
                "Delphi",
                "Django",
                "Drupal",
                "Eagle",
                "Erlang",
                "ExpressionEngine",
                "Finale",
                "ForceDotCom",
                "FuelPHP",
                "GWT",
                "Go",
                "Grails",
                "Haskell",
                "Java",
                "Jboss",
                "Jekyll",
                "Joomla",
                "Jython",
                "Kohana",
                "LaTeX",
                "Leiningen",
                "LemonStand",
                "Lilypond",
                "Lithium",
                "Magento",
                "Maven",
                "Node",
                "OCaml",
                "Objective-C",
                "Opa",
                "OracleForms",
                "Perl",
                "PlayFramework",
                "Plone",
                "Python",
                "Qooxdoo",
                "Qt",
                "R",
                "Rails",
                "RhodesRhomobile",
                "Ruby",
                "Scala",
                "Sdcc",
                "SeamGen",
                "SketchUp",
                "SugarCRM",
                "Symfony",
                "Symfony2",
                "SymphonyCMS",
                "Target3001",
                "Tasm",
                "Textpattern",
                "TurboGears2",
                "Typo3",
                "Unity",
                "VB.Net",
                "VisualStudio",
                "Waf",
                "WordPress",
                "Yii",
                "ZendFramework",
                "gcov",
                "nanoc",
                "opencart",
            ]
        )
