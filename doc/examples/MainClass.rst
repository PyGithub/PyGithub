Main Class
==========

This is the main class.

Get current user
----------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> user = g.get_user()
            >>> user.login
            u'sfdye'

    .. tab:: Async

        .. code-block:: python

            >>> user = await g.get_user()
            >>> await user.login
            u'sfdye'

Get user by name
----------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> user = g.get_user("sfdye")
            >>> user.name
            u'Wan Liuyang'

    .. tab:: Async

        .. code-block:: python

            >>> user = await g.get_user("sfdye")
            >>> await user.name
            u'Wan Liuyang'

Get repository by name
----------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> repo.name
            u'PyGithub'

    .. tab:: Async

        .. code-block:: python

            >>> repo = await g.get_repo("PyGithub/PyGithub")
            >>> await repo.name
            u'PyGithub'

Get organization by name
------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> org = g.get_organization("PyGithub")
            >>> org.login
            u'PyGithub'

    .. tab:: Async

        .. code-block:: python

            >>> org = await g.get_organization("PyGithub")
            >>> await org.login
            u'PyGithub'

Get enterprise consumed licenses by name
----------------------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> enterprise = g.get_enterprise_consumed_licenses("PyGithub")
            >>> enterprise_consumed_licenses = enterprise.get_enterprise_consumed_licenses()
            >>> enterprise_consumed_licenses.total_seats_consumed
            5000

    .. tab:: Async

        .. code-block:: python

            >>> enterprise = await g.get_enterprise_consumed_licenses("PyGithub")
            >>> enterprise_consumed_licenses = await enterprise.get_enterprise_consumed_licenses()
            >>> enterprise_consumed_licenses.total_seats_consumed
            5000

Search repositories by language
-------------------------------

.. tabs::

    .. tab:: Sync

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

    .. tab:: Async

        .. code-block:: python

            >>> repositories = g.search_repositories(query='language:python')
            >>> async for repo in repositories:
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

.. tabs::

    .. tab:: Sync

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

    .. tab:: Async

        .. code-block:: python

            >>> repositories = g.search_repositories(query='good-first-issues:>3')
            >>> async for repo in repositories:
            ...    print(repo)
            ...
            Repository(full_name="vuejs/vue")
            Repository(full_name="facebook/react")
            Repository(full_name="facebook/react-native")
            Repository(full_name="electron/electron")
            Repository(full_name="Microsoft/vscode")
