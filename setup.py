#!/usr/bin/env python

from distutils.core import setup

setup(
    name = 'PyGithub',
    version = '0.1-beta',
    description = 'Use the full Github API v3',
    author = 'Vincent Jacques',
    author_email = 'vincent@vincent-jacques.net',
    url = 'http://github.com/jacquev6/PyGithub',
    long_description = open( "CheeseShopDescription.rst" ).read(),
    packages = [
        'github'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
)
