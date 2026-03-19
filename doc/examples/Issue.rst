Issues
======

Get issue
---------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> repo.get_issue(number=874)
            Issue(title="PyGithub example usage", number=874)

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> await repo.get_issue(number=874)
            Issue(title="PyGithub example usage", number=874)

Create comment on issue
-----------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> issue = repo.get_issue(number=874)
            >>> issue.create_comment("Test")
            IssueComment(user=NamedUser(login="user"), id=36763078)

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> issue = await repo.get_issue(number=874)
            >>> await issue.create_comment("Test")
            IssueComment(user=NamedUser(login="user"), id=36763078)

Create issue
------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> repo.create_issue(title="This is a new issue")
            Issue(title="This is a new issue", number=XXX)

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> await repo.create_issue(title="This is a new issue")
            Issue(title="This is a new issue", number=XXX)

Create issue with body
----------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> repo.create_issue(title="This is a new issue", body="This is the issue body")
            Issue(title="This is a new issue", number=XXX)

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> await repo.create_issue(title="This is a new issue", body="This is the issue body")
            Issue(title="This is a new issue", number=XXX)

Create issue with labels
------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> label = repo.get_label("My Label")
            >>> repo.create_issue(title="This is a new issue", labels=[label])
            Issue(title="This is a new issue", number=XXX)

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> label = await repo.get_label("My Label")
            >>> await repo.create_issue(title="This is a new issue", labels=[label])
            Issue(title="This is a new issue", number=XXX)

Create issue with assignee
--------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> repo.create_issue(title="This is a new issue", assignee="github-username")
            Issue(title="This is a new issue", number=XXX)

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> await repo.create_issue(title="This is a new issue", assignee="github-username")
            Issue(title="This is a new issue", number=XXX)

Create issue with milestone
---------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> milestone = repo.create_milestone("New Issue Milestone")
            >>> repo.create_issue(title="This is a new issue", milestone=milestone)
            Issue(title="This is a new issue", number=XXX)

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> milestone = await repo.create_milestone("New Issue Milestone")
            >>> await repo.create_issue(title="This is a new issue", milestone=milestone)
            Issue(title="This is a new issue", number=XXX)

Close all issues
-----------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> open_issues = repo.get_issues(state='open')
            >>> for issue in open_issues:
            ...     issue.edit(state='closed')

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> open_issues = await repo.get_issues(state='open')
            >>> async for issue in open_issues:
            ...     await issue.edit(state='closed')
