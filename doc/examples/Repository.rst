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
	Issue(title="How to get public events?", number=913)
	Issue(title="Prevent .netrc from overwriting Auth header", number=910)
	Issue(title="Cache fetch responses", number=901)
	Issue(title="Is suspended_users for github enterprise implemented in NamedUser?", number=900)
	Issue(title="Adding migration api wrapper", number=899)

Get all the labels of the repository
------------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> labels = repo.get_labels()
    >>> for label in labels:
    ...    print(label)
    ...
    Label(name="Hacktoberfest")
    Label(name="WIP")
    Label(name="bug")
    Label(name="documentation")
