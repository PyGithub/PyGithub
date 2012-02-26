This is a Python library to access the [Gitub API v3](http://developer.github.com/v3).

With it, you can manage your repositories, your organizations and your user profile from Python scripts.

It is still a work in progress, but I'm sure I'll finish it soon. The aim is to cover the **full** API in version 1.0.

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

    for repo in g.get_user().get_repos():
        print repo.name
        repo.edit( has_wiki = False )

History
=======

Version 0.2 (February 23rd, 2012)
---------------------------------

* Refactoring
* Teams details and modification
    * basic attributes
    * list teams in organizations, on repositories
* Git objects
    * create and get tags, references, commits, trees, blobs
    * list and edit references

Version 0.1 (February 19th, 2012)
---------------------------------

* User details and modification
    * basic attributes
    * followers, following, watching
    * organizations
    * repositories
* Repository details and modification
    * basic attributes
    * forking
    * collaborators, contributors, watchers
* Organization details and modification
    * basic attributes
    * members and public members
