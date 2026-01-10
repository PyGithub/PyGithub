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

A few class have paginated properties. The classes and their paginated properties are:

- :meth:`github.Commit.Commit.files`
- :meth:`github.Comparison.Comparison.commits`
- :meth:`github.EnterpriseConsumedLicenses.EnterpriseConsumedLicenses.users`

Iterating those properties may fetch multiple pages of items. The size of these pages is controlled by the ``per_page`` setting:

Objects created directly
""""""""""""""""""""""""

Objects created via the following methods fetch the first page of items, together with the object itself. Each method
provides a ``…_per_page`` parameter. The first page and all subsequent pages have this size.

- :meth:`github.Repository.Repository.compare` via parameter ``comparison_commits_per_page``
- :meth:`github.Repository.Repository.get_commit` via parameter ``commit_files_per_page``
- :meth:`github.Enterprise.Enterprise.get_consumed_licenses` via parameter ``licence_users_per_page``

Objects created indirectly
""""""""""""""""""""""""""

Objects return by other methods fetch pages with size equivalent to the value given
via ``Github(per_page=…)`` (unless ``Github(per_page=30)``).

The classes also provide a ``get`` method that fetches the paginated property with a page size as given to these methods:

- :meth:`github.Commit.Commit.get_files` with parameter ``commit_files_per_page``
- :meth:`github.Comparison.Comparison.get_commits` with parameter ``comparison_commits_per_page``
- :meth:`github.EnterpriseConsumedLicenses.EnterpriseConsumedLicenses.get_users` with parameter ``licence_users_per_page``

PyGithub per_page setting
"""""""""""""""""""""""""

If none of the above ``…_per_page`` parameters is used, the value give via ``Github(per_page=…)`` is used (unless ``Github(per_page=30)``) instead.
If no value for ``per_page`` is given, the default page size is used as defined by the GitHub API.

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
