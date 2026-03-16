Milestone
==========

Get Milestone list
------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo('PyGithub/PyGithub')
            >>> open_milestones = repo.get_milestones(state='open')
            >>> for milestone in open_milestones:
            ...    print(milestone)
            ...
            Milestone(number=1)
            Milestone(number=2)

    .. tab:: Async

        .. code-block:: python

            >>> repo = await g.get_repo('PyGithub/PyGithub')
            >>> open_milestones = await repo.get_milestones(state='open')
            >>> async for milestone in open_milestones:
            ...    print(milestone)
            ...
            Milestone(number=1)
            Milestone(number=2)

Get Milestone
-------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo('PyGithub/PyGithub')
            >>> repo.get_milestone(number=1)
            Milestone(number=1)

    .. tab:: Async

        .. code-block:: python

            >>> repo = await g.get_repo('PyGithub/PyGithub')
            >>> await repo.get_milestone(number=1)
            Milestone(number=1)

Create Milestone
----------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo('PyGithub/PyGithub')
            >>> repo.create_milestone(title='New Milestone')
            Milestone(number=1)

    .. tab:: Async

        .. code-block:: python

            >>> repo = await g.get_repo('PyGithub/PyGithub')
            >>> await repo.create_milestone(title='New Milestone')
            Milestone(number=1)

Create Milestone with State and Description
-------------------------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo('PyGithub/PyGithub')
            >>> repo.create_milestone(title='New Milestone', state='open', description='Milestone description')
            Milestone(number=1)

    .. tab:: Async

        .. code-block:: python

            >>> repo = await g.get_repo('PyGithub/PyGithub')
            >>> await repo.create_milestone(title='New Milestone', state='open', description='Milestone description')
            Milestone(number=1)
