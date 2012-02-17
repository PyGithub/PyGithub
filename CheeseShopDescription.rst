Tutorial
========

First create a Gihub instance::

    from github import Github

    g = Github( "user", "password" )

Then play with your Github objects::

    for repo in g.user().get_repos():
        print repo.name
        repo.edit( has_wiki = False )

Reference documentation
=======================

See https://github.com/jacquev6/PyGithub/blob/master/Reference.md
