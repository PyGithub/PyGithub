Repository
==========

Get repository topics
---------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.get_topics()
    [u'pygithub', u'python', u'github', u'github-api']

Get count of stars
------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.stargrazers_count
    2086

Get list of open issues
--------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> open_issues = repo.get_issues(state='open')
    >>> for issue in open_issues:
    ...    print(issue)
    ...
	How to get public events?
	get_repo crashes with UnicodeEncodeError if log level..
	Prevent .netrc from overwriting Auth header

Get all the labels of the repository
------------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> labels = repo.get_labels(state='open')
    >>> for label in labels:
    ...    print(label)
    ...
    Hacktoberfest
    WIP
    bug
    documentation
