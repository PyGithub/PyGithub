# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *

# @todoAlpha Test that the object of a ref is correct after editing it with a sha pointing to another type of object

class GitRefAttributes(TestCase):
    @Enterprise("electra")
    def testCommitRef(self):
        # @todoAlpha testTreeRef and testBlobRef?
        r = self.g.get_repo(("electra", "git-objects")).get_git_ref("refs/heads/develop")
        self.assertEqual(r.ref, "refs/heads/develop")
        self.assertEqual(r.object.type, "commit")
        self.assertEqual(r.object.message, "Create bar.md")


class GitRefEdit(TestCase):
    @Enterprise("electra")
    def testEdit(self):
        r = self.g.get_repo(("electra", "git-objects")).create_git_ref("refs/heads/ephemeral", "f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        r.edit("dd641d6c97b24778945a43a768b36c997610a8b6")
        r.delete()

    @Enterprise("electra")
    def testEdit_allParameters(self):
        r = self.g.get_repo(("electra", "git-objects")).create_git_ref("refs/heads/ephemeral", "dd641d6c97b24778945a43a768b36c997610a8b6")
        r.edit("f739e7ae2fd0e7b2bce99c073bcc7b57d713877e", force=True)
        r.delete()

    @Enterprise("electra")
    def testEdit_backward(self):
        r = self.g.get_repo(("electra", "git-objects")).create_git_ref("refs/heads/ephemeral", "dd641d6c97b24778945a43a768b36c997610a8b6")
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            r.edit("f739e7ae2fd0e7b2bce99c073bcc7b57d713877e")
        r.delete()
