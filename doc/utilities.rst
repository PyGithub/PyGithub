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

.. autofunction:: github.enable_console_debug_logging

Error Handling
--------------

.. automodule:: github.GithubException

Default argument
----------------

:const:`github.NotSet` is a special value for arguments you don't want to provide. You should not have to manipulate it directly, because it's the default value of all parameters accepting it. Just note that it is different from :const:`None`, which is an allowed value for some parameters.

Pagination
----------

.. autoclass:: github.PaginatedList.PaginatedList()

Classes with paginated properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
