Commit
======

Create commit status check
--------------------------

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