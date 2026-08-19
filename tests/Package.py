############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Henkhogan <henkhogan@gmail.com>                               #
# Copyright 2025 Harrison Boyd <8950185+hboyd2003@users.noreply.github.com>    #
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
from datetime import datetime, timezone

from github.NamedUser import NamedUser

import github

from github import GithubException, Repository

from github.Package import PackageType
from github.PackageVersion import PackageVersion
from . import Framework


class Package(Framework.TestCase):
    def setUp(self):
        self.tokenAuthMode = True
        super().setUp()
        self.authUser = self.g.get_user()
        self.user = self.g.get_user_by_id(1024025)
        self.user.complete()
        self.org = self.g.get_organization("test-org")
        self.package = self.authUser.get_package(package_type=PackageType.CONTAINER, package_name="test-pkg5")

        # Complete them now so we can verify their output
        self.user.complete()
        self.org.complete()
        self.package.complete()

    def testListVersions(self):
        expected_versions = {
            406855102: {
                "name": "sha256:424cf437ed23c9f9a3c35e81e2de7add978eacd6309d1e2fc768a7ca91085f45",
                "url": "https://api.github.com/users/test-user/packages/container/test-pkg5/versions/406855102",
                "package_html_url": "https://github.com/users/test-user/packages/container/package/test-pkg5",
                "created_at": datetime(2025, 5, 1, 23, 4, 10, tzinfo=timezone.utc),
                "updated_at": datetime(2025, 5, 3, 1, 5, 57, tzinfo=timezone.utc),
                "html_url": "https://github.com/users/test-user/packages/container/test-pkg5/406855102",
                "metadata": {"package_type": "container", "container": {"tags": ["v1.10.0-alpha.0-88-g42f9b84"]}}
            },
            406855100: {
                "name": "sha256:3309a86716a26f8c73f53d8ec7acee5cfabdbb4b6c87527559b6d85540a8956f",
                "url": "https://api.github.com/users/test-user/packages/container/test-pkg5/versions/406855100",
                "package_html_url": "https://github.com/users/test-user/packages/container/package/test-pkg5",
                "created_at": datetime(2025, 5, 1, 23, 4, 9, tzinfo=timezone.utc),
                "updated_at": datetime(2025, 5, 3, 1, 5, 57, tzinfo=timezone.utc),
                "html_url": "https://github.com/users/test-user/packages/container/test-pkg5/406855100",
                "metadata": {"package_type": "container", "container": {"tags": []}}
            },
            406855098: {
                "name": "sha256:31a3eb5bd9c14406c6cb7c65b81430a040c7f75b85300c9b01dd123065543425",
                "url": "https://api.github.com/users/test-user/packages/container/test-pkg5/versions/406855098",
                "package_html_url": "https://github.com/users/test-user/packages/container/package/test-pkg5",
                "created_at": datetime(2025, 5, 1, 23, 4, 9, tzinfo=timezone.utc),
                "updated_at": datetime(2025, 5, 3, 1, 5, 57, tzinfo=timezone.utc),
                "html_url": "https://github.com/users/test-user/packages/container/test-pkg5/406855098",
                "metadata": {"package_type": "container", "container": {"tags": []}}
            },
            388378656: {
                "name": "sha256:7b05418cacb50f036159b662b2d12b305743691dca2e58188100fce5c0b9843a",
                "url": "https://api.github.com/users/test-user/packages/container/test-pkg5/versions/388378656",
                "package_html_url": "https://github.com/users/test-user/packages/container/package/test-pkg5",
                "created_at": datetime(2025, 4, 3, 23, 39, 46, tzinfo=timezone.utc),
                "updated_at": datetime(2025, 5, 3, 1, 5, 57, tzinfo=timezone.utc),
                "html_url": "https://github.com/users/test-user/packages/container/test-pkg5/388378656",
                "metadata": {"package_type": "container", "container": {"tags": ["v1.9.0-37-ga89d960", "v1.9.0-36-g792f5ca-dirty"]}}
            },
            388310993: {
                "name": "sha256:424c453e1258136e16a1434b07501da83eef402855dcec05d305a90f9b1814b2",
                "url": "https://api.github.com/users/test-user/packages/container/test-pkg5/versions/388310993",
                "package_html_url": "https://github.com/users/test-user/packages/container/package/test-pkg5",
                "created_at": datetime(2025, 4, 3, 20, 50, 20, tzinfo=timezone.utc),
                "updated_at": datetime(2025, 5, 3, 1, 5, 57, tzinfo=timezone.utc),
                "html_url": "https://github.com/users/test-user/packages/container/test-pkg5/388310993",
                "metadata": {"package_type": "container", "container": {"tags": []}}
            }
        }

        versions = self.package.list_versions()
        for version in versions:
            assert isinstance(version, PackageVersion)
            self.assertIn(version.id, expected_versions)
            expected_version = expected_versions[version.id]
            self.assertEqual(version.name, expected_version["name"])
            self.assertEqual(version.url, expected_version["url"])
            self.assertEqual(version.package_html_url, expected_version["package_html_url"])
            self.assertEqual(version.created_at, expected_version["created_at"])
            self.assertEqual(version.updated_at, expected_version["updated_at"])
            self.assertEqual(version.html_url, expected_version["html_url"])
            self.assertEqual(version.metadata, expected_version["metadata"])

    def testGetVersion(self):
        version = self.package.get_version(package_version_id=406855102)

        self.assertIsInstance(version, PackageVersion)
        self.assertIsNotNone(version.url)
        self.assertFalse(version.completed)
        self.assertEqual(version.id, 406855102)
        self.assertEqual(version.name, "sha256:424cf437ed23c9f9a3c35e81e2de7add978eacd6309d1e2fc768a7ca91085f45")
        self.assertEqual(version.url, "https://api.github.com/users/test-user/packages/container/test-pkg5/versions/406855102")
        self.assertEqual(version.package_html_url, "https://github.com/users/test-user/packages/container/package/test-pkg5")
        self.assertEqual(version.created_at, datetime(2025, 5, 1, 23, 4, 10, tzinfo=timezone.utc))
        self.assertEqual(version.updated_at, datetime(2025, 5, 3, 1, 5, 57, tzinfo=timezone.utc))
        self.assertEqual(version.html_url, "https://github.com/users/test-user/packages/container/test-pkg5/406855102")
        self.assertEqual(version.metadata, {'container': {'tags': ['v1.10.0-alpha.0-88-g42f9b84']}, 'package_type': 'container'})

    def testAuthUserGetPackages(self):
        expected_packages = {
    7931961: {
        "name": "test-pkg5",
        "package_type": "container",
        "owner_id": 1024025,
        "visibility": "private",
        "url": "https://api.github.com/users/test-user/packages/container/test-pkg5",
        "created_at": datetime(2025, 4, 4, 4, 59, 42, tzinfo=timezone.utc),
        "updated_at": datetime(2025, 4, 4, 4, 59, 42, tzinfo=timezone.utc),
        "repository_id": None,
        "html_url": "https://github.com/users/test-user/packages/container/package/test-pkg5"
    },
    7948400: {
        "name": "test-pkg6",
        "package_type": "container",
        "owner_id": 1024025,
        "visibility": "public",
        "url": "https://api.github.com/users/test-user/packages/container/test-pkg5",
        "created_at": datetime(2025, 4, 8, 0, 44, 43, tzinfo=timezone.utc),
        "updated_at": datetime(2025, 4, 27, 0, 11, 16, tzinfo=timezone.utc),
        "repository_id": 962289158,
        "html_url": "https://github.com/users/test-user/packages/container/package/test-pkg5"
    }
}
        packages = self.authUser.get_packages(package_type=PackageType.CONTAINER)
        packages = packages.get_page(1)

        self.assertEqual(len(packages), len(expected_packages))
        for package in packages:
            assert isinstance(package, github.Package.Package)
            self.assertIsNotNone(package.url)
            self.assertFalse(package.completed)
            expectedPackage = expected_packages[package.id]
            self.assertEqual(package.name, expectedPackage["name"])
            self.assertEqual(package.package_type , expectedPackage[ "package_type"])
            assert isinstance(package.owner, NamedUser)
            self.assertEqual(package.owner.id, expectedPackage["owner_id"])
            self.assertEqual(package.visibility , expectedPackage[ "visibility"])
            self.assertEqual(package.url , expectedPackage[ "url"])
            self.assertEqual(package.created_at , expectedPackage[ "created_at"])
            self.assertEqual(package.updated_at , expectedPackage[ "updated_at"])
            self.assertEqual(package.html_url , expectedPackage[ "html_url"])
            self.assertIsNone(package.version_count)

            if expectedPackage["repository_id"] is None:
                self.assertIsNone(package.repository)
            else:
                assert isinstance(package.repository, github.Repository.Repository)
                self.assertEqual(package.repository.id, expectedPackage["repository_id"])

    def testAuthUserGetPackage(self):
        package = self.authUser.get_package(package_type=PackageType.CONTAINER, package_name="test-pkg3")

        assert isinstance(package, github.Package.Package)
        self.assertIsNotNone(package.url)
        self.assertFalse(package.completed)
        self.assertEqual(package.name, "test-pkg3")
        self.assertEqual(package.id, 7930767)
        assert isinstance(package.owner, NamedUser)
        self.assertEqual(package.owner.id, 1024025)
        self.assertIsNotNone(package.version_count)
        self.assertEqual(package.version_count, 5)
        self.assertEqual(package.visibility, "private")
        self.assertEqual(package.url, "https://api.github.com/users/test-user/packages/container/test-pkg3")
        self.assertEqual(package.created_at, datetime(2025, 4, 3, 20, 50, 20, tzinfo=timezone.utc))
        self.assertEqual(package.updated_at, datetime(2025, 5, 3, 1, 5, 25, tzinfo=timezone.utc))
        assert isinstance(package.repository, github.Repository.Repository)
        self.assertEqual(package.repository.id, 959646125)
        self.assertEqual(package.html_url, "https://github.com/users/test-user/packages/container/package/test-pkg3")

    def testUserGetPackages(self):
        expected_packages = {
        7931961: {
            "name": "test-pkg5",
            "package_type": "container",
            "owner_id": 1024025,
            "visibility": "private",
            "url": "https://api.github.com/users/test-user/packages/container/test-pkg5",
            "created_at": datetime(2025, 4, 4, 4, 59, 42, tzinfo=timezone.utc),
            "updated_at": datetime(2025, 4, 4, 4, 59, 42, tzinfo=timezone.utc),
            "repository_id": None,
            "html_url": "https://github.com/users/test-user/packages/container/package/test-pkg5"
        },
        7948400: {
            "name": "test-pkg6",
            "package_type": "container",
            "owner_id": 1024025,
            "visibility": "public",
            "url": "https://api.github.com/users/test-user/packages/container/test-pkg5",
            "created_at": datetime(2025, 4, 8, 0, 44, 43, tzinfo=timezone.utc),
            "updated_at": datetime(2025, 4, 27, 0, 11, 16, tzinfo=timezone.utc),
            "repository_id": 962289158,
            "html_url": "https://github.com/users/test-user/packages/container/package/test-pkg5"
        }
    }
        packages = self.user.get_packages(package_type=PackageType.CONTAINER)
        packages = packages.get_page(1)

        self.assertEqual(len(packages), len(expected_packages))
        for package in packages:
            assert isinstance(package, github.Package.Package)
            self.assertIsNotNone(package.url)
            self.assertFalse(package.completed)
            expectedPackage = expected_packages[package.id]
            self.assertEqual(package.name, expectedPackage["name"])
            self.assertEqual(package.package_type , expectedPackage[ "package_type"])
            assert isinstance(package.owner, NamedUser)
            self.assertEqual(package.owner.id, expectedPackage["owner_id"])
            self.assertEqual(package.visibility , expectedPackage[ "visibility"])
            self.assertEqual(package.url , expectedPackage[ "url"])
            self.assertEqual(package.created_at , expectedPackage[ "created_at"])
            self.assertEqual(package.updated_at , expectedPackage[ "updated_at"])
            self.assertEqual(package.html_url , expectedPackage[ "html_url"])
            self.assertIsNone(package.version_count)

            if expectedPackage["repository_id"] is None:
                self.assertIsNone(package.repository)
            else:
                assert isinstance(package.repository, github.Repository.Repository)
                self.assertEqual(package.repository.id, expectedPackage["repository_id"])

    def testUserGetPackage(self):
        package = self.user.get_package(package_type=PackageType.CONTAINER, package_name="test-pkg3")

        assert isinstance(package, github.Package.Package)
        self.assertIsNotNone(package.url)
        self.assertFalse(package.completed)
        self.assertEqual(package.name, "test-pkg3")
        self.assertEqual(package.id, 7930767)
        assert isinstance(package.owner, NamedUser)
        self.assertEqual(package.owner.id, 1024025)
        self.assertIsNotNone(package.version_count)
        self.assertEqual(package.version_count, 5)
        self.assertEqual(package.visibility, "private")
        self.assertEqual(package.url, "https://api.github.com/users/test-user/packages/container/test-pkg3")
        self.assertEqual(package.created_at, datetime(2025, 4, 3, 20, 50, 20, tzinfo=timezone.utc))
        self.assertEqual(package.updated_at, datetime(2025, 5, 3, 1, 5, 57, tzinfo=timezone.utc))
        assert isinstance(package.repository, github.Repository.Repository)
        self.assertEqual(package.repository.id, 959646125)
        self.assertEqual(package.html_url, "https://github.com/users/test-user/packages/container/package/test-pkg3")


    def testGetOrgPackages(self):
        expected_packages = {
    8079081: {
        "name": "test-pkg",
        "package_type": "container",
        "owner_id": 210109354,
        "visibility": "private",
        "url": "https://api.github.com/orgs/test-org/packages/container/test-pkg",
        "created_at": datetime(2025, 5, 3, 3, 32, 46, tzinfo=timezone.utc),
        "updated_at": datetime(2025, 5, 3, 3, 32, 47, tzinfo=timezone.utc),
        "repository_id": None,
        "html_url": "https://github.com/orgs/test-org/packages/container/package/test-pkg"
    },
    8075481: {
        "name": "test-pkg2",
        "package_type": "container",
        "owner_id": 210109354,
        "visibility": "public",
        "url": "https://api.github.com/orgs/test-org/packages/container/test-pkg2",
        "created_at": datetime(2025, 5, 3, 3, 32, 46, tzinfo=timezone.utc),
        "updated_at": datetime(2025, 5, 3, 3, 32, 47, tzinfo=timezone.utc),
        "repository_id": None,
        "html_url": "https://github.com/orgs/test-org/packages/container/package/test-pkg2"
    }
}
        packages = self.org.get_packages(package_type=PackageType.CONTAINER)
        packages = packages.get_page(1)

        self.assertEqual(len(packages), len(expected_packages))
        for package in packages:
            assert isinstance(package, github.Package.Package)
            self.assertIsNotNone(package.url)
            self.assertFalse(package.completed)
            expectedPackage = expected_packages[package.id]
            self.assertEqual(package.name, expectedPackage["name"])
            self.assertEqual(package.package_type , expectedPackage[ "package_type"])
            assert isinstance(package.owner, NamedUser)
            self.assertEqual(package.owner.id, expectedPackage["owner_id"])
            self.assertEqual(package.visibility , expectedPackage[ "visibility"])
            self.assertEqual(package.url , expectedPackage[ "url"])
            self.assertEqual(package.created_at , expectedPackage[ "created_at"])
            self.assertEqual(package.updated_at , expectedPackage[ "updated_at"])
            self.assertEqual(package.html_url , expectedPackage[ "html_url"])
            self.assertIsNone(package.version_count)

            if expectedPackage["repository_id"] is None:
                self.assertIsNone(package.repository)
            else:
                assert isinstance(package.repository, github.Repository.Repository)
                self.assertEqual(package.repository.id, expectedPackage["repository_id"])

    def testOrgGetPackage(self):
        package = self.org.get_package(package_type=PackageType.CONTAINER, package_name="test-pkg")

        assert isinstance(package, github.Package.Package)
        self.assertIsNotNone(package.url)
        self.assertFalse(package.completed)
        self.assertEqual(package.name, "test-pkg")
        self.assertEqual(package.id, 8079081)
        assert isinstance(package.owner, NamedUser)
        self.assertEqual(package.owner.id, 210109354)
        self.assertIsNotNone(package.version_count)
        self.assertEqual(package.version_count, 2)
        self.assertEqual(package.visibility, "private")
        self.assertEqual(package.url, "https://api.github.com/orgs/test-org/packages/container/test-pkg")
        self.assertEqual(package.created_at, datetime(2025, 5, 3, 3, 32, 46, tzinfo=timezone.utc))
        self.assertEqual(package.updated_at, datetime(2025, 5, 3, 3, 32, 47, tzinfo=timezone.utc))
        self.assertIsNone(package.repository)
        self.assertEqual(package.html_url, "https://github.com/orgs/test-org/packages/container/package/test-pkg")