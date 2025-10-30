############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2020 Victor Zeng <zacker150@users.noreply.github.com>              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Trim21 <trim21.me@gmail.com>                                  #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

from __future__ import annotations

from . import Framework


class SelfHostedActionsRunner(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.user = self.g.get_user("ReDASers")
        self.repo = self.user.get_repo("Phishing-Detection")

    def testAttributes(self):
        runner = self.repo.get_self_hosted_runner(2217)
        self.assertFalse(runner.busy)
        self.assertIsNone(runner.ephemeral)
        self.assertEqual(runner.id, 2217)
        self.assertEqual(
            runner.labels,
            [
                {"id": 1, "name": "self-hosted", "type": "read-only"},
                {"id": 3, "name": "X64", "type": "read-only"},
                {"id": 4, "name": "Linux", "type": "read-only"},
            ],
        )
        self.assertEqual(runner.name, "4306125c7c84")
        self.assertEqual(runner.os, "linux")
        self.assertEqual(runner.name, "4306125c7c84")
        self.assertIsNone(runner.runner_group_id)
        self.assertEqual(runner.status, "offline")
        labels = runner.labels
        self.assertEqual(len(labels), 3)
        self.assertEqual(labels[0]["name"], "self-hosted")
        self.assertEqual(labels[1]["name"], "X64")
        self.assertEqual(labels[2]["name"], "Linux")
