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

Get commit date
--------------------------

.. code-block:: python

    >>> commit = repo.get_commit(sha=sha)
    >>> print(commit.commit.author.date)
    2018-10-11 03:04:52
    >>> print(commit.commit.committer.date)
    2018-10-11 03:04:52

Create a signed commit
----------------------

:meth:`github.Repository.Repository.create_git_commit` takes an optional ``signature`` argument,
an ASCII-armored detached PGP signature that Github stores in the ``gpgsig`` header of the commit.

The signature has to be made over the commit payload, in the canonical format git uses::

    tree <tree sha>
    parent <parent sha>
    author <name> <email> <unix timestamp> <utc offset>
    committer <name> <email> <unix timestamp> <utc offset>

    <commit message>

The author and committer in that payload must be identical to the ones sent to the API, otherwise
Github considers the signature invalid. Pass them explicitly rather than letting Github fill them in:

.. code-block:: python

    import subprocess
    from datetime import datetime

    from github import InputGitAuthor


    def git_date(date: datetime) -> str:
        # the API takes ISO-8601 dates, the signed payload takes "<timestamp> <offset>"
        return f"{int(date.timestamp())} {date.strftime('%z')}"


    branch = repo.get_branch("main")
    parent = repo.get_git_commit(branch.commit.sha)
    tree = repo.get_git_tree(parent.tree.sha)

    # drop sub-second precision: isoformat() keeps it, git_date() truncates it,
    # and a one second disagreement is enough to invalidate the signature
    date = datetime.now().astimezone().replace(microsecond=0)
    author = InputGitAuthor("Monalisa Octocat", "octocat@github.com", date.isoformat())
    message = "Commit created by PyGithub"

    payload = (
        f"tree {tree.sha}\n"
        f"parent {parent.sha}\n"
        f"author Monalisa Octocat <octocat@github.com> {git_date(date)}\n"
        f"committer Monalisa Octocat <octocat@github.com> {git_date(date)}\n"
        f"\n{message}\n"
    )

    # any PGP implementation will do, here gpg signs the payload read from stdin
    signature = subprocess.run(
        ["gpg", "--armor", "--detach-sign", "--output", "-"],
        input=payload.encode(),
        capture_output=True,
        check=True,
    ).stdout.decode()

    commit = repo.create_git_commit(
        message, tree, [parent], author=author, committer=author, signature=signature
    )
    repo.get_git_ref("heads/main").edit(commit.sha)

Github reports the result of its own verification on the commit it created:

.. code-block:: python

    >>> commit.verification.verified
    True
    >>> commit.verification.reason
    'valid'
