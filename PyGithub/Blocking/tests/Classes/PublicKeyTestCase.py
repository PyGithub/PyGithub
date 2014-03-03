# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import PyGithub.Blocking

import PyGithub.Blocking.tests.Framework as Framework


class PublicKeyTestCase(Framework.SimpleLoginTestCase):
    def testAttributes(self):
        key = self.g.get_authenticated_user().get_key(7229148)
        self.assertEqual(key.id, 7229148)
        self.assertEqual(key.key, "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkQih2DtSwBzLUtSNYEKULlI5M1qa6vnq42xt9qZpkLav3G9eD/GqJRST+zZMsyfpP62PtiYKXJdLJX2MQIzUgI2PzNy+iMy+ldiTEABYEOCa+BH9+x2R5xXGlmmCPblpamx3kstGtCTa3LSkyIvxbt5vjbXCyThhJaSKyh+42Uedcz7l0y/TODhnkpid/5eiBz6k0VEbFfhM6h71eBdCFpeMJIhGaPTjbKsEjXIK0SRe0v0UQnpXJQkhAINbm+q/2yjt7zwBF74u6tQjRqJK7vQO2k47ZmFMAGeIxS6GheI+JPmwtHkxvfaJjy2lIGX+rt3lkW8xEUxiMTlxeh+0R")
        self.assertEqual(key.title, "vincent@test")
        self.assertEqual(key.url, "https://api.github.com/user/keys/7229148")
        self.assertEqual(key.verified, True)

    def testDeleteUserKey(self):
        key = self.g.get_authenticated_user().get_key(7229148)
        key.delete()

    def testDeleteRepositoryKey(self):
        key = self.g.get_repo("jacquev6/CodingDojos").get_key(7229238)
        self.assertEqual(key.url, "https://api.github.com/user/keys/7229238")  # @todoSomeday Open an issue to GitHub so that they return "https://api.github.com/repos/jacquev6/CodingDojos/keys/7229238"
        with self.assertRaises(PyGithub.Blocking.ObjectNotFoundException):
            key.delete()
