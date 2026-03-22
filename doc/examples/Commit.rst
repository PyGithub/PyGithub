Commit
======

Create commit status check
--------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            # sha -> commit on which the status check will be created
            # For example, for a webhook payload
            # sha = data["pull_request"]["head"]["sha"]
            repo.get_commit(sha=sha).create_status(
                state="pending",
                target_url="https://FooCI.com",
                description="FooCI is building",
                context="ci/FooCI"
            )

    .. tab:: Async

        .. code-block:: python

            # sha -> commit on which the status check will be created
            # For example, for a webhook payload
            # sha = data["pull_request"]["head"]["sha"]
            commit = await repo.get_commit(sha=sha)
            await commit.create_status(
                state="pending",
                target_url="https://FooCI.com",
                description="FooCI is building",
                context="ci/FooCI"
            )

Get commit date
--------------------------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            >>> commit = repo.get_commit(sha=sha)
            >>> print(commit.commit.author.date)
            2018-10-11 03:04:52
            >>> print(commit.commit.committer.date)
            2018-10-11 03:04:52

    .. tab:: Async

        .. code-block:: python

            >>> commit = await repo.get_commit(sha=sha)
            >>> git_commit = await commit.commit
            >>> print((await git_commit.author).date)
            2018-10-11 03:04:52
            >>> print((await git_commit.committer).date)
            2018-10-11 03:04:52
