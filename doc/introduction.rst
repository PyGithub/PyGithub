.. _introduction:

Introduction
============

Installation
------------

While v2 is in alpha, you have to clone or download it from `Github <https://github.com/jacquev6/PyGithub/tree/develop_v2>`__ and run ``python setup.py install``. You may want to use `Virtualenv <http://www.virtualenv.org/>`__ to avoid conflicts with your existing install of v1::

    git clone git@github.com:jacquev6/PyGithub --branch develop_v2
    cd PyGithub
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    python setup.py install
    python -c "import PyGithub"



First use
---------

::

    >>> import PyGithub

    >>> g = PyGithub.BlockingBuilder().Build()

    >>> u = g.get_user("jacquev6")
    >>> print u.name
    Vincent Jacques

    >>> r = u.get_repo("PyGithub")
    >>> print r.stargazers_count
    366

Identification
--------------

To access your private resources, `you must authenticate <http://developer.github.com/v3/auth/>`__.
The simplest authentication is with your login and password::

    >>> g = PyGithub.BlockingBuilder().Login("your_login", "your_password").Build()

..  Authenticate for doctest but don't show it in the doc
    >>> import GithubCredentials
    >>> g = PyGithub.BlockingBuilder().Login(GithubCredentials.login, GithubCredentials.password).Build()

Then you can retrieve the authenticated user::

    >>> u = g.get_authenticated_user()
    >>> print u.login
    jacquev6

For other authentication methods, see the :ref:`User Guide <configuration>`.
