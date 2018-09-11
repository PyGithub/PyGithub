Repository
==========

Get repository topics
---------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.get_topics()
    [u'pygithub', u'python', u'github', u'github-api']