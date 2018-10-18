Branch
==========

Get list of branches
--------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> list(repo.get_branches())
    [Branch(name="master")]

Note that the Branch object returned by get_branches() is not fully populated,
and you can not query everything. Use get_branch(branch="master") once you
have the branch name.

Get a branch
------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.get_branch(branch="master")
    Branch(name="master")

Get HEAD commit of a branch
---------------------------

.. code-block:: python

    >>> branch = g.get_repo("PyGithub/PyGithub").get_branch("master")
    >>> branch.commit
    Commit(sha="5e69ff00a3be0a76b13356c6ff42af79ff469ef3")

Get protection status of a branch
---------------------------------

.. code-block:: python

    >>> branch = g.get_repo("PyGithub/PyGithub").get_branch("master")
    >>> branch.protection
    True

See required status checks of a branch
--------------------------------------

.. code-block:: python

    >>> branch = g.get_repo("PyGithub/PyGithub").get_branch("master")
    >>> branch.get_required_status_checks()
    RequiredStatusChecks(url="https://api.github.com/repos/PyGithub/PyGithub/branches/master/protection/required_status_checks", strict=True)
