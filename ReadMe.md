This is a Python library to access the [Gitub API v3](http://developer.github.com/v3).

Download and install
====================

This package is in the [Python Package Index](http://pypi.python.org/pypi/PyGithub).
You can also clone it on [Github](http://github.com/jacquev6/PyGithub).

Planned releases (updated February 18th 2012)
==============================================

 - First partial release (version 0.1, planned about February 27th)
   - no remaining known bugs
   - full implementation of relations between users, organizations and repositories
   - documentation

 - Partial releases (versions 0.x)
   - implementation of other object types (git objects in priority)

 - First full release (version 1.0, planned mid-March 2015)
   - full coverage of the API

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
