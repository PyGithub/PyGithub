#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import setuptools
import textwrap
import subprocess
import shutil
import os.path

with open("PyGithub/__init__.py") as f:
    for line in f:
        if line.startswith("Version = \""):
            version = line.strip()[11:-1]


if __name__ == "__main__":
    setuptools.setup(
        name="PyGithub",
        version=version,
        description="Use the full Github API v3",
        author="Vincent Jacques",
        author_email="vincent@vincent-jacques.net",
        url="http://jacquev6.github.com/PyGithub",
        packages=[
            "PyGithub",
            "PyGithub.Blocking",
            "PyGithub.Blocking.tests",
            "PyGithub.Blocking.tests.Classes",
            "PyGithub.Blocking.tests.Topics",
        ],
        package_data={
            "PyGithub": ["Blocking/tests/*/*/*.json"],
        },
        classifiers=[
            "Development Status :: 3 - Alpha",  # @todoBeta Review
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Topic :: Software Development",
            "License :: OSI Approved",
            "License :: OSI Approved :: MIT License",
        ],
        test_suite="PyGithub.tests",
        use_2to3=True
    )
