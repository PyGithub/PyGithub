Async Support
=============

PyGithub ships with full async support built on top of `Niquests <https://niquests.readthedocs.io>`__'s
native ``AsyncSession``. Every sync class and method has an automatically generated async counterpart
in the ``github.asyncio`` subpackage.

Turning sync code into async
-----------------------------

If you already have working sync code, converting it to async is straightforward.
The following rules cover the vast majority of cases:

1. **Import from** ``github.asyncio`` **instead of** ``github``:

   .. code-block:: python

       # Sync
       from github import Github

       # Async
       from github.asyncio import Github

   ``Auth``, exceptions, and input classes (``InputGitTreeElement``, etc.) are still
   imported from ``github`` -- only the I/O classes move.

2. **Add** ``await`` **to any method that hits the network**:

   .. code-block:: python

       # Sync
       user = g.get_user()
       repo = g.get_repo("PyGithub/PyGithub")
       issue = repo.get_issue(number=874)
       issue.create_comment("Hello")

       # Async
       user = await g.get_user()
       repo = g.get_repo("PyGithub/PyGithub")   # no HTTP call, no await needed
       issue = await repo.get_issue(number=874)
       await issue.create_comment("Hello")

   ``get_repo()`` is a special case: it builds the URL locally and does not send a
   request until a property or method on the returned object is accessed.

3. **Add** ``await`` **to properties that lazy-load data**:

   .. code-block:: python

       # Sync
       print(repo.description)
       print(user.login)

       # Async
       print(await repo.description)
       print(await user.login)

   This applies to any property on a ``CompletableGithubObject`` subclass that
   internally calls ``_completeIfNotSet``. Common examples: ``name``,
   ``description``, ``url``, ``login``, ``id``, ``html_url``, ``full_name``, etc.

4. **Replace** ``for`` **with** ``async for`` **when iterating paginated results**:

   .. code-block:: python

       # Sync
       for repo in g.get_user().get_repos():
           print(repo.name)

       # Async
       async for repo in (await g.get_user()).get_repos():
           print(await repo.name)

5. **Use** ``getitem()`` **instead of** ``[]`` **for index access on paginated lists**:

   .. code-block:: python

       # Sync
       first = repos[0]

       # Async
       first = await repos.getitem(0)

   Python cannot implicitly ``await`` dunder methods like ``__getitem__``.

6. **Use** ``async with`` **for context managers**:

   .. code-block:: python

       # Sync
       with Github(auth=auth) as g:
           ...

       # Async
       async with Github(auth=auth) as g:
           ...

Async examples
--------------

Below are a few representative examples showing complete async usage.

**Listing repositories**

.. code-block:: python

    import asyncio
    from github.asyncio import Github
    from github import Auth

    async def main():
        auth = Auth.Token("access_token")
        async with Github(auth=auth) as g:
            user = await g.get_user()
            async for repo in user.get_repos():
                print(await repo.name)

    asyncio.run(main())

**Creating an issue**

.. code-block:: python

    import asyncio
    from github.asyncio import Github
    from github import Auth

    async def main():
        auth = Auth.Token("access_token")
        async with Github(auth=auth) as g:
            repo = g.get_repo("PyGithub/PyGithub")
            issue = await repo.create_issue(
                title="Found a bug",
                body="Description of the bug",
            )
            print(issue)

    asyncio.run(main())

**Working with pull requests**

.. code-block:: python

    import asyncio
    from github.asyncio import Github
    from github import Auth

    async def main():
        auth = Auth.Token("access_token")
        async with Github(auth=auth) as g:
            repo = g.get_repo("PyGithub/PyGithub")
            pulls = repo.get_pulls(state="open", sort="created", base="master")
            async for pr in pulls:
                print(await pr.number, await pr.title)

    asyncio.run(main())

**App installation authentication**

.. code-block:: python

    import asyncio
    from github.asyncio import Github
    from github import Auth

    async def main():
        auth = Auth.AppAuth(123456, private_key).get_installation_auth(
            installation_id, token_permissions
        )
        async with Github(auth=auth) as g:
            repo = g.get_repo("user/repo")
            print(await repo.name)

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

What stays the same
-------------------

- **Authentication** -- ``Auth.Token``, ``Auth.AppAuth``, ``Auth.Login`` etc. are
  the same sync objects used identically in both modes.
- **Data classes** -- ``InputGitTreeElement``, ``InputGitAuthor``, and similar input
  objects are plain data holders and are not async.
- **Exceptions** -- ``GithubException``, ``UnknownObjectException``,
  ``BadCredentialsException``, etc. are raised the same way.
- **``__repr__`` / ``__eq__`` / ``__hash__``** -- These dunder methods stay synchronous;
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
