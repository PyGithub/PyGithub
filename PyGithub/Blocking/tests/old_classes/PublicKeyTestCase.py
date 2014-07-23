# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import PyGithub.Blocking

import PyGithub.Blocking.tests.Framework as Framework


class PublicKeyTestCase(Framework.SimpleLoginTestCase):
    def testDeleteRepositoryKey(self):
        key = self.g.get_repo("jacquev6/CodingDojos").get_key(7229238)
        self.assertEqual(key.url, "https://api.github.com/user/keys/7229238")  # @todoSomeday Open an issue to GitHub so that they return "https://api.github.com/repos/jacquev6/CodingDojos/keys/7229238"
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            key.delete()
