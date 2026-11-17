Exceptions
==========

PyGithub raises exceptions when the GitHub API responds with an error, rather than
returning ``None`` or ``False``. All exceptions raised because of a GitHub API error
are (or derive from) :class:`github.GithubException.GithubException`, so it is always
safe to catch that type if you don't need to distinguish between different failures:

.. code-block:: python

    from github import Github, GithubException

    g = Github(auth=auth)

    try:
        repo = g.get_repo("PyGithub/a-repo-that-does-not-exist")
    except GithubException as e:
        print(f"Request failed with status {e.status}: {e.data}")

The most commonly encountered subclasses are:

- :class:`github.GithubException.UnknownObjectException` — raised when the requested
  object does not exist (HTTP 404), for example ``get_repo``, ``get_issue`` or
  ``get_user`` with an unknown name/number.
- :class:`github.GithubException.BadCredentialsException` — raised when authentication
  fails or the token doesn't have the required permissions (HTTP 401/403).
- :class:`github.GithubException.RateLimitExceededException` — raised when you have hit
  the GitHub API rate limit (HTTP 403).

Since these all derive from ``GithubException``, catch the most specific exception
first if you want to handle cases differently:

.. code-block:: python

    from github import Github, GithubException, UnknownObjectException, RateLimitExceededException

    g = Github(auth=auth)

    try:
        repo = g.get_repo("PyGithub/PyGithub")
        issue = repo.get_issue(number=999999)
    except UnknownObjectException:
        print("That repository or issue does not exist")
    except RateLimitExceededException:
        print("You have exceeded the GitHub API rate limit, try again later")
    except GithubException as e:
        print(f"Something else went wrong: {e.status} {e.data}")

Every ``GithubException`` carries the HTTP ``status`` code, the (decoded) ``data``
returned by the API, and the response ``headers``, which is often what you need to
build your own error message or retry logic:

.. code-block:: python

    try:
        repo.create_issue(title="")
    except GithubException as e:
        # e.g. 422 {'message': 'Validation Failed', 'errors': [...]}
        print(e.status, e.data.get("message"))
