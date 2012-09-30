#!/usr/bin/env python

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup, Command
import textwrap

class test( Command ):
    user_options = []

    def initialize_options( self ):
        pass

    def finalize_options( self ):
        pass

    def run( self ):
        import github.tests
        github.tests.run()

setup(
    name = "PyGithub",
    version = "1.8.0",
    description = "Use the full Github API v3",
    author = "Vincent Jacques",
    author_email = "vincent@vincent-jacques.net",
    url = "http://vincent-jacques.net/PyGithub",
    long_description = textwrap.dedent( """\
        Tutorial
        ========

        First create a Gihub instance::

            from github import Github

            g = Github( "user", "password" )

        Then play with your Github objects::

            for repo in g.get_user().get_repos():
                print repo.name
                repo.edit( has_wiki = False )

        You can also create a Github instance with an OAuth token::

            g = Github( token )

        Or without authentication::

            g = Github()

        Reference documentation
        =======================

        See http://vincent-jacques.net/PyGithub""" ),
    packages = [
        "github",
        "github.tests",
    ],
    package_data = {
        "github": [ "ReadMe.md", "COPYING*", "doc/*.md", "tests/ReplayData/*.txt" ]
    },
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    cmdclass = { "test": test },
)
