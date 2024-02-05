############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Denis Blanchette <dblanchette@coveo.com>                      #
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
from datetime import datetime, timezone

from . import Framework


class SelfHostedActionsRunnerRegistrationToken(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("coveo")
        self.repo = self.org.get_repo("github-app")

    def testAttributes(self):
        token = self.repo.get_self_hosted_action_runner_registration_token()
        self.assertEqual("INSERTABEAUTIFULTOKENHERE", token.token)
        # the expiration date will be tz-aware with -04:00, which compares to UTC 4 hours later.
        self.assertEqual(
            datetime(2021, 7, 5, 17 + 4, 7, 52, 961000, tzinfo=timezone.utc),
            token.expires_at,  # 2021-07-05T17:07:52.961-04:00
        )
