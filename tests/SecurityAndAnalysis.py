############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 karsten-wagner <39054096+karsten-wagner@users.noreply.github.com>#
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Caleb McCombs <caleb@mccombalot.net>                          #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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


class SecurityAndAnalysis(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("PyGithub/PyGithub")
        self.maxDiff = None

    def testAttributes(self):
        security_and_analysis = self.repo.security_and_analysis
        self.assertIsNone(security_and_analysis.advanced_security)
        self.assertEqual(security_and_analysis.dependabot_security_updates.status, "enabled")
        self.assertEqual(security_and_analysis.secret_scanning.status, "disabled")
        self.assertIsNone(security_and_analysis.secret_scanning_ai_detection)
        self.assertEqual(security_and_analysis.secret_scanning_push_protection.status, "disabled")
        self.assertEqual(security_and_analysis.secret_scanning_non_provider_patterns.status, "disabled")
        self.assertIsNone(security_and_analysis.secret_scanning_validity_checks)

    def testRepresentation(self):
        self.assertEqual(
            repr(self.repo.security_and_analysis),
            "SecurityAndAnalysis("
            'secret_scanning_validity_checks="None", '
            'secret_scanning_push_protection="SecurityAndAnalysisFeature(status="disabled")", '
            'secret_scanning_non_provider_patterns="SecurityAndAnalysisFeature(status="disabled")", '
            'secret_scanning="SecurityAndAnalysisFeature(status="disabled")", '
            'dependabot_security_updates="SecurityAndAnalysisFeature(status="enabled")", '
            'advanced_security="None")',
        )
