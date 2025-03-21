############################ Copyrights and license ############################
#                                                                              #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Agor Maxime <maxime.agor23@gmail.com>                         #
# Copyright 2018 Joel Koglin <JoelKoglin@gmail.com>                            #
# Copyright 2018 Shubham Singh <41840111+singh811@users.noreply.github.com>    #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 h.shi <10385628+AnYeMoWang@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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


class Search(Framework.TestCase):
    def setUp(self):
        super().setUp()

    def testSearchUsers(self):
        users = self.g.search_users("vincent", sort="followers", order="desc")
        self.assertEqual(users.totalCount, 2781)

    def testPaginateSearchUsers(self):
        users = self.g.search_users("", location="Berlin")
        self.assertListKeyBegin(
            users,
            lambda u: u.login,
            [
                "cloudhead",
                "felixge",
                "sferik",
                "rkh",
                "jezdez",
                "janl",
                "marijnh",
                "nikic",
                "igorw",
                "froschi",
                "svenfuchs",
                "omz",
                "chad",
                "bergie",
                "roidrage",
                "pcalcado",
                "durran",
                "hukl",
                "mttkay",
                "aFarkas",
                "ole",
                "hagenburger",
                "jberkel",
                "naderman",
                "joshk",
                "pudo",
                "robb",
                "josephwilk",
                "hanshuebner",
                "txus",
                "paulasmuth",
                "splitbrain",
                "langalex",
                "bendiken",
                "stefanw",
            ],
        )
        self.assertEqual(users.totalCount, 6038)
        self.assertEqual(users[0].score, 1.0)

    def testGetPageOnSearchUsers(self):
        users = self.g.search_users("", location="Berlin")
        self.assertEqual(
            [u.login for u in users.get_page(7)],
            [
                "ursachec",
                "bitboxer",
                "fs111",
                "michenriksen",
                "witsch",
                "booo",
                "mortice",
                "r0man",
                "MikeBild",
                "mhagger",
                "bkw",
                "fwbrasil",
                "mschneider",
                "lydiapintscher",
                "asksven",
                "iamtimm",
                "sneak",
                "kr1sp1n",
                "Feh",
                "GordonLesti",
                "annismckenzie",
                "eskimoblood",
                "tsujigiri",
                "riethmayer",
                "lauritzthamsen",
                "scotchi",
                "peritor",
                "toto",
                "hwaxxer",
                "lukaszklis",
            ],
        )

    def testSearchRepos(self):
        repos = self.g.search_repositories("github", sort="stars", order="desc", language="Python")
        self.assertListKeyBegin(
            repos,
            lambda r: r.full_name,
            [
                "kennethreitz/legit",
                "RuudBurger/CouchPotatoV1",
                "gelstudios/gitfiti",
                "gpjt/webgl-lessons",
                "jacquev6/PyGithub",
                "aaasen/github_globe",
                "hmason/gitmarks",
                "dnerdy/factory_boy",
                "binaryage/drydrop",
                "bgreenlee/sublime-github",
                "karan/HackerNewsAPI",
                "mfenniak/pyPdf",
                "skazhy/github-decorator",
                "llvmpy/llvmpy",
                "lexrupy/gmate",
                "ask/python-github2",
                "audreyr/cookiecutter-pypackage",
                "tabo/django-treebeard",
                "dbr/tvdb_api",
                "jchris/couchapp",
                "joeyespo/grip",
                "nigelsmall/py2neo",
                "ask/chishop",
                "sigmavirus24/github3.py",
                "jsmits/github-cli",
                "lincolnloop/django-layout",
                "amccloud/django-project-skel",
                "Stiivi/brewery",
                "webpy/webpy.github.com",
                "dustin/py-github",
                "logsol/Github-Auto-Deploy",
                "cloudkick/libcloud",
                "berkerpeksag/github-badge",
                "bitprophet/ssh",
                "azavea/OpenTreeMap",
            ],
        )

    def testSearchReposWithNoResults(self):
        repos = self.g.search_repositories("doesnotexist")
        self.assertEqual(repos.totalCount, 0)

    def testSearchIssues(self):
        issues = self.g.search_issues("compile", sort="comments", order="desc", language="C++")
        self.assertListKeyBegin(
            issues,
            lambda i: i.id,
            [
                12068673,
                23250111,
                14371957,
                9423897,
                24277400,
                2408877,
                11338741,
                13980502,
                27697165,
                23102422,
            ],
        )
        self.assertEqual(issues[0].score, 0.08252439)

    def testSearchCommits(self):
        pages = self.g.search_commits(query="hash:5b0224e868cc9242c9450ef02efbe3097abd7ba2")
        commits = list(pages)
        self.assertEqual(pages.totalCount, 12)
        self.assertEqual(commits[0].commit.message, "Fix README instructions")
        self.assertEqual(commits[0].score, 1.0)
        self.assertEqual(commits[0].sha, "5b0224e868cc9242c9450ef02efbe3097abd7ba2")

    def testSearchCommitsOrder(self):
        pages = self.g.search_commits(
            query="hash:1265747e992ba7d34a469b6b2f527809f8bf7067",
            sort="author-date",
            order="asc",
            merge="false",
        )
        commits = list(pages)
        self.assertEqual(pages.totalCount, 4)
        self.assertEqual(len(commits[0].commit.message), 490)
        self.assertEqual(commits[0].score, 1.0)
        self.assertEqual(commits[0].sha, "1265747e992ba7d34a469b6b2f527809f8bf7067")

    def testSearchTopics(self):
        topics = self.g.search_topics("python", repositories=">950")
        self.assertListKeyBegin(
            topics,
            lambda r: r.name,
            ["python", "django", "flask", "ruby", "scikit-learn", "wagtail"],
        )

    def testPaginateSearchTopics(self):
        repos = self.g.search_topics("python", repositories=">950")
        self.assertEqual(repos.totalCount, 6)

    def testSearchCode(self):
        files = self.g.search_code("toto", sort="indexed", order="asc", user="jacquev6")
        self.assertListKeyEqual(
            files,
            lambda f: f.name,
            [
                "Commit.setUp.txt",
                "PullRequest.testGetFiles.txt",
                "NamedUser.testGetEvents.txt",
                "PullRequest.testCreateComment.txt",
                "PullRequestFile.setUp.txt",
                "Repository.testGetIssuesWithWildcards.txt",
                "Repository.testGetIssuesWithArguments.txt",
                "test_ebnf.cpp",
                "test_abnf.cpp",
                "PullRequestFile.py",
                "SystemCalls.py",
                "tests.py",
                "LexerTestCase.py",
                "ParserTestCase.py",
            ],
        )
        self.assertEqual(files[0].score, 0.31651077)
        self.assertEqual(files[0].repository.full_name, "jacquev6/PyGithub")
        content = files[0].decoded_content
        if isinstance(content, bytes):
            content = content.decode("utf-8")
        self.assertEqual(content[:30], "https\nGET\napi.github.com\nNone\n")

    def testSearchHighlightingCode(self):
        files = self.g.search_code("toto", sort="indexed", order="asc", user="jacquev6", highlight=True)
        self.assertEqual(files[0].score, 14.030813)
        self.assertEqual(
            files[0].text_matches,
            [
                {
                    "fragment": ".assertEqual(\n"
                    "            self.recorded.instance_method(42, 43, 44, 45, "
                    "toto=46, tutu=47",
                    "matches": [{"indices": [72, 76], "text": "toto"}],
                    "object_type": "FileContent",
                    "object_url": "https://api.github.com/repositories/6430524/contents/MockMockMock/tests/record_replay.py?ref=562a55542f55426f6853f3013309c85f402c359e",
                    "property": "content",
                },
                {
                    "fragment": "),\n"
                    "            \"(42, 43, (44, 45), [('toto', 46), ('tutu', "
                    '47)])"\n'
                    "        )\n"
                    "        self.assertEqual",
                    "matches": [{"indices": [38, 42], "text": "toto"}],
                    "object_type": "FileContent",
                    "object_url": "https://api.github.com/repositories/6430524/contents/MockMockMock/tests/record_replay.py?ref=562a55542f55426f6853f3013309c85f402c359e",
                    "property": "content",
                },
            ],
        )

    def testUrlquotingOfQualifiers(self):
        # Example taken from #236
        issues = self.g.search_issues("repo:saltstack/salt-api type:Issues", updated=">2014-03-04T18:28:11Z")
        self.assertEqual(issues[0].id, 29138794)

    def testUrlquotingOfQuery(self):
        # Example taken from #236
        issues = self.g.search_issues("repo:saltstack/salt-api type:Issues updated:>2014-03-04T18:28:11Z")
        self.assertEqual(issues[0].id, 29138794)
