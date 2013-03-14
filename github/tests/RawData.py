# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import Framework

class RawData(Framework.TestCase):
    jacquev6RawData = {
        u'disk_usage': 13812,
        u'private_gists': 5,
        u'public_repos': 21,
        u'subscriptions_url': u'https://api.github.com/users/jacquev6/subscriptions',
        u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225',
        u'hireable': False,
        u'id': 327146,
        u'followers_url': u'https://api.github.com/users/jacquev6/followers',
        u'following_url': u'https://api.github.com/users/jacquev6/following',
        u'collaborators': 1,
        u'total_private_repos': 4,
        u'blog': u'http://vincent-jacques.net',
        u'followers': 22,
        u'location': u'Paris, France',
        u'type': u'User',
        u'email': u'vincent@vincent-jacques.net',
        u'bio': u'',
        u'gists_url': u'https://api.github.com/users/jacquev6/gists{/gist_id}',
        u'owned_private_repos': 4,
        u'company': u'Criteo',
        u'events_url': u'https://api.github.com/users/jacquev6/events{/privacy}',
        u'html_url': u'https://github.com/jacquev6',
        u'updated_at': u'2013-03-12T22:13:32Z',
        u'plan': {
            u'collaborators': 1,
            u'name': u'micro',
            u'private_repos': 5,
            u'space': 614400,
        },
        u'received_events_url': u'https://api.github.com/users/jacquev6/received_events',
        u'starred_url': u'https://api.github.com/users/jacquev6/starred{/owner}{/repo}',
        u'public_gists': 2,
        u'name': u'Vincent Jacques',
        u'organizations_url': u'https://api.github.com/users/jacquev6/orgs',
        u'url': u'https://api.github.com/users/jacquev6',
        u'created_at': u'2010-07-09T06:10:06Z',
        u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png',
        u'repos_url': u'https://api.github.com/users/jacquev6/repos',
        u'following': 38,
        u'login': u'jacquev6',
    }

    planRawData = {
        u'collaborators': 1,
        u'name': u'micro',
        u'private_repos': 5,
        u'space': 614400,
    }

    def testCompletedObject(self):
        user = self.g.get_user("jacquev6")
        self.assertTrue(user._CompletableGithubObject__completed)
        self.assertEqual(user.raw_data, RawData.jacquev6RawData)

    def testNotYetCompletedObject(self):
        user = self.g.get_user().get_repo("PyGithub").owner
        self.assertFalse(user._CompletableGithubObject__completed)
        self.assertEqual(user.raw_data, RawData.jacquev6RawData)
        self.assertTrue(user._CompletableGithubObject__completed)

    def testNonCompletableObject(self):
        plan = self.g.get_user().plan
        self.assertEqual(plan.raw_data, RawData.planRawData)
