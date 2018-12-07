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

Search repositories by language
-------------------------------

.. code-block:: python

    >>> repositories = g.search_repositories(query='language:python')
    >>> for repo in repositories:
    ...    print(repo)
    ...
    Repository(full_name="vinta/awesome-python")
    Repository(full_name="donnemartin/system-design-primer")
    Repository(full_name="toddmotto/public-apis")
    Repository(full_name="rg3/youtube-dl")
    Repository(full_name="tensorflow/models")
    Repository(full_name="django/django")

Search repositories based on number of issues with good-first-issue
-------------------------------------------------------------------

.. code-block:: python

    >>> repositories = g.search_repositories(query='good-first-issues:>3')
    >>> for repo in repositories:
    ...    print(repo)
    ...
    Repository(full_name="vuejs/vue")
    Repository(full_name="facebook/react")
    Repository(full_name="facebook/react-native")
    Repository(full_name="electron/electron")
    Repository(full_name="Microsoft/vscode")
