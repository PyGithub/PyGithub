Issues
======

Get issue
---------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.get_issue(number=874)
	Issue(title="PyGithub example usage", number=874)

Create issue
------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.create_issue(title="This is a new issue")
	Issue(title="This is a new issue", number=XXX)

Create issue with body
----------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.create_issue(title="This is a new issue", body="This is the issue body")
	Issue(title="This is a new issue", number=XXX)

Create issue with labels
------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> label = repo.get_label("My Label")
    >>> repo.create_issue(title="This is a new issue", labels=[label])
	Issue(title="This is a new issue", number=XXX)

Create issue with assignee
--------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.create_issue(title="This is a new issue", assignee="github-username")
	Issue(title="This is a new issue", number=XXX)

Create issue with milestone
---------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> milestone = repo.create_milestone("New Issue Milestone")
    >>> repo.create_issue(title="This is a new issue", milestone=milestone)
	Issue(title="This is a new issue", number=XXX)
