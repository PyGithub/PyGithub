#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.github.io/PyGithub/v1/index.html                             #
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
# ##############################################################################

import setuptools
import textwrap

version = "1.32"


if __name__ == "__main__":
    setuptools.setup(
        name="PyGithub",
        version=version,
        description="Use the full Github API v3",
        author="Vincent Jacques",
        author_email="vincent@vincent-jacques.net",
        url="http://pygithub.github.io/PyGithub/v1/index.html",
        long_description=textwrap.dedent("""\
            (Very short) Tutorial
            =====================

            First create a Github instance::

                from github import Github

                g = Github("user", "password")

            Then play with your Github objects::

                for repo in g.get_user().get_repos():
                    print repo.name
                    repo.edit(has_wiki=False)

            You can also create a Github instance with an OAuth token::

                g = Github(token)

            Or without authentication::

                g = Github()

            Reference documentation
            =======================

            See http://pygithub.github.io/PyGithub/v1/index.html"""),
        packages=[
            "github",
            "github.tests",
        ],
        package_data={
            "github": ["tests/ReplayData/*.txt"]
        },
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.5",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Topic :: Software Development",
        ],
        test_suite="github.tests.AllTests",
        use_2to3=True,
        install_requires=[
            "python-jose"
        ]
    )
