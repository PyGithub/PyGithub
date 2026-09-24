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
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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


class Issue33(Framework.TestCase):  # https://github.com/jacquev6/PyGithub/issues/33
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_user("openframeworks").get_repo("openFrameworks")

    def testOpenIssues(self):
        # reduce the size of the record data file by executing the following:
        # cat -n tests/ReplayData/Issue33.testOpenIssues.txt | while read -r lineno line
        # do
        #   if [[ $(( lineno % 11 )) -eq 10 ]]
        #   then
        #     jq -c "[.[] | { id: .id }]" <<< "$line"
        #   else
        #     echo "$line"
        #   fi
        # done > tests/ReplayData/Issue33.testOpenIssues.txt.new
        # mv tests/ReplayData/Issue33.testOpenIssues.txt.new tests/ReplayData/Issue33.testOpenIssues.txt
        self.assertEqual(len(list(self.repo.get_issues())), 338)

    def testClosedIssues(self):
        # reduce the size of the record data file by executing the following:
        # cat -n tests/ReplayData/Issue33.testClosedIssues.txt | while read -r lineno line
        # do
        #   if [[ $(( lineno % 11 )) -eq 10 ]]
        #   then
        #     jq -c "[.[] | { id: .id }]" <<< "$line"
        #   else
        #     echo "$line"
        #   fi
        # done > tests/ReplayData/Issue33.testClosedIssues.txt.new
        # mv tests/ReplayData/Issue33.testClosedIssues.txt.new tests/ReplayData/Issue33.testClosedIssues.txt
        self.assertEqual(len(list(self.repo.get_issues(state="closed"))), 950)
