# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework


class FileTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_file_content("README.md")
        self.assertEqual(len(f.content), 151)
        self.assertEqual(f.encoding, "base64")
        self.assertEqual(f.git_url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/blobs/76a7c87928c256c0dec34784ffaf9b936162bfa3")
        self.assertEqual(f.html_url, "https://github.com/jacquev6/PyGithubIntegrationTests/blob/master/README.md")
        self.assertEqual(f.name, "README.md")
        self.assertEqual(f.path, "README.md")
        self.assertEqual(f.sha, "76a7c87928c256c0dec34784ffaf9b936162bfa3")
        self.assertEqual(f.size, 109)
        self.assertEqual(f.type, "file")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/README.md?ref=master")

    def testLazyCompletion(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_dir_content("")[0]
        self.assertEqual(f.size, 109)
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/README.md?ref=master")
        self.assertEqual(len(f.content), 151)

    def testEdit(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_file_content("README.md")
        self.assertEqual(f.size, 109)
        self.assertEqual(f.content, "UHlHaXRodWJJbnRlZ3JhdGlvblRlc3RzCj09PT09PT09PT09PT09PT09PT09\nPT09PQoKRHVtbXkgcmVwbyB0byBiZSBtb2RpZmllZCBieSBQeUdpdGh1Yidz\nIGludGVncmF0aW9uIHRlc3RzCg==\n")

        commit = f.edit("Modify Readme", "UHlHaXRodWJJbnRlZ3JhdGlvblRlc3RzDQo9PT09PT09PT09PT09PT09PT09PT09PT0NCg0KRHVtbXkgcmVwbyB0byBiZSBtb2RpZmllZCBieSBQeUdpdGh1YidzIGludGVncmF0aW9uIHRlc3RzDQoNCk1vZGlmaWVkIGJ5IFB5R2l0aHVi")
        self.assertEqual(f.size, 135)
        self.assertEqual(f.content, "UHlHaXRodWJJbnRlZ3JhdGlvblRlc3RzDQo9PT09PT09PT09PT09PT09PT09PT09PT0NCg0KRHVtbXkgcmVwbyB0byBiZSBtb2RpZmllZCBieSBQeUdpdGh1YidzIGludGVncmF0aW9uIHRlc3RzDQoNCk1vZGlmaWVkIGJ5IFB5R2l0aHVi")
        self.assertEqual(commit.sha, "f6ebb0a38ecd90239a28a528926e23c298b11495")

        commit = f.edit(
            "Reset Readme",
            "UHlHaXRodWJJbnRlZ3JhdGlvblRlc3RzCj09PT09PT09PT09PT09PT09PT09PT09PQoKRHVtbXkgcmVwbyB0byBiZSBtb2RpZmllZCBieSBQeUdpdGh1YidzIGludGVncmF0aW9uIHRlc3RzCg==",
            committer={"name": "John Doe", "email": "john@doe.com"},
            author={"name": "Jane Doe", "email": "jane@doe.com"},  # @todoAlpha Use a GitCommit.Author? Does the api accept an undocumented date?
        )
        self.assertEqual(f.size, 109)
        self.assertEqual(f.content, "UHlHaXRodWJJbnRlZ3JhdGlvblRlc3RzCj09PT09PT09PT09PT09PT09PT09PT09PQoKRHVtbXkgcmVwbyB0byBiZSBtb2RpZmllZCBieSBQeUdpdGh1YidzIGludGVncmF0aW9uIHRlc3RzCg==")
        self.assertEqual(commit.sha, "2b3fe89a93209260f79dc1acc5e4ced1a60cb090")
        self.assertEqual(commit.author.name, "Jane Doe")
        self.assertEqual(commit.committer.email, "john@doe.com")

    def testEditWithInvalidEncoding(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_file_content("README.md")
        self.assertEqual(f.size, 109)
        self.assertEqual(f.content, "UHlHaXRodWJJbnRlZ3JhdGlvblRlc3RzCj09PT09PT09PT09PT09PT09PT09\nPT09PQoKRHVtbXkgcmVwbyB0byBiZSBtb2RpZmllZCBieSBQeUdpdGh1Yidz\nIGludGVncmF0aW9uIHRlc3RzCg==\n")

        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException) as cm:
            f.edit("", "Not base64")
        self.assertEqual(cm.exception.args[2]["message"], "content is not valid Base64")

        self.assertEqual(f.content, "UHlHaXRodWJJbnRlZ3JhdGlvblRlc3RzCj09PT09PT09PT09PT09PT09PT09\nPT09PQoKRHVtbXkgcmVwbyB0byBiZSBtb2RpZmllZCBieSBQeUdpdGh1Yidz\nIGludGVncmF0aW9uIHRlc3RzCg==\n")

    def testDelete(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_file_content("hello.md")

        commit = f.delete("Delete hello.md")
        self.assertEqual(commit.sha, "7a408b2242ed53f057b7df08403c75c1d72f6635")

    def testDelete_allParameters(self):
        cc = self.g.get_repo("jacquev6/PyGithubIntegrationTests").create_file("hello.md", "Add hello.md", "SGVsbG8sIFdvcmxkIQ==")
        commit = cc.content.delete(
            "Delete hello.md",
            committer={"name": "John Doe", "email": "john@doe.com"},
            author={"name": "Jane Doe", "email": "jane@doe.com"},  # @todoAlpha Use a GitCommit.Author? Does the api accept an undocumented date?
        )
        self.assertEqual(commit.sha, "3bd4ab4a7dc9bcd03dc9a87b402c87eae9931e50")
        self.assertEqual(commit.author.name, "Jane Doe")
        self.assertEqual(commit.committer.email, "john@doe.com")
        # @todoAlpha Re-add attributes tree and parents in GitCommit
