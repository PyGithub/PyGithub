This is a Python library to access the [Gitub V3 API](http://developer.github.com/v3/).

Tutorial
========

First create a Gihub instance:

    from github import Github

    g = Github( "user", "password" )

Then play with your Github objects:

    for repository in g.user().repositories( type = "private" ):
        print repository.name
        repository.edit( has_wiki = False )

Documentation
=============

Here are the classes encapsulating the API. You can use them without knowing the API itself.
If you know what API you need to call, see file Reference.md to understand which class(es) impements it.

User
----

If `g` is a `Gihub`:

 - `g.user()` returns the authenticated `User`
 - `g.user( name )` returns the named `User`

If `user` is a `User`:

 - cf. paragraph Organizations to access its organizations
 - cf. paragraph Repositories to access its repositories

Organizations
-------------

If `g` is a `Gihub`:
 - `g.organization( name )` returns the named `Organization`

If `user` is a `User`:

 - user.organizations() lists its `Organization`s

If `org` is an `Organization`:

 - cf. paragraph Repositories to access its repositories

Repositories
------------

If `owner` is a `User` or an `Organization`:

 - `owner.repositories( type )` lists its `Repository`ies
 - `owner.repository( name )` returns the named `Repository`
 - `owner.createRepository( name )` creates a new repository and returns the new `Repository`

If `repo` is a `Repository`:

 - `repo.edit()` edits the repository (same optional arguments as [API](http://developer.github.com/v3/repos/#edit))
