#!/usr/bin/env python

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Tomas Radej <tradej@redhat.com>                               #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Jimmy Zelinskie <jimmyzelinskie@gmail.com>                    #
# Copyright 2016 Felix Yan <felixonmars@archlinux.org>                         #
# Copyright 2016 Jakub Wilk <jwilk@jwilk.net>                                  #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Hugo <hugovk@users.noreply.github.com>                        #
# Copyright 2017 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2017 Jannis Gebauer <jayfk@users.noreply.github.com>               #
# Copyright 2017 Nhomar Hernandez <nhomar@vauxoo.com>                          #
# Copyright 2017 Paul Ortman <paul.ortman@gmail.com>                           #
# Copyright 2018 Jason White <jasonaw0@gmail.com>                              #
# Copyright 2018 Mike Miller <github@mikeage.net>                              #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
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

import textwrap

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="PyGithub",
        use_scm_version=True,
        setup_requires=["setuptools_scm"],
        description="Use the full Github API v3",
        author="Vincent Jacques",
        author_email="vincent@vincent-jacques.net",
        url="https://github.com/pygithub/pygithub",
        project_urls={
            "Documentation": "http://pygithub.readthedocs.io/en/stable/",
            "Source": "https://github.com/pygithub/pygithub",
            "Tracker": "https://github.com/pygithub/pygithub/issues",
        },
        long_description=textwrap.dedent(
            """\
            (Very short) Tutorial
            =====================

            First create a Github instance::

                from github import Github

                # Authentication is defined via github.Auth
                from github import Auth

                # using an access token
                auth = Auth.Token("access_token")

                # Public Web Github
                g = Github(auth=auth)

                # Github Enterprise with custom hostname
                g = Github(auth=auth, base_url="https://{hostname}/api/v3")

            Then play with your Github objects::

                for repo in g.get_user().get_repos():
                    print(repo.name)
                    repo.edit(has_wiki=False)
                    # to see all the available attributes and methods
                    print(dir(repo))

            Reference documentation
            =======================

            See http://pygithub.readthedocs.io/en/stable/"""
        ),
        packages=["github"],
        package_data={"github": ["py.typed", "*.pyi"]},
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Software Development",
        ],
        python_requires=">=3.7",
        install_requires=[
            "deprecated",
            "pyjwt[crypto]>=2.4.0",
            "pynacl>=1.4.0",
            "requests>=2.14.0",
            "python-dateutil",
        ],
        # can be removed, still here to avoid breaking user code
        extras_require={"integrations": []},
        tests_require=["httpretty>=1.0.3"],
    )
