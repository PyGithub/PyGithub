Async Support
=============

PyGithub ships with full async support built on top of `Niquests <https://niquests.readthedocs.io>`__'s
native ``AsyncSession``. Every sync class and method has an automatically generated async counterpart
in the ``github.asyncio`` subpackage.

Quick start
-----------

.. tabs::

    .. tab:: Sync

        .. code-block:: python

            from github import Github, Auth

            auth = Auth.Token("access_token")
            g = Github(auth=auth)

            for repo in g.get_user().get_repos():
                print(repo.name)

            g.close()

    .. tab:: Async

        .. code-block:: python

            import asyncio
            from github.asyncio import Github
            from github import Auth

            async def main():
                auth = Auth.Token("access_token")
                g = Github(auth=auth)

                async for repo in (await g.get_user()).get_repos():
                    print(await repo.name)

                await g.close()

            asyncio.run(main())

How it works
------------

The async layer is **auto-generated** from the sync source code by the
``scripts/generate_async.py`` script. Every ``.py`` file under ``github/`` that
contains classes with I/O-dependent methods gets a mirror in
``github/asyncio/``. The generator:

1. Discovers which methods touch the network (directly or transitively).
2. Copies each source file and applies a series of AST + regex transformations:
   methods become ``async def``, calls to I/O methods receive ``await``, properties
   that trigger lazy-loading are promoted to awaitable properties, and so on.
3. Runs ``black``, ``ruff``, ``docformatter``, and ``pyupgrade`` to keep the output clean.

The generated files carry the header ``# FILE AUTO GENERATED DO NOT TOUCH`` --
do not edit them by hand.

What becomes awaitable
----------------------

Methods
~~~~~~~

Any method that performs an HTTP request (directly or indirectly) becomes a
coroutine. This includes:

- All methods on ``Github`` (``get_user()``, ``get_repo()``, ``search_repositories()``, ...).
- All methods on domain objects that call the API (``repo.get_issues()``,
  ``issue.create_comment()``, ``pr.merge()``, ...).
- Internal helpers like ``_completeIfNotSet`` / ``_completeIfNeeded`` /
  ``requestJsonAndCheck``.

In async code these must be ``await``-ed:

.. code-block:: python

    user = await g.get_user()
    repos = user.get_repos()  # not a coroutine on AuthenticatedUser

Properties (lazy-loading)
~~~~~~~~~~~~~~~~~~~~~~~~~

In the sync API, many properties trigger a hidden HTTP request on first access
to complete the object's data. For example:

.. code-block:: python

    repo = g.get_repo("PyGithub/PyGithub")
    print(repo.description)  # may trigger an HTTP call behind the scenes

In the async API, these properties return a coroutine and must be ``await``-ed:

.. code-block:: python

    repo = await g.get_repo("PyGithub/PyGithub")
    print(await repo.description)

This applies to any property on a ``CompletableGithubObject`` subclass that calls
``_completeIfNotSet`` internally. Common examples: ``name``, ``description``,
``url``, ``login``, ``id``, ``html_url``, ``full_name``, etc.

Pagination
~~~~~~~~~~

``PaginatedList`` objects support async iteration:

.. code-block:: python

    repos = (await g.get_user()).get_repos()
    async for repo in repos:
        print(await repo.name)

For indexing, use the ``getitem()`` method instead of ``[]`` — Python cannot
implicitly ``await`` dunder methods like ``__getitem__``, so ``[]`` only works on
already-fetched elements:

.. code-block:: python

    repos = (await g.get_user()).get_repos()
    first = await repos.getitem(0)      # fetches pages on demand
    print(await first.name)

You can also call ``await repos.get_page(0)`` to fetch a specific page, or use
``repos.totalCount`` (awaitable) to get the total count.

Context managers
~~~~~~~~~~~~~~~~

The ``Github`` object supports ``async with``:

.. code-block:: python

    async with Github(auth=auth) as g:
        user = await g.get_user()
        print(await user.login)

What stays the same
-------------------

- **Authentication** -- ``Auth.Token``, ``Auth.AppAuth``, ``Auth.Login`` etc. are
  the same sync objects used identically in both modes.
- **Data classes** -- ``InputGitTreeElement``, ``InputGitAuthor``, and similar input
  objects are plain data holders and are not async.
- **Exceptions** -- ``GithubException``, ``UnknownObjectException``,
  ``BadCredentialsException``, etc. are raised the same way.
- **``__repr__``/``__eq__``/``__hash__``** -- These dunder methods stay synchronous;
  they access internal ``_X.value`` attributes directly instead of going through the
  async property.

Import paths
------------

The async package mirrors the sync package structure:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Sync
     - Async
   * - ``from github import Github``
      - ``from github.asyncio import Github``
   * - ``github.Repository.Repository``
      - ``github.asyncio.Repository.Repository``

Threading vs asyncio
--------------------

The sync API uses ``threading.Lock`` for connection pooling. The async API
replaces these with ``asyncio.Lock`` and uses ``niquests.AsyncSession`` under the
hood. Do not mix sync and async ``Github`` instances.

Running tests
-------------

Async tests are generated alongside the source and live in ``tests/asyncio/``.
They reuse the same ``ReplayData`` fixtures as the sync tests:

.. code-block:: bash

    # run async tests
    python -m pytest tests/asyncio/ -q

    # run sync tests only
    python -m pytest tests/ --ignore=tests/asyncio/ -q
