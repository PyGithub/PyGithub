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

import github

from . import Framework


class Issue80(Framework.BasicTestCase):  # https://github.com/jacquev6/PyGithub/issues/80
    def testIgnoreHttpsFromGithubEnterprise(self):
        g = github.Github(auth=self.oauth_token, base_url="http://my.enterprise.com/some/prefix")  # http here
        org = g.get_organization("BeaverSoftware")
        self.assertEqual(org.url, "https://my.enterprise.com/some/prefix/orgs/BeaverSoftware")  # https returned
        self.assertListKeyEqual(
            org.get_repos(), lambda r: r.name, ["FatherBeaver", "TestPyGithub"]
        )  # But still http in second request based on org.url

    def testIgnoreHttpsFromGithubEnterpriseWithPort(self):
        g = github.Github(
            auth=self.oauth_token,
            base_url="http://my.enterprise.com:1234/some/prefix",
        )  # http here
        org = g.get_organization("BeaverSoftware")
        self.assertEqual(org.url, "https://my.enterprise.com:1234/some/prefix/orgs/BeaverSoftware")  # https returned
        self.assertListKeyEqual(
            org.get_repos(), lambda r: r.name, ["FatherBeaver", "TestPyGithub"]
        )  # But still http in second request based on org.url
