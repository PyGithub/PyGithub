############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Nicolas Agustín Torres <nicolastrres@gmail.com>               #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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


class RequiredStatusChecks(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.required_status_checks = (
            self.g.get_repo("jacquev6/PyGithub", lazy=True).get_branch("integrations").get_required_status_checks()
        )

    def testAttributes(self):
        self.assertEqual(len(self.required_status_checks.checks), 1)
        self.assertEqual(self.required_status_checks.checks[0].context, "continuous-integration/travis-ci")
        self.assertEqual(self.required_status_checks.checks[0].app_id, 123)
        self.assertEqual(
            self.required_status_checks.contexts_url,
            "https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_status_checks/contexts",
        )
        self.assertEqual(self.required_status_checks.enforcement_level, "non_admins")
        self.assertTrue(self.required_status_checks.strict)
        self.assertEqual(self.required_status_checks.contexts, ["foo/bar"])
        self.assertEqual(
            self.required_status_checks.url,
            "https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_status_checks",
        )
        self.assertEqual(
            self.required_status_checks.__repr__(),
            'RequiredStatusChecks(url="https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_status_checks", strict=True)',
        )
