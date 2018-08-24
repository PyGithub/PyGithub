Main Class
==========

This is the main class.

Get current user
----------------

.. code-block:: python

    >>> user = g.get_user()
    >>> user.login
    u'sfdye'

Get user by name
----------------

.. code-block:: python

    >>> user = g.get_user("sfdye")
    >>> user.name
    u'Wan Liuyang'

Get repository by name
----------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.name
    u'PyGithub'

Get organization by name
------------------------

.. code-block:: python

    >>> org = g.get_organization("PyGithub")
    >>> org.login
    u'PyGithub'