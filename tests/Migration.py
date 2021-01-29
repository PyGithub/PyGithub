############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Christopher Wilcox <git@crwilcox.com>                         #
# Copyright 2015 Dan Vanderkam <danvdk@gmail.com>                              #
# Copyright 2015 Enix Yu <enix223@163.com>                                     #
# Copyright 2015 Kyle Hornberg <khornberg@users.noreply.github.com>            #
# Copyright 2015 Uriel Corfa <uriel@corfa.fr>                                  #
# Copyright 2016 @tmshn <tmshn@r.recruit.co.jp>                                #
# Copyright 2016 Enix Yu <enix223@163.com>                                     #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Jimmy Zelinskie <jimmyzelinskie@gmail.com>                    #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Hayden Fuss <wifu1234@gmail.com>                              #
# Copyright 2018 Iraquitan Cordeiro Filho <iraquitanfilho@gmail.com>           #
# Copyright 2018 Jacopo Notarstefano <jacopo.notarstefano@gmail.com>           #
# Copyright 2018 Maarten Fonville <mfonville@users.noreply.github.com>         #
# Copyright 2018 Mateusz Loskot <mateusz@loskot.net>                           #
# Copyright 2018 Raihaan <31362124+res0nance@users.noreply.github.com>         #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2018 Victor Granic <vmg@boreal321.com>                             #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 Will Yardley <wyardley@users.noreply.github.com>              #
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

import github

from . import Framework


class Migration(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.user = self.g.get_user()
        self.migration = self.user.get_migrations()[0]

    def testAttributes(self):
        self.assertEqual(self.migration.id, 25320)
        self.assertEqual(self.migration.owner.login, "singh811")
        self.assertEqual(self.migration.guid, "608bceae-b790-11e8-8b43-4e3cb0dd56cc")
        self.assertEqual(self.migration.state, "exported")
        self.assertEqual(self.migration.lock_repositories, False)
        self.assertEqual(self.migration.exclude_attachments, False)
        self.assertEqual(len(self.migration.repositories), 1)
        self.assertEqual(self.migration.repositories[0].name, "sample-repo")
        self.assertEqual(
            self.migration.url, "https://api.github.com/user/migrations/25320"
        )
        self.assertEqual(
            self.migration.created_at,
            datetime.datetime(
                2018, 9, 14, 1, 35, 35, tzinfo=datetime.timezone(datetime.timedelta(0))
            ),
        )
        self.assertEqual(
            self.migration.updated_at,
            datetime.datetime(2018, 9, 14, 1, 35, 46, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            repr(self.migration),
            'Migration(url="https://api.github.com/user/migrations/25320", state="exported")',
        )

    def testGetArchiveUrlWhenNotExported(self):
        self.assertRaises(
            github.UnknownObjectException, lambda: self.migration.get_archive_url()
        )

    def testGetStatus(self):
        self.assertEqual(self.migration.get_status(), "exported")

    def testGetArchiveUrlWhenExported(self):
        self.assertEqual(
            self.migration.get_archive_url(),
            "https://github-cloud.s3.amazonaws.com/migration/25320/24575?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAISTNZFOVBIJMK3TQ%2F20180913%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180913T201100Z&X-Amz-Expires=300&X-Amz-Signature=a0aeb638facd0c78c1ed3ca86022eddbee91e5fe1bb48ee830f54b8b7b305026&X-Amz-SignedHeaders=host&actor_id=41840111&response-content-disposition=filename%3D608bceae-b790-11e8-8b43-4e3cb0dd56cc.tar.gz&response-content-type=application%2Fx-gzip",
        )

    def testDelete(self):
        self.assertEqual(self.migration.delete(), None)

    def testGetArchiveUrlWhenDeleted(self):
        self.assertRaises(
            github.UnknownObjectException, lambda: self.migration.get_archive_url()
        )

    def testUnlockRepo(self):
        self.assertEqual(self.migration.unlock_repo("sample-repo"), None)
