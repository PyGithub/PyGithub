#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import setuptools
import textwrap
import subprocess
import shutil
import os.path

version = "1.12.1"


def execute(*args):
    subprocess.check_call(args)


class SimpleCommand(setuptools.Command):
    user_options = []

    def __init__(self, dist, *args, **kwds):
        setuptools.Command.__init__(self, dist, *args, **kwds)
        self.dist = dist

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class Check(SimpleCommand):
    def run(self):
        execute("pep8", "--ignore=E501", "github", "setup.py")  # pip install pep8


class Coverage(SimpleCommand):
    def run(self):
        execute("coverage", "run", "--branch", "--include=github/*.py", "--omit=github/tests/*.py", "setup.py", "test", "--quiet")
        execute("python3", "setup.py", "test", "--quiet")
        execute("coverage", "report", "--show-missing")


class MakeDoc(SimpleCommand):
    def run(self):
        d = "doc/build"
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d)
        os.chdir(d)
        execute("git", "init")
        execute("sphinx-build", "-b", "html", "-d", "doctrees", "..", ".")
        with open(".nojekyll", "w"):
            pass
        with open(".gitignore", "w") as f:
            f.write("/doctrees/\n")
        execute("git", "add", ".")
        execute("git", "commit", "--message", "Automatic generation")
        execute("git", "push", "--force", "../..", "HEAD:gh-pages")


class Publish(SimpleCommand):
    def run(self):
        Check(self.dist).run()
        Coverage(self.dist).run()
        MakeDoc(self.dist).run()


if __name__ == "__main__":
    setuptools.setup(
        name="PyGithub",
        version=version,
        description="Use the full Github API v3",
        author="Vincent Jacques",
        author_email="vincent@vincent-jacques.net",
        url="http://jacquev6.github.com/PyGithub",
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

            See http://jacquev6.github.com/PyGithub"""),
        packages=[
            "github",
            "github.tests",
        ],
        package_data={
            "github": ["ReadMe.rst", "COPYING*", "tests/ReplayData/*.txt"]
        },
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development",
        ],
        test_suite="github.tests.AllTests",
        cmdclass={
            "check_": Check,
            "coverage": Coverage,
            "make_doc": MakeDoc,
            "publish": Publish,
        },
        use_2to3=True
    )
