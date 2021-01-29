############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

import datetime

from . import Framework


class Hook(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.hook = self.g.get_user().get_repo("PyGithub").get_hook(257993)

    def testAttributes(self):
        self.assertTrue(self.hook.active)  # WTF
        self.assertEqual(self.hook.config, {"url": "http://foobar.com"})
        self.assertEqual(
            self.hook.created_at,
            datetime.datetime(2012, 5, 19, 6, 1, 45, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(self.hook.events, ["push"])
        self.assertEqual(self.hook.id, 257993)
        self.assertEqual(self.hook.last_response.status, "ok")
        self.assertEqual(self.hook.last_response.message, "OK")
        self.assertEqual(self.hook.last_response.code, 200)
        self.assertEqual(self.hook.name, "web")
        self.assertEqual(
            self.hook.updated_at,
            datetime.datetime(2012, 5, 29, 18, 49, 47, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            self.hook.url, "https://api.github.com/repos/jacquev6/PyGithub/hooks/257993"
        )
        self.assertEqual(
            self.hook.test_url,
            "https://api.github.com/repos/jacquev6/PyGithub/hooks/257993/tests",
        )
        self.assertEqual(
            self.hook.ping_url,
            "https://api.github.com/repos/jacquev6/PyGithub/hooks/257993/pings",
        )

        self.assertEqual(
            repr(self.hook),
            'Hook(url="https://api.github.com/repos/jacquev6/PyGithub/hooks/257993", id=257993)',
        )
        self.assertEqual(repr(self.hook.last_response), 'HookResponse(status="ok")')

    def testEditWithMinimalParameters(self):
        self.hook.edit("web", {"url": "http://foobar.com/hook"})
        self.assertEqual(self.hook.config, {"url": "http://foobar.com/hook"})
        self.assertEqual(
            self.hook.updated_at,
            datetime.datetime(2012, 5, 19, 5, 8, 16, tzinfo=datetime.timezone.utc),
        )

    def testDelete(self):
        self.hook.delete()

    def testTest(self):
        self.hook.test()  # This does not update attributes of hook

    def testPing(self):
        self.hook.ping()  # This does not update attributes of hook

    def testEditWithAllParameters(self):
        self.hook.edit("web", {"url": "http://foobar.com"}, events=["fork", "push"])
        self.assertEqual(self.hook.events, ["fork", "push"])
        self.hook.edit("web", {"url": "http://foobar.com"}, add_events=["push"])
        self.assertEqual(self.hook.events, ["fork", "push"])
        self.hook.edit("web", {"url": "http://foobar.com"}, remove_events=["fork"])
        self.assertEqual(self.hook.events, ["push"])
        self.hook.edit("web", {"url": "http://foobar.com"}, active=True)
        self.assertTrue(self.hook.active)
