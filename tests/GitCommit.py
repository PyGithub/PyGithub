############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Simon <spam@esemi.ru>                                         #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Tim Gates <tim.gates@iress.com>                               #
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

from datetime import datetime, timezone

from . import Framework


class GitCommit(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.commit = self.g.get_repo("PyGithub/PyGithub").get_git_commit("3d84a47a88f6757514cb3ee91b829f53ba09e7e0")

    def testAttributes(self):
        self.assertEqual(self.commit.author.name, "Enrico Minack")
        self.assertEqual(self.commit.author.email, "github@enrico.minack.dev")
        self.assertEqual(self.commit.author.date, datetime(2024, 12, 18, 10, 40, 19, tzinfo=timezone.utc))
        self.assertIsNone(self.commit.comment_count)
        self.assertEqual(self.commit.committer.name, "GitHub")
        self.assertEqual(self.commit.committer.email, "noreply@github.com")
        self.assertEqual(self.commit.committer.date, datetime(2024, 12, 18, 10, 40, 19, tzinfo=timezone.utc))
        self.assertEqual(
            self.commit.html_url, "https://github.com/PyGithub/PyGithub/commit/3d84a47a88f6757514cb3ee91b829f53ba09e7e0"
        )
        self.assertIsNone(self.commit.id)
        self.assertEqual(
            self.commit.message,
            "Get branches where commit is head (#3083)\n\nImplements `GET\r\n/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head`\r\n\r\nhttps://docs.github.com/rest/commits/commits#list-branches-for-head-commit",
        )
        self.assertEqual(self.commit.node_id, "C_kwDOADYVqtoAKDNkODRhNDdhODhmNjc1NzUxNGNiM2VlOTFiODI5ZjUzYmEwOWU3ZTA")
        self.assertEqual(len(self.commit.parents), 1)
        self.assertEqual(self.commit.parents[0].sha, "a50ae51b2c351b889055568bcaa9ab6000f1677f")
        self.assertEqual(self.commit.sha, "3d84a47a88f6757514cb3ee91b829f53ba09e7e0")
        self.assertIsNone(self.commit.timestamp)
        self.assertEqual(self.commit.tree.sha, "d9e2468f2db35e158eb65e91b249dde20ca88c86")
        self.assertIsNone(self.commit.tree_id)
        self.assertEqual(
            self.commit.url,
            "https://api.github.com/repos/PyGithub/PyGithub/git/commits/3d84a47a88f6757514cb3ee91b829f53ba09e7e0",
        )
        self.assertEqual(repr(self.commit), 'GitCommit(sha="3d84a47a88f6757514cb3ee91b829f53ba09e7e0")')
        self.assertEqual(repr(self.commit.author), 'GitAuthor(name="Enrico Minack")')
        self.assertEqual(
            self.commit.verification.payload,
            "tree d9e2468f2db35e158eb65e91b249dde20ca88c86\n"
            "parent a50ae51b2c351b889055568bcaa9ab6000f1677f\n"
            "author Enrico Minack <github@enrico.minack.dev> 1734518419 +0100\n"
            "committer GitHub <noreply@github.com> 1734518419 +0100\n"
            "\n"
            "Get branches where commit is head (#3083)\n"
            "\n"
            "Implements `GET\r\n"
            "/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head`\r\n"
            "\r\n"
            "https://docs.github.com/rest/commits/commits#list-branches-for-head-commit",
        )
        self.assertEqual(self.commit.verification.reason, "valid")
        self.assertEqual(
            self.commit.verification.signature,
            "-----BEGIN PGP SIGNATURE-----\n"
            "\n"
            "wsFcBAABCAAQBQJnYqaTCRC1aQ7uu5UhlAAAp3wQAGPaBPEC4WlL9rvDA6G+kaRZ\n"
            "+296Qb/jRjZX6joS//aQq5rjHKn//qTv13lTBQnM1a7gFfvA7TSoxNsoqzkk6DAe\n"
            "ME7qoSMYWl+GdvXsySo4ksGbFN0LL77CSmJyFXRXB5TIjUJT7dbjTkjE9/4zcfq4\n"
            "mR8D57GowX7YgqUeRzf8+5zz7ySJ9hAMcF/n+OJjLiew0RFp3hQBSFOr/1B4YJbL\n"
            "0Ln9i/DH9KBhwIUnc68k04GxVtAMaS7X0SOVbezylaBlQyF2JV3bDbb38h77KPJ1\n"
            "ln0qPi+hamZu43pbKGNuj1BjiLsavKHx5v4EYQ5gUzBDLlUMvUUmFNb4lrbulmSw\n"
            "g2Fr13dbjRmgHa5Lj7VAay3xXFwdTGNH3o04uefpvZ/6sRB1e9fP4VR5UVECZLe0\n"
            "D5Au4VSA7usgOLdDjxoG6mBOzEY7vWkbCmbFxB1Q1tWY53ecw9NJ15p8NAtH2dR1\n"
            "+xUeNzDeQMHS4FIZ/Z6c6RuUyusK7fRAxddhUoXu4KVEwbdEV9qsEKDqtW4eUMXX\n"
            "QQBtkxzZkL1lMz4UTXnHwG5jSbHVz3tSyYYpQYZPO2zE/TOrfuZzYGOZ2g9vreNt\n"
            "Ta8u/MMtvhguLV1qCEqAgzDQo0Kx+dc+ueNt/ruCuhWxn0jl0LMX4qvmZX1d2X58\n"
            "J9ub7sFcpLb1gsueYKQ6\n"
            "=RKbN\n"
            "-----END PGP SIGNATURE-----\n",
        )
        self.assertEqual(self.commit.verification.verified, True)
        self.assertEqual(self.commit.verification.verified_at, datetime(2024, 12, 18, 10, 45, 21, tzinfo=timezone.utc))
