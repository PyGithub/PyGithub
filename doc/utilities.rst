Utilities
=========

Authentication
--------------

.. autoclass:: github.Auth.Login
.. autoclass:: github.Auth.Token
.. autoclass:: github.Auth.JWT
.. autoclass:: github.Auth.AppAuth
.. autoclass:: github.Auth.AppAuthToken
.. autoclass:: github.Auth.AppInstallationAuth
.. autoclass:: github.Auth.AppUserAuth
.. autoclass:: github.Auth.NetrcAuth

Logging
-------

PyGithub uses the ``github`` logger and inherits the application's logging configuration.
It does not write to the console by default. To enable console output for troubleshooting,
call ``github.enable_console_debug_logging()``.

.. autofunction:: github.enable_console_debug_logging

Error Handling
--------------

.. automodule:: github.GithubException

Rate limits
-----------

GitHub limits the number of API requests per authentication. Limits are counted separately for different resources,
like ``core``, ``search``, or ``graphql``. PyGithub provides these limits as a
:class:`github.RateLimitOverview.RateLimitOverview`, where ``resources`` has one :class:`github.Rate.Rate` per resource
with attributes ``resource``, ``limit``, ``remaining``, ``used`` and ``reset``.

There are three ways to retrieve an overview:

:meth:`github.MainClass.Github.get_rate_limits`
    Sends a request and returns the rate limits of all resources. This request does not count against any rate limit.
    Use this when you need all rate limits, for instance before starting work.

:attr:`github.GithubObject.GithubObject.current_rate_limits`
    Sends no request and returns the latest rate limits known so far, on any object returned by PyGithub.
    These are updated from each API response, and only for the resource that the request counted against.
    They are also updated when calling ``get_rate_limits()`` or ``update()``.
    Resources for which nothing is known yet are ``None``. This is cheap enough to be used between any two requests,
    without the need to hold on to the :class:`github.MainClass.Github` instance, which also provides
    :attr:`github.MainClass.Github.current_rate_limits`.

:meth:`github.RateLimitOverview.RateLimitOverview.update`
    Sends a request and returns a new overview with the rate limits of all resources, like ``get_rate_limits()``.
    An overview never changes, so make sure you use the returned object.
    Use this to get values for all resources when you only hold on to an object returned by PyGithub.

For example, pause before running out of requests, after a fetched page has been fully consumed. Searching code counts
against the ``code_search`` resource, not ``core`` like most other requests. The page tells which resource its
pagination requests count against, and ``current_rate_limits`` provides the latest rate limit of that resource.
There is no need to wait after the last page, and a response might not report any rate limit::

    import time

    results = gh.search_code("query")
    for page in results.pages():
        for result in page:
            print(result.path)

        if results.has_unfetched_pages and page.rate_limit is not None:
            rate = gh.current_rate_limits.get_rate(page.rate_limit.resource)
            if rate.remaining < 10:
                time.sleep(rate.resets_in_seconds)

Get values for a resource that has not been used yet::

    rate_limit = repo.current_rate_limits
    if rate_limit.resources.search is None:
        rate_limit = rate_limit.update()
    print(rate_limit.resources.search.remaining)

Any object also provides the rate limit reported by the response that it came with as a :class:`github.Rate.Rate` via
:attr:`github.GithubObject.GithubObject.rate_limit`, which is ``None`` if that response did not report any. This value
does not change with later requests, and it is ``None`` for lazy objects that have not been fetched yet.
This does not send any request.

Likewise, each page returned by :meth:`github.PaginatedList.PaginatedList.pages` and
``PaginatedList.get_page()`` provides the rate limit reported by the response of that page via
:attr:`github.PaginatedList.Page.rate_limit`.

Rate limits are counted per authentication and server, so objects retrieved with a different authentication,
for example through an installation of a GitHub App, provide their own rate limits.

:attr:`github.MainClass.Github.rate_limiting` and :attr:`github.MainClass.Github.rate_limiting_resettime` are deprecated
as they do not tell apart resources. :meth:`github.MainClass.Github.get_rate_limit` is deprecated in favour of
:meth:`github.MainClass.Github.get_rate_limits`.

Default argument
----------------

:const:`github.NotSet` is a special value for arguments you don't want to provide. You should not have to manipulate it directly, because it's the default value of all parameters accepting it. Just note that it is different from :const:`None`, which is an allowed value for some parameters.

