Lazy Mode
=========

In lazy mode, getting a PyGithub object does not send a request to the GitHub API.
Only accessing methods and properties sends the necessary requests to the GitHub API:

.. code-block:: python

    # Use lazy mode
    g = Github(auth=auth, lazy=True)

    # these method calls do not send requests to the GitHub API
    user = g.get_user("PyGithub")    # get the user
    repo = user.get_repo("PyGithub") # get the user's repo
    pull = repo.get_pull(3403)       # get a known pull request
    issue = pull.as_issue()          # turn the pull request into an issue

    # these method and property calls send requests to Github API
    issue.create_reaction("rocket")  # create a reaction
    created = repo.created_at        # get property of lazy object repo

    # once a lazy object has been fetched, all properties are available (no more requests)
    licence = repo.license

All PyGithub classes that implement ``CompletableGithubObject`` support lazy mode (if useful).
This is only useful for classes that have methods creating, changing, or getting objects.

By default, PyGithub objects are not lazy.
