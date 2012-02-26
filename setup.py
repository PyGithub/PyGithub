#!/usr/bin/env python

from distutils.core import setup
import textwrap

setup(
    name = 'PyGithub',
    version = '0.3',
    description = 'Use the full Github API v3',
    author = 'Vincent Jacques',
    author_email = 'vincent@vincent-jacques.net',
    url = 'http://vincent-jacques.net/PyGithub',
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

        Reference documentation
        =======================

        See http://vincent-jacques.net/PyGithub""" ),
    packages = [
        'github',
        'github.ObjectCapacities',
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
