Milestone
==========

Get Milestone list
------------------

.. code-block:: python

    >>> repo = g.get_repo('PyGithub/PyGithub')
    >>> open_milestones = repo.get_milestones(state='open')
    >>> for milestone in open_milestones:
    ...    print(milestone)
    ... 
    Milestone(number=1) 
    Milestone(number=2) 

Get Milestone
-------------

.. code-block:: python

    >>> repo = g.get_repo('PyGithub/PyGithub')
    >>> repo.get_milestone(number=1)
    Milestone(number=1) 

Create Milestone
----------------

.. code-block:: python

    >>> repo = g.get_repo('PyGithub/PyGithub')
    >>> repo.create_milestone(title='New Milestone')
    Milestone(number=1) 

Create Milestone with State and Description
-------------------------------------------

.. code-block:: python

    >>> repo = g.get_repo('PyGithub/PyGithub')
    >>> repo.create_milestone(title='New Milestone', state='open', description='Milestone description')
    Milestone(number=1) 