Pagination
----------

.. autoclass:: github.PaginatedList.PaginatedList()
   :inherited-members:

.. autoclass:: github.PaginatedList.Page()

.. _utilities-classes-with-paginated-properties:

Classes with paginated properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The GitHub API has the "feature" of paginated properties.
Some objects returned by the API have a property that allows for pagination.
Fetching subsequent pages of that property means fetching the entire object (with all other properties)
and the specified page of the paginated property. Iterating over the paginated property means fetching
all other properties multiple times. Fortunately, the allowed size of each page (``per_page`` is usually 300,
in contrast to the "usual" ``per_page`` maximum of 100).

A few classes have paginated properties. The classes and their paginated properties are:

- :meth:`github.Commit.Commit.files`
- :meth:`github.Comparison.Comparison.commits`
- :meth:`github.EnterpriseConsumedLicenses.EnterpriseConsumedLicenses.users`

Iterating those properties may fetch multiple pages of items. The size of these pages is controlled by the ``per_page`` setting:

Objects created directly
""""""""""""""""""""""""

Objects created via the following methods fetch the first page of items, together with the object itself. Each method
provides a ``…_per_page`` parameter. The first page and all subsequent pages have this size.

- :meth:`github.Repository.Repository.compare` with parameter ``comparison_commits_per_page``
- :meth:`github.Repository.Repository.get_commit` with parameter ``commit_files_per_page``
- :meth:`github.Enterprise.Enterprise.get_consumed_licenses` with parameter ``licence_users_per_page``

Objects created indirectly
""""""""""""""""""""""""""

Objects returned by other methods fetches pages with page size as configured via ``Github(per_page=…)`` (unless ``Github(per_page=30)``).

The classes also provide a ``get`` method to fetches the paginated property with a given page size:

- :meth:`github.Commit.Commit.get_files` with parameter ``commit_files_per_page``
- :meth:`github.Comparison.Comparison.get_commits` with parameter ``comparison_commits_per_page``
- :meth:`github.EnterpriseConsumedLicenses.EnterpriseConsumedLicenses.get_users` with parameter ``licence_users_per_page``

PyGithub per_page setting
"""""""""""""""""""""""""

If none of the above ``…_per_page`` parameters is set, the value given via ``Github(per_page=…)`` is used instead (unless ``Github(per_page=30)``).
If no value for ``Github(per_page=…)`` is given, the GitHub API defines a default page size for each paginated property.

Example:

.. code-block:: python

    sha = "c4ec16a18bb4401e89967a8e395103c95cca5c2f"
    repo_name = "PyGithub/PyGithub"

    # page size for paginated lists returned by get_… methods
    g = github.Github(per_page=100)
    repo = g.get_repo(repo_name)

    # page size for the Commit.files property only
    commit = repo.get_commit(sha, commit_files_per_page=300)

    # files are fetched in pages of 300, not 100,
    # where the first page has already been retrieved via repo.get_commit
    for file in commit.files:
        pass

Alternatively, a ``get_*`` method exists for each paginated property, which allows to provide a
``per_page`` argument. This method is usually useful if the object is retrieved indirectly.

Example:

.. code-block:: python

    sha1 = "18eeb269686aa5ee61ee7305ffbc3f0146c0bf5c"
    sha2 = "c4ec16a18bb4401e89967a8e395103c95cca5c2f"
    repo_name = "PyGithub/PyGithub"

    # page size for paginated lists returned by methods
    g = github.Github(per_page=100)
    repo = g.get_repo(repo_name)

    # page size for the Compare.commits property only
    compare = repo.compare(sha1, sha2, comparison_commits_per_page=1)

    # iterating over Compare.commits happens in pages of 1
    commit = compare.commits[0]

    # here, files are fetched with configured page size of 100
    for file in commit.files:
        pass

    # here, files are fetched in pages of 300
    for file in commit.get_files(per_page=300):
        pass

Input classes
-------------

.. autoclass:: github.InputFileContent.InputFileContent
.. autoclass:: github.InputGitAuthor.InputGitAuthor
.. autoclass:: github.InputGitTreeElement.InputGitTreeElement

Raw Requests
------------

If you need to make requests to APIs not yet supported by PyGithub,
you can use the :class:`.Requester` object directly, available as :attr:`object.requester` on most PyGithub objects.

.. autoclass:: github.Requester.Requester
    :members:
