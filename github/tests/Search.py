# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
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
# ##############################################################################

import Framework
import sys

atLeastPython3 = sys.hexversion >= 0x03000000


class Search(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)

    def testSearchUsers(self):
        users = self.g.search_users("vincent", sort="followers", order="desc")
        self.assertEqual(users.totalCount, 2781)
        self.assertEqual(users[0].login, "nvie")
        self.assertEqual(users[14].login, "Vayn")

    def testPaginateSearchUsers(self):
        users = self.g.search_users("", location="Berlin")
        self.assertListKeyBegin(users, lambda u: u.login, [u'cloudhead', u'felixge', u'sferik', u'rkh', u'jezdez', u'janl', u'marijnh', u'nikic', u'igorw', u'froschi', u'svenfuchs', u'omz', u'chad', u'bergie', u'roidrage', u'pcalcado', u'durran', u'hukl', u'mttkay', u'aFarkas', u'ole', u'hagenburger', u'jberkel', u'naderman', u'joshk', u'pudo', u'robb', u'josephwilk', u'hanshuebner', u'txus', u'paulasmuth', u'splitbrain', u'langalex', u'bendiken', u'stefanw'])
        self.assertEqual(users.totalCount, 6038)

    def testGetPageOnSearchUsers(self):
        users = self.g.search_users("", location="Berlin")
        self.assertEqual([u.login for u in users.get_page(7)], [u'ursachec', u'bitboxer', u'fs111', u'michenriksen', u'witsch', u'booo', u'mortice', u'r0man', u'MikeBild', u'mhagger', u'bkw', u'fwbrasil', u'mschneider', u'lydiapintscher', u'asksven', u'iamtimm', u'sneak', u'kr1sp1n', u'Feh', u'GordonLesti', u'annismckenzie', u'eskimoblood', u'tsujigiri', u'riethmayer', u'lauritzthamsen', u'scotchi', u'peritor', u'toto', u'hwaxxer', u'lukaszklis'])

    def testSearchRepos(self):
        repos = self.g.search_repositories("github", sort="stars", order="desc", language="Python")
        self.assertListKeyBegin(repos, lambda r: r.full_name, [u'kennethreitz/legit', u'RuudBurger/CouchPotatoV1', u'gelstudios/gitfiti', u'gpjt/webgl-lessons', u'jacquev6/PyGithub', u'aaasen/github_globe', u'hmason/gitmarks', u'dnerdy/factory_boy', u'binaryage/drydrop', u'bgreenlee/sublime-github', u'karan/HackerNewsAPI', u'mfenniak/pyPdf', u'skazhy/github-decorator', u'llvmpy/llvmpy', u'lexrupy/gmate', u'ask/python-github2', u'audreyr/cookiecutter-pypackage', u'tabo/django-treebeard', u'dbr/tvdb_api', u'jchris/couchapp', u'joeyespo/grip', u'nigelsmall/py2neo', u'ask/chishop', u'sigmavirus24/github3.py', u'jsmits/github-cli', u'lincolnloop/django-layout', u'amccloud/django-project-skel', u'Stiivi/brewery', u'webpy/webpy.github.com', u'dustin/py-github', u'logsol/Github-Auto-Deploy', u'cloudkick/libcloud', u'berkerpeksag/github-badge', u'bitprophet/ssh', u'azavea/OpenTreeMap'])

    def testSearchIssues(self):
        issues = self.g.search_issues("compile", sort="comments", order="desc", language="C++")
        self.assertListKeyBegin(issues, lambda i: i.id, [12068673, 23250111, 14371957, 9423897, 24277400, 2408877, 11338741, 13980502, 27697165, 23102422])

    def testSearchCode(self):
        files = self.g.search_code("toto", sort="indexed", order="asc", user="jacquev6")
        self.assertListKeyEqual(files, lambda f: f.name, [u'Commit.setUp.txt', u'PullRequest.testGetFiles.txt', u'NamedUser.testGetEvents.txt', u'PullRequest.testCreateComment.txt', u'PullRequestFile.setUp.txt', u'Repository.testGetIssuesWithWildcards.txt', u'Repository.testGetIssuesWithArguments.txt', u'test_ebnf.cpp', u'test_abnf.cpp', u'PullRequestFile.py', u'SystemCalls.py', u'tests.py', u'LexerTestCase.py', u'ParserTestCase.py'])
        self.assertEqual(files[0].repository.full_name, "jacquev6/PyGithub")
        if atLeastPython3:
            self.assertEqual(files[0].decoded_content[:30], b'https\nGET\napi.github.com\nNone\n')
        else:
            self.assertEqual(files[0].decoded_content[:30], "https\nGET\napi.github.com\nNone\n")

    def testUrlquotingOfQualifiers(self):
        # Example taken from #236
        issues = self.g.search_issues("repo:saltstack/salt-api type:Issues", updated=">2014-03-04T18:28:11Z")
        self.assertEqual(issues[0].id, 29138794)

    def testUrlquotingOfQuery(self):
        # Example taken from #236
        issues = self.g.search_issues("repo:saltstack/salt-api type:Issues updated:>2014-03-04T18:28:11Z")
        self.assertEqual(issues[0].id, 29138794)
