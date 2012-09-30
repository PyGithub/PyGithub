# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import github
import sys

import Framework

atLeastPython26 = sys.hexversion >= 0x02060000


class Exceptions(Framework.TestCase):  # To stay compatible with Python 2.6, we do not use self.assertRaises with only one argument
    def testInvalidInput(self):
        try:
            self.g.get_user().create_key("Bad key", "xxx")
            self.fail("Should have raised")
        except github.GithubException, exception:
            self.assertEqual(exception.status, 422)
            self.assertEqual(
                exception.data,
                {
                    "errors": [
                        {
                            "code": "custom",
                            "field": "key",
                            "message": "key is invalid. It must begin with 'ssh-rsa' or 'ssh-dss'. Check that you're copying the public half of the key",
                            "resource": "PublicKey"
                        }
                    ],
                    "message": "Validation Failed"
                }
            )
            if atLeastPython26:
                self.assertEqual(str(exception), "422 {u\'message\': u\'Validation Failed\', u\'errors\': [{u\'field\': u\'key\', u\'message\': u\"key is invalid. It must begin with \'ssh-rsa\' or \'ssh-dss\'. Check that you\'re copying the public half of the key\", u\'code\': u\'custom\', u\'resource\': u\'PublicKey\'}]}")
            else:
                self.assertEqual(str(exception), "422 {\'message\': \'Validation Failed\', \'errors\': [{\'field\': \'key\', \'message\': \"key is invalid. It must begin with \'ssh-rsa\' or \'ssh-dss\'. Check that you\'re copying the public half of the key\", \'code\': \'custom\', \'resource\': \'PublicKey\'}]}")

    def testUnknownObject(self):
        try:
            self.g.get_user().get_repo("Xxx")
            self.fail("Should have raised")
        except github.GithubException, exception:
            self.assertEqual(exception.status, 404)
            self.assertEqual(exception.data, {"message": "Not Found"})
            if atLeastPython26:
                self.assertEqual(str(exception), "404 {u'message': u'Not Found'}")
            else:
                self.assertEqual(str(exception), "404 {'message': 'Not Found'}")

    def testUnknownUser(self):
        try:
            self.g.get_user("ThisUserShouldReallyNotExist")
            self.fail("Should have raised")
        except github.GithubException, exception:
            self.assertEqual(exception.status, 404)
            self.assertEqual(exception.data, {"message": "Not Found"})
            if atLeastPython26:
                self.assertEqual(str(exception), "404 {u'message': u'Not Found'}")
            else:
                self.assertEqual(str(exception), "404 {'message': 'Not Found'}")

    def testBadAuthentication(self):
        try:
            github.Github("BadUser", "BadPassword").get_user().login
            self.fail("Should have raised")
        except github.GithubException, exception:
            self.assertEqual(exception.status, 401)
            self.assertEqual(exception.data, {"message": "Bad credentials"})
            if atLeastPython26:
                self.assertEqual(str(exception), "401 {u'message': u'Bad credentials'}")
            else:
                self.assertEqual(str(exception), "401 {'message': 'Bad credentials'}")
