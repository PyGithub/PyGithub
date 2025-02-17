############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Hayden Fuss <wifu1234@gmail.com>                              #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
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


class SourceImport(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.user = self.g.get_user("brix4dayz")
        self.repo = self.user.get_repo("source-import-test")
        self.source_import = self.repo.get_source_import()

    def testAttributes(self):
        self.assertEqual(self.source_import.authors_count, 1)
        self.assertEqual(
            self.source_import.authors_url,
            "https://api.github.com/repos/brix4dayz/source-import-test/import/authors",
        )
        self.assertIsNone(self.source_import.commit_count)
        self.assertIsNone(self.source_import.error_message)
        self.assertIsNone(self.source_import.failed_step)
        self.assertEqual(self.source_import.has_large_files, False)
        self.assertEqual(
            self.source_import.html_url,
            "https://github.com/brix4dayz/source-import-test/import",
        )
        self.assertIsNone(self.source_import.import_percent)
        self.assertEqual(self.source_import.large_files_count, 0)
        self.assertEqual(self.source_import.large_files_size, 0)
        self.assertIsNone(self.source_import.message)
        self.assertIsNone(self.source_import.project_choices)
        self.assertIsNone(self.source_import.push_percent)
        self.assertEqual(
            self.source_import.repository_url,
            "https://api.github.com/repos/brix4dayz/source-import-test",
        )
        self.assertEqual(self.source_import.status, "complete")
        self.assertEqual(self.source_import.status_text, "Done")
        self.assertIsNone(self.source_import.svc_root)
        self.assertIsNone(self.source_import.svn_root)
        self.assertIsNone(self.source_import.tfvc_project)
        self.assertEqual(
            self.source_import.url,
            "https://api.github.com/repos/brix4dayz/source-import-test/import",
        )
        self.assertEqual(self.source_import.use_lfs, "undecided")
        self.assertEqual(self.source_import.vcs, "mercurial")
        self.assertEqual(self.source_import.vcs_url, "https://bitbucket.org/hfuss/source-import-test")

        self.assertEqual(
            self.source_import.__repr__(),
            'SourceImport(vcs_url="https://bitbucket.org/hfuss/source-import-test", url="https://api.github.com/repos/brix4dayz/source-import-test/import", status="complete", repository_url="https://api.github.com/repos/brix4dayz/source-import-test")',
        )

    def testUpdate(self):
        # The real test is that update() method passes the header
        update_ret = self.source_import.update()
        self.assertTrue(update_ret)
        self.assertEqual(self.source_import.status, "complete")
