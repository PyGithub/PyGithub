PullRequest
===========

Get Pull Request by Number
---------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> pr = repo.get_pull(664)


Get Pull Requests by Query
--------------------------

.. code-block:: python

    # Filters for the pull requests to collect.
    # state = 'open' | 'closed' | 'all', Default = 'open'
    # sort = 'created' | 'updated' | popularity' | 'long-running', Default = 'created'
    # direction = 'asc' | 'desc', 'desc' when sort = 'created" otherwise 'asc'
    # base = Filter by base (i.e. target) branch name
    # head = Filter by head (i.e. source) user and branch name (ex. user:ref-name)
    repo = g.get_repo("PyGithub/PyGithub")
    pulls = repo.get_pulls(state='open', sort='created', base='master') 
    pr in pulls:
        print pr.number
