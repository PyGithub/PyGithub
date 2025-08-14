############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Matthew Neal <meneal@matthews-mbp.raleigh.ibm.com>            #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2016 Sam Corbett <sam.corbett@cloudsoftcorp.com>                   #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Olof-Joachim Frahm (欧雅福) <olof@macrolet.net>                  #
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

from . import Framework


class PullRequest1684(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.user = self.g.get_user("ReDASers")
        self.repo = self.user.get_repo("Phishing-Detection")

    def testGetRunners(self):
        runners = self.repo.get_self_hosted_runners()
        self.assertEqual(19, runners.totalCount)
        runner = runners[0]
        self.assertEqual(1363, runner.id)
        self.assertEqual("windows", runner.os)
        self.assertEqual("0D80B14DC506", runner.name)
        self.assertEqual("offline", runner.status)
        self.assertFalse(runner.busy)
        labels = runner.labels
        self.assertEqual(3, len(labels))
        self.assertEqual("self-hosted", labels[0]["name"])
        self.assertEqual("Windows", labels[1]["name"])
        self.assertEqual("X64", labels[2]["name"])

    def testDeleteRunnerObject(self):
        runners = self.repo.get_self_hosted_runners()
        initial_length = runners.totalCount
        runner_to_delete = runners[0]

        result = self.repo.remove_self_hosted_runner(runner_to_delete)
        self.assertTrue(result)

        runners = self.repo.get_self_hosted_runners()
        ids = [runner.id for runner in self.repo.get_self_hosted_runners()]
        self.assertEqual(initial_length - 1, runners.totalCount)
        self.assertNotIn(runner_to_delete.id, ids)

    def testDeleteRunnerId(self):
        ids = [runner.id for runner in self.repo.get_self_hosted_runners()]
        id_to_delete = ids[0]

        result = self.repo.remove_self_hosted_runner(id_to_delete)
        self.assertTrue(result)

        ids = [runner.id for runner in self.repo.get_self_hosted_runners()]
        self.assertNotIn(id_to_delete, ids)
