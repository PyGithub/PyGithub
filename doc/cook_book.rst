.. _cook_book:

=========
Cook book
=========

Working with gists
==================

This cook book shows you everything about `gists <https://gist.github.com>`__ and the `gists API <https://developer.github.com/v3/gists>`__.

Initialization::

    >>> import PyGithub
    >>> g = PyGithub.BlockingBuilder().Login("your_login", "your_password").Build()

..  Authenticate for doctest but don't show it in the doc
    >>> import GithubCredentials
    >>> g = PyGithub.BlockingBuilder().Login(GithubCredentials.login, GithubCredentials.password).Build()

::

    >>> u = g.get_authenticated_user()

Creating gists
--------------

The simplest, personal, private gist, with one file::

    >>> gist = u.create_gist(files={"foo.txt":{"content": "barbaz"}})
    >>> print gist.owner.login
    jacquev6
    >>> print gist.public
    False

..
    >>> gist.delete()

An anonymous gist::

    >>> gist = g.create_anonymous_gist()
    >>> print gist.owner
    None

.. Let's not polute GitHub
    >>> gist.delete()
    None

A secret gist (works with personal and anonymous gists)::

    >>> gist = u.create_gist(secret=True)
    >>> print gist.secret
    True

..
    >>> gist.delete()
    None

A gist with several files::

    >>> gist = u.create_gist()

..
    >>> gist.delete()
    None

Retrieving gists
----------------

List public gists::

    >>> g.get_public_gists()

List personal gists::

    >>> u.get_gists()

Get a single gist::

    >>> u.get_gist()

Modifying gists
---------------

Change attributes::

    >>> gist.edit()

Add a file::

    >>> gist.edit()

Delete a file::

    >>> gist.edit()

Rename a file::

    >>> gist.edit()

Starring and unstarring::

    >>> gist.star()
    >>> print gist.is_starred()
    True
    >>> gist.unstar()
    >>> print gist.is_starred()
    False

Forking
-------

    >>> fork = gist.create_fork()

..
    >>> fork.delete()

Deleting gists
--------------

    >>> gist.delete()
