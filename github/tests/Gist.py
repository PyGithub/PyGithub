# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
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
################################################################################

import Framework

import github
import datetime


class Gist(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.gist = self.g.get_gist("2729810")

    def testAttributes(self):
        self.assertEqual(self.gist.comments, 0)
        self.assertEqual(self.gist.created_at, datetime.datetime(2012, 2, 29, 16, 47, 12))
        self.assertEqual(self.gist.description, "How to error 500 Github API v3, as requested by Rick (GitHub Staff)")
        self.assertEqual(self.gist.files.keys(), ["fail_github.py"])
        self.assertEqual(self.gist.files["fail_github.py"].size, 1636)
        self.assertEqual(self.gist.files["fail_github.py"].filename, "fail_github.py")
        self.assertEqual(self.gist.files["fail_github.py"].language, "Python")
        self.assertEqual(self.gist.files["fail_github.py"].content, 'import httplib\nimport base64\nimport json\n\nlogin = ""\npassword = ""\norgName = ""\nrepoName = "FailGithubApi"\n\ndef doRequest( verb, url, input ):\n    input = json.dumps( input )\n    cnx = httplib.HTTPSConnection( "api.github.com", strict = True )\n    cnx.request( verb, url, input, { "Authorization" : "Basic " + base64.b64encode( login + ":" + password ).replace( \'\\n\', \'\' ) } )\n    response = cnx.getresponse()\n    status = response.status\n    output = response.read()\n    cnx.close()\n    print verb, url, input, "=>", status, output\n    print\n    if status < 200 or status >= 300:\n        exit( 1 )\n    return json.loads( output )\n\n# Create a repo\ndoRequest( "POST", "/user/repos", { "name": repoName } )\n\n# Create a blob, a tree, a commit and the master branch\nb = doRequest(\n    "POST", "/repos/%s/%s/git/blobs" % ( login, repoName ),\n    { "content": "Content of the blob", "encoding": "latin1" }\n)\nt = doRequest(\n    "POST", "/repos/%s/%s/git/trees" % ( login, repoName ),\n    { "tree" : [ { "path": "foo.bar", "type": "blob", "mode": "100644", "sha": b["sha"] } ] }\n)\nc = doRequest(\n    "POST", "/repos/%s/%s/git/commits" % ( login, repoName ),\n    { "parents": [], "message": "Message of the commit", "tree": t["sha"] }\n)\ndoRequest(\n    "POST", "/repos/%s/%s/git/refs" % ( login, repoName ),\n    { "ref": "refs/heads/master", "sha": c["sha"] }\n)\n\n# Fork the repo\ndoRequest( "POST", "/repos/%s/%s/forks?org=%s" % ( login, repoName, orgName ), None )\n\n# Create a new blob => BOOM error 500\ndoRequest(\n    "POST", "/repos/%s/%s/git/blobs" % ( orgName, repoName ),\n    { "content": "Content of the new blob", "encoding": "latin1" }\n)\n')
        self.assertEqual(self.gist.files["fail_github.py"].raw_url, "https://gist.github.com/raw/2729810/2fb3aa84e0efa50dc0f4c18b5df5b7b9ab27076b/fail_github.py")
        self.assertEqual(self.gist.forks, [])
        self.assertEqual(self.gist.git_pull_url, "git://gist.github.com/2729810.git")
        self.assertEqual(self.gist.git_push_url, "git@gist.github.com:2729810.git")
        self.assertEqual(len(self.gist.history), 1)
        self.assertEqual(self.gist.history[0].change_status.additions, 52)
        self.assertEqual(self.gist.history[0].change_status.deletions, 0)
        self.assertEqual(self.gist.history[0].change_status.total, 52)
        self.assertEqual(self.gist.history[0].committed_at, datetime.datetime(2012, 2, 29, 16, 47, 12))
        self.assertEqual(self.gist.history[0].url, "https://api.github.com/gists/2729810/a40de483e42ba33bda308371c0ef8383db73be9e")
        self.assertEqual(self.gist.history[0].user.login, "jacquev6")
        self.assertEqual(self.gist.history[0].version, "a40de483e42ba33bda308371c0ef8383db73be9e")
        self.assertEqual(self.gist.html_url, "https://gist.github.com/2729810")
        self.assertEqual(self.gist.id, "2729810")
        self.assertTrue(self.gist.public)
        self.assertEqual(self.gist.updated_at, datetime.datetime(2012, 2, 29, 16, 47, 12))
        self.assertEqual(self.gist.url, "https://api.github.com/gists/2729810")
        self.assertEqual(self.gist.user.login, "jacquev6")

    def testNewAttributes(self):
        # For gists after https://github.com/blog/1276-welcome-to-a-new-gist
        gist = self.g.get_gist("3800341")
        self.assertEqual(gist.git_pull_url, "https://gist.github.com/3800341.git")
        self.assertEqual(gist.git_push_url, "https://gist.github.com/3800341.git")
        self.assertEqual(gist.html_url, "https://gist.github.com/3800341")
        self.assertEqual(gist.url, "https://api.github.com/gists/3800341")

    def testEditWithoutParameters(self):
        self.gist.edit()
        self.assertEqual(self.gist.description, "Gist created by PyGithub")
        self.assertEqual(self.gist.updated_at, datetime.datetime(2012, 5, 19, 7, 0, 58))

    def testEditWithAllParameters(self):
        self.gist.edit("Description edited by PyGithub", {"barbaz.txt": github.InputFileContent("File also created by PyGithub")})
        self.assertEqual(self.gist.description, "Description edited by PyGithub")
        self.assertEqual(self.gist.updated_at, datetime.datetime(2012, 5, 19, 7, 6, 10))
        self.assertEqual(set(self.gist.files.keys()), set(["foobar.txt", "barbaz.txt"]))

    def testDeleteFile(self):
        gist = self.g.get_gist("5339374")
        self.assertEqual(sorted(gist.files.keys()), ["bar.txt", "foo.txt"])
        gist.edit(files={"foo.txt": None})
        self.assertEqual(gist.files.keys(), ["bar.txt"])

    def testRenameFile(self):
        gist = self.g.get_gist("5339374")
        self.assertEqual(gist.files.keys(), ["bar.txt"])
        gist.edit(files={"bar.txt": github.InputFileContent(gist.files["bar.txt"].content, new_name="baz.txt")})
        self.assertEqual(gist.files.keys(), ["baz.txt"])

    def testCreateComment(self):
        comment = self.gist.create_comment("Comment created by PyGithub")
        self.assertEqual(comment.id, 323629)

    def testGetComments(self):
        self.assertListKeyEqual(self.gist.get_comments(), lambda c: c.id, [323637])

    def testStarring(self):
        self.assertFalse(self.gist.is_starred())
        self.gist.set_starred()
        self.assertTrue(self.gist.is_starred())
        self.gist.reset_starred()
        self.assertFalse(self.gist.is_starred())

    def testFork(self):
        gist = self.g.get_gist("6296553")  # Random gist
        myGist = gist.create_fork()
        self.assertEqual(myGist.id, "6296732")
        self.assertEqual(myGist.fork_of, None)  # WTF
        sameGist = self.g.get_gist("6296732")
        self.assertEqual(sameGist.fork_of.id, "6296553")

    def testDelete(self):
        self.gist.delete()
