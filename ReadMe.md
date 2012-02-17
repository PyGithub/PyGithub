This is a Python library to access the [Gitub API v3](http://developer.github.com/v3).

Download and install
====================

This package is in the [Python Package Index](http://pypi.python.org/pypi/PyGithub).
You can also clone it on [Github](http://github.com/jacquev6/PyGithub).

Tutorial
========

First create a Gihub instance:

    from github import Github

    g = Github( "user", "password" )

Then play with your Github objects:

    for repo in g.user().get_repos():
        print repo.name
        repo.edit( has_wiki = False )

Reference documentation
=======================

See file "Reference.md".
