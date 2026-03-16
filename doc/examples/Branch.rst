Branch
==========

Get list of branches
--------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> list(repo.get_branches())
            [Branch(name="master")]

    .. tab:: Async

        .. code-block:: python

            >>> repo = await g.get_repo("PyGithub/PyGithub")
            >>> [branch async for branch in (await repo.get_branches())]
            [Branch(name="master")]

Note that the Branch object returned by get_branches() is not fully populated,
and you can not query everything. Use get_branch(branch="master") once you
have the branch name.

Get a branch
------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> repo.get_branch(branch="master")
            Branch(name="master")

    .. tab:: Async

        .. code-block:: python

            >>> repo = await g.get_repo("PyGithub/PyGithub")
            >>> await repo.get_branch(branch="master")
            Branch(name="master")

Get HEAD commit of a branch
---------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> branch = g.get_repo("PyGithub/PyGithub").get_branch("master")
            >>> branch.commit
            Commit(sha="5e69ff00a3be0a76b13356c6ff42af79ff469ef3")

    .. tab:: Async

        .. code-block:: python

            >>> repo = await g.get_repo("PyGithub/PyGithub")
            >>> branch = await repo.get_branch("master")
            >>> branch.commit
            Commit(sha="5e69ff00a3be0a76b13356c6ff42af79ff469ef3")

Get protection status of a branch
---------------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> branch = g.get_repo("PyGithub/PyGithub").get_branch("master")
            >>> branch.protected
            True

    .. tab:: Async

        .. code-block:: python

            >>> repo = await g.get_repo("PyGithub/PyGithub")
            >>> branch = await repo.get_branch("master")
            >>> branch.protected
            True

See required status checks of a branch
--------------------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> branch = g.get_repo("PyGithub/PyGithub").get_branch("master")
            >>> branch.get_required_status_checks()
            RequiredStatusChecks(url="https://api.github.com/repos/PyGithub/PyGithub/branches/master/protection/required_status_checks", strict=True)

    .. tab:: Async

        .. code-block:: python

            >>> repo = await g.get_repo("PyGithub/PyGithub")
            >>> branch = await repo.get_branch("master")
            >>> await branch.get_required_status_checks()
            RequiredStatusChecks(url="https://api.github.com/repos/PyGithub/PyGithub/branches/master/protection/required_status_checks", strict=True)
