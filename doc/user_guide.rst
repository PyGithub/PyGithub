.. _user_guide:

User guide
==========

.. _configuration:

Configuring the GitHub session
------------------------------

.. automodule:: PyGithub.Blocking.Builder

Common functionalities
----------------------

.. automodule:: PyGithub.Blocking.BaseGithubObject

.. @todoSomeday Fix this ref...
.. _pagination_foo:

Pagination
----------

.. automodule:: PyGithub.Blocking.PaginatedList

Naming conventions
------------------

Methods and attributes mapping exactly to the GitHub API v3 are in lower case like :meth:`.AuthenticatedUser.create_repo` and :attr:`.Repository.stargazers_count`.

Methods and attributes more specific to PyGithub are in upper camel case like :attr:`.Session.RateLimit`.

Access to common resources
--------------------------

..  Authenticate for doctest but don't show it in the doc
    >>> import PyGithub.Blocking
    >>> import GithubCredentials
    >>> g = PyGithub.BlockingBuilder().Login(GithubCredentials.login, GithubCredentials.password).Build()

Users, organizations
~~~~~~~~~~~~~~~~~~~~

You can access a user by :meth:`.Github.get_user` and the authenticated user by :meth:`.Github.get_authenticated_user`. For orgs, use :meth:`.Github.get_org`::

    >>> nvie = g.get_user("nvie")
    >>> print nvie.name
    Vincent Driessen

::

    >>> me = g.get_authenticated_user()
    >>> print me.login
    jacquev6
    >>> print me.name
    Vincent Jacques

::

    >>> github = g.get_org("github")
    >>> print github.location
    San Francisco, CA

Repositories
~~~~~~~~~~~~

There are several ways to access a repository:

* if you already have the :class:`.User`, :class:`.AuthenticatedUser` or :class:`.Organization` owning the repo, call its :meth:`get_repo` method::

    >>> gitflow = nvie.get_repo("gitflow")
    >>> print gitflow.description
    Git extensions to provide high-level repository operations for Vincent Driessen's branching model.

  ::

    >>> pygithub = me.get_repo("PyGithub")
    >>> print pygithub.description
    Python library implementing the full GitHub API v3

* if you have its full name, use :meth:`.Github.get_repo`::

    >>> whisper = g.get_repo("graphite-project/whisper")  # You don't have to know if graphite-project is a user or an org
    >>> whisper.created_at
    datetime.datetime(2012, 5, 7, 21, 30, 26)

* if you have the login of its owner and its name, you can call :meth:`.Github.get_repo` with a tuple::

    >>> apidoc = g.get_repo(("github", "developer.github.com"))
    >>> print apidoc.description
    GitHub Developer site

* if you want to list someone's repositories, use :meth:`get_repos`::

    >>> for repo in g.get_org("graphite-project").get_repos():
    ...     print repo.name
    carbon
    whisper
    graphite-web
    ceres
    graphite-project.github.com
