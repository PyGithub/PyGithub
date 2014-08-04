# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class GitTagAttributes(TestCase):
    @Enterprise("electra")
    def test(self):
        t = self.g.get_repo(("electra", "git-objects")).get_git_tag("b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        self.assertEqual(t.message, "This is a tag")
        self.assertEqual(t.object.sha, "f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        self.assertEqual(t.object.type, "commit")
        self.assertIsInstance(t.object, PyGithub.Blocking.GitCommit.GitCommit)
        self.assertEqual(t.sha, "b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        self.assertEqual(t.tag, "heavy-tag")
        self.assertEqual(t.tagger.name, "John Doe")
        self.assertEqual(t.type, None)


class GitTagUpdate(TestCase):
    @Enterprise("electra")
    def testThroughLazyCompletion(self):
        r = self.g.get_repo(("electra", "git-objects")).create_git_ref(ref="refs/tests/tag_ref", sha="b55a47efb4f8c891b6719a3d85a80c7f875e33ec")
        t = r.object
        self.assertEqual(t.tagger.name, "John Doe")
        r.delete()
