# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import Framework

import datetime


class Event(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.event = self.g.get_user("jacquev6").get_events()[0]

    def testAttributes(self):
        self.assertEqual(self.event.actor.login, "jacquev6")
        self.assertEqual(self.event.created_at, datetime.datetime(2012, 5, 26, 10, 1, 39))
        self.assertEqual(self.event.id, "1556114751")
        self.assertEqual(self.event.org, None)
        self.assertEqual(self.event.payload, {u'commits': [{u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/5bb654d26dd014d36794acd1e6ecf3736f12aad7', u'sha': u'5bb654d26dd014d36794acd1e6ecf3736f12aad7', u'message': u'Implement the three authentication schemes', u'distinct': False, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/cb0313157bf904f2d364377d35d9397b269547a5', u'sha': u'cb0313157bf904f2d364377d35d9397b269547a5', u'message': u"Merge branch 'topic/Authentication' into develop", u'distinct': False, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/0cec0d25e606c023a62a4fc7cdc815309ebf6d16', u'sha': u'0cec0d25e606c023a62a4fc7cdc815309ebf6d16', u'message': u'Publish version 0.7', u'distinct': False, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'sha': u'ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'message': u"Merge branch 'develop'", u'distinct': False, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/3a3bf4763192ee1234eb0557628133e06f3dfc76', u'sha': u'3a3bf4763192ee1234eb0557628133e06f3dfc76', u'message': u"Merge branch 'master' into topic/RewriteWithGeneratedCode\n\nConflicts:\n\tgithub/Github.py\n\tgithub/Requester.py", u'distinct': True, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/608f17794664f61693a3dc05e6056fea8fbef0ff', u'sha': u'608f17794664f61693a3dc05e6056fea8fbef0ff', u'message': u'Restore some form of Authorization header in replay data', u'distinct': True, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/2c04b8adbd91d38eef4f0767337ab7a12b2f684b', u'sha': u'2c04b8adbd91d38eef4f0767337ab7a12b2f684b', u'message': u'Allow test without pre-set-up Github', u'distinct': True, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/5b97389988b6fe43e15a079702f6f1671257fb28', u'sha': u'5b97389988b6fe43e15a079702f6f1671257fb28', u'message': u'Test three authentication schemes', u'distinct': True, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/12747613c5ec00deccf296b8619ad507f7050475', u'sha': u'12747613c5ec00deccf296b8619ad507f7050475', u'message': u'Test Issue.getComments', u'distinct': True, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/2982fa96c5ca75abe717d974d83f9135d664232e', u'sha': u'2982fa96c5ca75abe717d974d83f9135d664232e', u'message': u'Test the new Repository.full_name attribute', u'distinct': True, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/619eae8d51c5988f0d2889fc767fa677438ba95d', u'sha': u'619eae8d51c5988f0d2889fc767fa677438ba95d', u'message': u'Improve coverage of AuthenticatedUser', u'distinct': True, u'author': {u'name': u'Vincent Jacques', u'email': u'vincent@vincent-jacques.net'}}], u'head': u'619eae8d51c5988f0d2889fc767fa677438ba95d', u'push_id': 80673538, u'ref': u'refs/heads/topic/RewriteWithGeneratedCode', u'size': 11})
        self.assertEqual(self.event.public, True)
        self.assertEqual(self.event.repo.name, "jacquev6/PyGithub")
        self.assertEqual(self.event.type, "PushEvent")
