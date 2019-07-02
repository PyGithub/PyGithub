# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Steve Brown <steve@evolvedlight.co.uk>                        #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Tyler Treat <ttreat31@gmail.com>                              #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Svend Sorensen <svend@svends.net>                             #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2018 itsbruce <it.is.bruce@gmail.com>                              #
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

import Framework

import Time

import github


class Github(Framework.TestCase):
    def testGetGists(self):
        self.assertListKeyBegin(self.g.get_gists(), lambda g: g.id, ["2729695", "2729656", "2729597", "2729584", "2729569", "2729554", "2729543", "2729537", "2729536", "2729533", "2729525", "2729522", "2729519", "2729515", "2729506", "2729487", "2729484", "2729482", "2729441", "2729432", "2729420", "2729398", "2729372", "2729371", "2729351", "2729346", "2729316", "2729304", "2729296", "2729276", "2729272", "2729265", "2729195", "2729160", "2729143", "2729127", "2729119", "2729113", "2729103", "2729069", "2729059", "2729051", "2729029", "2729027", "2729026", "2729022", "2729002", "2728985", "2728979", "2728964", "2728937", "2728933", "2728884", "2728869", "2728866", "2728855", "2728854", "2728853", "2728846", "2728825", "2728814", "2728813", "2728812", "2728805", "2728802", "2728800", "2728798", "2728797", "2728796", "2728793", "2728758", "2728754", "2728751", "2728748", "2728721", "2728716", "2728715", "2728705", "2728701", "2728699", "2728697", "2728688", "2728683", "2728677", "2728649", "2728640", "2728625", "2728620", "2728615", "2728614", "2728565", "2728564", "2728554", "2728523", "2728519", "2728511", "2728497", "2728496", "2728495", "2728487"])

    def testGetGistsWithSince(self):
        self.assertListKeyBegin(self.g.get_gists(since=datetime.datetime(2018, 10, 2, 10, 38, 30, 00, tzinfo=Time.UTCtzinfo())), lambda g: g.id, ["69b8a5831b74946db944c5451017fa40", "c22050a8705e93d170e0d4ca9c02e40c", "a7a95e1a194e07960364a5b32c56ac5f", "a25d9ace89b574f95bf0724f95a84fc2", "3195465"])

    def testGetHooks(self):
        hooks = self.g.get_hooks()
        hook = hooks[0]
        self.assertEqual(hook.name, "activecollab")
        self.assertEqual(hook.supported_events, ["push"])
        self.assertEqual(hook.events, ["push"])
        self.assertEqual(hook.schema, [["string", "url"], ["string", "token"], ["string", "project_id"], ["string", "milestone_id"], ["string", "category_id"]])

    def testGetEmojis(self):
        emojis = self.g.get_emojis()
        first = emojis.get("+1")
        self.assertEqual(first, "https://github.global.ssl.fastly.net/images/icons/emoji/+1.png?v5")

    def testGetHook(self):
        hook = self.g.get_hook("activecollab")
        self.assertEqual(hook.name, "activecollab")
        self.assertEqual(hook.supported_events, ["push"])
        self.assertEqual(hook.events, ["push"])
        self.assertEqual(hook.schema, [["string", "url"], ["string", "token"], ["string", "project_id"], ["string", "milestone_id"], ["string", "category_id"]])

    def testGetRepoFromFullName(self):
        self.assertEqual(self.g.get_repo("jacquev6/PyGithub").description, "Python library implementing the full Github API v3")

    def testGetRepoFromId(self):
        self.assertEqual(self.g.get_repo(3544490).description, "Python library implementing the full Github API v3")

    def testGetGitignoreTemplates(self):
        self.assertEqual(self.g.get_gitignore_templates(), ["Actionscript", "Android", "AppceleratorTitanium", "Autotools", "Bancha", "C", "C++", "CFWheels", "CMake", "CSharp", "CakePHP", "Clojure", "CodeIgniter", "Compass", "Concrete5", "Coq", "Delphi", "Django", "Drupal", "Erlang", "ExpressionEngine", "Finale", "ForceDotCom", "FuelPHP", "GWT", "Go", "Grails", "Haskell", "Java", "Jboss", "Jekyll", "Joomla", "Jython", "Kohana", "LaTeX", "Leiningen", "LemonStand", "Lilypond", "Lithium", "Magento", "Maven", "Node", "OCaml", "Objective-C", "Opa", "OracleForms", "Perl", "PlayFramework", "Python", "Qooxdoo", "Qt", "R", "Rails", "RhodesRhomobile", "Ruby", "Scala", "Sdcc", "SeamGen", "SketchUp", "SugarCRM", "Symfony", "Symfony2", "SymphonyCMS", "Target3001", "Tasm", "Textpattern", "TurboGears2", "Unity", "VB.Net", "Waf", "Wordpress", "Yii", "ZendFramework", "gcov", "nanoc", "opencart"])

    def testGetGitignoreTemplate(self):
        t = self.g.get_gitignore_template("Python")
        self.assertEqual(t.name, "Python")
        self.assertEqual(t.source, "*.py[cod]\n\n# C extensions\n*.so\n\n# Packages\n*.egg\n*.egg-info\ndist\nbuild\neggs\nparts\nbin\nvar\nsdist\ndevelop-eggs\n.installed.cfg\nlib\nlib64\n\n# Installer logs\npip-log.txt\n\n# Unit test / coverage reports\n.coverage\n.tox\nnosetests.xml\n\n# Translations\n*.mo\n\n# Mr Developer\n.mr.developer.cfg\n.project\n.pydevproject\n")

        t = self.g.get_gitignore_template("C++")
        self.assertEqual(t.name, "C++")
        self.assertEqual(t.source, "# Compiled Object files\n*.slo\n*.lo\n*.o\n\n# Compiled Dynamic libraries\n*.so\n*.dylib\n\n# Compiled Static libraries\n*.lai\n*.la\n*.a\n")

    def testStringOfNotSet(self):
        self.assertEqual(str(github.GithubObject.NotSet), "NotSet")

    def testGetUsers(self):
        self.assertListKeyBegin(self.g.get_users(), lambda u: u.login, ["mojombo", "defunkt", "pjhyett", "wycats", "ezmobius", "ivey", "evanphx", "vanpelt", "wayneeseguin", "brynary", "kevinclark", "technoweenie", "macournoyer", "takeo", "Caged", "topfunky", "anotherjesse", "roland", "lukas", "fanvsfan", "tomtt", "railsjitsu", "nitay", "kevwil", "KirinDave", "jamesgolick", "atmos", "errfree", "mojodna", "bmizerany", "jnewland", "joshknowles", "hornbeck", "jwhitmire", "elbowdonkey", "reinh", "timocratic", "bs", "rsanheim", "schacon", "uggedal", "bruce", "sam", "mmower", "abhay", "rabble", "benburkert", "indirect", "fearoffish", "ry", "engineyard", "jsierles", "tweibley", "peimei", "brixen", "tmornini", "outerim", "daksis", "sr", "lifo", "rsl", "imownbey", "dylanegan", "jm", "willcodeforfoo", "jvantuyl", "BrianTheCoder", "freeformz", "hassox", "automatthew", "queso", "lancecarlson", "drnic", "lukesutton", "danwrong", "hcatlin", "jfrost", "mattetti", "ctennis", "lawrencepit", "marcjeanson", "grempe", "peterc", "ministrycentered", "afarnham", "up_the_irons", "evilchelu", "heavysixer", "brosner", "danielmorrison", "danielharan", "kvnsmth", "collectiveidea", "canadaduane", "nate", "dstrelau", "sunny", "dkubb", "jnicklas", "richcollins", "simonjefford"])

    def testGetUsersSince(self):
        self.assertListKeyBegin(self.g.get_users(since=1000), lambda u: u.login, ["sbecker"])

    def testGetOrganizations(self):
        self.assertListKeyBegin(self.g.get_organizations(), lambda u: u.login, ['errfree', 'engineyard', "ministrycentered", "collectiveidea", "ogc", "sevenwire", "entryway"])

    def testGetOrganizationsSince(self):
        self.assertListKeyBegin(self.g.get_organizations(since=1000), lambda u: u.login, ["railslove", "railsdog", "netguru", "webhostio", "animikii", "sauspiel", "wherecloud", "triveos"])

    def testGetRepos(self):
        self.assertListKeyBegin(self.g.get_repos(), lambda r: r.name, ["grit", "merb-core", "rubinius", "god", "jsawesome", "jspec", "exception_logger", "ambition"])

    def testGetReposSince(self):
        self.assertListKeyBegin(self.g.get_repos(since=1000), lambda r: r.name, ["jquery-humanize-messages-plugin", "4slicer", "fixture-scenarios", "mongrel_proctitle", "rails-plugins"])

    def testGetLicenses(self):
        self.assertListKeyBegin(self.g.get_licenses(), lambda r: r.name, ['GNU General Public License v3.0',
                                                                          'BSD 2-Clause "Simplified" License',
                                                                          'MIT License',
                                                                          'GNU Lesser General Public License v2.1',
                                                                          'GNU General Public License v2.0',
                                                                          'GNU Lesser General Public License v3.0',
                                                                          'Mozilla Public License 2.0',
                                                                          'BSD 3-Clause "New" or "Revised" License'])

    def testGetLicense(self):
        self.assertEqual(self.g.get_license("mit").description, "A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.")
