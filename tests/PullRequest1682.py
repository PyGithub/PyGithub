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


class PullRequest1682(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("ReDASers/Phishing-Detection")

    def test_no_parameters(self):
        runs = self.repo.get_workflow_runs()
        self.assertEqual(313400760, runs[0].id)

    def test_object_parameters(self):
        branch = self.repo.get_branch("adversary")
        runs = self.repo.get_workflow_runs(branch=branch)
        self.assertEqual(204764033, runs[0].id)
        self.assertEqual(1, runs.totalCount)

        user = self.g.get_user("shahryarabaki")
        runs = self.repo.get_workflow_runs(actor=user)
        self.assertEqual(28372848, runs[0].id)

    def test_string_parameters(self):
        runs = self.repo.get_workflow_runs(actor="xzhou29")
        self.assertEqual(226142695, runs[0].id)

        runs = self.repo.get_workflow_runs(branch="API_Flatten")
        self.assertEqual(287515889, runs[0].id)

        runs = self.repo.get_workflow_runs(event="pull_request")
        self.assertEqual(298867254, runs[0].id)

        runs = self.repo.get_workflow_runs(status="failure")
        self.assertEqual(292080359, runs[0].id)
