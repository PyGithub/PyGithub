This is a Python library to access the [Gitub V3 API](http://developer.github.com/v3/).

Tutorial
========

First create a Gihub instance:

    from github import Github

    g = Github( "user", "password" )

Then play with your Github objects:

    for repository in g.user().get_repositories():
        print repository.name
        repository.edit( has_wiki = False )
