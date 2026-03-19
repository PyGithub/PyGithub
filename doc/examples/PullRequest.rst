PullRequest
===========

Create a new Pull Request
-------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> body = '''
            >>> SUMMARY
            >>> Change HTTP library used to send requests
            >>>
            >>> TESTS
            >>>   - [x] Send 'GET' request
            >>>   - [x] Send 'POST' request with/without body
            >>> '''
            >>> pr = repo.create_pull(base="master", head="develop", title="Use 'requests' instead of 'httplib'", body=body)
            >>> pr
            PullRequest(title="Use 'requests' instead of 'httplib'", number=664)

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> body = '''
            >>> SUMMARY
            >>> Change HTTP library used to send requests
            >>>
            >>> TESTS
            >>>   - [x] Send 'GET' request
            >>>   - [x] Send 'POST' request with/without body
            >>> '''
            >>> pr = await repo.create_pull(base="master", head="develop", title="Use 'requests' instead of 'httplib'", body=body)
            >>> pr
            PullRequest(title="Use 'requests' instead of 'httplib'", number=664)

Get Pull Request by Number
---------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> pr = repo.get_pull(664)
            >>> pr
            PullRequest(title="Use 'requests' instead of 'httplib'", number=664)

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> pr = await repo.get_pull(664)
            >>> pr
            PullRequest(title="Use 'requests' instead of 'httplib'", number=664)

Get Pull Requests by Query
--------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> pulls = repo.get_pulls(state='open', sort='created', base='master')
            >>> for pr in pulls:
            ...    print(pr.number)
            ...
            400
            861
            875
            876

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> pulls = await repo.get_pulls(state='open', sort='created', base='master')
            >>> async for pr in pulls:
            ...    print(await pr.number)
            ...
            400
            861
            875
            876

Add and modify Pull Request comment
-----------------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> pr = repo.get_pull(2390)
            >>> last_commit = pr.get_commits()[pr.commits - 1]
            >>> comment = pr.create_comment("This is a comment", last_commit, "file.txt", 0)
            >>> comment
            PullRequestComment(user=NamedUser(login="anonymous"), id=1057297855)
            >>> comment.body
            'This is a comment'
            >>> comment.edit("This is a modified comment")
            >>> comment.body
            'This is a modified comment'

    .. tab:: Async

        .. code-block:: python

            >>> repo = g.get_repo("PyGithub/PyGithub")
            >>> pr = await repo.get_pull(2390)
            >>> commits = await pr.get_commits()
            >>> last_commit = await commits.getitem(await pr.commits - 1)
            >>> comment = await pr.create_comment("This is a comment", last_commit, "file.txt", 0)
            >>> comment
            PullRequestComment(user=NamedUser(login="anonymous"), id=1057297855)
            >>> await comment.body
            'This is a comment'
            >>> await comment.edit("This is a modified comment")
            >>> await comment.body
            'This is a modified comment'
